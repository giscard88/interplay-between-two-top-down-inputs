import pylab
import numpy
import json
from Param import w_bu_pyr
import mtspec

from scipy import stats

reference_p_p=[]
no_super_p_p=[]
no_deep_p_p=[]

reference_np_p=[]
no_super_np_p=[]
no_deep_np_p=[]

reference_p_p_err=[]
no_super_p_p_err=[]
no_deep_p_p_err=[]

reference_np_p_err=[]
no_super_np_p_err=[]
no_deep_np_p_err=[]

gammas=[]
beta=[]

for xin in range(1,21):


    fp=open('lfp_super_ON_deep_ON_'+str(xin)+'.json','r')
    data=json.load(fp)
    fp.close()
    times=numpy.array(data['time'])
    lfps=numpy.array(data['lfp'])
   
    
    res=mtspec.multitaper.mtspec(lfps,1.0/1000.0, 4)
    freq=res[1]
    psd=res[0]
    ind=numpy.where((freq>=30.0)&(freq<100))[0]
    temp_gamma=numpy.mean(psd[ind])
    gammas.append(temp_gamma)


    fp=open('lfp_l5_super_ON_deep_ON_'+str(xin)+'.json','r')
    data=json.load(fp)
    fp.close()
    times=numpy.array(data['time'])
    lfps=numpy.array(data['lfp'])
   
    
    res=mtspec.multitaper.mtspec(lfps,1.0/1000.0, 4)
    freq=res[1]
    psd=res[0]
    ind=numpy.where((freq>=15.0)&(freq<30))[0]
    temp_gamma=numpy.mean(psd[ind])
    beta.append(temp_gamma)

gammas=numpy.array(gammas)
gammas=gammas/numpy.amax(gammas)


beta=numpy.array(beta)
beta=beta/numpy.amax(beta)



slope, intercept, r_value, p_value, std_err = stats.linregress(beta, gammas)

print (slope, r_value, p_value)

pylab.scatter(beta, gammas, s=30,c='b',edgecolors='none')
pylab.title('gamma beta correlations')
pylab.ylabel('normalized gamma power')
pylab.xlabel('normalized beta')


#pylab.subplot(2,1,2)    
#pylab.scatter(reference_np_p, gammas, s=10,c='b',edgecolors='none')
pylab.savefig('/local2/STDP_prune_refined/figs/beta_gamma_correl.png')
pylab.savefig('/local2/STDP_prune_refined/figs/beta_gamma_correl.eps')
pylab.show()







