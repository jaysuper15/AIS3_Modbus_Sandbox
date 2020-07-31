from pymodbus.client.sync import ModbusTcpClient

def write(host, dataList, unit):
    starterAddress = 14
    # print("HERE", host)
    try:
        client = ModbusTcpClient(host)
    except:
        print("[X](write)connection failed.")
        return False
    for addr in range(0, len(dataList)):
        try:
            print("[-]Write regsiter %s(%s) to %s" % (addr, dataList[addr], unit))
            client.write_register(starterAddress+addr, dataList[addr], unit=unit)
        except:
            print("[X]unable to write data to unit:%d" % (unit))
            return False
    client.close()
    return True
