import arcpy
from arcpy import env
from arcpy.sa import *

cc10_list = [
110000 ,
120000 ,
130100 ,
130200 ,
130300 ]  # not including all 


for year in [1995,2000,2005,2008,2010,2013]:
    for cc10 in cc10_list:
        expression = '"'+'tif_urban51_reclassify_'+str(year)+'"'+ ' * ' + '"'+'distance_'+str(cc10)+'"'
        output = "E:/GuanghuaRA/direction_analysis/urban_multi_distance.gdb/"+"urban_multi_distance_"+str(year)+"_"+str(cc10)
        arcpy.gp.RasterCalculator_sa(expression,output)


#arcpy.gp.RasterCalculator_sa(""""tif_urban1990_51" * "distance_110000"""","E:/GuanghuaRA/direction_analysis/every_feature.gdb/beijing_1990")
