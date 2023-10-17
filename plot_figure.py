
import numpy as np
import pandas as pd
import sunposition as sunpos
from  datetime import datetime
from timezonefinder import TimezoneFinder
import pytz

import matplotlib.pyplot as plt

# fin VS epais
plt.clf()
deb_fin=pd.read_csv('data/debords_fins.csv',index_col=0)
deb_epais=pd.read_csv('data/debords_epais.csv',index_col=0)
x=np.arange(0.1,1.1,.1)
deb_fin=deb_fin.set_index(x)
deb_epais=deb_epais.set_index(x)
columns=deb_fin.columns
colors=['r','g','b','k']
marks=['x','d','o']

for col,c in zip(columns,colors):
    plt.plot(x,deb_fin[col],'-',color=c,label=col+'_fin')
    plt.plot(x,deb_epais[col],'--',color=c,label=col+'_epais')
plt.ylim(0,1)
plt.xlim(0.0,1.1)
plt.legend()
plt.savefig('debords.png')

#plt.show()


# fin VS epais casquette
plt.clf()
deb_fin=pd.read_csv('data/debords_casquettes_fins.csv',index_col=0)
deb_epais=pd.read_csv('data/debords_casquettes_epais.csv',index_col=0)
x=np.arange(0.1,1.1,.1)
deb_fin=deb_fin.set_index(x)
deb_epais=deb_epais.set_index(x)

for col,c in zip(columns,colors):
    plt.plot(x,deb_fin[col],'-',color=c,label=col+'_fin')
    plt.plot(x,deb_epais[col],'--',color=c,label=col+'_epais')

plt.ylim(0,1)
plt.xlim(0.0,1.1)

plt.legend()
plt.savefig('debords_casquette.png')

#plt.show()

# prediction VS mesure
plt.clf()
deb_fin=pd.read_csv('data/debords_casquettes_fins.csv',index_col=0)
#rtaas=pd.read_csv('data/debords_casquette.xlsx')
rtaa= pd.read_excel('data/debords_casquette.xlsx')
x=np.arange(0.1,1.1,.1)
deb_fin=deb_fin.set_index(x)
rtaa=rtaa.set_index(x)
columns=deb_fin.columns
colors=['r','g','b','k']
marks=['x','d','o']

for col,c in zip(columns,colors):
    plt.plot(x,deb_fin[col],'-',color=c,label=col)
    plt.plot(x,rtaa[col],'--',color=c,label=col+'_rtaa')

plt.ylim(0,1)
plt.xlim(0.0,1.1)

plt.legend()
#plt.show()
plt.savefig('debords_casquettes_rtaa.png')


plt.clf()
deb_fin=pd.read_csv('data/debords_fins.csv',index_col=0)
#rtaas=pd.read_csv('data/debords_casquette.xlsx')
rtaa= pd.read_excel('data/debords.xlsx')
x=np.arange(0.1,1.1,.1)
deb_fin=deb_fin.set_index(x)
rtaa=rtaa.set_index(x)
columns=deb_fin.columns
colors=['r','g','b','k']
marks=['x','d','o']

for col,c in zip(columns,colors):
    plt.plot(x,deb_fin[col],'-',color=c,label=col)
    plt.plot(x,rtaa[col],'--',color=c,label=col+'_rtaa')

plt.ylim(0,1)
plt.xlim(0.0,1.1)

plt.legend()
#plt.show()
plt.savefig('debords_rtaa.png')


plt.clf()
deb_fin_tri=pd.read_csv('data/debords_casquettes_fins_triangle.csv',index_col=0)
deb_fin=pd.read_csv('data/debords_fins.csv',index_col=0)
deb_fin_cas=pd.read_csv('data/debords_casquettes_fins.csv',index_col=0)


#rtaas=pd.read_csv('data/debords_casquette.xlsx')

x=np.arange(0.1,1.1,.1)
deb_fin=deb_fin.set_index(x)
rtaa=rtaa.set_index(x)
columns=deb_fin.columns
colors=['r','g','b','k']
marks=['x','d','o']

for col,c in zip(columns,colors):
    plt.plot(x,deb_fin[col],'-',color=c,label=col)
    plt.plot(x,deb_fin_tri[col],'--',color=c,label=col+'_tri')
    plt.plot(x,deb_fin_cas[col],'--',marker='o',color=c,label=col+'_all')


plt.ylim(0,1)
plt.xlim(0.0,1.1)

plt.legend()
#plt.show()
plt.savefig('debords_casquette_triangle.png')

