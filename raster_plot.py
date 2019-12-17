import pylab
import numpy
import json
import sys


sel=str(sys.argv[1])
fp=open('spikes_super_ON_deep_ON_'+sel+'.json','r')
spikes=json.load(fp)
fp.close()

pylab.figure(1)

simtime=1000.0
layers=['l23','l4','l5']
celltypes=['pyr','pv','sst']
colors={'pyr':'r','pv':'b','sst':'k'}

for xi, xin in enumerate(layers):
    pylab.subplot(3,1,xi+1)
    if xi==0:
        pylab.title('V1_1')
    for yin in celltypes:
        spks=spikes['V1_1'+xin+yin]
        pylab.scatter(spks[0],spks[1],c=colors[yin], s=5, edgecolors='none')
        pylab.xlim([0.0,simtime])
    pylab.ylabel(xin)
pylab.savefig('/local2/STDP_prune_refined/figs/raster1-'+sel+'.eps')
pylab.figure(2)

for xi, xin in enumerate(layers):
    pylab.subplot(3,1,xi+1)
    if xi==0:
        pylab.title('V1_2')
    for yin in celltypes:
        spks=spikes['V1_2'+xin+yin]
        pylab.scatter(spks[0],spks[1],c=colors[yin], s=5, edgecolors='none')
        pylab.xlim([0.0,simtime])
    pylab.ylabel(xin)
pylab.savefig('/local2/STDP_prune_refined/figs/raster2-'+sel+'.eps')
pylab.figure(3)

for xi, xin in enumerate(layers):
    pylab.subplot(3,1,xi+1)
    if xi==0:
        pylab.title('LM')
    for yin in celltypes:
        spks=spikes['LM'+xin+yin]
        pylab.scatter(spks[0],spks[1],c=colors[yin], s=5, edgecolors='none')
        pylab.xlim([0.0,simtime])
    pylab.ylabel(xin)    

pylab.savefig('/local2/STDP_prune_refined/figs/raster-'+sel+'.eps')
#pylab.show()
