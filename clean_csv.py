import pandas as pd
df = pd.read_csv('bcci_batting_test.csv')

df = df.replace('-', '0')
df.to_csv('BCCI_Test_Batting.csv', index=False)