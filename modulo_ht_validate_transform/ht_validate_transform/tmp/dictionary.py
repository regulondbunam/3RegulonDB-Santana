import os
import pandas as pd
import json


path = 'datasets/Park2019-HTGeneExpression_v3.0.xlsx'
df = pd.read_excel(path, sheet_name="Dataset", header=4, 
    usecols=["Metadata Label", "Value", "Comments"], nrows=12)

df['Metadata Label'] = df['Metadata Label'].str.replace(r'[\#\:]', '')
df['Metadata Label'] = df['Metadata Label'].str.replace(r'\s', '_')
df = df.where(pd.notnull(df), None)
metadata_dict = {row['Metadata Label'] : {"value": row['Value'], 
    "comments": row['Comments']} for index, row in df.iterrows()}

with open('metadata1.json', 'w') as file:
    json.dump(metadata_dict, file, indent=4,separators =(", ", " : "))