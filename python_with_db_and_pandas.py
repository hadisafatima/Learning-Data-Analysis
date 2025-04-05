import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

username = "root"
password = "hadisa69_sql"
host = "localhost"
port = "3306"
database = "Online_course_management_system"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}") # for creating connection of database with python

query = "select * from Students where id/10 = 1 or id/10 = 2 or id/10 = 3 or id/10 = 4 or id/10 = 5" # this can be any query even complex ones

ocms = pd.read_sql(query, con = engine) # "con" is connection argument

print(ocms.head()) # provide first 5 rows' data of the dataset
print(ocms.describe()) # provides statistical properties of the numerical col's data
print(ocms.info()) # provide datatypes of each col
print(ocms.shape) # provides total no: of rows and cols as a tuple such as (rows, cols)

print(ocms["id"].value_counts().plot(kind = "pie", figsize = (10,10))) # plots the mentioned numeric col of Students table, id, as a graph
plt.show() # this method shows/represents the graph in a seprate window