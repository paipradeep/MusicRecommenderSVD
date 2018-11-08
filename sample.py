import pandas as pd

df = pd.read_csv("modifiedDataset.csv")

userNewId = 1
userDict = {}

users = df['user_id']

for u in users:
	if u in userDict.keys():
		pass
	else:
		userDict[u] = userNewId
		userNewId += 1

songNewId = 1
songDict = {}

songs = df['song_id']

for s in songs:
	if s in songDict.keys():
		pass
	else:
		songDict[s] = songNewId
		songNewId += 1

for i in range(0,len(df)):
	temp = df.loc[i,'song_id']
	temp2 = df.loc[i,'user_id']
	df.loc[i,'song_id'] = songDict[temp]
	df.loc[i,'user_id'] = userDict[temp2]

df.to_csv('FinalDataset.csv',sep=",")


