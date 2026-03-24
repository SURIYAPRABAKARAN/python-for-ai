print("practice")

listOfNumbers =[0,2,1,3]
listOfNumbers.append(4)
listOfNumbers.remove(0)
listOfNumbers.sort(reverse=True)
listOfNumbers.append(True)
listOfNumbers.append("String")
listOfNumbers.insert(4,False)
listOfNumbers.pop(3)
print(listOfNumbers)

print(f"len : ",len(listOfNumbers))
print(f"type : ",type(listOfNumbers))

print(f"count : ",listOfNumbers.count(2))

tuples = (1,2,3,4,5,2)

print(f"tuples count : ",tuples.count(2))
print(f"tuples index : ",tuples.index(1))

sets = {1,2,3,4,5,5}
sets.remove(2)
sets.discard(2)
sets.pop()

copySet = sets.copy()

print(f"sets : ",sets)
print(f"copySet : ",copySet)

newDict = {
    "name" : "suriya",
    "age" : 25,
    "married" : False,
    "married" : True,
    "Fav Sports" : ["cricket","badminton"]
}

print(f"newDict : ",newDict)
print(f"newDict married : ",newDict["married"],newDict.get("Fav Sports"))
print(f"newDist Items : ",newDict.items())

#list task
numbers = [20, 30, 40, 50]
numbers.remove(20)
print(numbers[0])
numbers.append(60)
print(numbers[numbers.__len__() -1])
print(numbers)


def passOrFail():
      scores = [45, 67, 82, 49, 90]
      for score in scores:
            if(score >= 50):
                  print(f"Pass",score)
            else:
                  print(f"fail",score)

passOrFail()

#set task
person = ("suriya",25,"chennai")
print(f"name :",person[0])
print(f"age :",person[1])
print(f"city :",person[2])

for per in person:
      print(per)

# for eachElement in listOfNumbers:
#     print(f"eachElement : ",eachElement*10)

# for i in range(len(listOfNumbers)):
#     print(f"i in range : ",listOfNumbers[i])

# create a function task
def calculate(a,b):
      add = a + b
      sub = a - b
      mul = a * b
      return add,sub,mul

add,sub,mul = calculate(10,5)

print(f"add : ",add)
print(f"sub : ",sub)
print(f"mul : ",mul)

# set task
numbersSet = [1,2,3,4,5,5,6,7,1,2,3]

print(set(numbersSet))

a = {1,2,3,4}
b = {3,4,5,6}

print(f"union :",a.union(b))
print(f"intersection :",a.intersection(b))
print(f"difference a :",a.difference(b))
print(f"difference b :",b.difference(a))
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)

def printDist():
      student = {
            "name" : "suriya",
            "age" : 25,
            "address" : "chennai"
      }
      print(student.items())
      print(student.get("name"))
      print(student.keys())

      for key in student.keys():
             print(key , " : ",student.get(key))


      products = {
            "mobile" : 70000,
            "laptop" : 30000,
            "tablet" : 25000
      }
      print(products.items())
      for pro in products:
         products[pro] *= 1.10

      print(products.items())
      
      students = [
        {"name":"A","score":80},
        {"name":"B","score":40},
        {"name":"C","score":75}
        ]
      print(students)

      for st in students:
            print(students.index(st))
            print(st)
            singleStudent = st

            if(singleStudent.get("score") >= 50):
                  print("passed")
            else:
                  print("fail")
            
      numbers = [1,2,2,3,3,3,4,4,4,4]
      distNew = {}

      for num in numbers:
       if num in distNew:
            distNew[num] += 1
       else:
            distNew[num] = 1

         #  isPresent = distNew.get(num)
         #  print(f"sss",isPresent)
         #  if(isPresent != None):
        #     distNew.popitem(num) = distNew.get(num) + 1
          # else:
           #  distNew.pop(num,1) 
       print(distNew)
printDist()

def oddOrEven():
     list = [1,2,3,4,5,6,7,8]
     newList = []
     for item in list:
          if item % 2 == 0:
               newList.append(item)
     print(newList)
     newListTwo = [item % 2 == 0 for item in list]
     print(newListTwo)
     newListThree = [item * 2 for item in list]
     print(newListThree)

     students = [
          {"name" : "a" , "score":51},
          {"name" : "b" , "score":49},
          {"name" : "c" , "score":100}
     ]

     for student in students:
         if student["score"] >= 50:
              print(student["name"])
         
     passedStudents = ["pass" if student["score"] >= 50 else "fail" for student in students]
     print(passedStudents)

oddOrEven()

print("\n DSA")

ex_list = [1,2,3,"hi"]
ex_tuple = (1,2,3,"hi")


# ex_list[4] = "hey"
ex_list[3] = "hello"
print(f"ex_list {ex_list}\n")

# ex_tuple[4] = "hey"
# ex_tuple[3] = "hello"
print(f"ex_tuple {ex_tuple}\n")