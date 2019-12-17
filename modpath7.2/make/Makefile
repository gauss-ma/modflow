# makefile created on 2017-12-01 13:31:56.054283
# by pymake (version 1.1.0)
# using the gfortran fortran and gcc c/c++ compilers.

# Define the directories for the object and module files,
# the executable, and the executable name and path.
OBJDIR = ./obj_temp_cygwin
BINDIR = .
PROGRAM = mpath7gf.exe

SOURCEDIR1=../source

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
$(OBJDIR)/BudgetListItem.o \
$(OBJDIR)/GridLocation.o \
$(OBJDIR)/compilerversion.o \
$(OBJDIR)/HeadRecordHeader.o \
$(OBJDIR)/GlobalData.o \
$(OBJDIR)/UtilMisc.o \
$(OBJDIR)/ParticleLocation.o \
$(OBJDIR)/ModpathSubCellData.o \
$(OBJDIR)/ModpathUnstructuredBasicData.o \
$(OBJDIR)/TrackCellOptions.o \
$(OBJDIR)/openspec.o \
$(OBJDIR)/ParticleTrackingOptions.o \
$(OBJDIR)/Particle.o \
$(OBJDIR)/utl7.o \
$(OBJDIR)/BudgetRecordHeader.o \
$(OBJDIR)/Coordinate.o \
$(OBJDIR)/GridLocationList.o \
$(OBJDIR)/GeoReference.o \
$(OBJDIR)/TrackSubCellResult.o \
$(OBJDIR)/utl8.o \
$(OBJDIR)/ParticleLocationList.o \
$(OBJDIR)/ParticleGroup.o \
$(OBJDIR)/BudgetReader.o \
$(OBJDIR)/TimeDiscretizationData.o \
$(OBJDIR)/HeadReader.o \
$(OBJDIR)/ParticleCoordinate.o \
$(OBJDIR)/ParticleLocationPtr.o \
$(OBJDIR)/TrackSubCell.o \
$(OBJDIR)/ModflowGrid.o \
$(OBJDIR)/ParticleCoordinateList.o \
$(OBJDIR)/ParticlePath.o \
$(OBJDIR)/TrackPathResult.o \
$(OBJDIR)/ModflowRectangularGrid.o \
$(OBJDIR)/StartingLocationReader.o \
$(OBJDIR)/ModpathBasicData.o \
$(OBJDIR)/RectangularGridDisMf6.o \
$(OBJDIR)/RectangularGridDisuMf6.o \
$(OBJDIR)/RectangularGridDis.o \
$(OBJDIR)/ModpathSimulationData.o \
$(OBJDIR)/ModpathCellData.o \
$(OBJDIR)/RectangularGridDisvMf6.o \
$(OBJDIR)/RectangularGridDisuMfusg.o \
$(OBJDIR)/ModpathCellDataContainer.o \
$(OBJDIR)/TrackCellResult.o \
$(OBJDIR)/ParticleManager.o \
$(OBJDIR)/TrackCell.o \
$(OBJDIR)/ParticleTrackingEngine.o \
$(OBJDIR)/MPath7.o 

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

