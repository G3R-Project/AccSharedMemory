from MemorySpyInterface import MemorySpyInterface

class StaticSpy(MemorySpyInterface):

    def __init__(self,configFile):
        super().__init__(configFile)

    def spy(self) -> dict:

        rawData = self._collect()
        data = {}
        for index,value in enumerate(rawData):
            if isinstance(value,bytes):
                value = value.decode("utf-8")
            data[self._fields[index]]=value

        return data

if __name__ == "__main__":

    staticSpy = StaticSpy(".configFiles/static.json")
    data = staticSpy.spy()
    for key in data.keys():
        print(key,data[key])
