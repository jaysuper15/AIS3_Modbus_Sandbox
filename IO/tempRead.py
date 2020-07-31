from pymodbus.client.sync import ModbusTcpClient


def read(host, addr, count, unit):
    try:
        client = ModbusTcpClient(host)
    except:
        print("[X](read)connection failed.")
        return False

    try:
        result = client.read_holding_registers(addr, count, unit=unit)
        client.close()
        return result.registers
    except:
        print("[X]read failed.")
        return False

