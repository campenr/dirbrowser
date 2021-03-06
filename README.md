dirbrowser version 0.1.0
========================

What's new
----------

- To specify files to select you can now enter either a single file, or a range of files by specifying hypen separated
start and stop file numbers (inclusive), or a comma separated combination of any/all of the above.

Bugs and issue tracking
-----------------------

This module should be platform independent, however testing has to
date only been performed with Windows 8.1 Pro using cmd.exe. Bug
reports should be submitted via the github issue tracker.


Description
-----------

This module is built for python 3, and is not backwards compatible
with python 2. 

This module includes a number of functions that provide basic directory browser functionality within the python
interpreter. The display of the directory is formatted as follows, where the '..', represents the parent directory: ::

  [1] ..
  [2] Folder1
  [3] File1.py
  [4] File2.txt
  [5] Folder2
  Enter a number to select the corresponding directory, or 0 to confirm current directory:

Entering the number corresponding to the desired directory changes to that
directory, providing the browsing functionality.

Usage
-----

You can browse the directory tree by calling browse_dir as follows: ::

  from dirbrowser import dirbrowser
  dirbrowser.browse_dir()

The function browse_dir is a wrapper for change_dir that calls another
function list_children, to create a list of all child items in the
current directory and display them. change_dir then takes the user input sets
the new working direcotry, and returns the current working directory on termination.

To display the files within a directory and select a subset (all or one): ::

  from dirbrowser import dirbrowser
  dirbrowser.select_files()

The function select_files calls list_children with specific filter
arguments to show only files, and optionally files of a specific type.

Used in combination, these functions can be used to set directories for
saving and for opening files, and processing a selection of the files: ::

  from dirbrowser import dirbrowser
  origin = os.getcwd()
  # Set save directory
  save_dir = dirbrowser.browse_dir()
  # Reset directory to original location
  os.chdir(origin)
  # Navigate to files to process
  open_dir = dirbrowser.browse_dir()
  files = dirbrowser.select_files()
  for file in files:
      os.chdir(open_dir)
      # Do things to file
      os.chdir(save_dir)
      # Save new file in new location

For a full description of these functions run ``help(dirbrowser)``

Installation
------------

Download the latest source package and run ``setup.py install`` or alternatively install the latest release via
pip with ``pip install dirbrowser``. A binary wheel distribution of the latest release is also available at PyPI (https://pypi.python.org/pypi/dirbrowser).

TODO
----

 - Add more checking of valid inputs when selecting files



License
-------

This software is released under the Modified BSD license. See 
LICENSE.txt for the full license.