# A Project Folder For Use of BirdNET

This is a project folder for using BirdNET. 

The BirdNET python library has been added to this project. 

Note that it is important to use the V3.0 models, which can be used for any purpose, incuding commercial. V2.4 cannot. 

There is an R package ("birdnetR") that is a wrapper for the python library. However, its seems yo can only use the v2.4 model. 

So it looks like it is best to run birdnet in python. Then process the data using the R Package birdnetTools. Both R and python scripts can be run (assuming you are using Positron). 

## BirdNET Update

If BirdNET releases a new version, run this in the terminal
```{powershell}
uv add --upgrade birdnet
```
