import random
import keyboard
import os
from colorama import Fore, Back, Style


mapPartBlankRow = Back.BLUE + "                            " + Style.RESET_ALL
mapPartBlankSingular = Back.BLUE + " " + Style.RESET_ALL
mapPartBlankLong = Back.BLUE + "         " + Style.RESET_ALL
mapPartBlankShort = Back.BLUE + "    " + Style.RESET_ALL

mapPartWayRow = Back.GREEN + " -- " + Style.RESET_ALL
mapPartWayColumn = Back.GREEN + "|" + Style.RESET_ALL




maploc00 = Back.GREEN + " " + Style.RESET_ALL
maploc01 = Back.GREEN + " " + Style.RESET_ALL
maploc02 = Back.GREEN + " " + Style.RESET_ALL
maploc03 = Back.MAGENTA + " " + Style.RESET_ALL
maploc04 = Back.GREEN + " " + Style.RESET_ALL
maploc05 = Back.RED + " " + Style.RESET_ALL
maploc06 = Back.CYAN + " " + Style.RESET_ALL
maploc07 = Back.GREEN + " " + Style.RESET_ALL
maploc08 = Back.YELLOW + " " + Style.RESET_ALL
maploc09 = Back.MAGENTA + " " + Style.RESET_ALL
maploc10 = Back.RED + " " + Style.RESET_ALL
maploc11 = Back.GREEN + " " + Style.RESET_ALL
maploc12 = Back.BLACK + " " + Style.RESET_ALL
maploc13 = Back.GREEN + " " + Style.RESET_ALL
maploc14 = Back.MAGENTA + " " + Style.RESET_ALL
maploc15 = Back.GREEN + " " + Style.RESET_ALL
maploc16 = Back.GREEN + " " + Style.RESET_ALL
maploc17 = Back.GREEN + " " + Style.RESET_ALL
maploc18 = Back.YELLOW + " " + Style.RESET_ALL
maploc19 = Back.GREEN + " " + Style.RESET_ALL
maploc20 = Back.RED + " " + Style.RESET_ALL
maploc21 = Back.GREEN + " " + Style.RESET_ALL
maploc22 = Back.BLACK + " " + Style.RESET_ALL
maploc23 = Back.GREEN + " " + Style.RESET_ALL
maploc24 = Back.CYAN + " " + Style.RESET_ALL

    
coloredMapList = [mapPartBlankRow, "\n", mapPartBlankSingular, maploc08, mapPartWayRow, maploc07, mapPartWayRow, maploc06, mapPartBlankShort, maploc22, mapPartWayRow, maploc21, mapPartWayRow, maploc20, mapPartBlankSingular, "\n"]
coloredMapList += [mapPartBlankSingular, mapPartWayColumn, mapPartBlankLong, mapPartWayColumn, mapPartBlankShort, mapPartWayColumn, mapPartBlankLong, mapPartWayColumn, mapPartBlankSingular, "\n"]
coloredMapList += [mapPartBlankSingular, maploc09, mapPartBlankLong, maploc05, mapPartWayRow, maploc23, mapPartBlankLong, maploc19, mapPartBlankSingular, "\n"]
coloredMapList += [mapPartBlankSingular, mapPartWayColumn, mapPartBlankLong, mapPartWayColumn, mapPartBlankShort, mapPartWayColumn, mapPartBlankLong, mapPartWayColumn, mapPartBlankSingular, "\n"]
coloredMapList += [mapPartBlankSingular, maploc10, mapPartBlankLong, maploc04, mapPartBlankShort, maploc24, mapPartBlankLong, maploc18, mapPartBlankSingular, "\n"]
coloredMapList += [mapPartBlankSingular, mapPartWayColumn, mapPartBlankLong, mapPartWayColumn, mapPartBlankShort, mapPartWayColumn, mapPartBlankLong, mapPartWayColumn, mapPartBlankSingular, "\n"]
coloredMapList += [mapPartBlankSingular, maploc11, mapPartBlankLong, maploc03, mapPartWayRow, maploc13, mapPartBlankLong, maploc17, mapPartBlankSingular, "\n"]
coloredMapList += [mapPartBlankSingular, mapPartWayColumn, mapPartBlankLong, mapPartWayColumn, mapPartBlankShort, mapPartWayColumn, mapPartBlankLong, mapPartWayColumn, mapPartBlankSingular, "\n"]
coloredMapList += [mapPartBlankSingular, maploc12, mapPartWayRow, maploc01, mapPartWayRow, maploc02, mapPartBlankShort, maploc14, mapPartWayRow, maploc15, mapPartWayRow, maploc16, mapPartBlankSingular, "\n", mapPartBlankRow]


