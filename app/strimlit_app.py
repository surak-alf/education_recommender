import streamlit as st
import pandas as pd

# Load data
students = pd.read_csv("../data/students.csv")
courses = pd.read_csv("../data/courses.csv")

# Mock recommender (replace with GNN)
def recommend(student_id):
    enrolled = pd.read_csv("../data/interactions.csv")
    taken = enrolled[enrolled.student_id == student_id].course_id.tolist()
    all_courses = set(courses.course_id)
    return list(all_courses - set(taken))[:3]  # Recommend 3 untaken courses

# UI
st.title("Course Recommender (20 Students)")
student_id = st.selectbox("Select Student", students.student_id)
if st.button("Recommend"):
    recs = recommend(student_id)
    st.write(f"Recommended courses for {students[students.student_id == student_id].name.values[0]}:")
    for course in recs:
        title = courses[courses.course_id == course].title.values[0]
        feedback = st.radio(
            f"{course}: {title}",
            ["👍", "👎"],
            key=f"fb_{student_id}_{course}"
        )