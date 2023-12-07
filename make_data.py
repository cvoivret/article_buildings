import sys
sys.path.append("../rtaa_ifc/")
from rtaa_ifc import solar   

import numpy as np  
from collections import defaultdict
import pandas as pd

    
filename_list=['data/debords_casquettes_fins.ifc',
               'data/debords_fins.ifc',
               'data/debords_casquettes_fins_triangle.ifc']
                
tn_angle=[0.0,np.pi*.5,np.pi,3.*np.pi*.5]
orientations_name=['NORD','EST','SUD','OUEST']

config={name:(angle) for name,angle in zip(orientations_name,tn_angle)}
    
res=[]

totake=orientations_name#['NORD']
list_angle= [ config[n] for n in totake]
              


for filename in filename_list:
    rss=solar.rtaa_solar_study(filename)
    rss.add_building_elements([],['IfcWall','IfcSlab'])
    rss.add_solar_elements([],['IfcWindow','IfcDoor'])
    rss.set_geometries()
        
    cm_orientation=defaultdict(list)   
    for angle,orient in zip(list_angle,totake):
        rss._proj_loc.update_northing_from_angle(angle)
        rss.run()
        cm_orientation[orient]=rss.cm()
    
    res=pd.DataFrame(cm_orientation)
    res=res.sort_values(by='NORD',ascending=False)
    res.to_csv(filename[:-3]+'csv')
    
    
