from Course import Course  # Make sure you're importing the correct class

class Test_Course:
    '''Course in Course.py'''

    def test_title_instance_variable(self):
        "Test setting and getting for title"
        course = Course(title="Programming Robots for Outer Space", schedule="Full-Time", description="Learn how to program robots.")
        assert course.title == "Programming Robots for Outer Space"

    def test_schedule_instance_variable(self):
        "Test setting and getting for schedule"
        course = Course(title="Programming Robots for Outer Space", schedule="Full-Time", description="Learn how to program robots.")
        assert course.schedule == "Full-Time"

    def test_description_instance_variable(self):
        "Test setting and getting for description"
        course = Course(title="Programming Robots for Outer Space", schedule="Full-Time", description="Learn how to program robots.")
        assert course.description == "Learn how to program robots."
