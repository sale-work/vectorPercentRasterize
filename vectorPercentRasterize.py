import sys
import os
import Rasterizer
os.environ["GDAL_DATA"] = r'C:\OSGeo4W64\share\gdal'

def main(argv):
    bdotMainDirPath = "G:/_temp/BDOT_to_samples/bdot"
    inputPercent = 100

    gdalDirPath = 'C:/OSGeo4W64/bin'
    workingDir = 'G:/_temp/BDOT_to_samples'
    r = Rasterizer.Rasterizer(gdalDirPath)
    r.prepareData(workingDir, bdotMainDirPath, inputPercent)
    r.doRasterize()



if __name__ == "__main__":
    main(sys.argv[1:])