import pandas as pd
import os

folder_path = "/" # Change to your file name
combined = pd.DataFrame()
count = 0

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if filename.endswith(".txt"):
        print(filename)
        # df = pd.read_csv(filename)

        column_names = ['Unnamed: 0', filename + ", Tau ", "G2 Fit ", "Error ", "R-Size ", "Prob "]
        df = pd.read_csv(filename, delimiter="|", header=0, names=column_names, usecols=column_names, skiprows=0)
        df.drop(['Unnamed: 0'], axis=1, inplace=True) # drop unnecessary column
        df = df.iloc[1:] # remove first row
        # df.columns = column_names

        if combined.empty:
            combined = df
        else:
            combined = combined.join(df, rsuffix=str(count))
        count += 1
        combined.to_csv('combined.csv', index=False) 
        # print(combined.head())

        

