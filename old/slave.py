import subprocess

def startSlave(mode="a"):
    args = ("./diagslave/diagslave")
    # args = ("ls")
    print("slave working...")
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    try:
        outs, errs = popen.communicate(timeout=2)
        popen.wait()
        output = popen.stdout.read()
        return output
    except subprocess.TimeoutExpired:
        popen.kill()
        outs, errs = popen.communicate()
        return outs
