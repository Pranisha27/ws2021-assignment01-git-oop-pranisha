# Environment
In order to do the assignments, every student needs to have a properly setup Python development environment. To make it easier to help in the case of errors, the following document will describe the reference environment which is recommended in order to perform the assignments. This will also make solutions to occuring problems applicable for all students and not only for the particular environment of each group or student.

Since this is an interdisciplinary master course and the level of programming and general computer knowledge can widely differ a guide to setup the respective environment on both Linux (definitly recommended) and Windows 10 will be provided aswell.

## Reference Environment Specifications
There are generally two popular ways of managing Python environments. One is directly using Python and the virtual environment functionality, the other one is using *Conda/Anaconda*. Either way of setting up Python is fine. However, the usage of a dedicated *virtual environment* or *conda Environment* is highly recommended, since you will most likely use Python for multiple courses within this semester, all of which might have different requirements when it comes to packages, Python version and other specifics.

The specifications of the environment recommended for this course are as follows:
- Python `3.8.x`, where `x` should be the most recent patch.
- Anaconda `>4.9.2` (4.9.2 or higher) *(optional)*

## Python Setup - Linux
There are a variety of ways to setup a Python environment on Linux machines. For the sake of simplicity most of you might opt to installing Python via the package manager of your Linux distribution. However, there might arise problems once you are required to manage different versions of Python. Therefore I will walk you through setting up Python `3.8.x` in a way that will allow you to install and manage multiple version of it easily.

### Ubuntu 20.04
It should be noted at this point that **Ubuntu 20.04** comes with **Python 3.8.5** preinstalled. In case that you have this version of Ubuntu LTS installed on your system you might not have to make any changes to your Python installation for this course. However, this guide might still help you to setup different versions for other courses or software projects in the future. To check the Python version you are running on, open the terminal and execute the following command
```shell
$ python3 --version
```
It should return `Python 3.8.5`.

