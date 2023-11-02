import opendp
import pandas as pd

df = pd.read_csv("forbes_2640_billionaires.csv")
df.columns = ['rank', 
              'name', 
              'forbes_id', 
              'net_worth', 
              'age', 
              'age_range', 
              'country', 
              'source', 
              'industry', 
              'Age', 
              'Source of Wealth', 
              'Self-Made Score', 
              'Philanthropy Score', 
              'Residence', 
              'Citizenship', 
              'Marital Status', 
              'Children', 
              'Education', 
              'Bachelor', 
              'Master', 
              'Doctorate', 
              'Drop Out', 
              'Self Made']

del df["name"]
del df["forbes_id"]
