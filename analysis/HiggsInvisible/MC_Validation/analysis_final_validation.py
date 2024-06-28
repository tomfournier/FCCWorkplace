import os
#python examples/FCCee/higgs/mH-recoil/mumu/finalSel.py
os.environ["FCCDICTSDIR"] = "/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsInvisible/lia/FCCDicts/"
#Input directory where the files produced at the pre-selection level are
inputDir = "/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsInvisible/lia/MC_Validation/stage1"

#Input directory where the files produced at the pre-selection level are
outputDir = "/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsInvisible/lia/MC_Validation/final"

###Link to the dictonary that contains all the cross section informations etc...
procDict = "FCCee_procDict_winter2023_IDEA.json"
#Add MySample_p8_ee_ZH_ecm240 as it is not an offical process

###Process list that should match the produced files.
processList = {
                #signal
                "wzp6_ee_mumuH_HZZ4nu_ecm240",
                "wzp6_ee_nunuH_HZZ_mumununu_ecm240",
                "wzp6_ee_nunuH_HWW_munumunu_ecm240"
              }
###Add MySample_p8_ee_ZH_ecm240 as it is not an offical process

#Number of CPUs to use
nCPUS = 2
#produces ROOT TTrees, default is False
doTree = False

###Dictionnay of the list of cuts. The key is the name of the selection that will be added to the output file
cutList = {
            "NoSel":"return true",
            "sel1":"muons_no==2",
            "sel2":"muons_no==2 && electrons_no==0",
            "sel3":"muons_no==2 && electrons_no==0 && Z_m[0] > 86 && Z_m[0] < 96",
            "sel4":"muons_no==2 && electrons_no==0 && Z_m[0] > 86 && Z_m[0] < 96 && missing_mass[0] > 100 && missing_mass[0] < 140", 
            "sel5":"muons_no==2 && electrons_no==0 && Z_m[0] > 86 && Z_m[0] < 96 && missing_mass[0] > 100 && missing_mass[0] < 140 && visible_mass[0] > 86 && visible_mass[0] < 96",
            }


###Dictionary for the ouput variable/hitograms. The key is the name of the variable in the output files. "name" is the name of the variable in the input file, "title" is the x-axis label of the histogram, "bin" the number of bins of the histogram, "xmin" the minimum x-axis value and "xmax" the maximum x-axis value.


