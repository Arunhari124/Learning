import pandas as pd

dict={"names":["arun","vipin","nigga"],
      "Age":[30,35,50]}



df=pd.DataFrame(dict,index=["a",'b','c'])
#colum
df["job"]=["job1",'job2','job3']
#row

nw_rows=pd.DataFrame([{"names":"sandy","Age":15,"job":"engin"},
                      {"names":"eugwnw","Age":60,"job":"man"}]
                     ,index=["d","e"])
df=pd.concat([df,nw_rows])
print(df)