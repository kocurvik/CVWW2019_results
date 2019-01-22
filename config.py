# -*- coding: utf-8 -*-

"""
For which systems the evaluation should be done.
It needs to be in the results dir defined in dataset_info.py
"""
RUN_FOR_SYSTEMS = ( "CVWW2019_Transform3D",
                    "CVWW2019_Transform2D",
                    "CVWW2019_Orig2D")
                    
"""
For which video the evaluation should be done. 
You can use keys A,B or C.
See dataset_info.py for more information and 
training videos for each splitting
"""
RUN_FOR_VIDEOS = SPLIT_TEST_VIDEOS["C"]


"""
Defines systems and thresholds
If a speed estmiation error for a system in the set is larger
then the threshold, the trajectory is shown
WARNING: You need to delete the cached results (or use -rc argument)
"""
SHOW_BAD_FOR_SYSTEMS = set()
SHOW_BAD_THRESHOLD = 30


"""
If true, vehicles' trajectories for which the computation
of intersections wihh measurement lines failes are shown
WARNING: You need to delete the cached results (or use -rc argument)
"""
SHOW_ERRORS = False



#%%
"""
##############################################################
################### PRESENTATION HELPER FUNCTIONS ############
##############################################################
"""

"""
Conversions for plotting and printing statistics
"""
def labelConversion(systemId):
    return systemId

"""
Styles for cumulative histograms
"""
def plotStyleCumulativeHist(systemId):
    styleDict = {"linewidth":2}
    return styleDict


"""
Styles for error histograms
"""
def plotStyleErrorHist(systemId):
    styleDict = {"linewidth":2}
    return styleDict
    
