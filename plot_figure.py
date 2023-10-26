
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 16}

plt.rc('font', **font)


# prediction VS mesure
plt.clf()
debcas=pd.read_csv('data/debords_casquettes_fins.csv',index_col=0)
#rtaas=pd.read_csv('data/debords_casquette.xlsx')
rtaadebcas= pd.read_excel('data/debords_casquette.xlsx')
x=np.arange(0.1,1.1,.1)
debcas=debcas.set_index(x)
rtaadebcas=rtaadebcas.set_index(x)
columns=debcas.columns
colors=['r','g','b','k']
marks=['x','d','o']
orient=['N','E','S','W']
error_debcas={}
all_error=[]
for col,c,lab in zip(columns,colors,orient):
    plt.plot(x,debcas[col],'-',color=c,label=lab+' ref')
    plt.plot(x,rtaadebcas[col],'--',color=c,label=lab+' bim')
    err=np.abs(debcas[col]-rtaadebcas[col])
    error_debcas[col]=err.mean()
    all_error.append(err.values)
plt.xlabel('$d$')
plt.ylabel('$S_R$')

plt.ylim(0,1)
plt.xlim(0.1,1.0)

plt.legend(ncol=2,loc='lower left')
#plt.show()
plt.savefig('debords_casquettes_rtaa.png')


plt.clf()
deb=pd.read_csv('data/debords_fins.csv',index_col=0)
#rtaas=pd.read_csv('data/debords_casquette.xlsx')
rtaadeb= pd.read_excel('data/debords.xlsx')
x=np.arange(0.1,1.1,.1)
deb=deb.set_index(x)
rtaadeb=rtaadeb.set_index(x)
columns=deb.columns
colors=['r','g','b','k']
marks=['x','d','o']
error_deb={}
for col,c,lab in zip(columns,colors,orient):
    plt.plot(x,deb[col],'-',color=c,label=lab+' ref')
    plt.plot(x,rtaadeb[col],'--',color=c,label=lab+' bim')
    err=np.abs(deb[col]-rtaadeb[col])
    error_deb[col]=err.mean()
    all_error.append(err.values)
plt.xlabel('$d$')
plt.ylabel('$S_R$')
plt.ylim(0,1)
plt.xlim(0.1,1.0)


plt.legend(ncol=2)
#plt.show()
plt.savefig('debords_rtaa.png')
plt.clf()

error={'h':error_deb,'c':error_debcas}
err_pd=pd.DataFrame(data=error)
global_error=np.array(all_error).flatten().mean()
print(err_pd)
print('global error ',global_error)



deb_fin_tri=pd.read_csv('data/debords_casquettes_fins_triangle.csv',index_col=0)
deb_fin=pd.read_csv('data/debords_fins.csv',index_col=0)
deb_fin_cas=pd.read_csv('data/debords_casquettes_fins.csv',index_col=0)


#rtaas=pd.read_csv('data/debords_casquette.xlsx')

x=np.arange(0.1,1.1,.1)
deb_fin=deb_fin.set_index(x)

columns=deb_fin.columns[:1]
colors=['r','g','b','k']
marks=['x','d','o']

col='NORD'
c='k'


plt.plot(x,deb_fin[col],'-',color=c,label='h')
plt.plot(x,deb_fin_tri[col],'-',marker='o',color=c,label='ht')
plt.plot(x,deb_fin_cas[col],'--',color=c,label='hr')


plt.xlabel('$d$')
plt.ylabel('$S_R$')
plt.ylim(0,1)
plt.xlim(0.1,1.0)

plt.legend()
#plt.show()
plt.savefig('debords_casquette_triangle.png')



"""
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
"""
#plt.show()
"""

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
"""