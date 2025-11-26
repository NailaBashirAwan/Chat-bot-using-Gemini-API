import json
import requests
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# --- Configuration ---
# WARNING: Replace "" with your actual Gemini API Key. 
GEMINI_API_KEY = "AIzaSyBCSkQ2Gh75rxjBiasRHr0GoZtfn7PEQ9s" 
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent"
MAX_RETRIES = 3

def chat_view(request):
    """Renders the main chat application page."""
    return render(request, 'chatbot.html')

# Use csrf_exempt for the API endpoint since the request is being made via client-side JavaScript 
# that may not include a CSRF token (though it's better practice to include it).
@csrf_exempt
def gemini_chat_api(request):
    """Handles the AJAX POST request, calls the Gemini API, and returns the response."""
    if request.method == 'POST':
        if not GEMINI_API_KEY:
            return JsonResponse({'error': 'Gemini API Key is not configured on the server.'}, status=500)
            
        try:
            # 1. Parse incoming JSON data
            data = json.loads(request.body)
            user_message = data.get('message', '').strip()

            if not user_message:
                return JsonResponse({'error': 'No message provided.'}, status=400)

            # 2. Construct the Gemini API Payload
            payload = {
                "contents": [{"parts": [{"text": user_message}]}],
                "systemInstruction": {
                    "parts": [{"text": "You are a helpful and friendly chatbot integrated into a Django application. Respond concisely and clearly."}]
                },
            }

            headers = {
                'Content-Type': 'application/json',
            }
            
            # 3. Call the Gemini API with exponential backoff (server-side)
            api_response_text = "An error occurred on the server while processing the AI request."
            
            for i in range(MAX_RETRIES):
                try:
                    full_url = f"{GEMINI_API_URL}?key={GEMINI_API_KEY}"
                    
                    # Make the external API call
                    response = requests.post(full_url, headers=headers, json=payload)
                    response.raise_for_status() # Raises an HTTPError for 4xx or 5xx responses

                    result = response.json()
                    candidate = result.get('candidates', [{}])[0]
                    
                    # Extract the generated text
                    if candidate and candidate.get('content') and candidate['content'].get('parts'):
                        api_response_text = candidate['content']['parts'][0]['text']
                        return JsonResponse({'response': api_response_text}) # Success!

                except requests.exceptions.RequestException as e:
                    print(f"Gemini API Request failed (Attempt {i+1}): {e}")
                    if i < MAX_RETRIES - 1:
                        # Simple backoff logic
                        import time
                        time.sleep(1 * (i + 1))
                    else:
                        break # Exit loop after all retries fail

            # If the loop finishes without success, return the generic error
            return JsonResponse({'error': api_response_text}, status=500)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in request body.'}, status=400)
        except Exception as e:
            print(f"Unexpected server error: {e}")
            return JsonResponse({'error': 'An unexpected server error occurred.'}, status=500)

    return HttpResponse(status=405) # Method Not Allowed for non-POST requests