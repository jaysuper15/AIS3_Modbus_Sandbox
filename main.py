import time
import sys
import Read
import Write
import Sandbox

global sandboxON
sandboxON = True

global registerSize
registerSize = 1


def sentToDevice(targetIP, toWriteData, unit):
    return Write.write(targetIP, toWriteData, unit)

def checkStorage(unitMap, status, sandbox):
    for unitNum in range(0, len(unitMap)):
        currentStatusData = Read.read('127.0.0.1', 0, registerSize, unitNum)
        print("[%d] %s" % (unitNum, currentStatusData))
        if(status[unitNum] is False):
            print("[X]read failed, ignore this unit.")
            continue

        # compare current status , it don't match old status, write to storage, and sent to sandbox.
        if(currentStatusData == status[unitNum]):
            continue

        if(sandboxON):
            sandboxAccept = sandbox.checkSandBox(unitNum, currentStatusData[0])
            if(sandboxAccept):
                if(sentToDevice(unitMap[unitNum], currentStatusData, unitNum)):
                    status[unitNum] = currentStatusData
                else:
                    print("[X]sent to device failed.")
            else:
                print("[!]dangerous action to device[%s]: %s" % (unitMap[unitNum], currentStatusData))
                print("[!]Recovery to last status.")
                if(sentToDevice(unitMap[unitNum], status[unitNum], unitNum)):
                    print("[-]Recover success.")
                else:
                    print("[X]Recover failed.")
        else:
            print(currentStatusData, " <-> ", status[unitNum])
            if(sentToDevice(unitMap[unitNum], currentStatusData, unitNum)):
                status[unitNum] = currentStatusData
            else:
                print("[X]sent to device failed.")


def initial(unitMap, status):
    for unitNum in range(0, len(unitMap)):
        statusData = Read.read('127.0.0.1', 0, registerSize, unitNum)
        if(statusData == False):
            sys.exit("initial failed.")
        status.append(statusData)
    sandbox = None
    if(sandboxON):
        print("[-]The sandbox is ON!")
        sandbox = Sandbox.SandBox()
        return sandbox
    else:
        print("[!]The sandbox is current OFF!")
        return None

def startIO():
    # unitMapIP = ["172.20.10.11", "172.20.10.7", "172.20.10.8"]
    unitMapIP = ["127.0.0.1", "127.0.0.1", "127.0.0.1"]
    lastUnitStatus = []
    sandbox = initial(unitMapIP, lastUnitStatus)
    while(True):
        print("keep reading storage...")
        checkStorage(unitMapIP, lastUnitStatus, sandbox)
        time.sleep(1.5)
        print()

if __name__ == "__main__":
    startIO()
