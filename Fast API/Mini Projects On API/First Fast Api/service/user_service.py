
def get_all():
    return {"name":"suriya",
            "age" : 25,
            "skills" : ["Java","python","ML"]}


def get_with_name(name: str):
    print(f"from service layer : {name}")
    return {"name":{name}}

def calculate_square(number : int):
    return number * number