Note: Pyjnius Wrapper only works with Python 2.7.x as of now.

# Pre-requesites
- Python 2.7.x
- Cython (`sudo apt-get install cython`)
- Pyjnius (build from source as explained below)

# Installing Pyjnius
1) Make sure Cython is already installed since it is a pre-requisite to Pyjnius
2) Download Source from Github Repo - https://github.com/kivy/pyjnius (master branch)
3) Goto source directory and run make.
4) Goto Source directory and run setup.py ( `sudo python setup.py install` )

Pyjnius Documentation - https://pyjnius.readthedocs.io/en/latest/installation.html
 
# Running the code
1) Clone this repository.
2) Goto `/Pyjnius Prototype Wrap/SiddhiPythonApiProxy/` and run `mvn install`
3) Copy `pyjnius.jar` file from `[pyjnius_source_directory]/build` to `/Pyjnius Prototype Wrap/SiddhiPythonApiProxy/target/lib/`
4) Run `/Pyjnius Prototype Wrap/TestApp.py` ( `python TestApp.py`)

