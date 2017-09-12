import pandas

df=pandas.read_csv("Train_1.csv",header=None)
y=df.iloc[:,-1]
df=df.iloc[:,0:41]
df=(df-df.min())/(df.max()-df.min())*100
df.join(y)
df.to_csv("Train.csv")

df=pandas.read_csv("Test_1.csv",headers=None)
y=df.iloc[:,-1]
df=df.iloc[:,0:41]
df=(df-df.min())/(df.max()-df.min())*100
df.join(y)
df.to_csv("Test.csv")
