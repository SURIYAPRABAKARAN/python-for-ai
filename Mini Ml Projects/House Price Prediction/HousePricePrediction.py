import pandas as pd

# brokered_by,status,price,bed,bath,acre_lot,street,city,state,zip_code,house_size,prev_sold_date
# 103378    ,for_sale,105000,3,2,   0.12, 1962661,Adjuntas,Puerto Rico,601,920,
# 
# data set loaded and converted into data frame
df = pd.read_csv("Mini Ml Projects/House Price Prediction/House_Price_data.csv")


# data cleaning
df = df.drop(['brokered_by', 'prev_sold_date'], axis=1)
df['bath'] = df['bath'].fillna(df['bath'].median())
# Condition: bed is null OR bed is 0
mask = (df['bed'].isna()) | (df['bed'] == 0)
# Fill bed = bath + 1 where condition is true
df.loc[mask, 'bed'] = df.loc[mask, 'bath'] + 1
df['acre_lot'] = df['acre_lot'].fillna(df['acre_lot'].median())



def findTheState(df:pd.DataFrame):
    null_index = df[df['state'].isnull()].index
    for i in null_index:
        street_name = df.loc[i, 'street']
    
    # find state from another row with same street
        state_value = df[df['street'] == street_name]['state'].dropna()
    
        if len(state_value) > 0:
            df.loc[i, 'state'] = state_value.iloc[0]
        
def findTheCity(df:pd.DataFrame):
    null_index = df[df['city'].isnull()].index
    for i in null_index:
        street_name = df.loc[i, 'street']
    
    # find city from another row with same street
        city_value = df[df['street'] == street_name]['city'].dropna()
    
        if len(city_value) > 0:
            df.loc[i, 'city'] = city_value.iloc[0]
        
findTheState(df)
findTheCity(df)
print(df.isna().sum())