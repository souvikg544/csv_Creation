import os, glob
import pandas as pd

path = "D:/python projects/Assignment1"

all_files = glob.glob(os.path.join(path, "*.csv"))

all_df = []
for f in all_files:
    df = pd.read_csv(f, sep=',')
    df['file'] = f.split('1')[-1]
    all_df.append(df)

merged_df = pd.concat(all_df, ignore_index=True,sort = True)
merged_df.to_csv("merged.csv")
df1=pd.read_csv("merged.csv")
df2=df1[['Number','file']]
print(df2)