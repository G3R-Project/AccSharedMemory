from MemorySpyInterface import MemorySpyInterface
import time

class GraphicsSpy(MemorySpyInterface):

    def __init__(self,configFile):
        super().__init__(configFile)
        self.__activeCars = 60
        self.__reiterate = True
        # Restablish the fields needed to accomodate all the cars in track
        self._fields = self._fields[:22]+[f"coordinates_{axis}_{index}" for index in range(self.__activeCars) for axis in ['X','Y','Z'] ]+[f"carID_{index}" for index in range(self.__activeCars)]+self._fields[22:]
        # Restablish the layout to be interpreted acordingly
        self._layout = self._layout[:32]+f"{self.__activeCars*3}f"+f"{self.__activeCars}i"+self._layout[32:]
        
    def spy(self) -> dict:

        # Main function to request for information to the class
        rawData = self._collect()
        data = {}

        for index,value in enumerate(rawData): # transcript list to dict.
            if isinstance(value,bytes):
                value = value.decode('ISO-8859-1')
            data[self._fields[index]] = value

        return data

if __name__ == "__main__":

    graphicSpy = GraphicsSpy("./configFiles/graphics.json")

    while 1:
        
        data = graphicSpy.spy()
        print("wiperLV: ",data["wiperLV"])
        print("rainLights: ",data["rainLights"])
        print("lightsStage: ",data["lightsStage"])
        print("flashingLights: ",data["flashingLights"])
        print("========")
        time.sleep(1)