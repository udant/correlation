import pandas as pd
import plotly.express as px
import csv
import numpy as np
def getDataSource(path):
    coffee=[]
    sleep=[]
    with open(path) as csvFile:
        df=csv.DictReader(csvFile)
        for row in df:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return{"x":coffee,"y":sleep}
       # fig=px.scatter(df,x='Temperature',y='Ice-cream Sales')
        #fig.show()
def findCorrelation(source):
    correlation=np.corrcoef(source["x"],source["y"]) 
    print(correlation) 
def setup():
    path="./studentActivity4_c106.csv"      
    source=getDataSource(path)
    findCorrelation(source)    
setup()    