import random



class attend:
    def __init__(self,marks):
        self.marks=marks
        
    def my_marks(self):
        # self.marks=random()
        if self.marks>80:
            print(f'Your get A+ and result is {self.marks}')
        elif self.marks>60:
            print(f'Your get A- and result is {self.marks}')
        else:
            print(f'Your result is {self.marks}. So, it is not good and try improve next time')



get_mark=random.randint(40,100)

amena=attend(get_mark)
amena.my_marks()


get_mark=random.randint(40,100)

sadia=attend(get_mark)
sadia.my_marks()

