import pandas as pd
import os
import glob
import numpy as np

d=os.listdir()
dd=[]
for i in d:
    if i.endswith('.json'):
        dd.append(i)


df=pd.read_json(path_or_buf=dd[0],orient='index')
print('complete >>', dd[0])

for i in range(1,len(dd)):
    try:
        df1=pd.read_json(path_or_buf=dd[i],orient='index')
    except:
        print('file is not reading in dataframe >>>>', dd[i])
    
    try:
        df=pd.concat([df,df1],ignore_index=True)
    except:
        print('while concat having issues >>>',dd[i])
    
    
    print('complete >>', dd[i])


#to json logi
try:
    df.to_json('output.json',orient='records')
    
    print('Done ')
except:
    print('problem to json file')