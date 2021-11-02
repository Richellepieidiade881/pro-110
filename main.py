from pandas.io.parsers import read_csv
import plotly.figure_factory as ff
import plotly.graph_objects as go 
import statistics
import random 
import csv 
import pandas as pd 
df=read_csv("newdata.csv")
data=df["average"].tolist()
def random_mean (counter):
    dataset=[]
    for i in range (0,counter):
        index=random.randint(0,len(data)-1)
        value=data[index]
        dataset.append(value)

    mean=statistics.mean(dataset)
    return mean

def showfigure(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["average"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines"))
    fig.show 

def mean():
    mean_list=[]
    for i in range (0,1000):
        mean=random_mean(100)
        mean_list.append(mean)

    showfigure(mean_list)
    sd=statistics.stdev(mean_list)
    print(sd)

mean()
