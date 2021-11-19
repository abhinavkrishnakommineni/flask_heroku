import json

import pandas as pd

def codescdv(inputfiletext):
    data = pd.read_table(inputfiletext)
    data=data["Time Log:"].str.split(expand=True)
    count=0
    for i in data[0]:
       if("/" not in str(i)):
        data.iloc[count, :] = data.iloc[count, :].shift()
       count=count+1


    data['task'] = data[data.columns[4:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
    data['Time'] = data[data.columns[1:4]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
    # data.drop(data.columns[[range(1,24)]], axis=1, inplace=True)

    data=data.rename(columns={0:"Date"})
    data=data[["Date","Time","task"]]
    count1=0
    for i in data["Time"]:
       if(":" not in str(i)):
        data.iloc[count1, :] = data.iloc[count1, :].shift()
       count1=count1+1
    

    data["Time"] = data["Time"].str.lower()

    data=data.bfill().ffill()
    tokktk = json.loads(data.to_json(orient="index"))
    print(tokktk)
    return tokktk

# codescdv("/home/anvitha/Desktop/logproject/TimeLogCarbon.txt")

