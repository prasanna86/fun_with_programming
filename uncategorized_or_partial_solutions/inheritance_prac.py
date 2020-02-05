class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        avg_score = sum(self.scores) / len(self.scores)
        if(avg_score < 40):
            s = "T"
        elif(40 <= avg_score< 55):
            s = "D"
        elif(55 <= avg_score < 70):
            s = "P"
        elif(70 <= avg_score < 80):
            s = "A"
        elif(80 <= avg_score < 90):
            s = "E"
        else:
            s = "O"
        return s

# testing the classes
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
print(s.firstName)