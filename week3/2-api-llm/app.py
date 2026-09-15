import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)


def generate_response(question: str) -> str:
    """Send a user question to the OpenAI API and return the generated answer."""
    cleaned_question = (question or "").strip()
    if not cleaned_question:
        raise ValueError("Question cannot be empty.")

    prompt = f"Answer this question clearly and simply: {cleaned_question}"
    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
    )
    return response.output_text.strip()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    question = data.get("question", "")

    try:
        answer = generate_response(question)
        return jsonify({"answer": answer})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


if __name__ == "__main__":
    app.run(debug=True)
