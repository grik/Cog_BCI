## Modules


### Board management module

Basicly, a central command unit of our BCI. It should be able to choose between different board types, config and all necessary options. Should be implemented within one process, and as a listener (so no other actions besides connecting to board).

TODO: Imports of modules should work properly. At this moment, they dont :C
TODO: Tests coverage
TODO: Some improvments, but the base seems to be ok.


### // Connector module (Cyton)
Connect and standby. 

Module should be implemented in `modules/boards/cyton` and should allow for connecting to the board and sending commands, from upper - board management - level.

So. 

Board management sends command to Connector module, and connector evaluates this command and waits for further instructions.


### Board Simulator 

This module should simulate work of bci device.
Read from file -> simulation of signal samples, so
array 8 x 250 per second.
Start and stop of signal streaming.



### Data managment 

TBD


