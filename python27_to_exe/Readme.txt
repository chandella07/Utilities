Convert python27 script to exe

- Download py2exe module using pip
  pip install py2exe (if get any error for microsoft c++ compiler for python, download that and install)

- create a setup.py file.
  add script name and dependent modules in this.

- Go to script directory and put setup.py there.
  open cmd prompt and execute : python setup.py py2exe

- It will create two dir
  dist and build, you can get your exe in dist folder. It may contain some dependent dll or other files.
