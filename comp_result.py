import pylab
import numpy
import json
from Param import w_bu_pyr

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




xv=range(2,42,2)
xv=numpy.array(xv)
xv1=xv-0.5
xv2=xv+0.5


pylab.figure(1)

xv1=[0,4]
xv2=[1,5]
xv3=[2,6]

y1=[numpy.mean(reference_p_p),numpy.mean(reference_np_p)]
y1err=[numpy.std(reference_p_p),numpy.std(reference_np_p)]

y2=[numpy.mean(no_super_p_p),numpy.mean(no_super_np_p)]
y2err=[numpy.std(no_super_p_p),numpy.std(no_super_np_p)]

y3=[numpy.mean(no_deep_p_p),numpy.mean(no_deep_np_p)]
y3err=[numpy.std(no_deep_p_p),numpy.std(no_deep_np_p)]

pylab.bar(xv1,y1,color='r',label='reference')
pylab.errorbar(xv1,y1,fmt='r+',yerr=y1err)

pylab.bar(xv2,y2,color='g',label='varf0.1')
pylab.errorbar(xv2,y2,fmt='g+',yerr=y2err)

pylab.bar(xv3,y3,color='b',label='varf0.2')
pylab.errorbar(xv3,y3,fmt='b+',yerr=y3err)
pylab.legend()
pylab.savefig('/local2/STDP_prune_refined/figs/comp_result.eps')

pylab.show()



