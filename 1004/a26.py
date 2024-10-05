class people:
    
    name = ''
    age = 0
    
    __weight = 0
    
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 說: 我 %d 歲。" %(self.name,self.age))
 
 
s = people('ken',10,60)
s.speak()