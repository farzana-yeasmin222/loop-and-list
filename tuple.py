# tuple :
grades = ("A", "B", "C" )
(first, second, third) = grades
#print(second+third)

name, age = "Farzana", 38
#print(name,type(age))



def myFunct():
    return 11, 12, 13

(one, two, three) = myFunct()
#print(one, two, three)


myList = ["Farzana", 38, "Rupa"]
myTuple = ("Farzana", [1, 2, 3], 38, "Rupa", "Yeasmin" , "Farzana")
myTupleOne = (120, 220, -234)
#myList[1] = 'Islam'
#print(myList.index)
myTuple[1][2] = 23
print(-234 in myTupleOne)

Name = "Hello"
newStr = Name + "i am Farzana"
print(newStr)