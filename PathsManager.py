import glob
import os

def FindPathsWithWildcard(mainDir, wildcard):
    foundPaths = []
    # fullWildCard = mainDir + '/*/' +wildcard
    fullWildCard2 = mainDir + wildcard
    files = glob.glob(fullWildCard2, recursive=True)
    # listing = glob.glob(fullWildCard, recursive=True)
    for filename in files:
        foundPaths.append(filename)
    return foundPaths

def FindDirPathsWithWildcard(mainDir, wildcard):
    foundPaths = FindPathsWithWildcard(mainDir, wildcard);
    foundDirs = []
    for p in foundPaths:
        if os.path.isdir(p):
            foundDirs.append(p)
    return foundDirs

def FindFilePathsWithWildcard(mainDir, wildcard):
    foundPaths = FindPathsWithWildcard(mainDir, wildcard);
    foundFiles = []
    for p in foundPaths:
        if os.path.isfile(p):
            foundFiles.append(p)
    return foundFiles


def FindShpFileForCountyAndClass(bdotMainDir, county, bdotClass):
    foundPath = ''
    # wildcard = '*' + county.BDOTnumber + '*' + bdotClass.name + '*.xml'0000000
    wildcard = '/**/*.' + str(county.BDOTnumber) + '_*' + bdotClass.name + '*A.xml'
    foundPaths = FindFilePathsWithWildcard(bdotMainDir, wildcard)
    if len(foundPaths) > 0:
        foundPath = foundPaths[0]
    return foundPath