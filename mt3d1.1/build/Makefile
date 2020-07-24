# makefile created on 2017-12-01 13:31:56.054283
# by pymake (version 1.1.0)
# using the gfortran fortran and gcc c/c++ compilers.

# Define the directories for the object and module files,
# the executable, and the executable name and path.
OBJDIR = ./obj_temp
BINDIR = \
PROGRAM = ../mt3d.exe
SOURCEDIR1=../src

VPATH = \
${SOURCEDIR1} 

.SUFFIXES: .c .cpp .f .f90 .F90 .fpp .o

# Define the Fortran compile flags
FC = gfortran
FFLAGS = -O2 -fbacktrace 

# Define the C compile flags
CC = gcc
CFLAGS = -O3 -D_UF 

# Define the libraries
SYSLIBS = 

OBJECTS = \
$(OBJDIR)/utl1.o \
$(OBJDIR)/mt_module.o \
$(OBJDIR)/fmi1.o \
$(OBJDIR)/gcg1.o \
$(OBJDIR)/cts1.o \
$(OBJDIR)/hss1.o \
$(OBJDIR)/tob1.o \
$(OBJDIR)/uzt1.o \
$(OBJDIR)/xmdlib1.o \
$(OBJDIR)/dsp1.o \
$(OBJDIR)/adv1.o \
$(OBJDIR)/lkt1.o \
$(OBJDIR)/mf6grb.o \
$(OBJDIR)/rct1.o \
$(OBJDIR)/ssm1.o \
$(OBJDIR)/xmd1.o \
$(OBJDIR)/gnt1.o \
$(OBJDIR)/mf6bud.o \
$(OBJDIR)/sft1.o \
$(OBJDIR)/fmi1mf6.o \
$(OBJDIR)/btn1.o \
$(OBJDIR)/mt3d-usgs.o \

# Define task functions

# Create the bin directory and compile and link the program
all: makebin | $(PROGRAM)

# Make the bin directory for the executable
makebin :
	mkdir -p $(BINDIR)

# Define the objects that make up the program
$(PROGRAM) : $(OBJECTS)
	-$(FC) $(FFLAGS) -o $@ $(OBJECTS) $(SYSLIBS) -I$(OBJDIR) -J$(OBJDIR) 

$(OBJDIR)/%.o : %.f
	@mkdir -p $(@D)
	$(FC) $(FFLAGS) -c $< -o $@ -I$(OBJDIR) -J$(OBJDIR) 

$(OBJDIR)/%.o : %.f90
	@mkdir -p $(@D)
	$(FC) $(FFLAGS) -c $< -o $@ -I$(OBJDIR) -J$(OBJDIR) 

$(OBJDIR)/%.o : %.F90
	@mkdir -p $(@D)
	$(FC) $(FFLAGS) -c $< -o $@ -I$(OBJDIR) -J$(OBJDIR) 

$(OBJDIR)/%.o : %.fpp
	@mkdir -p $(@D)
	$(FC) $(FFLAGS) -c $< -o $@ -I$(OBJDIR) -J$(OBJDIR) 

$(OBJDIR)/%.o : %.c
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) -c $< -o $@

$(OBJDIR)/%.o : %.cpp
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) -c $< -o $@

# Clean the object and module files and the executable
.PHONY : clean
clean : 
	-rm -rf $(OBJDIR)
	-rm -rf $(PROGRAM)

# Clean the object and module files
.PHONY : cleanobj
cleanobj : 
	-rm -rf $(OBJDIR)

