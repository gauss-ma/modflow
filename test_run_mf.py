import numpy as np
import matplotlib.pyplot as plt
import flopy
import flopy.modflow as mf
import flopy.mt3d as mt
import flopy.utils as fu
#MODFLOW 2005
modelname = 'flowModel'
modPath= '/home/alumno/Git/modflow/run/'
exePath='/home/alumno/Git/modflow/mf2005/exe/mf2005.exe'
mfModel = mf.Modflow(modelname = modelname, model_ws=modPath, exe_name=exePath)

#DIS (discretizacion)
Lx = 610
Ly = 310
nrow = 61
ncol = 61
nlay = 1
delr = Lx / ncol
delc = Ly / nrow
top = np.ones((nrow, ncol))*20
botm = np.ones((nrow, ncol))*-40
nper = 1
perlen = 2700
nstp = 5

dis = mf.ModflowDis(mfModel, nlay, nrow, ncol, delr = delr, delc = delc, 
                    top = top, botm = botm, laycbd = 0, itmuni=4, 
                    nper = nper, perlen = perlen, nstp = nstp, tsmult=1.4)

#BCF file
laycon=1 #confined
tran=1600.0 #transmissivity
bcf = flopy.modflow.mfbcf.ModflowBcf(mfModel,laycon=laycon, tran=tran)

#BAS file
strt=15 #starting head
ibound=np.ones((nrow, ncol))
bas = mf.ModflowBas(mfModel, ibound = ibound, strt = strt)

#PCG file
pcg = flopy.modflow.mfpcg.ModflowPcg(mfModel, mxiter=20, iter1=30, hclose=1e-03, rclose=1e-03, relax=1.0)

#CHD (Constant Head Discharge?)
chd_data = []
for c in range(mfModel.dis.nrow):
    lChd = np.array([0, c, 0, 20, 20])
    rChd = np.array([0, c, mfModel.dis.ncol-1, 12, 15])
    chd_data.append(lChd)
    chd_data.append(rChd)
stress_period_data = {0:chd_data}
chd = mf.mfchd.ModflowChd(mfModel, stress_period_data=stress_period_data)

#WELL (pozo)
inyectingWell = 200 #m3/d
pumpingWell = -400
wel_sp1 = []
wel_sp1.append([0, 15, 15, inyectingWell])
wel_sp1.append([0, 5, 45, pumpingWell])
stress_period_data = {0: wel_sp1}
wel = flopy.modflow.ModflowWel(mfModel, stress_period_data=stress_period_data)


#LMT Linkage with MT3DMS for multi-species mass transport modeling
lmt = flopy.modflow.ModflowLmt(mfModel, output_file_name='mt3d_link.ftl')

# OC (Output Control)
oc = mf.ModflowOc(mfModel,stress_period_data={(nper-1, nstp-1): ['save head']},)


#Write input files
mfModel.write_input()

# run the model
mfModel.run_model()



#Plot model results
import matplotlib.pyplot as plt
import flopy.utils.binaryfile as bf

# Create the headfile object
headobj = bf.HeadFile(modPath + modelname+'.hds')
times = headobj.get_times()
print(times)
head = headobj.get_data(totim=times[-1])


# Setup contour parameters
levels = np.arange(10, 20, 1)
extent = (delr/2., Lx - delr/2., delc/2., Ly - delc/2.)

# Make the plots
fig = plt.figure(figsize=(18,8))
plt.subplot(1, 1, 1, aspect='equal')
plt.title('Head distribution (m)')
plt.imshow(head[0, :, :], extent=extent, cmap='YlGnBu', vmin=15., vmax=20.)
plt.colorbar()

contours = plt.contour(np.flipud(head[0, :, :]), levels=levels, extent=extent, zorder=10)
plt.clabel(contours, inline=1, fontsize=10, fmt='%d')# zorder=11)

plt.show()








#MT3D-USGS
mt_exe='/home/alumno/Git/modflow/mt3d1.1/exe/mt3d.exe'
mt_name='transModel'
mt_model= mt.Mt3dms(modelname=mt_name, model_ws=modPath, version='mt3d-usgs', exe_name=mt_exe, modflowmodel=mfModel)

#BTN file
btn = flopy.mt3d.Mt3dBtn(mt_model, sconc=0.0, prsity=0.3, thkmin=0.01, munit='g')#, icbund=icbund)

#ADV file
mixelm = -1 #Third-order TVD scheme (ULTIMATE)
percel = 1  #Courant number PERCEL is also a stability constraint
adv = flopy.mt3d.Mt3dAdv(mt_model, mixelm=mixelm, percel=percel)

#GCG file
mxiter = 1  #Maximum number of outer iterations
iter1 = 200 #Maximum number of inner iterations
isolve = 3  #Preconditioner = Modified Incomplete Cholesky
gcg = flopy.mt3d.Mt3dGcg(mt_model, mxiter=mxiter, iter1=iter1, isolve=isolve)

#DSP file
al = 10     #longitudinal dispersivity
dmcoef = 0  #effective molecular diffusion coefficient
trpt = 0.1  #ratio of the horizontal transverse dispersivity to the longitudinal dispersivity
trpv = 0.01 #ratio of the vertical transverse dispersivity to the longitudinal dispersivity
dsp = mt.Mt3dDsp(mt_model, al=al, dmcoef=dmcoef, trpt=trpt, trpv=trpv)

#SSM file
itype = flopy.mt3d.Mt3dSsm.itype_dict()
#itype
#{'CHD': 1,
# 'BAS6': 1,
# 'PBC': 1,
# 'WEL': 2,
# 'DRN': 3,
# 'RIV': 4,
# 'GHB': 5,
# 'MAS': 15,
# 'CC': -1}
#[K,I,J,CSS,iSSType] = layer, row, column, source concentration, type of sink/source: well-constant concentration cell 
ssm_data = {}
ssm_data[0] = [(0, 15, 15, 65.0, 2)]

ssm = flopy.mt3d.Mt3dSsm(mt_model, stress_period_data=ssm_data)
#Write model input
mt_model.write_input()

#Run the model
mt_model.run_model(silent=True)
#(False, [])

#Plot concentration results
conc = fu.UcnFile(modPath+'MT3D001.UCN')
conc.get_times()
fig = plt.figure(figsize=(18,8))
conc.plot(totim=times[-1], colorbar='Concentration (mg/l)', cmap='Blues')
plt.title('Concentration distribution (mg/l)')
plt.show()


flopy.export.vtk.export_array(mt_model,array=conc,name='prueba.vtk',output_folder='./')
