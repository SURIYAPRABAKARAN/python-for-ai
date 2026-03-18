import pandas as pd

data = {
    "names" : ["suriya","arun","kumar"],
    "age" : [25,35,45],
    "course": ["AI ENGINEER","Data Analyze","ML"]
}

df = pd.DataFrame(data)
print(df)