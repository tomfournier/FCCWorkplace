# run as: fccanalysis final analysis_HInvjj_final.py
import os
os.environ["FCCDICTSDIR"] = "/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsInvisible/lia/FCCDicts/"

#Input directory where the files produced at the pre-selection level are
inputDir  = "outputs_HInvjj/Validation/"
#inputDir  = "outputs_HInvjj_IDEA/stage1"

#Input directory where the files produced at the pre-selection level are
outputDir  = "outputs_HInvjj/Validation_final/"
#outputDir  = "outputs_HInvjj_IDEA/final/"


#Mandatory: List of processes
processList = {
    'output_ee_WW_munumunu':{},
}


#Link to the dictonary that contains all the cross section informations etc...
# can be found at: /cvmfs/fcc.cern.ch/FCCDicts/
procDict = "FCCee_procDict_winter2023_IDEA.json"

#Add MySample_p8_ee_ZH_ecm240 as it is not an offical process
procDictAdd={
    "output_wzp6":{"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 1.0, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "output_p8":{"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 1.0, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "output_ee_WW_lvqq":{"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 1.0, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "output_ee_WW_munumunu":{"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 1.0, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "output_ee_WW_enuenu":{"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 1.0, "kfactor": 1.0, "matchingEfficiency": 1.0},
    "output_ee_ZZ_nunuqq":{"numberOfEvents": 100000, "sumOfWeights": 100000, "crossSection": 1.0, "kfactor": 1.0, "matchingEfficiency": 1.0},
}

#Number of CPUs to use
nCPUS = 1

#produces ROOT TTrees, default is False
doTree = False

###Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {
    "sel0_NoCuts" : "1",
    #"sel1_METCut" : "MET[0] > 10",
    # cut 60 < mZ < 100 GeV for bb, cut mZ \pm 5 GeV for qq/mumu ,  cut mZ \pm 4 GeV for ee
    "sel2_mZCut" : "ZBosonMass[0] > 60 && ZBosonMass[0] < 100", 

    #"sel3" : "selected_jets_pt_0 > 40",
    #"sel4" : "selected_jets_pt_0 > 50",
    #"sel0" : "Zcand_m > 40 && Zcand_m < 120",
}

#Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.
histoList = {

    "muons_p":{"name":"muons_p","title":"Muon pT [GeV]","bin":100,"xmin":0,"xmax":200},
    "muons_e":{"name":"muons_e","title":"Muon Energy [GeV]","bin":100,"xmin":0,"xmax":200},
    "muons_y":{"name":"muons_y","title":"Muon Rapidity","bin":100,"xmin":-5,"xmax":5},
    "ZBosonP":{"name":"ZBosonP","title":"ZBosonPt [GeV]","bin":100,"xmin":0,"xmax":200},
    "ZBosonMass":{"name":"ZBosonMass","title":"m_Z [GeV]","bin":200,"xmin":0,"xmax":200},
    #"MET":{"name":"MET","title":"MET [GeV]","bin":100,"xmin":0,"xmax":-1},
    "recoil_M":{"name":"recoil_M","title":"recoil_M [GeV]","bin":200,"xmin":0,"xmax":200},
    "MC_GenID":{"name":"MC_GenID","title":"MC_GenID","bin":24,"xmin":-0.5,"xmax":23.5}, 
    "W_MC_no":{"name":"W_MC_no","title":"W_MC_no","bin":6,"xmin":-0.5,"xmax":5.5},
    "W_MC_m":{"name":"W_MC_m","title":"W_MC_m","bin":80,"xmin":20,"xmax":100},
    "W_MC_p":{"name":"W_MC_p","title":"W_MC_p","bin":80,"xmin":20,"xmax":100},
    "W_MC_GenID":{"name":"W_MC_GenID","title":"W_MC_GenID","bin":24,"xmin":-0.5,"xmax":23.5},
    "pdgID":{"name":"pdgID","title":"pdgID","bin":101,"xmin":-50.5,"xmax":50.5},
    "n_muons":{"name":"n_muons","title":"n_muons","bin":10,"xmin":-0.5,"xmax":9.5},
    "n_electrons":{"name":"n_electrons","title":"n_electrons","bin":10,"xmin":-0.5,"xmax":9.5},
    "n_jets":{"name":"n_jets","title":"n_jets","bin":10,"xmin":-0.5,"xmax":9.5},
    "Wp_MC_no":{"name":"Wp_MC_no","title":"Wp_MC_no","bin":6,"xmin":-0.5,"xmax":5.5},
    "daughter_Wp_no":{"name":"daughter_Wp_no","title":"daughter_Wp_no","bin":6,"xmin":-0.5,"xmax":5.5},
    "daughter_Wp_0_pid":{"name":"daughter_Wp_0_pid","title":"daughter_Wp_0_pid","bin":101,"xmin":-50.5,"xmax":50.5},
    "daughter_Wp_1_pid":{"name":"daughter_Wp_1_pid","title":"daughter_Wp_1_pid","bin":101,"xmin":-50.5,"xmax":50.5},
    "Wm_MC_no":{"name":"Wm_MC_no","title":"Wm_MC_no","bin":6,"xmin":-0.5,"xmax":5.5},
    "daughter_Wm_no":{"name":"daughter_Wm_no","title":"daughter_Wm_no","bin":6,"xmin":-0.5,"xmax":5.5},
    "daughter_Wm_0_pid":{"name":"daughter_Wm_0_pid","title":"daughter_Wm_0_pid","bin":101,"xmin":-50.5,"xmax":50.5},
    "daughter_Wm_1_pid":{"name":"daughter_Wm_1_pid","title":"daughter_Wm_1_pid","bin":101,"xmin":-50.5,"xmax":50.5},
    }