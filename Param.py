import sys

# set parameters for depressing synapse: 
h=0.1   # simulation step size (ms)
Tau     = 10.    # membrane time constant
Theta   = -50.    # threshold
U0      = -65.     # reset potential of membrane potential
R       =0.1    # 100 M Ohm Not being used
C       = 250.#  Not being used (Tau/R, Tau (ms)/R in NEST units)
TauR    = 2.     # refractory time
Tau_syn=0.5 # for original cell types
cpn=1



msd=1
super_down=1
deep_down=1

if len(sys.argv)>1:
   
    msd=int(sys.argv[1])
    super_down=float(sys.argv[2]) 
    deep_down=float(sys.argv[3])
    
if super_down==0:
    flag_super='OFF'
else:
    flag_super='ON'

if deep_down==0:
    flag_deep='OFF'
else:
    flag_deep='ON'






layers=['l23','l4','l5']

####l23
P_l23_l23={'pyr_pyr':0.2,'pyr_pv':0.5,'pyr_sst':0.3,'pv_pv':1.0,'pv_pyr':1.0,'pv_sst':0.0,'sst_sst':0.0,'sst_pyr':0.3,'sst_pv':0.5}
P_l23_l4={'pyr_pyr':0.0,'pyr_pv':0.0,'pyr_sst':0.0,'pv_pv':0.0,'pv_pyr':0.0,'pv_sst':0.0,'sst_sst':0.0,'sst_pyr':0.0,'sst_pv':0.0}
P_l23_l5={'pyr_pyr':0.2,'pyr_pv':0.2,'pyr_sst':0.5,'pv_pv':0.0,'pv_pyr':0.0,'pv_sst':0.0,'sst_sst':0.0,'sst_pyr':0.0,'sst_pv':0.0}




####l4
P_l4_l23={'pyr_pyr':0.5,'pyr_pv':0.2,'pyr_sst':0.0,'pv_pv':0.3,'pv_pyr':0.2,'pv_sst':0.0,'sst_sst':0.0,'sst_pyr':0.0,'sst_pv':0.0}
P_l4_l4={'pyr_pyr':0.5,'pyr_pv':0.5,'pyr_sst':0.3,'pv_pv':1.0,'pv_pyr':1.0,'pv_sst':0.3,'sst_sst':0.0,'sst_pyr':0.3,'sst_pv':0.5}
P_l4_l5={'pyr_pyr':0.2,'pyr_pv':0.2,'pyr_sst':0.2,'pv_pv':0.0,'pv_pyr':0.0,'pv_sst':0.0,'sst_sst':0.0,'sst_pyr':0.0,'sst_pv':0.0}



#########l5
P_l5_l23={'pyr_pyr':0.0,'pyr_pv':0.0,'pyr_sst':0.3,'pv_pv':0.0,'pv_pyr':0.0,'pv_sst':0.0,'sst_sst':0.0,'sst_pyr':0.0,'sst_pv':0.4}
P_l5_l4={'pyr_pyr':0.0,'pyr_pv':0.0,'pyr_sst':0.0,'pv_pv':0.0,'pv_pyr':0.0,'pv_sst':0.0,'sst_sst':0.0,'sst_pyr':0.0,'sst_pv':0.4}
P_l5_l5={'pyr_pyr':0.2,'pyr_pv':0.2,'pyr_sst':0.2,'pv_pv':1.0,'pv_pyr':1.0,'pv_sst':0.5,'sst_sst':0.0,'sst_pyr':0.5,'sst_pv':0.5}



P_conn={'l23_l23':P_l23_l23, 'l23_l4':P_l23_l4, 'l23_l5':P_l23_l5, 'l4_l23':P_l4_l23, 
'l4_l4':P_l4_l4,'l4_l5':P_l4_l5, 'l5_l23':P_l5_l23,'l5_l4':P_l5_l4,'l5_l5':P_l5_l5}

