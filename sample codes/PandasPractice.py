import pandas as pd

data = {
    "names" : ["suriya","arun","kumar"],
    "age" : [25,15,45],
    "course": ["AI ENGINEER","Data Analyze","ML"]
}

df = pd.DataFrame(data)
print(f"data frame \n{df}\n\n")
print(f"names \n{df["names"]}\n\n")
print(f"head \n{df.head()}\n\n")
print(f"shape \n{df.shape}\n\n")
print(f"tail \n{df.tail()}\n\n")
print(f"coulmns \n{df.columns}\n\n")

dataProduct = {
    "Product": ["Laptop", "Mobile", "Tablet"],
    "Price": [70000, 30000, 25000],
    "Quantity": [2, 5, 3]
}

pdoductPd = pd.DataFrame(dataProduct)

print(f"data product \n {pdoductPd} \n")

print(f"Product \n {pdoductPd["Product"]} \n")

print(f"first 2 row \n {pdoductPd[0:2]} \n")

print(f"shape \n {pdoductPd.shape} \n")

print(f"filter \n {df[df["age"] > 24]}\n")

print(f"multiple filter \n{df[(df['age'] > 24) & (df['course'] == 'AI ENGINEER')]}\n")

print(f"multiple columns \n{df[["age","course"]]}\n")

print(f"zero row \n {df.loc[0]}\n")


print(f"first row \n {df.iloc[1]}\n")


data_csv = pd.read_csv("data.csv")

print(data_csv)

filtered_df = data_csv[data_csv["Name"] == "Suriya"]

filtered_df.to_csv("filtered_data.csv",index=False)

filter_data = pd.read_csv("filtered_data.csv")

print(f"filter \n {filter_data} \n")

# handling dirty data - data cleaning

dirty_data_loading = pd.read_csv("dirty_data.csv")

print(f"dirty data \n{dirty_data_loading}\n")

print(f"missing null \n{dirty_data_loading.isnull()}\n")

print(f"missing null sum \n{dirty_data_loading.isnull().sum()}\n")

print(f"remove null rows \n{dirty_data_loading.dropna()}\n")

dirty_data_loading["Age"] = dirty_data_loading["Age"].fillna( dirty_data_loading["Age"].mean())

print(f"after fill the age \n{dirty_data_loading}\n")

dirty_data_loading["Marks"] = dirty_data_loading["Marks"].fillna(0)

print(f"after fill the mark \n{dirty_data_loading}\n")

cleaned_data = dirty_data_loading.to_csv("cleaned_data.csv",index=False)

final_cleaned_data = pd.read_csv("cleaned_data.csv")

print(f"final_cleaned_data \n{final_cleaned_data}\n")

