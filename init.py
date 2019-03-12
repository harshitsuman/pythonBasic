class Computer:

    def __init__(self,a1,a2):
        self.a1=a1
        self.a2=a2

    def config(self):
        print("config is ",self.a1,self.a2)

com1 = Computer("i5","16gb")
com2 = Computer("RD i5", "RDi9")

com1.config()
com2.config()