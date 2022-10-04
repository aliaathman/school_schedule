from school_schedule.student import Student
def test_adding_one_class_increases_class_length():
    #arrange 
    name = "Ellis"
    grade = "Junior"
    classes = ["Painting"]
    ellis = Student(name, grade, classes)

    #act
    ellis.add_class("Pottery")

    #assert 
    assert len(ellis.classes) == 2
def test_empty_class_list_is_valid():
    #arrange
    name = "Ellis"
    grade = "Junior"
    classes = []
    ellis = Student(name, grade, classes)

    #act
    #assert
    assert ellis.classes == []
    assert len(ellis.classes) == 0
def test_summary_is_accurate():
    name = "Ellis"
    grade = "Junior"
    classes = ["Painting"]
    ellis = Student(name, grade, classes)
    #act 
    # ellis.get_num_classes()
    result = ellis.summary()

    #assert
    assert result == (f"Ellis is a Junior enrolled in 1 classes")