### Installation from Source
Before we start with the actual installation procedure we should make sure that the mirrors and package lists the package manager is using are up to date.
```shell
$ sudo apt update && apt upgrade -y
```
In order to be able to properly install Python from sources we need to install a few dependencies. Execute the following two lines one after another.
```shell
$ sudo apt-get install build-essential checkinstall
$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
```
The latest version of Python can always be found on the Python Source Releases page on [Python.org](https://www.python.org/downloads/). Next to the most recent release, it also lists all previous active and inactive releases. Whenever you are looking to install Python on a machine please refer to this official site!

With this said we can go ahead and install the desired version of Python, in our case this is `3.8.9` at the time of writing this guide, since it is the most recent `3.8` release of Python.
```shell
$ cd /opt
$ sudo wget https://www.python.org/ftp/python/3.8.9/Python-3.8.9.tgz
$ echo "41a5eaa15818cee7ea59e578564a2629 Python-3.8.9.tgz" | md5sum -c -
```
First we change the directory to `/opt`, which is where we will install Python. The second command uses `wget` to download the applicable version of Python as a *gzipped source tarball*. The downloaded file is then checked against the MD5 sum to ensure that the file was not manipulated or is corrupted. We can now go ahead and unpack the archive file.
```shell
sudo tar xzf Python-3.8.9.tgz
```
With the sources now present on our machine we can proceed with the next step, which is actually installing the desired version of Python from its sources. To do is we will use a functionallity called `altinstall`. This enables us to install multiple versions of the same program on a Linux machine and make the operating system aware of it.
```shell
$ cd Python-3.8.9
$ sudo ./configure --enable-optimizations
$ sudo make altinstall
```
This may take a moment to complete. Once complete, `python3.8` should be visible in the `/usr/local/bin/` directory. To check this you can use the following command
```shell
$ ls /usr/local/bin/ | grep python3.8
```
If it outputs `python3.8` you have successfully installed **Python 3.8.9** on your system. Since you now have multiple versions of Python on your machine we can use the `update-alternatives` command to make Linux aware of this fact. The first command installes the already present version of Python3 as an alternative (please replace the `x` by the appropriate version already present on your system). The second one adds the newly installed Python 3.8.9 as another alternative.
```shell
$ update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.x 1
$ update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.8 2
```
Now we can use `update-alternatives --list` to list all the alternative installations we have of certain software:
```shell
$ update-alternatives --list python3
/usr/bin/python3.6
/usr/local/bin/python3.8
```

### Installing pip3
In order to use the Python package manager `pip` we need to install it on our system using the systems package manager. We will then update it to the latest version.
```shell
$ sudo apt install python3-pip
$ python3.8 -m pip install --upgrade pip
```

### Creating the virtual environment
Now that we have installed **Python 3.8.9** on our system the next step is to create the virtual environment, which we will use for the assignments in this course.

For those of you who are not yet farmiliar with the concepts of virtual environments in Python, it is basically a way to separate the packages that we are using in one project from the system and our other projects to avoid conflicts and other unwanted behaviour. The official documentation of the `venv` module states the following:

> The venv module provides support for creating lightweight “virtual environments” with their own site directories, optionally isolated from system site directories. Each virtual environment has its own Python binary (which matches the version of the binary that was used to create this environment) and can have its own independent set of installed Python packages in its site directories.

To create a new virtual environment we will use the `venv` module with Python
```shell
$ python3 -m venv /path/to/new/virtual/environment
```
The virtual environment is nothing but a directory in your file system containing the python packages that you are installing in it. To use the created virtual environment you will have to `source` the environment first by executing
```shell
$ source my-project-env/bin/activate
```
This has to be done everytime you want to use the virtual environment from a new terminal or after a system restart since the configuration is only temporary and limited to the very shell you are executing it in.

### Managing Python Packages
For managing our python packages we installed `pip` earlier in the installation guide and upgraded it to the most recent version. When you want to use a python package in your project you can now install it by simply running
```shell
pip3 install thepackagetoinstall
```
> Note that we are using `pip3` explicitly. This is important, since depending on the system you are on `pip` will refer to a python2 installation.

This however, must be run **inside** your respective virtual environment that you want to install it for. You therefore have to `source` the environment before running the installation.

### Switching the System default Python version
> This step is **NOT** required, since you will setup a virtual environment for this course. This is generally preferred over changing the systems Python version. However, I am noting it here, since it might be useful in some cases and it is the greatest benefit of this particular installation method over others, for example involving the package manager.

To switch the **system default Python** we can now do the following:
```shell
update-alternatives --config python3
```
You should be hit with a prompt like the one below. This will list all the versions of Python your system recognizes. Select the version of Python you'd like to use by providing the "selection" number to the prompt.
```shell
There are 2 choices for the alternative python3 (providing /usr/bin/python3).

  Selection    Path                      Priority   Status
------------------------------------------------------------
  0            /usr/local/bin/python3.8   2         auto mode
* 1            /usr/bin/python3.8         1         manual mode
  2            /usr/local/bin/python3.6   2         manual mode

Press <enter> to keep the current choice[*], or type selection number:
```
And that's basically it! To switch the **systems** Python versions, all you need to do is respond to the above prompt with the selection number representing the Python version you want to use.

## Python Setup - Windows
As for Linux there are different ways to setup a Python Environment on Windows. However, the most prominent and according to my experience both the most reliable and easiest way is to use *Conda*.

### Initial Installation
Since Anaconda has a very good [documentation](https://docs.anaconda.com/anaconda/install/windows/) I want to refer you to it at this point for the initial installation.

### Setup
After the installation is completed you should now press the *Super Key* and search for "Anaconda". There should be a command line application called "Anaconda PowerShell (Anaconda3)". After opening the application you should be greeted with a standard Windows Terminal that has the Anaconda environment loaded.

Since the Python version bundeled with Anaconda can differ I will now describe how you can install different versions of Python using the *Conda* commandline application.

First we will search for the Python versions available in our current Anaconda installation.
```shell
> conda search python
```
The output should look something like this:
```shell
Loading channels: done
# Name                       Version           Build  Channel
python                        2.7.13     h1b6d89f_16  pkgs/main
python                        2.7.13     h9912b81_15  pkgs/main
python                        2.7.13     hb034564_12  pkgs/main
python                        2.7.14     h2765ee6_18  pkgs/main
...
...
...
python                         3.8.0      hff0d562_2  pkgs/main
python                         3.8.1      h5fd99cc_1  pkgs/main
python                         3.8.1 h5fd99cc_8_cpython  pkgs/main
python                         3.8.1 he1778fa_7_cpython  pkgs/main
python                         3.8.2      h5fd99cc_0  pkgs/main
python                         3.8.2     h5fd99cc_11  pkgs/main
python                         3.8.2     he1778fa_13  pkgs/main
python                         3.8.3      he1778fa_0  pkgs/main
python                         3.8.3      he1778fa_2  pkgs/main
python                         3.8.5      h5fd99cc_1  pkgs/main
python                         3.8.5      he1778fa_0  pkgs/main
python                         3.8.8      hdbf39b2_4  pkgs/main
python                         3.9.0      h6244533_2  pkgs/main
python                         3.9.0      h8aef87e_1  pkgs/main
python                         3.9.1      h6244533_2  pkgs/main
python                         3.9.2      h6244533_0  pkgs/main
```
To change your python version you can now just type
```shell
conda install python=3.8.5
```

### Creating an Environment
As described in the [linux part](#creating-the-virtual-environment) we do not want to alter our system installation of Python we will create a *Conda Environment* which is equivalent to a python virtual environment concept wise.

In the terminal client enter the following where `yourenvname` is the name you want to call your environment, and replace `3.8.5` with the Python version you wish to use.
```shell
conda create -n yourenvname python=3.8.5
```

Once the environment is setup you can run where `yourenvname` is again replaced by the name you gave your environment.
```shell
conda activate yourenvname
```

### Managing Python Packages
Since we are using *Conda* as a package management system for our python installation I suggest that it is also used **exclusively** to manage Python packages.

Installing a package is as easy as running the following command, where `yourenvname` is again your environment name and `thepackagetoinstall` is the Python package you want to install.
```shell
conda install --name yourenvname thepackagetoinstall
```

> It should be noted, that some packages have a slightly different name or are not available in all desired versions via conda. You might have to conduct a short Google search in order to find the appropriate name.

In this assignment you will also learn the usage of `requirements.txt` files for setting up Python development environments without much manual effort. Such files can also be consumed by conda by running
```shell
conda install --file requirements.txt
```

## Configuring your IDE
One you have everything setup it comes to configuring your IDE to use the appropriate Python environment. There is a bunch of different IDEs out there, and while the choice of IDE is completely left up to you I from a personal experience can recommend both Visual Studio Code and PyCharm. For setting up a Python environment in VS Code please refer to [this link](https://code.visualstudio.com/docs/python/environments). For PyCharm [click here](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html).