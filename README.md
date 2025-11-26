Django Gemini Chatbot

A simple, real-time chatbot application built with Django that leverages the Google Gemini API for powerful, conversational AI interactions.
<img width="1113" height="1111" alt="screencapture-127-0-0-1-8000-2025-11-26-14_06_24" src="https://github.com/user-attachments/assets/9192338b-5b33-45d9-b1ff-d8258e27c609" />

🌟 Features

Gemini API Integration: Uses the google-genai SDK to interact with the Gemini models.

Conversational History: Maintains chat context within the session to allow for coherent, multi-turn conversations.

Web Interface: A basic, responsive Django web interface for easy interaction.

Secure API Key Handling: Utilizes environment variables for secure storage of the Gemini API key.

📋 Prerequisites

Before you begin, ensure you have the following installed:

Python (3.8+): The language runtime for Django.

pip: Python package installer (usually included with Python).

A Google Gemini API Key: You can obtain one from Google AI Studio.

🚀 Setup and Installation

Follow these steps to get your local development environment set up.

1. Clone the Repository

git clone [https://github.com/your-username/django-gemini-chatbot.git](https://github.com/your-username/django-gemini-chatbot.git)
cd django-gemini-chatbot


2. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

# Create the environment
python -m venv venv

# Activate the environment (Linux/macOS)
source venv/bin/activate

# Activate the environment (Windows)
.\venv\Scripts\activate


3. Install Dependencies

Install Django and the Google GenAI SDK using the requirements.txt file (assuming you have one):

pip install -r requirements.txt
# If you don't have a requirements.txt, you can install manually:
# pip install django google-genai


4. Configure the Gemini API Key

You must set your Gemini API key as an environment variable. The application will read this variable when initializing the API client.

Linux/macOS:

export GEMINI_API_KEY='YOUR_API_KEY_HERE'


Windows (Command Prompt):

set GEMINI_API_KEY=YOUR_API_KEY_HERE


Windows (PowerShell):

$env:GEMINI_API_KEY="YOUR_API_KEY_HERE"


Replace YOUR_API_KEY_HERE with the actual key you obtained.

5. Apply Migrations

Run database migrations (though this minimal project may not require them, it's a good practice):

python manage.py migrate


⚙️ Usage

1. Start the Development Server

Run the standard Django development server:

python manage.py runserver


2. Access the Chatbot

Open your web browser and navigate to:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)


You should see the chatbot interface where you can begin your conversation with the Gemini model.
