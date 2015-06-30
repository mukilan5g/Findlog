# Findlog
Findlog is a python package,which helps you to do operations like grep.
If you install this you can able to retrieve the files which contains the pattern you specify.
And also you can use this package in other python packages.

#Dependencies
Findlog is tested to work under Python 2.6, Python 2.7. 

The required dependencies to build the software are py2exe and working C/C++ compiler.

For running the tests you need nose >= 1.1.2.

#Install
Before installing the package:

1. create a .files file in your local system.
2. copy the directory path of that file.
3. Open the findlog.py file in notepad.
   * change the content ``` paste the path here ``` into the path you copied. It was in line ``` 58 ```.
   * save the file.

This package uses distutils, which is the default way of installing python modules. To install in your home directory, use:

``` python setup.py install ```
