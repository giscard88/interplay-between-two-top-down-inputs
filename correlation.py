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

for xin in range(1,21):
    fp=open('weights_super_ON_deep_ON_'+str(xin)+'.json','r')
    data=json.load(fp)
    temp=data['after_p_p']
    temp=numpy.array(temp)-w_bu_pyr
    reference_p_p.append(numpy.mean(temp))
    reference_p_p_err.append(numpy.std(temp))

    temp=data['after_np_p']
    temp=numpy.array(temp)-w_bu_pyr
    reference_np_p.append(numpy.mean(temp))
    reference_np_p_err.append(numpy.std(temp))
    fp.close()
  
    fp=open('weights_super_OFF_deep_ON_'+str(xin)+'.json','r')
    data=json.load(fp)
    temp=data['after_p_p']
    temp=numpy.array(temp)-w_bu_pyr
    no_super_p_p.append(numpy.mean(temp))
    no_super_p_p_err.append(numpy.std(temp))

    temp=data['after_np_p']
    temp=numpy.array(temp)-w_bu_pyr
    no_super_np_p.append(numpy.mean(temp))
    no_super_np_p_err.append(numpy.std(temp))
    fp.close()

    fp=open('weights_super_ON_deep_OFF_'+str(xin)+'.json','r')
    data=json.load(fp)
    temp=data['after_p_p']
    temp=numpy.array(temp)-w_bu_pyr
    no_deep_p_p.append(numpy.mean(temp))
    no_deep_p_p_err.append(numpy.std(temp))

    temp=data['after_np_p']
    temp=numpy.array(temp)-w_bu_pyr
    no_deep_np_p.append(numpy.mean(temp))
    no_deep_np_p_err.append(numpy.std(temp))
    fp.close()

    fp=open('lfp_super_ON_deep_ON_'+str(xin)+'.json','r')
    data=json.load(fp)
    times=data['time']
    lfps=data['lfp']
   
    
    res=mtspec.multitaper.mtspec(lfps,1.0/1000.0, 4)
    freq=res[1]
    psd=res[0]
    ind=numpy.where((freq>=30.0)&(freq<100))[0]
    temp_gamma=numpy.mean(psd[ind])
    gammas.append(temp_gamma)

#pylab.subplot(2,1,1)    
slope, intercept, r_value, p_value, std_err = stats.linregress(reference_p_p, gammas)

print (slope, r_value, p_value)
gammas=gammas/numpy.amax(gammas)
pylab.scatter(reference_p_p, gammas, s=30,c='b',edgecolors='none')
pylab.title('correlation of L2/3 gamma and weight change')
pylab.ylabel('normalized gamma power')
pylab.xlabel('weight change')



#pylab.subplot(2,1,2)    
#pylab.scatter(reference_np_p, gammas, s=10,c='b',edgecolors='none')
pylab.savefig('/local2/STDP_prune_refined/figs/gamma_L23.png')
pylab.savefig('/local2/STDP_prune_refined/figs/gamma_L23.eps')
pylab.show()







