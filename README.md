# A Project Folder For Use of BirdNET

## Introduction

This is a project folder for using BirdNET. 

The BirdNET python library has been added to this project. 

Note that it is important to use the V3.0 models, which can be used for any purpose, incuding commercial. V2.4 cannot. 

There is an R package ("birdnetR") that is a wrapper for the BirdNET Python library. However, its seems you can only use the v2.4 model. Until that is updated, it is necessary t the use the Python version. 

So it looks like it is best to run birdnet in python. Then process the data using the R Package birdnetTools. Both R and python scripts can be run from within the same project (assuming you are using the Positron IDE). 

## How to Set Up and New Project

1. First off, the easiest approach to working in a mixed R and Python environment is to use the Positron IDE from Posit. Positron handles both languages natively. The Positron IDE is free and there are no licensing or use restrictions. A single project can run Python for the BidNET model and then R scripts can be run for cleaning and processing etc. (unless of course you want to keep using Python). An alternative could be to work in another type of Python environment like a bare command line prompt and using Conda or other package and environment manager. 

2. Install Positron. If not already installed, also install R. In Positron, add extensions to work with R and Python and for syntax completion in each language. See Posit's guide.  https://positron.posit.co/welcome.html. The python package and environment manager 'uv' can be used to install python and set up environments. 

4. Create a new project in Positron. Create the remote repository on Github as well, if you are using it. Create some folders for audio input files, outputs, and folder for R and Python scripts. 

5. Install birdnet using the following at the terminal prompt. 

    ```{powershell}
    uv add birdnet
    # Check all packages:
    uv pip list
    ```
6. Run the birdnet functions. See the example script called "run_birdnet.py".



## BirdNET Update

If BirdNET releases a new version, run this in the terminal (make sure you are in your project folder):
```{powershell}
uv add --upgrade birdnet
```

## Other Packages 

NSNSDAAcoustics has a bunch of additional tools for wrangling and anlyzing BirdNet outputs.
https://github.com/nationalparkservice/NSNSDAcoustics
