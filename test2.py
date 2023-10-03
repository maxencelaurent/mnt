import os
from osgeo import ogr, gdal
from gdalconst import *
import numpy as np

# Input DEM
filename = raw_input("Input DEM FILE : ")
dem = gdal.Open( filename, GA_ReadOnly )
geotransform = dem.GetGeoTransform()
DEM_Value = np.array(dem_surface.GetRasterBand(1).ReadAsArray(), dtype ="float") #Raster to Array

# Determine Basic Raster's Parameter
Col = dem.RasterXSize
Row = dem.RasterYSize
Origin_X = geotransform[0]
Origin_Y = geotransform[3]
Cell_Size = geotransform[1]
CRS = dem.GetProjection() # make sure that CRS is on geographic coordinate system because you use lat/long 

#Coordinate in row and column
X =  input("Input longitude Coordinate :")
Y =  input("Input latitude Coordinate :")
# This is formula to define cell's column and row base on X and Y
# Try to sketch it so you can understand or maybe there's something wrong with my formula
col_x = int(((X - Origin_X)/Cell_Size)+1) 
row_y = int(((Origin_Y - Y)/Cell_Size)+1)  

#Get cell's value as height
H = DEM_Value[row_y-1][col_x-1] # why it should be reduce by 1? because array's index start from 0 
print H
