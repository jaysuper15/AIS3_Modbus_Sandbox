class Light:
    state = 0

    def __init__(self):
        pass


class SandBox:
    def __init__(self):
        self.light_num = 3
        self.light_list = [Light() for i in range(self.light_num)]

    def checkSandBox(self, unitID, data):
        print('Start checkSandBox')
        if data > 1 and data != 3:
            return False
        elif data == 3:
            self.light_list[unitID].state = 0
        else:
            self.light_list[unitID].state = data
        print('End checkSandBox')
        return True

    def checkAll(self):
        for l in self.light_list:
            print(l.state)


if __name__ == "__main__":
    sb = SandBox()
    sb.checkSandBox(0, 1)
