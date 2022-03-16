from osgeo import gdal
import numpy as np
import os
from pathlib import Path

import BdotClass
import County
import PathsManager
import Tile


class Rasterizer:
    inputRaster = ''
    percent = 0
    outputRaster = ''
    workdir = ''
    gdalRasterizePath = ''
    gdalTranslatePath = ''
    gdalTindexPath = ''
    temp1percentRasterPath = ''
    tempSum1percentRasterPath = ''
    tempNormalRasterPath = ''
    resultPath = ''
    bdotMainDirPath = ''
    BdotClasses = []
    tiles = []
    outputCommandsFilePath = ''
    outputCommandsFileHandle = 0
    currentReferenceTif = None
    currentTile = None
    Xsize = 0
    Ysize = 0
    nominalSpatialResolution = 0
    resultMatrix = None

    def __init__(self, gdalDirPath):
        self.gdalRasterizePath = gdalDirPath + '/gdal_rasterize'
        self.gdalTranslatePath = gdalDirPath + '/gdal_translate'
        self.gdalTindexPath = gdalDirPath + '/gdaltindex'
        self.fillBdotClasses()
        self.fillTilesWithCounties()

    def fillBdotClasses(self):
        # self.BdotClasses.append(BdotClass.BdotClass('BUBD', 62))
        # self.BdotClasses.append(BdotClass.BdotClass('PTKM', 62))
        # self.BdotClasses.append(BdotClass.BdotClass('SKDR', 62))
        # self.BdotClasses.append(BdotClass.BdotClass('OIMK', 105))
        # self.BdotClasses.append(BdotClass.BdotClass('OISZ', 105))
        #
        # self.BdotClasses.append(BdotClass.BdotClass('PTRK', 103))
        # self.BdotClasses.append(BdotClass.BdotClass('PTTR', 102, "x_kod ='PTTR01'"))
        self.BdotClasses.append(BdotClass.BdotClass('PTTR', 73, "x_kod ='PTTR02'"))
        # self.BdotClasses.append(BdotClass.BdotClass('PTLZ', 83, "rodzaj='Las' and kategoria='lisciasty'"))
        # #
        # self.BdotClasses.append(BdotClass.BdotClass('PTLZ', 83, "rodzaj='Las' and kategoria='iglasty'"))
        # self.BdotClasses.append(BdotClass.BdotClass('PTWP', 162))
        # #
        # self.BdotClasses.append(BdotClass.BdotClass('PTGN', 121)) #, "rodzaj='piargUsypiskoRumowiskoSkalne'"
        # self.BdotClasses.append(BdotClass.BdotClass('PTWZ', 121, "x_kod ='PTWZ01'"))
        ###
        # self.BdotClasses.append(BdotClass.BdotClass('PTWP', 3))
        #
        # self.BdotClasses.append(BdotClass.BdotClass('BUCM', 21))
        # self.BdotClasses.append(BdotClass.BdotClass('BUSP', 21))
        # self.BdotClasses.append(BdotClass.BdotClass('KUKO', 21))
        # self.BdotClasses.append(BdotClass.BdotClass('OIKM', 21))
        #
        # self.BdotClasses.append(BdotClass.BdotClass('PTPL', 21))
        # self.BdotClasses.append(BdotClass.BdotClass('BUIB', 21))
        # self.BdotClasses.append(BdotClass.BdotClass('PTLZ', 20))


        # self.BdotClasses.append(BdotClass.BdotClass('PTUT', 20))
        # self.BdotClasses.append(BdotClass.BdotClass('KUKO', 20, "RODZAJ='parking'"))

        # self.BdotClasses.append(BdotClass.BdotClass('BUBD', 1))
        # self.BdotClasses.append(BdotClass.BdotClass('OIKM', 2))
        # self.BdotClasses.append(BdotClass.BdotClass('OISZ', 3))
        #

        #
        # self.BdotClasses.append(BdotClass.BdotClass('PTPL', 6))
        #
        # self.BdotClasses.append(BdotClass.BdotClass('PTTR', 7, "rodzaj='Gr'"))
        # self.BdotClasses.append(BdotClass.BdotClass('PTTR', 8, "rodzaj='Rt'"))
        #

        # # self.BdotClasses.append(BdotClass.BdotClass('PTGN', 10, "rodzaj='terenKamienisty'"))
        # # self.BdotClasses.append(BdotClass.BdotClass('PTGN', 10, "rodzaj='terenPiaszczystyZwirowy'"))
        #
        # self.BdotClasses.append(BdotClass.BdotClass('PTGN', 10, "rodzaj='Ski'"))
        # self.BdotClasses.append(BdotClass.BdotClass('PTGN', 10, "rodzaj='Kam'"))
        # self.BdotClasses.append(BdotClass.BdotClass('PTGN', 10, "rodzaj='Psk'"))



    def fillTilesWithCounties(self):

        # self.tiles.append(Tile.Tile('PLANET2', "N:/BAMS/TIFF_selected/PS/mosaic_june_2018_utm_likeS2GLC.tif"))
        # self.tiles[-1].addCounty(County.County('1434'))
        # self.tiles[-1].addCounty(County.County('1412'))
        # self.tiles[-1].addCounty(County.County('1408'))
        # self.tiles[-1].addCounty(County.County('1435'))
        # self.tiles[-1].addCounty(County.County('1465'))
        # self.tiles.append(Tile.Tile('34UED', "M:/mrybicki/S2GLC/post/34UED/resultClassificationAggreagtion_DivByAll.tif"))
        # self.tiles[-1].addCounty(County.County('1408'))
        # self.tiles[-1].addCounty(County.County('1411'))
        # self.tiles[-1].addCounty(County.County('1412'))
        # self.tiles[-1].addCounty(County.County('1415'))
        # self.tiles[-1].addCounty(County.County('1416'))
        # self.tiles[-1].addCounty(County.County('1422'))
        # self.tiles[-1].addCounty(County.County('1424'))
        # self.tiles[-1].addCounty(County.County('1426'))
        # self.tiles[-1].addCounty(County.County('1429'))
        # self.tiles[-1].addCounty(County.County('1433'))
        # self.tiles[-1].addCounty(County.County('1434'))
        # self.tiles[-1].addCounty(County.County('1435'))
        # self.tiles[-1].addCounty(County.County('1461'))
        # self.tiles[-1].addCounty(County.County('1465'))
        #
        # self.tiles.append(Tile.Tile('34UCD', "N:/BAMS/2019/classification/34UCD/34UCD/agg/stepBamsPost1resultClassificationAggreagtion_DivByAll.tif"))
        # self.tiles[-1].addCounty(County.County('1404'))
        # self.tiles[-1].addCounty(County.County('1419'))
        # self.tiles[-1].addCounty(County.County('1427'))
        # self.tiles[-1].addCounty(County.County('0461'))
        # self.tiles[-1].addCounty(County.County('0463'))
        # self.tiles[-1].addCounty(County.County('0464'))
        # self.tiles[-1].addCounty(County.County('0401'))
        # self.tiles[-1].addCounty(County.County('0402'))
        # self.tiles[-1].addCounty(County.County('0405'))
        # self.tiles[-1].addCounty(County.County('0407'))
        # self.tiles[-1].addCounty(County.County('0408'))
        # self.tiles[-1].addCounty(County.County('0411'))
        # self.tiles[-1].addCounty(County.County('0412'))
        # self.tiles[-1].addCounty(County.County('0415'))
        # self.tiles[-1].addCounty(County.County('0418'))
        # self.tiles[-1].addCounty(County.County('1002'))
        # self.tiles[-1].addCounty(County.County('1437'))
        # self.tiles[-1].addCounty(County.County('1462'))

        # self.tiles.append(Tile.Tile('34UDB', "M:/mrybicki/S2GLC/post/34UDB/resultClassificationAggreagtion_DivByAll.tif"))
        # self.tiles[-1].addCounty(County.County('1423'))
        # self.tiles[-1].addCounty(County.County('1425'))
        # self.tiles[-1].addCounty(County.County('1430'))
        # self.tiles[-1].addCounty(County.County('1463'))
        # self.tiles[-1].addCounty(County.County('1062'))
        # self.tiles[-1].addCounty(County.County('1007'))
        # self.tiles[-1].addCounty(County.County('1010'))
        # self.tiles[-1].addCounty(County.County('1012'))
        # self.tiles[-1].addCounty(County.County('2661'))
        # self.tiles[-1].addCounty(County.County('2601'))
        # self.tiles[-1].addCounty(County.County('2602'))
        # self.tiles[-1].addCounty(County.County('2604'))
        # self.tiles[-1].addCounty(County.County('2605'))
        # self.tiles[-1].addCounty(County.County('2608'))
        # self.tiles[-1].addCounty(County.County('2610'))
        # self.tiles[-1].addCounty(County.County('2611'))
        # self.tiles[-1].addCounty(County.County('2613'))
        #
        # self.tiles.append(Tile.Tile('34UDC', "M:/mrybicki/S2GLC/post/34UDC/resultClassificationAggreagtion_DivByAll.tif"))
        # self.tiles[-1].addCounty(County.County('1401'))
        # self.tiles[-1].addCounty(County.County('1405'))
        # self.tiles[-1].addCounty(County.County('1406'))
        # self.tiles[-1].addCounty(County.County('1418'))
        # self.tiles[-1].addCounty(County.County('1421'))
        # self.tiles[-1].addCounty(County.County('1423'))
        # self.tiles[-1].addCounty(County.County('1425'))
        # self.tiles[-1].addCounty(County.County('1428'))
        # self.tiles[-1].addCounty(County.County('1432'))
        # self.tiles[-1].addCounty(County.County('1438'))
        # self.tiles[-1].addCounty(County.County('1463'))
        # self.tiles[-1].addCounty(County.County('1465'))
        # self.tiles[-1].addCounty(County.County('1062'))
        # self.tiles[-1].addCounty(County.County('1063'))
        # self.tiles[-1].addCounty(County.County('1005'))
        # self.tiles[-1].addCounty(County.County('1013'))
        # self.tiles[-1].addCounty(County.County('1015'))
        # self.tiles[-1].addCounty(County.County('1016'))
        # self.tiles[-1].addCounty(County.County('1404'))
        # self.tiles[-1].addCounty(County.County('1407'))
        # self.tiles[-1].addCounty(County.County('1414'))
        # self.tiles[-1].addCounty(County.County('1434'))
        # self.tiles[-1].addCounty(County.County('1419'))
        #
        # self.tiles.append(Tile.Tile('34UDD', "M:/mrybicki/S2GLC/post/34UDD/resultClassificationAggreagtion_DivByAll.tif"))
        # self.tiles[-1].addCounty(County.County('1402'))
        # self.tiles[-1].addCounty(County.County('1404'))
        # self.tiles[-1].addCounty(County.County('1408'))
        # self.tiles[-1].addCounty(County.County('1411'))
        # self.tiles[-1].addCounty(County.County('1413'))
        # self.tiles[-1].addCounty(County.County('1414'))
        # self.tiles[-1].addCounty(County.County('1419'))
        # self.tiles[-1].addCounty(County.County('1420'))
        # self.tiles[-1].addCounty(County.County('1422'))
        # self.tiles[-1].addCounty(County.County('1424'))
        # self.tiles[-1].addCounty(County.County('1427'))
        # self.tiles[-1].addCounty(County.County('1428'))
        # self.tiles[-1].addCounty(County.County('1432'))
        # self.tiles[-1].addCounty(County.County('1437'))
        # self.tiles[-1].addCounty(County.County('1462'))
        # self.tiles[-1].addCounty(County.County('1465'))
        # self.tiles[-1].addCounty(County.County('1434'))
        # self.tiles[-1].addCounty(County.County('1435'))
        #
        # self.tiles.append(Tile.Tile('34UDE', "M:/mrybicki/S2GLC/post/34UDE/resultClassificationAggreagtion_DivByAll.tif"))
        # self.tiles[-1].addCounty(County.County('1413'))
        # self.tiles[-1].addCounty(County.County('1422'))
        # self.tiles[-1].addCounty(County.County('1437'))
        # self.tiles[-1].addCounty(County.County('0402'))
        # self.tiles[-1].addCounty(County.County('2862'))
        # self.tiles[-1].addCounty(County.County('2803'))
        # self.tiles[-1].addCounty(County.County('2804'))
        # self.tiles[-1].addCounty(County.County('2807'))
        # self.tiles[-1].addCounty(County.County('2809'))
        # self.tiles[-1].addCounty(County.County('2811'))
        # self.tiles[-1].addCounty(County.County('2812'))
        # self.tiles[-1].addCounty(County.County('2814'))
        # self.tiles[-1].addCounty(County.County('2815'))
        # self.tiles[-1].addCounty(County.County('2817'))
        # self.tiles[-1].addCounty(County.County('1415'))
        #
        # self.tiles.append(Tile.Tile('34UEB', "M:/mrybicki/S2GLC/post/34UEB/resultClassificationAggreagtion_DivByAll.tif"))
        # self.tiles[-1].addCounty(County.County('1409'))
        # self.tiles[-1].addCounty(County.County('1425'))
        # self.tiles[-1].addCounty(County.County('1430'))
        # self.tiles[-1].addCounty(County.County('1436'))
        # self.tiles[-1].addCounty(County.County('1463'))
        # self.tiles[-1].addCounty(County.County('0663'))
        # self.tiles[-1].addCounty(County.County('0605'))
        # self.tiles[-1].addCounty(County.County('0607'))
        # self.tiles[-1].addCounty(County.County('0609'))
        # self.tiles[-1].addCounty(County.County('0612'))
        # self.tiles[-1].addCounty(County.County('0614'))
        # self.tiles[-1].addCounty(County.County('2606'))
        # self.tiles[-1].addCounty(County.County('2607'))
        # self.tiles[-1].addCounty(County.County('2609'))
        # self.tiles[-1].addCounty(County.County('2611'))
        # self.tiles[-1].addCounty(County.County('2612'))
        # self.tiles[-1].addCounty(County.County('1407'))
        #
        # self.tiles.append(Tile.Tile('34UEC', "M:/mrybicki/S2GLC/post/34UEC/resultClassificationAggreagtion_DivByAll.tif"))
        # self.tiles[-1].addCounty(County.County('1401'))
        # self.tiles[-1].addCounty(County.County('1403'))
        # self.tiles[-1].addCounty(County.County('1406'))
        # self.tiles[-1].addCounty(County.County('1407'))
        # self.tiles[-1].addCounty(County.County('1412'))
        # self.tiles[-1].addCounty(County.County('1417'))
        # self.tiles[-1].addCounty(County.County('1418'))
        # self.tiles[-1].addCounty(County.County('1425'))
        # self.tiles[-1].addCounty(County.County('1426'))
        # self.tiles[-1].addCounty(County.County('1433'))
        # self.tiles[-1].addCounty(County.County('1434'))
        # self.tiles[-1].addCounty(County.County('1436'))
        # self.tiles[-1].addCounty(County.County('1463'))
        # self.tiles[-1].addCounty(County.County('1464'))
        # self.tiles[-1].addCounty(County.County('1465'))
        # self.tiles[-1].addCounty(County.County('0611'))
        # self.tiles[-1].addCounty(County.County('0614'))
        # self.tiles[-1].addCounty(County.County('0616'))
        # self.tiles[-1].addCounty(County.County('1410'))
        # self.tiles[-1].addCounty(County.County('1429'))
        # self.tiles[-1].addCounty(County.County('1408'))
        #
        # self.tiles.append(Tile.Tile('34UEE', "M:/mrybicki/S2GLC/post/34UEE/resultClassificationAggreagtion_DivByAll.tif"))
        # self.tiles[-1].addCounty(County.County('1415'))
        # self.tiles[-1].addCounty(County.County('1422'))
        # self.tiles[-1].addCounty(County.County('2062'))
        # self.tiles[-1].addCounty(County.County('2004'))
        # self.tiles[-1].addCounty(County.County('2006'))
        # self.tiles[-1].addCounty(County.County('2007'))
        # self.tiles[-1].addCounty(County.County('2805'))
        # self.tiles[-1].addCounty(County.County('2806'))
        # self.tiles[-1].addCounty(County.County('2810'))
        # self.tiles[-1].addCounty(County.County('2816'))
        # self.tiles[-1].addCounty(County.County('2817'))
        #
        # self.tiles.append(Tile.Tile('34UFC', "M:/mrybicki/S2GLC/post/34UFC/resultClassificationAggreagtion_DivByAll.tif"))
        # self.tiles[-1].addCounty(County.County('1410'))
        # self.tiles[-1].addCounty(County.County('1426'))
        # self.tiles[-1].addCounty(County.County('0661'))
        # self.tiles[-1].addCounty(County.County('0601'))
        # self.tiles[-1].addCounty(County.County('0608'))
        # self.tiles[-1].addCounty(County.County('0611'))
        # self.tiles[-1].addCounty(County.County('0613'))
        # self.tiles[-1].addCounty(County.County('0615'))
        # self.tiles[-1].addCounty(County.County('0619'))
        # self.tiles[-1].addCounty(County.County('1429'))
        #
        # self.tiles.append(Tile.Tile('34UFD', "M:/mrybicki/S2GLC/post/34UFD/resultClassificationAggreagtion_DivByAll.tif"))
        # self.tiles[-1].addCounty(County.County('1410'))
        # self.tiles[-1].addCounty(County.County('1426'))
        # self.tiles[-1].addCounty(County.County('2061'))
        # self.tiles[-1].addCounty(County.County('2002'))
        # self.tiles[-1].addCounty(County.County('2003'))
        # self.tiles[-1].addCounty(County.County('2005'))
        # self.tiles[-1].addCounty(County.County('2010'))
        # self.tiles[-1].addCounty(County.County('2013'))
        # self.tiles[-1].addCounty(County.County('1429'))

        # self.tiles.append(Tile.Tile('33UWT', "N:/S2GLCextension/S2glcPoland2020/data/LC_DB/CLCFilteredByHRL/33UWT.tif"))
        # self.tiles[-1].addCounty(County.County('0807'))
        # self.tiles[-1].addCounty(County.County('3013'))
        # self.tiles[-1].addCounty(County.County('3063'))
        # self.tiles[-1].addCounty(County.County('0203'))
        # self.tiles[-1].addCounty(County.County('0225'))
        # self.tiles[-1].addCounty(County.County('0812'))
        # self.tiles[-1].addCounty(County.County('0803'))
        # self.tiles[-1].addCounty(County.County('3015'))
        # self.tiles[-1].addCounty(County.County('0211'))
        # self.tiles[-1].addCounty(County.County('0862'))
        # self.tiles[-1].addCounty(County.County('0810'))
        # self.tiles[-1].addCounty(County.County('0811'))
        # self.tiles[-1].addCounty(County.County('0802'))
        # self.tiles[-1].addCounty(County.County('0201'))
        # self.tiles[-1].addCounty(County.County('3011'))
        # self.tiles[-1].addCounty(County.County('3005'))
        # self.tiles[-1].addCounty(County.County('0222'))
        # self.tiles[-1].addCounty(County.County('0808'))
        # self.tiles[-1].addCounty(County.County('0216'))
        # self.tiles[-1].addCounty(County.County('0804'))
        # self.tiles[-1].addCounty(County.County('0204'))
        # self.tiles[-1].addCounty(County.County('0809'))
        # self.tiles[-1].addCounty(County.County('3029'))
        # self.tiles[-1].addCounty(County.County('0209'))
        # self.tiles[-1].addCounty(County.County('3021'))

        # self.tiles.append(Tile.Tile('33UWU', "N:/S2GLCextension/S2glcPoland2020/data/LC_DB/CLCFilteredByHRL/33UWU.tif"))
        # self.tiles[-1].addCounty(County.County('3016'))
        # self.tiles[-1].addCounty(County.County('3214'))
        # self.tiles[-1].addCounty(County.County('3202'))
        # self.tiles[-1].addCounty(County.County('0801'))
        # self.tiles[-1].addCounty(County.County('0805'))
        # self.tiles[-1].addCounty(County.County('3212'))
        # self.tiles[-1].addCounty(County.County('3002'))
        # self.tiles[-1].addCounty(County.County('3024'))
        # self.tiles[-1].addCounty(County.County('0806'))
        # self.tiles[-1].addCounty(County.County('3014'))
        # self.tiles[-1].addCounty(County.County('0861'))
        # self.tiles[-1].addCounty(County.County('3019'))
        # self.tiles[-1].addCounty(County.County('3210'))
        # self.tiles[-1].addCounty(County.County('3217'))
        # self.tiles[-1].addCounty(County.County('3203'))
        # self.tiles[-1].addCounty(County.County('0807'))
        # self.tiles[-1].addCounty(County.County('0803'))
        # self.tiles[-1].addCounty(County.County('3015'))
        # self.tiles[-1].addCounty(County.County('3005'))
        # self.tiles[-1].addCounty(County.County('0808'))
        # self.tiles[-1].addCounty(County.County('3021'))
        #
        # self.tiles.append(Tile.Tile('33UXV', "N:/S2GLCextension/S2glcPoland2020/data/LC_DB/CLCFilteredByHRL/33UXV.tif"))
        # self.tiles[-1].addCounty(County.County('2206'))
        # self.tiles[-1].addCounty(County.County('0416'))
        # self.tiles[-1].addCounty(County.County('2212'))
        # self.tiles[-1].addCounty(County.County('0410'))
        # self.tiles[-1].addCounty(County.County('2213'))
        # self.tiles[-1].addCounty(County.County('0413'))
        # self.tiles[-1].addCounty(County.County('3031'))
        # self.tiles[-1].addCounty(County.County('2203'))
        # self.tiles[-1].addCounty(County.County('3209'))
        # self.tiles[-1].addCounty(County.County('2201'))
        # self.tiles[-1].addCounty(County.County('0414'))
        # self.tiles[-1].addCounty(County.County('2202'))
        # self.tiles[-1].addCounty(County.County('3215'))
        # self.tiles[-1].addCounty(County.County('0403'))
        # self.tiles[-1].addCounty(County.County('0461'))
        # self.tiles[-1].addCounty(County.County('3019'))
        # self.tiles[-1].addCounty(County.County('3217'))
        #
        # self.tiles.append(Tile.Tile('34UCC', "N:/S2GLCextension/S2glcPoland2020/data/LC_DB/CLCFilteredByHRL/34UCC.tif"))
        # self.tiles[-1].addCounty(County.County('1404'))
        # self.tiles[-1].addCounty(County.County('1020'))
        # self.tiles[-1].addCounty(County.County('3018'))
        # self.tiles[-1].addCounty(County.County('3009'))
        # self.tiles[-1].addCounty(County.County('3023'))
        # self.tiles[-1].addCounty(County.County('0418'))
        # self.tiles[-1].addCounty(County.County('1008'))
        # self.tiles[-1].addCounty(County.County('1061'))
        # self.tiles[-1].addCounty(County.County('1010'))
        # self.tiles[-1].addCounty(County.County('3062'))
        # self.tiles[-1].addCounty(County.County('1018'))
        # self.tiles[-1].addCounty(County.County('1005'))
        # self.tiles[-1].addCounty(County.County('1002'))
        # self.tiles[-1].addCounty(County.County('1006'))
        # self.tiles[-1].addCounty(County.County('3017'))
        # self.tiles[-1].addCounty(County.County('3061'))
        # self.tiles[-1].addCounty(County.County('1014'))
        # self.tiles[-1].addCounty(County.County('1021'))
        # self.tiles[-1].addCounty(County.County('3007'))
        # self.tiles[-1].addCounty(County.County('3027'))
        # self.tiles[-1].addCounty(County.County('1001'))
        # self.tiles[-1].addCounty(County.County('1003'))
        # self.tiles[-1].addCounty(County.County('1004'))
        # self.tiles[-1].addCounty(County.County('1019'))
        # self.tiles[-1].addCounty(County.County('1062'))
        # self.tiles[-1].addCounty(County.County('1011'))
        # self.tiles[-1].addCounty(County.County('1017'))
        # self.tiles[-1].addCounty(County.County('3010'))
        #
        # self.tiles.append(Tile.Tile('34UDA', "N:/S2GLCextension/S2glcPoland2020/data/LC_DB/CLCFilteredByHRL/34UDA.tif"))
        # self.tiles[-1].addCounty(County.County('1202'))
        # self.tiles[-1].addCounty(County.County('1261'))
        # self.tiles[-1].addCounty(County.County('1201'))
        # self.tiles[-1].addCounty(County.County('1263'))
        # self.tiles[-1].addCounty(County.County('1210'))
        # self.tiles[-1].addCounty(County.County('1204'))
        # self.tiles[-1].addCounty(County.County('1206'))
        # self.tiles[-1].addCounty(County.County('2416'))
        # self.tiles[-1].addCounty(County.County('1203'))
        # self.tiles[-1].addCounty(County.County('2612'))
        # self.tiles[-1].addCounty(County.County('1214'))
        # self.tiles[-1].addCounty(County.County('1219'))
        # self.tiles[-1].addCounty(County.County('2602'))
        # self.tiles[-1].addCounty(County.County('2603'))
        # self.tiles[-1].addCounty(County.County('1262'))
        # self.tiles[-1].addCounty(County.County('2601'))
        # self.tiles[-1].addCounty(County.County('2608'))
        # self.tiles[-1].addCounty(County.County('1211'))
        # self.tiles[-1].addCounty(County.County('1216'))
        # self.tiles[-1].addCounty(County.County('2604'))
        # self.tiles[-1].addCounty(County.County('1215'))
        # self.tiles[-1].addCounty(County.County('1207'))
        # self.tiles[-1].addCounty(County.County('1208'))
        # self.tiles[-1].addCounty(County.County('1209'))
        # self.tiles[-1].addCounty(County.County('1212'))
        # self.tiles[-1].addCounty(County.County('1205'))
        # self.tiles[-1].addCounty(County.County('1218'))

        # self.tiles.append(Tile.Tile('34UEB', "N:/S2GLCextension/S2glcPoland2020/data/LC_DB/CLCFilteredByHRL/34UEB.tif"))
        # self.tiles[-1].addCounty(County.County('1425'))
        # self.tiles[-1].addCounty(County.County('1430'))
        # self.tiles[-1].addCounty(County.County('1463'))
        # self.tiles[-1].addCounty(County.County('0663'))
        # self.tiles[-1].addCounty(County.County('2607'))
        # self.tiles[-1].addCounty(County.County('1818'))
        # self.tiles[-1].addCounty(County.County('1864'))
        # self.tiles[-1].addCounty(County.County('1409'))
        # self.tiles[-1].addCounty(County.County('0607'))
        # self.tiles[-1].addCounty(County.County('0612'))
        # self.tiles[-1].addCounty(County.County('2611'))
        # self.tiles[-1].addCounty(County.County('1812'))
        # self.tiles[-1].addCounty(County.County('1820'))
        # self.tiles[-1].addCounty(County.County('0602'))
        # self.tiles[-1].addCounty(County.County('1806'))
        # self.tiles[-1].addCounty(County.County('1436'))
        # self.tiles[-1].addCounty(County.County('0609'))
        # self.tiles[-1].addCounty(County.County('0608'))
        # self.tiles[-1].addCounty(County.County('0614'))
        # self.tiles[-1].addCounty(County.County('2606'))
        # self.tiles[-1].addCounty(County.County('1811'))
        # self.tiles[-1].addCounty(County.County('1407'))
        # self.tiles[-1].addCounty(County.County('0605'))
        # self.tiles[-1].addCounty(County.County('2609'))
        # self.tiles[-1].addCounty(County.County('2612'))
        # self.tiles[-1].addCounty(County.County('2601'))
        # self.tiles[-1].addCounty(County.County('2604'))

        self.tiles.append(Tile.Tile('34UED', r"G:/_temp/BDOT_to_samples/s2a_pol_sub_msil2a_20200419t094031_n0214_r036_t34ued.safe.tif"))
        self.tiles[-1].addCounty(County.County('1433'))
        self.tiles[-1].addCounty(County.County('1461'))
        self.tiles[-1].addCounty(County.County('2003'))
        self.tiles[-1].addCounty(County.County('1416'))
        self.tiles[-1].addCounty(County.County('1426'))
        self.tiles[-1].addCounty(County.County('1435'))
        self.tiles[-1].addCounty(County.County('1411'))
        self.tiles[-1].addCounty(County.County('1412'))
        self.tiles[-1].addCounty(County.County('2010'))
        self.tiles[-1].addCounty(County.County('1429'))
        self.tiles[-1].addCounty(County.County('2013'))
        self.tiles[-1].addCounty(County.County('1408'))
        self.tiles[-1].addCounty(County.County('1424'))
        self.tiles[-1].addCounty(County.County('1465'))
        self.tiles[-1].addCounty(County.County('1434'))
        self.tiles[-1].addCounty(County.County('2062'))
        self.tiles[-1].addCounty(County.County('1422'))
        self.tiles[-1].addCounty(County.County('2006'))
        self.tiles[-1].addCounty(County.County('2002'))
        self.tiles[-1].addCounty(County.County('2014'))
        self.tiles[-1].addCounty(County.County('2008'))
        self.tiles[-1].addCounty(County.County('2007'))
        self.tiles[-1].addCounty(County.County('1415'))
        #
        # self.tiles.append(Tile.Tile('34UEE', "N:/S2GLCextension/S2glcPoland2020/data/LC_DB/CLCFilteredByHRL/34UEE.tif"))
        # self.tiles[-1].addCounty(County.County('2062'))
        # self.tiles[-1].addCounty(County.County('2806'))
        # self.tiles[-1].addCounty(County.County('2810'))
        # self.tiles[-1].addCounty(County.County('1422'))
        # self.tiles[-1].addCounty(County.County('2006'))
        # self.tiles[-1].addCounty(County.County('2012'))
        # self.tiles[-1].addCounty(County.County('2801'))
        # self.tiles[-1].addCounty(County.County('2004'))
        # self.tiles[-1].addCounty(County.County('2805'))
        # self.tiles[-1].addCounty(County.County('2817'))
        # self.tiles[-1].addCounty(County.County('2808'))
        # self.tiles[-1].addCounty(County.County('2002'))
        # self.tiles[-1].addCounty(County.County('2819'))
        # self.tiles[-1].addCounty(County.County('2813'))
        # self.tiles[-1].addCounty(County.County('2014'))
        # self.tiles[-1].addCounty(County.County('2008'))
        # self.tiles[-1].addCounty(County.County('2814'))
        # self.tiles[-1].addCounty(County.County('2007'))
        # self.tiles[-1].addCounty(County.County('2816'))
        # self.tiles[-1].addCounty(County.County('1415'))

    def prepareData(self, workdir, bdotMainDirPath, percent):
        self.workdir = workdir
        Path(self.workdir).mkdir(parents=True, exist_ok=True)
        self.bdotMainDirPath = bdotMainDirPath
        self.percent = percent
        self.temp1percentRasterPath = self.workdir + '/temp1p.tif'
        self.tempSum1percentRasterPath = self.workdir + '/tempSum1p.tif'
        self.tempNormalRasterPath = self.workdir + '/tempNormal.tif'
        self.outputCommandsFilePath = self.workdir + '/commands.txt'
        self.outputCommandsFileHandle = open(self.outputCommandsFilePath, "w")

    def doRasterize(self):
        for t in self.tiles:
            self.currentTile = t
            self.doRasterizeForTile(t)
            #return
        self.outputCommandsFileHandle.close()

    def getNominalSize(self):
        # if self.Xsize > 0 and self.Ysize > 0:
        return self.Ysize, self.Xsize

    def getNominalSpatialResolution(self):
        dataset = gdal.Open(self.currentReferenceTif, gdal.GA_ReadOnly)
        if not dataset:
            print("Cannot open " + self.currentReferenceTif)
        self.geotransform = dataset.GetGeoTransform()
        self.nominalSpatialResolution = self.geotransform[1]
        dataset = None
        return self.nominalSpatialResolution

    def doRasterizeForTile(self, tile):
        self.resultPath = self.workdir + '/trainingRaster_' + tile.name + '.tif'
        self.currentReferenceTif = tile.exampleImage
        print('create1PercentImage')
        self.create1PercentImage(tile.exampleImage)
        print('rasterizeTileOn1percentImage')
        self.rasterizeTileOn1percentImage(tile)
        print('sumDownsamplingRasterizedImagesAllClasses')
        self.sumDownsamplingRasterizedImagesAllClasses()
        # print('createNormalImage')
        # self.createNormalImage(tile.exampleImage)
        # print('rasterizeTileOnNormalImage')
        # self.rasterizeTileOnNormalImage(tile)
        print('combineRasterizedImages')
        # self.combineRasterizedImages()
        # self.clearTempData()

    def create1PercentImage(self, inputRaster, value=1):
        nominalSpatialRes = self.getNominalSpatialResolution()
        onePerSpatRes = float(nominalSpatialRes) / 10
        strOnePerSpatialRes = str(onePerSpatRes) + ' ' + str(onePerSpatRes)
        temp1percentRasterPath = self.get1percentImagePath(value)
        command = self.gdalTranslatePath + ' ' '-tr ' + strOnePerSpatialRes + ' -ot Byte -co "COMPRESS=LZW" ' + inputRaster + ' ' + temp1percentRasterPath
        self.runSystemProcess(command)
        self.zeros1PercentImage(value)

    def createNormalImage(self, inputRaster):
        command = self.gdalTranslatePath + ' -ot Byte -co "COMPRESS=LZW" ' + inputRaster + ' ' + self.tempNormalRasterPath
        self.runSystemProcess(command)
        self.zerosNormalImage()

    def zeros1PercentImage(self, value):
        framePath = self.workdir + '/frame.shp'
        command = self.gdalTindexPath + ' ' + framePath + ' ' + self.get1percentImagePath(value)
        self.runSystemProcess(command)
        # self.burnShpOn1percentImage(framePath, 0)
        shpPath = framePath
        if len(shpPath) < 2:
            print('No shp file')
            return
        command = self.gdalRasterizePath + ' -burn ' + str(0)
        command = command + ' ' + shpPath + ' ' + self.get1percentImagePath(value)
        self.runSystemProcess(command)
        os.remove(framePath)

    def zerosNormalImage(self):
        framePath = self.workdir + '/frame.shp'
        command = self.gdalTindexPath + ' ' + framePath + ' ' + self.tempNormalRasterPath
        self.runSystemProcess(command)
        self.burnShpOnNormalImage(framePath, 0)
        os.remove(framePath)

    def burnShpOn1percentImage(self, shpPath, value, detailedQuery=''):
        if len(shpPath) < 2:
            print('No shp file')
            return
        command = self.gdalRasterizePath + ' -burn ' + str(1)
        if len(detailedQuery) > 0:
            command = command + ' -where "' + detailedQuery + '"'
        command = command + ' ' + shpPath + ' ' + self.get1percentImagePath(value)
        self.runSystemProcess(command)

    def burnShpOnNormalImage(self, shpPath, value, detailedQuery=''):
        if len(shpPath) < 2:
            print('No shp file')
            return
        command = self.gdalRasterizePath + ' -burn ' + str(value)
        if len(detailedQuery) > 0:
            command = command + ' -where "' + detailedQuery + '"'
        command = command + ' ' + shpPath + ' ' + self.tempNormalRasterPath
        self.runSystemProcess(command)

    def rasterizeTileOn1percentImage(self, tile):
        for bdotClass in self.BdotClasses:
            self.create1PercentImage(tile.exampleImage, bdotClass.number)
        for county in tile.counties:
            for bdotClass in self.BdotClasses:
                # if bdotClass.number == 1:
                shpFile = PathsManager.FindShpFileForCountyAndClass(self.bdotMainDirPath, county, bdotClass)
                if len(shpFile) > 1:
                    self.burnShpOn1percentImage(shpFile, bdotClass.number, bdotClass.detailedQuery)
                else:
                    print('No file for class ' + str(bdotClass) + ' for county: ' + str(county.BDOTnumber))

    def rasterizeTileOnNormalImage(self, tile):
        for county in tile.counties:
            for bdotClass in self.BdotClasses:
                if bdotClass.number != 1:
                    shpFile = PathsManager.FindShpFileForCountyAndClass(self.bdotMainDirPath, county, bdotClass)
                    self.burnShpOnNormalImage(shpFile, bdotClass.number, bdotClass.detailedQuery)

    def clearTempData(self):
        #command = "del /f " + self.temp1percentRasterPath
        #self.runSystemProcess(command)
        os.remove(self.temp1percentRasterPath)
        dbfFile = "F:/MarcinRybicki/codes/BAMS/vectorPercentRasterize/workdir/frame.dbf"
        prjFile = "F:/MarcinRybicki/codes/BAMS/vectorPercentRasterize/workdir/frame.prj"
        shxFile = "F:/MarcinRybicki/codes/BAMS/vectorPercentRasterize/workdir/frame.shx"
        shpFile = "F:/MarcinRybicki/codes/BAMS/vectorPercentRasterize/workdir/frame.shp"
        try:
            os.remove(dbfFile)
            os.remove(prjFile)
            os.remove(shxFile)
            os.remove(shpFile)
        except:
            print('Error while deleting a file.')

    def runSystemProcess(self, command):
        if not self.outputCommandsFileHandle.closed:
            self.outputCommandsFileHandle.write(command)
            self.outputCommandsFileHandle.write('\n')
        print(command)
        os.system((command))

    def get1percentImagePath(self, value):
        temp1percentRasterPath = self.workdir + '/' + str(value) + 'temp1p.tif'
        return temp1percentRasterPath

    def getSum1percentImagePath(self, value):
        temp1percentRasterPath = self.workdir + '/' + str(value) + 'Sum1p.tif'
        return temp1percentRasterPath

    def sumDownsamplingRasterizedImagesAllClasses(self):
        for bdotClass in self.BdotClasses:
            value = bdotClass.number
            self.sumDownsamplingRasterizedImage(value)

    def sumDownsamplingRasterizedImage(self, value):
        img = self.readRaster(self.get1percentImagePath(value))
        img[img == 255] = 0
        H, W = img.shape
        wh = 10
        ww = 10
        imgReshaped = img.reshape(int(H/wh), wh, int(W/ww), ww)
        img = None
        resultSummed = np.einsum('ijkl->ik', imgReshaped)
        imgReshaped = None
        #thresholding:
        dst_filename = self.getSum1percentImagePath(value)
        driver = gdal.GetDriverByName("GTiff")
        referenceDataSet = gdal.Open(self.currentReferenceTif, gdal.GA_ReadOnly)
        self.geotransform = referenceDataSet.GetGeoTransform()
        self.projection = referenceDataSet.GetProjection()
        dst_ds = driver.Create(dst_filename, xsize=int(W/ww), ysize=int(H/wh), bands=1, eType=gdal.GDT_Byte)
        dst_ds.SetGeoTransform(self.geotransform)
        dst_ds.SetProjection(self.projection)
        dst_ds.GetRasterBand(1).WriteArray(resultSummed)

        resultSummed[resultSummed <= self.percent] = 0
        resultSummed[resultSummed > self.percent] = 1

        dst_filename = self.tempSum1percentRasterPath
        dst_ds = driver.Create(dst_filename, xsize=int(W / ww), ysize=int(H / wh), bands=1, eType=gdal.GDT_Byte)
        dst_ds.SetGeoTransform(self.geotransform)
        dst_ds.SetProjection(self.projection)
        dst_ds.GetRasterBand(1).WriteArray(resultSummed)

        dst_ds = None

    def readRaster(self, rasterPath):
        dataset = gdal.Open(rasterPath, gdal.GA_ReadOnly)
        if not dataset:
            print("Cannot open " + rasterPath)
        band = dataset.GetRasterBand(1)
        wholeImage = band.ReadAsArray(xoff=0, yoff=0, win_xsize=band.XSize, win_ysize=band.YSize)
        self.Xsize = band.XSize
        self.Ysize= band.YSize

        return wholeImage

    def combineRasterizedImages(self):
        summedImage = self.readRaster(self.tempSum1percentRasterPath)
        normalImage = self.readRaster(self.tempNormalRasterPath)
        normalImage[summedImage == 1] = 1
        summedImage = None
        driver = gdal.GetDriverByName("GTiff")
        dst_filename =self.resultPath
        dst_ds = driver.Create(dst_filename, xsize=int(self.Xsize), ysize=int(self.Ysize), bands=1, eType=gdal.GDT_Byte)
        dst_ds.SetGeoTransform(self.geotransform)
        dst_ds.SetProjection(self.projection)
        dst_ds.GetRasterBand(1).WriteArray(normalImage)
        dst_ds = None
