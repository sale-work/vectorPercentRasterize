import sys

import Rasterizer


def main(argv):
    # inputRaster = argv[0]
    # bdotMainDirPath = argv[1]
    # inputPercent = argv[2]
    # outputRaster = argv[3]

    inputRaster = "N:/BAMS/34UED/budynki_agregacja_RF_2.tif"
    bdotMainDirPath = "N:/BAMS/BDOT/1625_DIO_7211_86_2020_4_02_2020/1625_BDOT10k"
    inputPercent = 75
    outputRaster = "F:/MarcinRybicki/projects/BAMS/rasterize/workspace/test70p.tif"

    gdalDirPath = 'F:/OSGeo4W64/bin'
    workingDir = 'F:/MarcinRybicki/codes/BAMS/vectorPercentRasterize/workdir'
    r = Rasterizer.Rasterizer(gdalDirPath)
    r.prepareData(workingDir, inputRaster, bdotMainDirPath, inputPercent, outputRaster)
    r.doRasterize()



if __name__ == "__main__":
    main(sys.argv[1:])