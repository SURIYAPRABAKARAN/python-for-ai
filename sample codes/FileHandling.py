class Product:
    def __init__(self,product_name,product_price):
        self.product_name = product_name
        self.product_price = product_price
    
    def display(self):
        print(f"name : {self.product_name}, price : {self.product_price}")
        
p1 = Product("Laptop", 70000)
p2 = Product("Mobile", 30000)
p3 = Product("Tablet", 25000)
p1.display()

file = open("product.txt","w")


file.write(p1.product_name + " " + str(p1.product_price) + "\n")
file.write(p2.product_name + " " + str(p2.product_price) + "\n")
file.write(p3.product_name + " " + str(p3.product_price) + "\n")

file.close()

# file = open("product.txt", "w")
file = open("product.txt", "r")

for line in file:
    print(line)

file.close()