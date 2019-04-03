import pandas as pd

df = pd.read_json("./famous_restaurant.json")


df_sum = df.groupby("bloggername").count()


bloggernames = df['bloggername']


print(df.count())

print(df_sum)

print(bloggernames)