print(coloredMapList[3])
print(coloredMapList[5])
print(coloredMapList[7])
print(coloredMapList[9])
print(coloredMapList[11])
print(coloredMapList[13])

print(coloredMapList[27])
print(coloredMapList[29])
print(coloredMapList[31])
print(coloredMapList[33])

print(coloredMapList[47])
print(coloredMapList[49])
print(coloredMapList[51])
print(coloredMapList[53])



print(coloredMapList[67])
print(coloredMapList[69])
print(coloredMapList[71])
print(coloredMapList[73])

print(coloredMapList[87])
print(coloredMapList[89])
print(coloredMapList[91])
print(coloredMapList[93])
print(coloredMapList[95])
print(coloredMapList[97])








coloredMap = mapPartBlankRow + "\n" 
coloredMap += mapPartBlankSingular + maploc08 + mapPartWayRow + maploc07 + mapPartWayRow + maploc06 + mapPartBlankShort + maploc22 + mapPartWayRow + maploc21 + mapPartWayRow + maploc20 + mapPartBlankSingular + "\n"
coloredMap += mapPartBlankSingular + mapPartWayColumn + mapPartBlankLong + mapPartWayColumn + mapPartBlankShort + mapPartWayColumn + mapPartBlankLong + mapPartWayColumn + mapPartBlankSingular + "\n"
coloredMap += mapPartBlankSingular + maploc09 + mapPartBlankLong + maploc05 + mapPartWayRow + maploc23 + mapPartBlankLong + maploc19 + mapPartBlankSingular + "\n"
coloredMap += mapPartBlankSingular + mapPartWayColumn + mapPartBlankLong + mapPartWayColumn + mapPartBlankShort + mapPartWayColumn + mapPartBlankLong + mapPartWayColumn + mapPartBlankSingular + "\n"
coloredMap += mapPartBlankSingular + maploc10 + mapPartBlankLong + maploc04 + mapPartBlankShort + maploc24 + mapPartBlankLong + maploc18 + mapPartBlankSingular + "\n"
coloredMap += mapPartBlankSingular + mapPartWayColumn + mapPartBlankLong + mapPartWayColumn + mapPartBlankShort + mapPartWayColumn + mapPartBlankLong + mapPartWayColumn + mapPartBlankSingular + "\n"
coloredMap += mapPartBlankSingular + maploc11 + mapPartBlankLong + maploc03 + mapPartWayRow + maploc13 + mapPartBlankLong + maploc17 + mapPartBlankSingular + "\n"
coloredMap += mapPartBlankSingular + mapPartWayColumn + mapPartBlankLong + mapPartWayColumn + mapPartBlankShort + mapPartWayColumn + mapPartBlankLong + mapPartWayColumn + mapPartBlankSingular + "\n"
coloredMap += mapPartBlankSingular + maploc12 + mapPartWayRow + maploc01 + mapPartWayRow + maploc02 + mapPartBlankShort + maploc14 + mapPartWayRow + maploc15 + mapPartWayRow + maploc16 + mapPartBlankSingular + "\n"
coloredMap += mapPartBlankRow

for color in coloredMapList:
    print(color, end="")
    
print()
print(coloredMap)