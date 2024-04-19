[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# :car: ACC Shared Memory classes :car: :trophy:

Hi people, this is a small project for the community of ***G3R_project***.
accSharedMemory classes is a collection of 3 clases based on an common intarface and 3 config.json files, one for each class.
With this simple module you may import the class that you need to extract the information from the shared memory of Asseto Corsa (not tested yet) and Asseto Corsa Competizione.

If insterested in simracing and more remember to visit:

![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)  
@G3R-SimRacing :tada:


![Twitch](https://img.shields.io/badge/Twitch-9347FF?style=for-the-badge&logo=twitch&logoColor=white)
g3rsimracing :tada:

### Under the hood.

**How this module works?** 

Well it's based on the python's mmap module to read the shared memory of the simulator. The main core of the module is the interface called MemorySpyInterface.

**How do i use it?**

Just clone the repo and implement it in your project.
Import the module and the class you are interested in to the section of your project . Whenever you instantiate the class you need to inject it the path to the config file and that's just it.
If need any help in each of the classes there is an easy example in the *if __name__ == "__main__":* section.

**Known issues** :exclamation:

The current version has the following known bugs:

1) Initialization collision :collision: : if you implement the clases in a *"While True:"* loop, which is the way I use it almost all the time, when the loop is trying to access the memory at the same time that you load a track the game may freeze and never load the track. 

>[!TIP]
>A simple solution would be to implement a lower sample frequency until you detect that the field "packetId" has values **!=** of 0. And then increase the sampling frequency for accuracy in the values.

**Hope to have this bug fixed asap for the next commit :pray:**

# License

This python module is under an MIT license so feel free to use it as you wish and of course you are welcome to contribute with any upgrade you believe may be worth adding.

Hope you enjoy this module to create great simRacing stuff! :muscle:

