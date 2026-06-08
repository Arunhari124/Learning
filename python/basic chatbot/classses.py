import datetime

class chad_functions():
    def __init__(self,user_name):
        self.user_name=user_name
    def basic_response(self):
        now = datetime.datetime.now()
        resposes= {("HELLO","HI","HEY"):f"hi {self.user_name},how are you"
              ,"TIME":now.time()
              ,"DATE":now.date() }
        return resposes
    def joke(self):
        jokes={"Why do programmers prefer dark mode?":"Because light mode attracts bugs.",
           "My HDD told me it was tired":"Now it takes emotional support before booting Windows.",
           "I asked my PC to stop freezing.":"It said, “Im just chilling.",
           "Why did the gamer break up with his girlfriend?":"She said, Choose me or your FPS. He said, Can you repeat that after the benchmark?",
           "Student: “Sir, the exam was too hard.":"Teacher: “Thats why its called an exam, not a giveaway."}
        return jokes
    def motivate(self):
        motivation={1:"You won’t always feel ready, but showing up every day changes everything.",
                    2:"A few years of focused effort can completely change your life.",
                    3:"Even 1 hour of learning daily becomes hundreds of hours in a year.",
                    4:"Every skilled developer, athlete, or successful person was once confused and inexperienced.",
                    5:"Most people quit right before improvement starts showing."}
        return motivation
    def weather(self):
        return "look outside "

class calc():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def multi(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 / self.num2
