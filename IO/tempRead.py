from pymodbus.client.sync import ModbusTcpClient


def read(host, registerIndex, registerSize, unit):
    starterAddress = 14
    try:
        client = ModbusTcpClient(host)
    except:
        print("[X](read)connection failed.")
        return False

    try:
        result = client.read_holding_registers(starterAddress + registerIndex, registerSize, unit=unit)
        client.close()
        return result.registers
    except:
        print("[X]read failed.")
        return False

