# feedback.py
feedback_data = []

def get_feedback(response, user_feedback):
    feedback_data.append({"response": response, "feedback": user_feedback})

def save_feedback():
    with open("feedback.json", "w") as file:
        json.dump(feedback_data, file)

def load_feedback():
    try:
        with open("feedback.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
