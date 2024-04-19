from MemorySpyInterface import MemorySpyInterface

class GraphicsSpy(MemorySpyInterface):

    def __init__(self,configFile):
        super().__init__(configFile)
        self.__activeCars = 0
        self.__reiterate = True

    def __regenerateFields(self):

        # Restablish the fields needed to accomodate all the cars in track
        self._fields = self._fields[:22]+[f"coordinates_{axis}_{index}" for index in range(self.__activeCars) for axis in ['X','Y','Z'] ]+[f"carID_{index}" for index in range(self.__activeCars)]+self._fields[22:]
          
    def __regenerateLayout(self):

        # Restablish the layout to be interpreted acordingly
        self._layout = self._layout[:22]+f"{self.__activeCars*4}f"+self._layout[22:]
        
    def spy(self) -> dict:

        # Main function to request for information to the class

        rawData = self._collect()
        data = {}
        if self.__reiterate or self.__activeCars != rawData[21]: # In this section we check if the active cars in the track have changed, run at least in the first request
            self.__activeCars = int(rawData[21])
            self.__reiterate = False
            self.__regenerateFields()
            self.__regenerateLayout()
            rawData = self._collect()
        for index,value in enumerate(rawData): # transcript list to dict.
            if isinstance(value,bytes):
                value = value.decode('ISO-8859-1')
            data[self._fields[index]] = value

        return data

if __name__ == "__main__":

    graphicSpy = GraphicsSpy(".configFiles/graphics.json")

    while True:
        data = graphicSpy.spy()
        print("=== New Time ===")
        print(data["currentTime"])
        print(data["coordinates_X_12"],data["coordinates_Y_12"],data["coordinates_Z_12"])