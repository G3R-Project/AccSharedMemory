import mmap
import struct
from functools import reduce
import json
from abc import ABC, abstractmethod

class MemorySpyInterface(ABC):

    def __init__(self,configFile):

        # class constructor
        # INPUTS:
        #     configFile: a json file with proper configuration of memory space, layout and fields to gather.

        self._configFile = configFile
        self._ACCESS = mmap.ACCESS_READ
        self.__createScheme()

    def __createScheme(self):

        # method that builds the scheme and sets all parameters necesary for mmap to gather the data from sharedMemory(SM)
        # try:
        file = open(self._configFile)
        config = json.load(file)
        self._sharedMemorySpace = config["sharedMemorySpace"]
        self._generateFields(config)
        self._generateLayout(config)
    
    def _generateFields(self,config) -> list:

        # Reconstructs a list of the fields to be read from SM
        self._fields = list(config["data"].keys())

    def _generateLayout(self,config) -> list:

        # method to generate the bytes layout to gather the data from SM   
        self._layout = reduce(lambda x, y:x+y,[config["data"][key] for key in self._fields])

    def _collect(self) -> list:

        #Retrieves raw data from SM

        shm_size = struct.calcsize(self._layout)
        mmapData = mmap.mmap(-1,shm_size,self._sharedMemorySpace,access=self._ACCESS)
        mmapData.seek(0)
        dataList = struct.unpack(self._layout, mmapData.read(shm_size))

        return dataList
    
    @abstractmethod
    def spy(self) -> dict:
        
        # Method to be implemented with the caracteristics of each subclass
        pass