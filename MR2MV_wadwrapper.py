#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 16:30:34 2023

@author: tschakel
"""

# runfile('/smb/user/tschakel/BLD_RT_RESEARCH_DATA/USER/tschakel/projects/wadqc/QAtests/MR2MV/MR2MV/MR2MV_wadwrapper.py', args='-r results.json -c config/mr2mv_config.json -d /smb/user/tschakel/BLD_RT_RESEARCH_DATA/USER/tschakel/projects/wadqc/QAtests/MR2MV/MR2MV/data/dataset1', wdir='/smb/user/tschakel/BLD_RT_RESEARCH_DATA/USER/tschakel/projects/wadqc/QAtests/MR2MV/MR2MV')

from wad_qc.module import pyWADinput
from wad_qc.modulelibs import wadwrapper_lib

if __name__ == "__main__":
    data, results, config = pyWADinput()
    
    # Log which series are found
    data_series = data.getAllSeries()
    print("The following series are found:")
    for item in data_series:
        print(item[0]["SeriesDescription"].value+" with "+str(len(item))+" instances")
        
    for name,action in config['actions'].items():
        if name == 'acqdatetime':
            filters = action["filters"]
            datetime_series = data.getInstanceByTags(filters["datetime_filter"])
            dt = wadwrapper_lib.acqdatetime_series(datetime_series[0])
            results.addDateTime('AcquisitionDateTime', dt) 
            
    results.write()