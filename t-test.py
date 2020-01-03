import pylab
import numpy
import json
from Param import w_bu_pyr
from scipy import stats

numpy.random.seed(100)
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
  
    fp=open('varf/weights_super_ON_deep_ON_'+str(xin)+'_0.1.json','r')
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

    fp=open('varf/weights_super_ON_deep_ON_'+str(xin)+'_0.2.json','r')
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


_, p_s=stats.ttest_ind(numpy.array(reference_np_p),numpy.array(no_super_np_p))

print 'Conn_NPA between baseline and Cont1', p_s

_, p_s=stats.ttest_ind(numpy.array(reference_p_p),numpy.array(no_deep_p_p))

print 'Conn_PA between baseline and Cont2', p_s




