import pandas as pd
import torch
from torch_geometric.data import Data

def load_data():
    interactions = pd.read_csv("./data/interactions.csv")
    students = pd.read_csv("./data/students.csv")
    courses = pd.read_csv("./data/courses.csv")
    
    # Map IDs to indices
    student_ids = students["student_id"].unique()
    course_ids = courses["course_id"].unique()
    student_to_idx = {s: i for i, s in enumerate(student_ids)}
    course_to_idx = {c: i + len(student_ids) for i, c in enumerate(course_ids)}
    
    # Edge indices (student-course interactions)
    src = [student_to_idx[s] for s in interactions["student_id"]]
    dst = [course_to_idx[c] for c in interactions["course_id"]]
    edge_index = torch.tensor([src, dst], dtype=torch.long)
    
    # Labels (normalized grades)
    y = torch.tensor(interactions["grade"].values / 100, dtype=torch.float)
    
    return Data(
        edge_index=edge_index,
        y=y,
        num_students=len(student_ids),
        num_courses=len(course_ids),
        course_ids=course_ids
    )