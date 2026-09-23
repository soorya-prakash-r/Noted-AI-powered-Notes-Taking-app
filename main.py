from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enhance_note", methods=["POST"])
def enhance_note():
    data = request.get_json()
    note = data.get("note", "").strip()

    if not note:
        return jsonify({"enhanced_note": ""})

    prompt = f"""Enhance the following note for clarity, grammar, and readability without changing its meaning.
Keep all formatting tags like <b>, <i>, <u>, <strong>, <em>, etc. intact. Provide only enhanced text.

Note:
{note}
"""


    try:
        response = model.generate_content(prompt)
        enhanced_note = response.text.strip()
    except Exception as e:
        print("Error calling Gemini API:", e)
        enhanced_note = note  

    return jsonify({"enhanced_note": enhanced_note})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
