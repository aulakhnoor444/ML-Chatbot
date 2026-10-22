ML CHATBOT - WEB VERSION

PROJECT STRUCTURE

ML_Chatbot_Web/
│
├── app.py
├── requirements.txt
├── README.txt
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js


HOW TO RUN

1. Open the project folder in VS Code.

2. Open Terminal.

3. Install the required modules:

   python -m pip install -r requirements.txt

4. IMPORTANT:
   The Gemini API key should NOT be written directly in app.py.

   In Windows CMD, set your new API key for the current terminal:

   set GEMINI_API_KEY=YOUR_NEW_GEMINI_API_KEY

   In PowerShell:

   $env:GEMINI_API_KEY="YOUR_NEW_GEMINI_API_KEY"

5. Run:

   python app.py

6. Open this address in your browser:

   http://127.0.0.1:5000

7. Type a question in the chatbot.

IMPORTANT SECURITY NOTE

Do not upload your API key to GitHub or share it publicly.
The API key that was pasted in the chat should be revoked/regenerated.
