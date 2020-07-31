import subprocess
import time

def startMaster(host, data, port="502"):
    args = ["./mbpoll", host, data]
    # args = "./mbpoll %s -p %s -- %s" % (host, port, data)
    # args = "ls"
    print("master working...")
    print("arg; ", args)
    time.sleep(0.6)
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    try:
        outs, errs = popen.communicate(timeout=2)
        popen.wait()
        time.sleep(0.3)
        return outs
    except subprocess.TimeoutExpired:
        popen.kill()
        outs, errs = popen.communicate()
        return outs
