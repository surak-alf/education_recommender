def test_dataset_sizes():
    students = pd.read_csv("../data/students.csv")
    courses = pd.read_csv("../data/courses.csv")
    interactions = pd.read_csv("../data/interactions.csv")
    
    assert len(students) == 20, "Incorrect student count!"
    assert len(courses) == 10, "Incorrect course count!"
    assert len(interactions) >= 50, "Too few enrollments!"