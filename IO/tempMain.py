import time
import sys
import tempRead
import tempWrite

global sandboxON
sandboxON = False

global registerSize
registerSize = 1


def sentToDevice(targetIP, toWriteData, unit):
    return tempWrite.write(targetIP, toWriteData, unit)

def checkStorage(unitMap, status):
    for unitNum in range(0, len(unitMap)):
        currentStatusData = tempRead.read('127.0.0.1', 0, registerSize, unitNum)
        print("[%d] %s" % (unitNum, currentStatusData))
        # compare current status , it don't match old status, write to storage, and sent to sandbox.
        if(status[unitNum] is not False and
                currentStatusData == status[unitNum]):
            continue

        if(sandboxON):
            sandboxAccept = False
            if(sandboxAccept):
                if(sentToDevice(unitMap[unitNum], currentStatusData, unitNum)):
                    status[unitNum] = currentStatusData
            else:
                print("[!]dangerous action to device(%s): %s" % (unitMap[unitNum], currentStatusData))
        else:
            print(currentStatusData, " <-> ", status[unitNum])
            if(sentToDevice(unitMap[unitNum], currentStatusData, unitNum)):
                status[unitNum] = currentStatusData


def initial(unitMap, status):
    for unitNum in range(0, len(unitMap)):
        statusData = tempRead.read('127.0.0.1', 0, registerSize, unitNum)
        if(statusData == False):
            sys.exit("initial failed.")
        status.append(statusData)

def startIO():
    unitMapIP = ["172.20.10.8", "192.168.100.105", "192.168.100.33"]
    lastUnitStatus = []
    initial(unitMapIP, lastUnitStatus)
    while(True):
        print("keep reading storage...")
        checkStorage(unitMapIP, lastUnitStatus)
        time.sleep(0.8)


startIO()