histoList = {
    # Zed
    "Z_m": {"name": "Z_m", "title": "m_{Z} [GeV]", "bin": 125, "xmin": 0, "xmax": 250},
    "Z_p": {"name": "Z_p", "title": "zll_p", "bin": 200, "xmin": 0, "xmax": 200},
    "Z_theta": {"name": "Z_theta", "title": "zll_theta", "bin": 70, "xmin": -3.5, "xmax": 3.5},
    "Z_phi": {"name": "Z_phi", "title": "zll_phi", "bin": 70, "xmin": -3.5, "xmax": 3.5},

    # Recoil
    "Z_recoil_m": {"name": "Z_recoil_m", "title": "m_{recoil} [GeV]", "bin": 125, "xmin": 0, "xmax": 250},
    "Z_recoil_p": {"name": "Z_recoil_p", "title": "p_{recoil} [GeV]", "bin": 200, "xmin": 0, "xmax": 200},
    "Z_recoil_theta": {"name": "Z_recoil_theta", "title": "#theta_{recoil}", "bin": 70, "xmin": -3.5, "xmax": 3.5},
    "Z_recoil_phi": {"name": "Z_recoil_phi", "title": "#phi_{recoil}", "bin": 70, "xmin": -3.5, "xmax": 3.5},

    # Missing
    "missing_mass": {"name": "missing_mass", "title": "Missing Mass [GeV]", "bin": 125, "xmin": 0, "xmax": 250},
    "missing_e": {"name": "missing_e", "title": "Missing Energy [GeV]", "bin": 200, "xmin": 0, "xmax": 200},
    "missing_p": {"name": "missing_p", "title": "Missing Momentum [GeV]", "bin": 200, "xmin": 0, "xmax": 200},
    "missing_theta": {"name": "missing_theta", "title": "Missing #theta", "bin": 70, "xmin": -3.5, "xmax": 3.5},
    "missing_phi": {"name": "missing_phi", "title": "Missing #phi", "bin": 70, "xmin": -3.5, "xmax": 3.5},
    "missing_px": {"name": "missing_px", "title": "Missing p_{x} [GeV]", "bin": 200, "xmin": -100, "xmax": 100},
    "missing_py": {"name": "missing_py", "title": "Missing p_{y} [GeV]", "bin": 200, "xmin": -100, "xmax": 100},
    "missing_pz": {"name": "missing_pz", "title": "Missing p_{z} [GeV]", "bin": 200, "xmin": -100, "xmax": 100},

    # Visible
    "visible_mass": {"name": "visible_mass", "title": "Visible Mass [GeV]", "bin": 125, "xmin": 0, "xmax": 250},
    "visible_e": {"name": "visible_e", "title": "Visible Energy [GeV]", "bin": 200, "xmin": 0, "xmax": 200},
    "visible_p": {"name": "visible_p", "title": "Visible Momentum [GeV]", "bin": 200, "xmin": 0, "xmax": 200},
    "visible_theta": {"name": "visible_theta", "title": "Visible #theta", "bin": 70, "xmin": -3.5, "xmax": 3.5},
    "visible_phi": {"name": "visible_phi", "title": "Visible #phi", "bin": 70, "xmin": -3.5, "xmax": 3.5},
    "visible_px": {"name": "visible_px", "title": "Visible p_{x} [GeV]", "bin": 200, "xmin": -100, "xmax": 100},
    "visible_py": {"name": "visible_py", "title": "Visible p_{y} [GeV]", "bin": 200, "xmin": -100, "xmax": 100},
    "visible_pz": {"name": "visible_pz", "title": "Visible p_{z} [GeV]", "bin": 200, "xmin": -100, "xmax": 100},

    # Muons
    "muons_p": {"name": "muons_p", "title": "Muon Momentum [GeV]", "bin": 200, "xmin": 0, "xmax": 200},
    "muons_theta": {"name": "muons_theta", "title": "Muon #theta", "bin": 70, "xmin": -3.5, "xmax": 3.5},
    "muons_phi": {"name": "muons_phi", "title": "Muon #phi", "bin": 70, "xmin": -3.5, "xmax": 3.5},
    "muons_no": {"name": "muons_no", "title": "Number of Muons", "bin": 6, "xmin": -0.5, "xmax": 5.5},

    # Electrons
    "electrons_p": {"name": "electrons_p", "title": "Electron Momentum [GeV]", "bin": 200, "xmin": 0, "xmax": 200},
    "electrons_theta": {"name": "electrons_theta", "title": "Electron #theta", "bin": 70, "xmin": -3.5, "xmax": 3.5},
    "electrons_phi": {"name": "electrons_phi", "title": "Electron #phi", "bin": 70, "xmin": -3.5, "xmax": 3.5},
    "electrons_no": {"name": "electrons_no", "title": "Number of Electrons", "bin": 6, "xmin": -0.5, "xmax": 5.5},

    # Others
    "ZHChi2": {"name": "ZHChi2", "title": "ZHChi2", "bin": 100, "xmin": 0, "xmax": 100},
    "leps_iso": {"name": "leps_iso", "title": "Leptons Isolation", "bin": 100, "xmin": 0, "xmax": 100},

    "daughter_higgs_no": {"name": "daughter_higgs_no", "title": "daughter_higgs_no", "bin": 11, "xmin": -0.5, "xmax": 10.5},
    "daughter_higgs_0_pid": {"name": "daughter_higgs_0_pid", "title": "daughter_higgs_0_pid", "bin": 51, "xmin": -25.5, "xmax": 25.5},
    "daughter_higgs_1_pid": {"name": "daughter_higgs_1_pid", "title": "daughter_higgs_1_pid", "bin": 51, "xmin": -25.5, "xmax": 25.5},
    "daughter_higgs_2_pid": {"name": "daughter_higgs_2_pid", "title": "daughter_higgs_2_pid", "bin": 51, "xmin": -25.5, "xmax": 25.5},
    "daughter_higgs_3_pid": {"name": "daughter_higgs_3_pid", "title": "daughter_higgs_3_pid", "bin": 51, "xmin": -25.5, "xmax": 25.5},

    "daughter_Z_no": {"name": "daughter_Z_no", "title": "daughter_Z_no", "bin": 11, "xmin": -0.5, "xmax": 10.5},
    "daughter_Z_0_pid": {"name": "daughter_Z_0_pid", "title": "daughter_Z_0_pid", "bin": 51, "xmin": -25.5, "xmax": 25.5},
    "daughter_Z_1_pid": {"name": "daughter_Z_1_pid", "title": "daughter_Z_1_pid", "bin": 51, "xmin": -25.5, "xmax": 25.5},
    "daughter_Z_2_pid": {"name": "daughter_Z_2_pid", "title": "daughter_Z_2_pid", "bin": 51, "xmin": -25.5, "xmax": 25.5},
    "daughter_Z_3_pid": {"name": "daughter_Z_3_pid", "title": "daughter_Z_3_pid", "bin": 51, "xmin": -25.5, "xmax": 25.5},
    "daughter_Z_4_pid": {"name": "daughter_Z_4_pid", "title": "daughter_Z_4_pid", "bin": 51, "xmin": -25.5, "xmax": 25.5},
    "daughter_Z_5_pid": {"name": "daughter_Z_5_pid", "title": "daughter_Z_5_pid", "bin": 51, "xmin": -25.5, "xmax": 25.5}, 

    "daughter_Wm_no": {"name": "daughter_Wm_no", "title": "daughter_Wm_no", "bin": 11, "xmin": -0.5, "xmax": 10.5},
    "daughter_Wm_0_pid": {"name": "daughter_Wm_0_pid", "title": "daughter_Wm_0_pid", "bin": 51, "xmin": -25.5, "xmax": 25.5},
    "daughter_Wm_1_pid": {"name": "daughter_Wm_1_pid", "title": "daughter_Wm_1_pid", "bin": 51, "xmin": -25.5, "xmax": 25.5},
    "daughter_Wm_2_pid": {"name": "daughter_Wm_2_pid", "title": "daughter_Wm_2_pid", "bin": 51, "xmin": -25.5, "xmax": 25.5},
    "daughter_Wm_3_pid": {"name": "daughter_Wm_3_pid", "title": "daughter_Wm_3_pid", "bin": 51, "xmin": -25.5, "xmax": 25.5},

    "daughter_Wp_no": {"name": "daughter_Wp_no", "title": "daughter_Wp_no", "bin": 11, "xmin": -0.5, "xmax": 10.5},
    "daughter_Wp_0_pid": {"name": "daughter_Wp_0_pid", "title": "daughter_Wp_0_pid", "bin": 51, "xmin": -25.5, "xmax": 25.5},
    "daughter_Wp_1_pid": {"name": "daughter_Wp_1_pid", "title": "daughter_Wp_1_pid", "bin": 51, "xmin": -25.5, "xmax": 25.5},
    "daughter_Wp_2_pid": {"name": "daughter_Wp_2_pid", "title": "daughter_Wp_2_pid", "bin": 51, "xmin": -25.5, "xmax": 25.5},
    "daughter_Wp_3_pid": {"name": "daughter_Wp_3_pid", "title": "daughter_Wp_3_pid", "bin": 51, "xmin": -25.5, "xmax": 25.5},

    "muonp_MC_no": {"name": "muonp_MC_no", "title": "muonp_MC_no", "bin": 11, "xmin": -0.5, "xmax": 10.5},
    "muonm_MC_no": {"name": "muonm_MC_no", "title": "muonm_MC_no", "bin": 11, "xmin": -0.5, "xmax": 10.5},


}


