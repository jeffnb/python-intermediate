# Python Intermediate

## Setup Instructions

### Mac
By far the easiest way to install python and many programming applications such as mysql.  Consider it a package manager.  

#### Installing Homebrew
* Go to https://brew.sh/
* Use the command in the terminal application to download and install: `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
* Will install homebrew for you allowing you to use commands to install system packages

#### Installing Python
By default Mac OSX will come with an install of Python 2.7. This one is missing pip but can work in a pinch. For this class we are going to be using python 3 since that is the future of python and has started pulling away from 2.7 in terms of features.

##### With homebrew
* Run command: `brew install python3`
* Will install python 3.6 along with pip the package manager we will be using

##### Without Homebrew
* Go to https://www.python.org/downloads/release/python-362/ and grab the Mac OSX installation
* Download and install the package
* Keep in mind that you need to restart any terminals
* Open terminal and type `python3 --version` it should be 3.6

#### Installing Pip
You only need to do this if you decided to go without Homebrew
* Go to https://pip.pypa.io/en/latest/installing/
* Save the link for `get-pip.py` to your computer
* Find the file directory in the terminal and run `python3 get-pip.py`

### Windows

Windows takes a bit work to get python up and running correctly.  Once running it should be able to be used quickly going forward 

*Note*: Windows 10 allows for a built-in Ubuntu linux image that greatly enhances the power of Windows for development.  These instructions will get you started: https://www.windowscentral.com/how-install-linux-distros-windows-10

#### Python Install
* Download the installer for python from here: https://www.python.org/downloads/release/python-362/
* Run the installer to get python on the system.  Make a note of where the installer installs the python
* Restart any command shells you are using.
* Type `python --version` into a command prompt.  It should return you the version of python.
* If you receive an command not found error go to next section.

#### Python Not Found
* Make sure that you restarted any terminals before you try python.
* If the Python file isn't found then you will need to find the path where it was installed
* Open up the environment settings on your version of windows (Windows 10 hit windows key and type `path` for Edit Environment variables option).
* Add the path to the python install.  Windows 10 you should be able to use: `%USERPROFILE%\AppData\Local\Programs\Python\Python36`

#### Pip Install
Pip is the package manager you are going to be using to add external libraries to python
* Go to https://pip.pypa.io/en/latest/installing/
* Save the link for `get-pip.py` to your computer
* Find the file directory in the terminal and run `python3 get-pip.py`
* Add the python `scripts` path to Path Environment variable so the command can be used.  See above section.  In windows 10 it should be %USERPROFILE%\AppData\Local\Programs\Python\Python36\scripts
* Restart the terminals

### Linux Installs
Almost all distrobutions of linux have the python 3 options available in their respective package managers.  Look up what is easiest on your distrobution.

#### Ubuntu
* `sudo apt-get update`
* `sudo apt-get install python3`
* `sudo apt-get install python3-pip`

### Pycharm
Pycharm is one of the most powerful IDEs for python.  It is created by JetBrains who create IntelliJ for java.  We will be using it in class if possible to make things easier and give some autocomplete suggestions.  For this class it is recommended that you download the Professional Edition but the Community Edition is free and will still work just fine.

*Download*: https://www.jetbrains.com/pycharm/download/#section=windows
 
