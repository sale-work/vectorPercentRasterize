import sys

import Rasterizer


def main(argv):
    bdotMainDirPath = "H://S2GLC//data//bdot//bdot"
    inputPercent = 1

    gdalDirPath = 'F:/OSGeo4W64/bin'
    workingDir = 'F:/MarcinRybicki/codes/BAMS/vectorPercentRasterize/workdir/s2glc2020ForValidation'
    r = Rasterizer.Rasterizer(gdalDirPath)
    r.prepareData(workingDir, bdotMainDirPath, inputPercent)
    r.doRasterize()



if __name__ == "__main__":
    main(sys.argv[1:])