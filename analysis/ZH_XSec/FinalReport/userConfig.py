import os 
import numpy as np

repo = os.getenv('PWD')
# repo = "/eos/user/t/tofourni/public/FCC/FCCWorkplace/analysis/FinalReport"
#repo can be changed, but by default writes locally

class loc : pass
loc.ROOT = repo+'/'
loc.OUT = loc.ROOT+'output/'
loc.DATA = loc.OUT+'data'
loc.CSV = loc.DATA+'/csv'
loc.PKL = loc.DATA+'/pkl'
loc.PKL_Val = loc.DATA+'/pkl_val'
loc.ROOTFILES = loc.DATA+'/ROOT'
# loc.PLOTS = loc.DATA+'/plots'
loc.PLOTS = loc.OUT+'plots'
loc.PLOTS_Val = loc.OUT+'plots_val'
loc.TEX = loc.OUT+'tex'
loc.JSON = loc.OUT+'json'

#EOS location for files used in analysis
loc.EOS = os.path.abspath(".")+"/analysis/ZH_XSec/FinalReport"
# loc.EOS = "/eos/user/t/tofourni/public/FCC/FCCWorkplace/analysis/FinalReport"

#Output BDT model location - used in official sample production to assign MVA weights
loc.BDT = f"{loc.OUT}/BDT"

#Loaction of prod_04 tuples used in analysis
loc.PROD = f"{loc.EOS}"

#Samples for first stage BDT training
loc.TRAIN = f"{loc.OUT}/MVAInputs"

#Samples for second stage training
loc.TRAIN2 = f"{loc.OUT}/Training_4stage2/"

#Samples for final analysis
loc.ANALYSIS = f"{loc.OUT}/BDT_analysis_samples/"

#First stage BDT including event-level vars
train_vars = [
              #leptons
              "leading_zll_lepton_p",
              "leading_zll_lepton_theta",
              "subleading_zll_lepton_p",
              "subleading_zll_lepton_theta",
              "zll_leptons_acolinearity",
              "zll_leptons_acoplanarity",
              #Zed
              "zll_m",
              "zll_p",
              "zll_theta"
              #Higgsstrahlungness
              #"H",
              ]

latex_mapping = {
    'leading_zll_lepton_p': r'$p_{\ell_1}$',
    'leading_zll_lepton_theta': r'$\theta_{\ell_1}$',
    'subleading_zll_lepton_p': r'$p_{\ell_2}$',
    'subleading_zll_lepton_theta': r'$\theta_{\ell_2}$',
    'zll_leptons_acolinearity': r'$|\Delta\theta_{\ell\ell}|$',
    'zll_leptons_acoplanarity': r'$|\Delta\phi_{\ell\ell}|$',
    'zll_m': r'$m_{\ell\ell}$',
    'zll_p': r'$p_{\ell\ell}$',
    'zll_theta': r'$\theta_{\ell\ell}$',
    'H': r'$H$'
}

final_states = "mumu"

#First stage BDT including event-level vars and vertex vars

#Decay modes used in first stage training and their respective file names
mode_names = {"mumuH": "wzp6_ee_mumuH_ecm240",
              "ZZ": "p8_ee_ZZ_ecm240",
              "WWmumu": "p8_ee_WW_mumu_ecm240",
              "Zll": "wzp6_ee_mumu_ecm240",
              "egamma": "wzp6_egamma_eZ_Zmumu_ecm240",
              "gammae": "wzp6_gammae_eZ_Zmumu_ecm240",
              "gaga_mumu": "wzp6_gaga_mumu_60_ecm240"}
