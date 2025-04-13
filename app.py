# app.py
from flask import Flask, render_template, request
from modules.voice_input import listen_for_audio
from modules.responses import generate_response
from modules.feedback import get_feedback, save_feedback
from modules.utils import filter_content

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    filtered_input = filter_content(user_input)  # Filter inappropriate content
    response = generate_response(filtered_input)  # Generate KODEX's response
    user_feedback = request.form['feedback']  # Get feedback from the user
    get_feedback(response, user_feedback)  # Save the feedback
    save_feedback()  # Save feedback to file
    return response

if __name__ == "__main__":
    app.run(debug=True)
