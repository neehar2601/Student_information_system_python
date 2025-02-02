class Subject:
    def __init__(self, title, credits):
        self.title = title
        self.credits = credits

    def __str__(self):
        return f"Subject: {self.title}, Credits: {self.credits}"


class Course:
    def __init__(self, subject, instructor, fee):
        self.subject = subject
        self.instructor = instructor
        self.course_fee = fee
        self.assignment_marks = 0
        self.quiz_marks = 0


class ClassroomCourse(Course):
    def __init__(self, subject, instructor, fee, school, session):
        super().__init__(subject, instructor, fee)
        self.school = school
        self.session = session


class OnlineCourse(Course):
    def __init__(self, subject, instructor, fee, video_lessons, weeks):
        super().__init__(subject, instructor, fee)
        self.video_lessons = video_lessons
        self.weeks = weeks


class Assessments:
    def assignment_score(self, marks):
        pass

    def quiz_score(self, marks):
        pass


class Learner(Assessments):
    def __init__(self, name, grade, course):
        self.name = name
        self.grade = grade
        self.course = course
        self.grade_score = 0

    def __str__(self):
        return f"Name: {self.name}, Course: {self.course.subject.title}"

    def assignment_score(self, marks):
        self.course.assignment_marks = marks

    def quiz_score(self, marks):
        self.course.quiz_marks = marks

    def calculate_grade(self):
        if "Online" in self.course.subject.title:
            max_assignment_marks = 30
            max_quiz_marks = 10
        else:
            max_assignment_marks = 100
            max_quiz_marks = 30

        assignment_score_out_of_10 = (self.course.assignment_marks / max_assignment_marks) * 10
        quiz_score_out_of_10 = (self.course.quiz_marks / max_quiz_marks) * 10

        self.grade_score = (assignment_score_out_of_10 + quiz_score_out_of_10) / 2
        return self.grade_score


def main():
    subjects = {
        1: Subject("Java", 4),
        2: Subject("Java Online", 4),
        3: Subject("JavaScript", 3),
        4: Subject("JavaScript Online", 3)
    }

    print("Select a course:")
    for key, value in subjects.items():
        print(f"{key}: {value.title}")

    choice = int(input("Enter course number: "))
    selected_subject = subjects.get(choice, None)
    if not selected_subject:
        print("Invalid choice.")
        return

    instructor = "Dr. Smith"
    fee = 500

    if "Online" in selected_subject.title:
        course = OnlineCourse(selected_subject, instructor, fee, "Video Lessons", 6)
    else:
        course = ClassroomCourse(selected_subject, instructor, fee, "XYZ School", "Fall 2023")

    learner_name = input("Enter learner's name: ")
    learner = Learner(learner_name, 0, course)

    max_assignment = 30 if isinstance(course, OnlineCourse) else 100
    max_quiz = 10 if isinstance(course, OnlineCourse) else 30

    assignment_marks = int(input(f"Enter assignment marks (Max {max_assignment}): "))
    quiz_marks = int(input(f"Enter quiz marks (Max {max_quiz}): "))

    learner.assignment_score(assignment_marks)
    learner.quiz_score(quiz_marks)
    grade = learner.calculate_grade()

    result = "Successfully Passed" if grade >= 5 else "Completed"
    print(f"Grade Score: {grade:.2f} - {result}")


if __name__ == "__main__":
    main()
