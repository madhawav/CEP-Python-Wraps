Note: Pyjnius Wrapper only works with Python 2.7.x as of now.

# Pre-requisites
- Python 2.7.x or 3.x
- Cython (`sudo apt-get install cython`)
- Pyjnius (build from source as explained below)

# Installing Pyjnius
1) Make sure Cython is already installed since it is a pre-requisite to Pyjnius
2) Download Source from Github Repo - https://github.com/kivy/pyjnius (master branch)
3) Goto source directory and run make.
4) Goto Source directory and run setup.py ( `sudo python2 setup.py install` or `sudo python3 setup.py install`)

NOTE: if your doing a new build from same source, remember to delete pyjnius/jnius/jnius.c. 
Deleting the above file is necessary if your doing the new build for a different version of python.

Pyjnius Documentation - https://pyjnius.readthedocs.io/en/latest/installation.html
 
# Running the code
1) Clone this repository.
2) Goto `Pyjnius_Prototype_Wrap_Python2_3/SiddhiPythonApiProxy/` and run `mvn install`
3) Copy `pyjnius.jar` file from `[pyjnius_source_directory]/build` to `Pyjnius_Prototype_Wrap_Python2_3/SiddhiPythonApiProxy/target/lib/`
4) Run `/Pyjnius_Prototype_Wrap_Python2_3/TestApp.py` ( `python2 TestApp.py` or `python3 TestApp.py`)

