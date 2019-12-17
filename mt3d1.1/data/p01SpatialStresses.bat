@ECHO OFF
REM Change directory
cd .\p01SpatialStresses(mf6)

REM Generate FTL file using MODFLOW-NWT ver 1.1.4 (or greater)
..\..\bin\mf6.exe  

REM Run MT3D-USGS only after FTL is generated
..\..\bin\MT3D-USGS_1.1.0_64.exe  p01SpatialStresses_4mf6_mt.nam

ECHO.
ECHO Run complete. Please press enter when you want to continue.
PAUSE>NUL