V1_weights={'pyr_pyr':20.0,'pyr_sst':2.0,'pyr_pv':40.0,'pv_pyr':-60.0,'pv_pv':-60.0,
         'pv_sst':0.0,'sst_pyr':-15.0,'sst_pv':-40.0,'sst_sst':0.0}

V1_exceptions={ 'l23pv_l23pyr':-60.0,'l23pyr_l4pv':10.0,'l23pv_l23pv':-80.0,
                 'l4pyr_l23pyr':100.0, 'l4pyr_l4pv':40.0,'l4pyr_l5pyr':30.0, 'l4pyr_l23pv':60.0,'l4pyr_l5sst':0.0, 'l4pyr_l5pv':20.0,
                 'l4pv_l4pyr':-50.0, 'l4pv_l4pv':-60.0,'l4pv_l23pyr':-40.0,
                'l5pyr_l5pv':10.0,'l5pyr_l5sst':10.0,
                'l5sst_l5pyr':-50.0,'l5sst_l5pv':-30.0,'l5sst_l4pv':-40.0, 'l5sst_l23pv':-20.0,
               'l5pv_l5pyr':-10.0,'l5pv_l5sst':-30.0
               } 

LM_weights=V1_weights
LM_exceptions=V1_exceptions


LM_exceptions={'l4pv_l4pyr':-40.,'l4pyr_l5pyr':20.0, 'l4pyr_l5sst':0.0,'l4pyr_l23pyr':50.0,
               'l5pyr_l5sst':100.0, 'l5sst_l5pyr':-100.0} 


Ext={'V1l23pyr':1200.0,'V1l23pv':1200.0, 'V1l23sst':1200.0,
     'V1l4pyr':1300.0,'V1l4pv':1200.0, 'V1l4sst':1300.0,
     'V1l5pyr':1000.0,'V1l5pv':1150.0, 'V1l5sst':800.0,
     'LMl23pyr':1300.0,'LMl23pv':1000.0, 'LMl23sst':1200.0,
     'LMl4pyr':1400.0,'LMl4pv':1000.0, 'LMl4sst':1300.0,
     'LMl5pyr':1800.0,'LMl5pv':1000.0, 'LMl5sst':500.0}




#probabiilty
P_pref_pref_pyr=0.3
P_pref_pref_pv=0.3


#lgn inputs
w_lgn_pyr=50.0
w_lgn_pv=20.0


w_bu_pyr=40.0
w_bu_pv=10.0

#top-down weights
td_super_pyr=15.0*super_down  #15.0
td_super_pv=20.0*super_down  #10.0

td_deep_pyr=30.0*deep_down #30.0
td_deep_sst=20.0*deep_down

simtime=10000.0


Pyr_params = {"tau_m"     :  Tau,
            "t_ref"     :  TauR,
            "C_m"       :  C,
            "V_reset"   :  U0,
            "E_L"       :  U0,
            "V_th"      :  Theta,

	    "tau_syn":[2.0,6.0,7.5,6.2] #It depends on how to normalize.. This line includes time constants estimated directly Pfeffer 2013
	    }


PV_params = {"tau_m"     :  Tau,
            "t_ref"     :  TauR,
            "C_m"       :  C,
            "V_reset"   :  U0,
            "E_L"       :  U0,
            "V_th"      :  Theta,

	    "tau_syn":[2.0,4.3,3.4,0.5]
           }
SST_params = {"tau_m"     :  Tau,
            "t_ref"     :  TauR,
            "C_m"       :  C,
            "V_reset"   :  U0,
            "E_L"       :  U0,
            "V_th"      :  Theta,

	    "tau_syn":[2.0,0.5,0.5,10.4]
           }
VIP_params = {"tau_m"     :  Tau,
            "t_ref"     :  TauR,
            "C_m"       :  C,
            "V_reset"   :  U0,
            "E_L"       :  U0,
            "V_th"      :  Theta,

	    "tau_syn":[2.0,4.3,3.4,0.5]}
