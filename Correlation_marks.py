import pandas as pd
import plotly.express as px
import csv
import numpy as np
def getDataSource(path):
    marks=[]
    days=[]
    with open(path) as csvFile:
        df=csv.DictReader(csvFile)
        for row in df:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
    return{"x":marks,"y":days}
def findCorrelation(source):
    correlation=np.corrcoef(source["x"],source["y"]) 
    print(correlation) 
def setup():
    path="./studentActivity3_c106.csv"      
    source=getDataSource(path)
    findCorrelation(source)    
setup()    