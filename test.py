from math import floor
from osgeo import gdal,ogr

src_filename = './swissalti3d_2019_2566-1222_0.5_2056_5728.tif'
shp_filename = './line.geojson'

src_ds=gdal.Open(src_filename) 
gt_forward=src_ds.GetGeoTransform()
gt_reverse=gdal.InvGeoTransform(gt_forward)
rb=src_ds.GetRasterBand(1)

ds=ogr.Open(shp_filename)

lyr=ds.GetLayer()

for feat in lyr:
    geom = feat.GetGeometryRef()
    # Put points each meter
    geom.Segmentize(1)

    for point in geom.GetPoints():

        mx,my=point[0], point[1]  #coord in map units

        #Convert from map to pixel coordinates.
        px, py = gdal.ApplyGeoTransform(gt_reverse, mx, my)
        px = floor(px) #x pixel
        py = floor(py) #y pixel

        intval=rb.ReadAsArray(px,py,1,1)
        print (intval[0]) #intval is a numpy array, length=1 as we only asked for 1 pixel value

