class Course:
    def __init__(self, name: str, teacher: str, time: int):
        self.name = name
        self.teacher = teacher
        self.time = time 
    
    def destyti(self):
        print("Now is a lesson! ")
