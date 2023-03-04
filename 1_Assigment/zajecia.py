class Zajecia:
    def __init__(self, name):
        self.name = name
        self.list_of_students = []

    def enroll_student(self, name_and_surname_of_student):
        if(len(self.list_of_students) <= 10):
            self.list_of_students.append(name_and_surname_of_student)
        else:
            print("The class is full")
    
    def show_list_of_students(self):
        return self.list_of_students


matematyka = Zajecia("Matematyka")
matematyka.enroll_student("Maciej Jastrzębski")

print(matematyka.show_list_of_students())
