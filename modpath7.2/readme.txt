
December 15, 2017

                  MODPATH - Version: 7.2.001

MODPATH is a particle-tracking model designed to work with output from 
MODFLOW-2005, MODFLOW-USG, and MODFLOW-6. This version of MODPATH is packaged 
for personal computers using the Microsoft Windows operating system (versions
7, 8, or 10).  Executable files for personal computers are provided as 
well as the source code.  The source code can be compiled to run on 
other computers.

Instructions for installation, execution, and testing of MODPATH are
provided below.

SOFTWARE NOTICE:
This software has been approved for release by the U.S. Geological
Survey (USGS). Although the software has been subjected to rigorous
review, the USGS reserves the right to update the software as needed
pursuant to further analysis and review. No warranty, expressed or
implied, is made by the USGS or the U.S. Government as to the
functionality of the software and related material nor shall the
fact of release constitute any such warranty. Furthermore, the
software is released on condition that neither the USGS nor the U.S.
Government shall be held liable for any damages resulting from its
authorized or unauthorized use. Also refer to the USGS Water
Resources Software User Rights Notice for complete use, copyright,
and distribution information.

Any use of trade, product or firm names is for descriptive purposes 
only and does not imply endorsement by the U.S. Government.

                            TABLE OF CONTENTS

                         A. DISTRIBUTION FILE
                         B. DOCUMENTATION
                         C. INSTALLING
                         D. EXECUTING MODPATH
                         E. EXAMPLE PROBLEMS
                         F. COMPILING

A. DISTRIBUTION FILE

The files for this distribution are provided in a ZIP archive file named:

  modpath_7_2_001.zip
  
