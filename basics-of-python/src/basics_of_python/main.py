def main():
    print("Hello I'm suriya here")
    name = "suriya"
    age = 10
    print("name==> "+name)
    print(type(name))
    print(type(age))
    a,b= 10,25
    a,b=b,a
    print(a , b)
    result =   add(a,b)
    print("result==> ",result)
    if(result == 5):
        print('that was me')
    else:
        print('not me')
        greet()

def add(a,b):
    return a+b

def greet(name='Guest'):
    print("Hey ",name)


if __name__ == "__main__":
    main()   