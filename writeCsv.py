import pandas as pd
import numpy as np

def write():
    file=input("Enter the file name");
    number=int(input("Enter the number of files: "))
    for i in range(1,number+1):
        ar = []
        s=str(i)
        filename = file+str(i)+".csv"
        for j in range(1,51):
            ar.append(j*i)
        df = pd.DataFrame(ar,columns=["Number"])
        df.to_csv(filename)

write()

