import pandas as pd

df=pd.read_csv("data.csv")
#tall_pokemon=df[df["Height"]>=2]
#heavy_pok=df[df["Weight"]>100]
#lege_pok=df[df["Legendary"]==True]
#wat_pok=df[(df["Type1"]=="Water") | (df["Type2"]=="Water")]
fir_pok=df[(df["Type1"]=="Fire") & (df["Type2"]=="Flying")]
print(fir_pok)