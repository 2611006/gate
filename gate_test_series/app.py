from flask import Flask, render_template, request
import engineering_math
import ds
import statistics
import linear_algebra
import probability
import ml
import dbms
import computer_networks
import operating_systems

app = Flask(__name__)

# Streams page
@app.route('/streams')
def streams():
    streams = ["CSE", "DA"]
    return render_template('streams.html', streams=streams)

# Subjects page
@app.route('/subjects/<stream>')
def subjects(stream):
    subjects_by_stream = {
    "CSE": ["engineering_math", "data_structures", "dbms", "operating_systems", "computer_networks"],
    "DA": ["engineering_math", "statistics", "linear_algebra", "probability", "ml"]
}

    if stream not in subjects_by_stream:
        return "Stream not found", 404
    subjects = subjects_by_stream[stream]
    return render_template('subjects.html', stream=stream, subjects=subjects)

# Levels page
@app.route('/levels/<stream>/<subject>')
def levels(stream, subject):
    return render_template('levels.html', stream=stream, subject=subject)

# Quiz page
@app.route('/quiz/<stream>/<subject>/<difficulty>')
def quiz(stream, subject, difficulty):
    module = SUBJECT_MODULES.get(subject)
    
    if not module:
        return "Subject not found", 404

    if difficulty not in module.questions:
        return "Difficulty not found", 404

    return render_template(
    "questions.html",
    stream=stream,
    subject_slug=subject,                    # engineering_math
    subject_name=SUBJECT_NAMES[subject],     # Engineering Mathematics
    level=difficulty.capitalize(),
    difficulty=difficulty,
    questions=questions,
    results=None
)

# Dictionary mapping for cleaner lookup
SUBJECT_MODULES = {
    "engineering_math": engineering_math,
    "data_structures": ds,
    "statistics": statistics,
    "linear_algebra": linear_algebra,
    "probability": probability,
    "ml": ml,
    "dbms": dbms,
    "computer_networks": computer_networks,
    "operating_systems": operating_systems
}

SUBJECT_NAMES = {
    "engineering_math": "Engineering Mathematics",
    "data_structures": "Data Structures",
    "ml": "Machine Learning Basics",
    "dbms": "DBMS",
    "computer_networks": "Computer Networks",
    "operating_systems": "Operating Systems",
    "statistics": "Statistics",
    "linear_algebra": "Linear Algebra",
    "probability": "Probability"
}


@app.route('/submit_answers', methods=['POST'])
def submit_answers():
    user_answers = request.form.to_dict()
    
    # Safely get difficulty and subject
    difficulty = user_answers.pop("difficulty", "easy") 
    subject = user_answers.pop("subject", "Data Structures")

    # Get the correct module from our map
    module = SUBJECT_MODULES.get(subject)
    
    if not module:
        return f"Error: Subject '{subject}' not recognized.", 400

    # Fetch the specific questions list
    try:
        questions_data = module.questions[difficulty]
    except KeyError:
        return f"Error: Difficulty level '{difficulty}' not found for {subject}.", 404
    
    results = []
    score = 0
    for i, q in enumerate(questions_data, 1):
        user_choice = user_answers.get(f"q{i}")
        correct_choice = q.get("correct")
        is_correct = (user_choice == correct_choice)
        if is_correct: score += 1
        results.append({
            "user_choice": user_choice, 
            "correct_choice": correct_choice, 
            "is_correct": is_correct
        })

    return render_template(
        'questions.html',
        subject=subject,
        level=difficulty.capitalize(),
        difficulty=difficulty,
        questions=questions_data,
        results=results,
        score=score
    )
@app.route('/')
def index():
    # This will now correctly render your landing page
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)




