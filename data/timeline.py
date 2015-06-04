
import pylab as m


import pandas as pd
import os

PATH = 'names/'

girls, boys = [], []

for fn in sorted(os.listdir(PATH)):
    if not fn.endswith('.txt'): continue
    print(fn)
    year = int(fn[-8:-4])
    #if year % 10: continue
    df = pd.read_csv(PATH + fn, names=['gender', year], index_col=0)
    boy = df[df.gender=='M'][year]
    girl = df[df.gender=='F'][year]
    boys.append(boy)
    girls.append(girl)

girls = pd.DataFrame(girls).fillna(0)
boys = pd.DataFrame(boys).fillna(0)

tgirls = girls.transpose()
tboys = boys.transpose()

tgirls['sum'] = girls.apply(sum)
tboys['sum'] = boys.apply(sum)

"""
biggirls = tgirls[tgirls['sum']>=1000]
biggirls.to_csv('girls_1000.csv')

bigboys = tboys[tboys['sum']>=1000]
bigboys.to_csv('boys_1000.csv')

# last 25 years 
sum25 = lambda x:sum(list(x)[-25:])
tgirls['sum25'] = girls.apply(sum25)
tboys['sum25'] = boys.apply(sum25)

recent = girls.index[-25:]

tgirls25 = tgirls[recent][tgirls['sum25']>=100]
tgirls25.to_csv('girls_last25.csv')

tboys25 = tboys[recent][tboys['sum25']>=100]
tboys25.to_csv('boys_last25.csv')
"""
