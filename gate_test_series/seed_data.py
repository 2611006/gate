from app import app, db
from models import Stream, Subject

with app.app_context():

    # Streams
    cse = Stream(name="CSE")
    da = Stream(name="DA")

    db.session.add_all([cse, da])
    db.session.commit()

    # CSE Subjects
    cse_subjects = [
        "Engineering Mathematics",
        "Data Structures",
        "Algorithms",
        "Operating Systems",
        "DBMS"
    ]

    for sub in cse_subjects:
        db.session.add(Subject(name=sub, stream_id=cse.id))

    # DA Subjects
    da_subjects = [
        "Engineering Mathematics",
        "Probability & Statistics",
        "Machine Learning",
        "Data Analytics"
    ]

    for sub in da_subjects:
        db.session.add(Subject(name=sub, stream_id=da.id))

    db.session.commit()

    print("Sample streams and subjects inserted.")
