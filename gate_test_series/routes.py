from flask import render_template, request
from app import app, db
from models import Stream, Subject, Question

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/streams')
def streams():
    streams = Stream.query.all()
    return render_template('streams.html', streams=streams)

@app.route('/subjects/<int:stream_id>')
def subjects(stream_id):
    subjects = Subject.query.filter_by(stream_id=stream_id).all()
    return render_template('subjects.html', subjects=subjects)

@app.route('/levels/<int:subject_id>')
def levels(subject_id):
    return render_template('levels.html', subject_id=subject_id)

@app.route('/test/<int:subject_id>/<level>')
def test(subject_id, level):
    questions = Question.query.filter_by(
        subject_id=subject_id,
        difficulty=level.capitalize()
    ).all()
    return render_template('test.html', questions=questions)
