
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

### Global setting of mpl
plt.rcParams['text.usetex'] = True
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 16}

plt.rc('font', **font)
plt.clf()


#### overhang and vertical fins
# results from IFC analysis

debcas=pd.read_csv('data/debords_casquettes_fins.csv',index_col=0)
# results from rtaa spreadsheet
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
plt.savefig('debords_casquettes_rtaa.png')
plt.clf()


#### overhang only
# results from IFC analysis
deb=pd.read_csv('data/debords_fins.csv',index_col=0)
# results from rtaa spreadsheet
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
plt.savefig('debords_rtaa.png')
plt.clf()


### evaluation of error by orientation and by model
error={'h':error_deb,'c':error_debcas}
err_pd=pd.DataFrame(data=error)
global_error=np.array(all_error).flatten().mean()
print(" Error by orientation and model")
print(err_pd)
print(' Global error (all orientation and models) :::  ',global_error,' \n')


rtaadebcas.drop('d/h',axis=1,inplace=True)
rtaadeb.drop('Unnamed: 0',axis=1,inplace=True)



print(" ### Raw values in Tex format ### \n")

print(' overhang (rtaa spreadsheet)')
s=rtaadeb.style.format(precision=2)
s.format_index(precision=1)
print(s.to_latex())


print(' overhang and fins (rtaa spreadsheet)')
s=rtaadebcas.style.format(precision=2)
s.format_index(precision=1)
print(s.to_latex())
print(' overhang (IFC)  ')
s=deb.style.format(precision=2)
s.format_index(precision=1)
print(s.to_latex())
print(' overhang and fins (IFC)  ')
s=debcas.style.format(precision=2)
s.format_index(precision=1)
print(s.to_latex())






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