To extract the files, select a directory and extract the zip file to the 
selected directory.The following directory structure will be created:

  |-- modpath_7_2_001
      |-- bin                            [Executables for MODPATH]
      |
      |-- doc                            [User's guide and other documents]
      |
      |-- examples                       [Example simulations with input and output]
         |
         |-- ex01 
             |-- modflow-2005
                 |-- original
                 |-- work
             |-- modflow_mf6
                 |-- original
                 |-- work
         |-- ex02
             |-- modflow-usg
                 |-- original
                 |-- work
             |-- modflow-6
                 |-- original
                 |-- work
         |-- ex03
             |-- modflow-6
                 |-- original
                 |-- work
         |-- ex04
             |-- modflow-6
                 |-- original
                 |-- work
      |
      |-- make                           [gfortran makefiles]
      |
      |-- source                         [Source code for MODPATH]
      |
      |-- utilities
          |-- modpath_shapefile_exporter [Utility to convert MODPATH output to shapefiles]
          |-- quadpatch_grid_exporter    [Utility to create data files for quadpatch unstructured grids]
    
It is recommended that no user files are kept in the modpath_7_2_001 directory
structure.  If you do plan to put your own files in the modpath_7_2_001
directory structure, do so only by creating additional subdirectories.

Some of the documents provided are Portable Document Format (PDF) files. PDF files are 
readable and printable on various computer platforms using Acrobat Reader from Adobe. 
The Acrobat Reader is freely available from the following World Wide Web site:

      http://www.adobe.com/



B. DOCUMENTATION

The following documents are provided in the "doc" directory:

                   ofr20161086.pdf -- MODPATH-7 user's guide report
                  modpath_7_io.pdf -- Documentation of input and output files
            modpath_7_examples.pdf -- Description of example problems
    modpath_shapefile_exporter.pdf -- Documentation for a utility progran to export
                                      MODPATH particle coordinate file data as ESRI shapefiles
       quadpatch_grid_exporter.pdf -- Documentation for a utility program to generate unstructured
                                      grid data files for use by MODFLOW-USG, MODFLOW-6, and MODPATH-7.


C. INSTALLING

To make the executable version of MODPATH accessible from any
directory, the directory containing the executables (modpath_7_2_001\bin)
should be included in the PATH environment variable.  Also, if a 
prior release of MODPATH version 7 is installed on your system, the
directory containing the executables for the prior release should
be removed from the PATH environment variable. Existing installations
of MODPATH version 6 or earlier are not affected by the installation
of MODPATH version 7 and do not need to be removed.

As an alternative, the executable file, mpath7.exe in the modpath_7_2_001\bin 
directory can be copied into a directory already included in the PATH 
environment variable. System batch files also can be used to run MODPATH. 
System batch files are executable text files that can be constructed in a way
that allows MODPATH to be run from a specified directory without the need for
that directory to be in the user's search path. Refer to the Microsoft Windows 
help topics or consult your system administrator for assistance with batch files
instructions for modifying the PATH environment variable.


D. EXECUTING MODPATH

Two MODPATH runfiles are provided in the modpath_7_2_001\bin directory:

         mpath7.exe  -- a 64-bit executable file for Microsoft Windows computers
   mpath7_win32.exe  --  a 32-bit executable file for Microsoft Windows computers

if the executable files in the modpath_7_2_001\bin directory are installed
in a directory that is included in the system search path, MODPATH cab be run from
a Windows Command-Prompt window using the following command:

          mpath7.exe [Fname]
          
or

          mpath7_win32.exe [Fname]

The optional Fname argument is the name of a MODPATH simulation file.  
If no argument is used, the user is prompted to enter the name of a 
MODPATH simulation file.  If the simulation file name ends in ".mpsim", 
the file name can be specified without including ".mpsim". 

The data arrays in MODPATH are dynamically allocated, so models
are not limited by hard-coded array limits. However, it is best to have
enough random-access memory (RAM) available to hold all of the required
data.  If there is less available RAM than this, the program will use
virtual memory, but this slows computations significantly.

Documention for model input and output files is provided in the file
"modpath_7_io.pdf".


E. EXAMPLE PROBLEMS

Four example problems are provided with this distribution. Test problems
mptest001_mf2005, mptest001_mf6, mptest002_mfusg, and mptest002_mnf6 
correspond to example problems 1 and 2 that are described in the MODPATH-7 
documentation report that is provided in file ofr20161086.pdf located in 
the doc directory. Test problem mptest003_mf6 is a derivative of examples 
1 and 2, but includes transient flow and additional stress packages.

Each example problem directory contains the following subdirectories:
  - original
  - work

The directory "original" includes a master copy of the MODFLOW and MODPATH 
data files setup to run MODPATH. The MODFLOW input and output files are
provided so there is no need to run MODFLOW prior to running MODPATH. The 
directory "work" is an empty directory that is provided as a convenient
place to make test runs of the example problems. To make a test run, copy 
all of the files in directory "original" into directory "work". Then, run
MODPATH by double clicking on the batch file named "run-math7.bat" located
in directory "work". The batch file is setup to run the MODPATH executable
file mpath7.exe located in the bin directory. To preserve the original files, 
you should not run MODFLOW or MODPATH from directory "original". 

The example problems are described in the file "modpath_7_examples.pdf".


F. COMPILING

The executable file provided in modpath_7_2_001\bin was created using the Intel
Parallel Studio XE2016 Composer Edition for Fortran Windows in combination
with Microsoft Visual Studio 2015.  The source code is provided in the 
modpath_7_2_001\source directory so that MODPATH can be recompiled if necessary.  
However, the USGS cannot provide assistance to those compiling MODPATH. 
In general, the requirements are a Fortran compiler that fully supports the 
Fortran-2003 standard.

MODPATH-7 also can be compiled using the GFORTRAN compiler, which is a
component of the GNU Compiler Collection (GCC). GFORTRAN is available at
no charge for many computer operating systems, includig Microsoft Windows, 
most varieties of unix, and Apple MacOS. Makefiles are provided for compiling 
MODPATH-7 on MS Windows, using the CYGWIN installation of GFORTRABN, and Apple 
MacOS.


