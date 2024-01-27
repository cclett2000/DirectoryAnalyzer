import os

# converting bytes: https://stackoverflow.com/a/12912296
#   ^ this is way sexier than div/mult

DevFlag = False

UNITS_MAPPING = [
    (1<<50, ' PB'),
    (1<<40, ' TB'),
    (1<<30, ' GB'),
    (1<<20, ' MB'),
    (1<<10, ' KB'),
    (1, (' byte', ' bytes')),
]

if(DevFlag):
    mainDirectory = "D:/Games/steamapps/common/Skyrim/ModOrganizer/mods"
else:
    mainDirectory = os.getcwd()

directoryDataArray = []

"""
main runner for sub processes
"""
def main():
    getDirectorySize()
    for i in directoryDataArray:
        print("Directory: " + i[0] + " || Size: " + i[1])
    print()

"""
scan through directory and get size of every directory
"""
def getDirectorySize():
    try:
        for rootDirectoryPath, directory, file in os.walk(mainDirectory):
            for d in directory:
                directorySize = 0
                for f in os.scandir(rootDirectoryPath + '/' + d):
                    try:
                        directorySize += os.path.getsize(f)
                    except:
                        print("An error occurred trying get file/size")

                directoryDataArray.append([d, convertAndFormatSizeValue(directorySize), directorySize])
                directoryDataArray.sort(key=sortDirectoryArray)
            break
    except:
        print("Welp something broke")

"""
convert byte sizes and return formatted string
"""
def convertAndFormatSizeValue(bytes):
    # factor = bitwise shift factor
    # suffix = size suffix
    for factor, suffix in UNITS_MAPPING:
        if bytes >= factor:
            break

    # division to get pretty printed value
    amount = int(bytes / factor)

    if isinstance(suffix, tuple):
        singular, multiple = suffix
        if amount == 1:
            suffix = singular
        else:
            suffix = multiple
    return str(amount) + suffix

"""
sort directory array, this is so the largest files will show at the bottom
"""
def sortDirectoryArray(arrayElement):
    return arrayElement[2]

main()