
"""
tn_angle=[0.0,np.pi*.5,np.pi,3.*np.pi*.5]
orientations_name=['NORD','EST','SUD','OUEST']

config={name:(angle) for name,angle in zip(orientations_name,tn_angle)}
    
res=[]

totake=orientations_name#['NORD']
list_angle= [ config[n] for n in totake]

x=np.arange(0.15,1.15,.1)

filename = 'data/debords_casquettes_fins_triangle.ifc'
rss=rtaa_solar_study(filename)
rss.add_building_elements([],['IfcWall','IfcSlab'])
rss.add_solar_elements([],['IfcWindow','IfcDoor'])
rss.set_geometries()
    
cm_orientation=defaultdict(list)   
for angle,orient in zip(list_angle,totake):
    rss._proj_loc.update_northing_from_angle(angle)
    #rss.display(True)
    rss.run()
    cm_orientation[orient]=rss.cm()

res=pd.DataFrame(cm_orientation)
res=res.sort_values(by='NORD',ascending=False)
res.to_csv(filename[:-3]+'csv')

"""
import sys
sys.path.append("../rtaa_ifc/")
from shadow import *     


    
filename_list=['data/debords_casquettes_epais.ifc',
                'data/debords_casquettes_fins.ifc',
                'data/debords_epais.ifc',
                'data/debords_fins.ifc',
                'data/debords_casquettes_fins_triangle.ifc']
                
tn_angle=[0.0,np.pi*.5,np.pi,3.*np.pi*.5]
orientations_name=['NORD','EST','SUD','OUEST']

config={name:(angle) for name,angle in zip(orientations_name,tn_angle)}
    
res=[]

totake=orientations_name#['NORD']
list_angle= [ config[n] for n in totake]

x=np.arange(0.15,1.15,.1)                
                


for filename in filename_list[4:]:
    rss=rtaa_solar_study(filename)
    rss.add_building_elements([],['IfcWall','IfcSlab'])
    rss.add_solar_elements([],['IfcWindow','IfcDoor'])
    rss.set_geometries()
        
    cm_orientation=defaultdict(list)   
    for angle,orient in zip(list_angle,totake):
        rss._proj_loc.update_northing_from_angle(angle)
        #rss.display(True)
        rss.run()
        cm_orientation[orient]=rss.cm()
    
    res=pd.DataFrame(cm_orientation)
    res=res.sort_values(by='NORD',ascending=False)
    res.to_csv(filename[:-3]+'csv')
    
    """
    rtaa_data= pd.read_excel('data/debords_casquette.xlsx')
        
    colors=['r','g','b','k']
    marks=['x','d','o']
    #for cmo,m in zip(cm_orientation,marks):
    for name,c in zip(cm_orientation.keys(),colors):
        data=list(cm_orientation[name].values())
        data.sort(reverse=True)
        plt.plot(x,data,'-',color=c,marker='o',lw=2,label=name+'_computed')
    
    for name,c in zip(totake,colors):
        plt.plot(x,rtaa_data[name],'--',color=c,lw=2,label=name+'_ref')
    plt.ylim(0,1)
    plt.xlim(0.1,1.1)
    plt.legend()
    plt.show()
    """
