import master
import slave

# master.startMaster("", "", "")
while(True):
    data = master.startMaster("127.0.0.1", "13")
    # data = master.startMaster("127.0.0.1", "12")
    # data = master.startMaster("127.0.0.1", "11")
    # data = master.startMaster("127.0.0.1", "10")
    # data = master.startMaster("127.0.0.1", "2")
    # data = slave.startSlave()
    if(data is not False):
        print(data)
        #analyze data to get host , port, data
        host = ""
        port = ""
        data = ""
        virtualResponse = master.startMaster(host, data, port)
        if(virtualResponse is True):
            # 4. sent to real device
            pass
        else:
            # ignore
            pass
