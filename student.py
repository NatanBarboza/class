class Student:
    def __init__(self, name:str, registration:int, grade_1:float, grade_2:float, grade_3:float):
        self.__name = name
        self.__registration = registration
        self.__grade_1 = grade_1
        self.__grade_2 = grade_2
        self.__grade_3 = grade_3

    @property
    def name(self):
        return self.__name

    @property
    def registration(self):
        return self.__registration
    
    @property
    def grade_1(self):
        return self.__grade_1

    @property
    def grade_2(self):
        return self.__grade_2

    @property
    def grade_3(self):
        return self.__grade_3

    def get_media(self):
        media = (self.__grade_1 + self.__grade_2 + self.__grade_3) / 3
        if media < 6:
            print(f"{self.__name} wasn't approved...")
        else:
            print(f"{self.__name} was approved!")
        return media