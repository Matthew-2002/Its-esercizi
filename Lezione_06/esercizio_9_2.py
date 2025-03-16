class Student:

    def __init__(self, name: str, studyProgram: str, age: int, gender: str):
        
        self.name = name
        self.studyProgram = studyProgram
        self.gender = gender
        self.age = age

    def print_info(self):

        print(
            f"Scheda:\n"
            f"    Nome: {self.name}\n"
            f"    Corso di studi: {self.studyProgram}\n"
            f"    Età: {self.age}\n"
            f"    Sesso: {self.gender}\n"
        )
        
student1 = Student("Matteo", "Fabbri", 22, "Maschio")
student2 = Student("Fabio", "Gabriele", 32, "Maschio")
student3 = Student("Alice", "Cacmpolungo", 19, "Femmina")

student1.print_info()
student2.print_info()
student3.print_info()

