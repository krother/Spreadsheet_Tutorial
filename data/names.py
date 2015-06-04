
import pandas as pd
import os

PATH = 'names/'

tables = []
for fn in os.listdir(PATH):
    if not fn.endswith('.txt'): continue
    print(fn)
    year = int(fn[-8:-4])
    #if year % 2: continue
    df = pd.read_csv(PATH + fn, names=['name', 'gender', 'count'])
    df['year'] = year
    tables.append(df)

names = pd.concat(tables)
del tables

# statistics on single names
nfind = lambda x:names[names['name']==x].sort('year')
male = lambda y:y[y['gender']=='M']
female = lambda x:x[x['gender']=='F']

# total population
g = names.groupby('year')
pop = g['count'].apply(sum)

# first letter
first = lambda x:x[0]
# names['first'] = names['name'].apply(first)

mr = names[names['gender']=='M']
mrc = mr.groupby('first')['count'].apply(sum)
fr = names[names['gender']=='F']
frc = mr.groupby('first')['count'].apply(sum)
mrc / frc

# names[names['first'] == 'Q'].groupby('name')['count'].apply(sum).sort()

years = pd.Series(sorted(set(names.year)))
