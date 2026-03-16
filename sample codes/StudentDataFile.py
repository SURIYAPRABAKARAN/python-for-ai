class Students:
    pass

file = open("students.png","w")
file.write("Hi")

file.close()

file = open("students","r")

for i in file:
    print(i)
    
try:
    file = open("sss.txt")
    print(file.read())
except:
    print("File not found")
    
try:
    num = int(input("Enter number: "))
    result = 10 / num
    print(result)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")