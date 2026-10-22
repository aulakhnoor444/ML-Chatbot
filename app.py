from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Read the API key from an environment variable
API_KEY = os.getenv("GEMINI_API_KEY")

URL = "https://generativelanguage.googleapis.com/v1beta/interactions"


def chat(message):
    if not API_KEY:
        return "API key is missing. Set GEMINI_API_KEY in PowerShell."

    try:
        response = requests.post(
            URL,
            headers={
                "x-goog-api-key": API_KEY,
                "Content-Type": "application/json"
            },
            json={
                "model": "gemini-3.5-flash-lite",
                "input": message
            },
            timeout=60
        )

        # Check whether the API returned an error
        if not response.ok:
            print("Gemini API status:", response.status_code)
            print("Gemini API response:", response.text)
            return "Gemini API request failed. Check the terminal for details."

        data = response.json()

        # Extract the generated text
        if data.get("output_text"):
            return data["output_text"]

        # Fallback for responses containing output steps
        for step in data.get("steps", []):
            if step.get("type") == "model_output":
                for item in step.get("content", []):
                    if item.get("type") == "text" and item.get("text"):
                        return item["text"]

        print("Unexpected Gemini response:", data)
        return "Gemini returned no text response."

    except requests.exceptions.Timeout:
        return "The request timed out. Please try again."

    except requests.exceptions.RequestException as error:
        print("Request error:", error)
        return "Could not connect to Gemini. Check your internet connection."

    except ValueError as error:
        print("Response parsing error:", error)
        return "Gemini returned an invalid response."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat_api():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")

    if not isinstance(message, str) or not message.strip():
        return jsonify({"reply": "Please type a message."}), 400

    reply = chat(message.strip())

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
