import pandas as pd

# =================== To Convert List Into Series ===================

# data = [101, 102, 103, 200 ,202]
# series = pd.Series(data, index=["a","b","c","d","e"])
# print(series.loc["a"]) # Location by index
# print(series.iloc[2]) # Location by lable
# series.loc["a"] = 100

# print(series[series < 200])

# =================== Dictionary ===================

calories = {
    "Day 1": 1750,
    "Day 2": 2000,
    "Day 3": 1700
}

# series = pd.Series(calories)

# series.loc["Day 3"] += 500

# # print(series.loc["Day 3"])
# print(series[series >= 2000])

# =================== Dataframes ===================

# data = {
#     "Name": ["Spongebob", "Patrick", "Squidward"],
#     "Age": [30, 25, 50]
# }

# df = pd.DataFrame(data)

# # print(df.iloc[2])

# # Add a column
# df["Job"] = ["Shef", "N/A", "Cashier"]
# # print(df)

# # Add a row

# data = {
#     "Name": ["Steve", "Crab"],
#     "Age": [18, 26],
#     "Job": ["Gamer", "Manager"]
# }
# # new_row = pd.DataFrame([{"Name": "Steve", "Age": 18, "Job": "Engineer"}])
# new_rows = pd.DataFrame(data)
# print(new_rows)

# df = pd.concat([df, new_rows])
# print(df)

# =================== Importing ===================

# df = pd.read_csv("data.csv", index_col="Name")

# # Selection by column/s
# # print(df[["Name", "Height"]])

# # Selection by rows/s

# # print(df.loc["Pikachu"])
# # print(df.loc["Pikachu", ["Height", "Weight"]])
# # print(df.loc["Charizard": "Pikachu", ["Height", "Weight"]])
# # print(df.iloc[0:11:2, 0:0])

# pokemon = input("Enter a pokemon name: ")

# try:
#     print(df.loc[pokemon])
# except KeyError:
#     print(f"{pokemon} not found")

# =================== Filtering ===================

# df = pd.read_csv("data.csv")

# # print(df[df["Height"] > 2.0])

# fire_pokemon = df[(df["Type1"] == "Water") |
#                   (df["Type2"] == "Water")]

# print(fire_pokemon)

# =================== Aggregation ===================

# df = pd.read_csv("data.csv")

# # All columns

# # print(df.mean(numeric_only=True))
# # print(df.max(numeric_only=True))
# # print(df.min(numeric_only=True))
# # print(df.sum(numeric_only=True))
# # print(df.count())

# # Single column
# # print(df["Height"].min())

# # Grouping

# group = df.groupby("Type1")

# print(group["Height"].mean())

# =================== Cleaning Data ===================

df = pd.read_csv("data.csv")

# df = df.drop(columns=["Legendary", "No"])

# df = df.dropna(subset=["Type2"])

# df = df.fillna({"Type2": "None"})

# df["Type1"] = df["Type1"].replace({"Grass": "GRASS"})

# df["Legendary"] = df["Legendary"].astype(bool)

df = df.drop_duplicates()

print(df)

