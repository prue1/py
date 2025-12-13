class Simple:
    def __init__(self, value):
        self.__value = value

    def getValue(self):
        return self.__value

    def __add__(self, other):
        return Simple(self.__value + other.__value)


sim1 = Simple(1)
sim2 = Simple(2)
print(f"1:{sim1.getValue()}")
print(f"2:{sim2.getValue()}")
sim3 = sim1 + sim2
print(f"3:{sim3.getValue()}")
print(f"4:{(sim1 + sim2).getValue()}")
