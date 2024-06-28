import ROOT
import os
import shutil

# Suppress the canvas display
ROOT.gROOT.SetBatch(True)

Lumi = 10.8e+6
processList = [
                #signal
                "wzp6_ee_mumuH_HZZ4nu_ecm240",
                "wzp6_ee_nunuH_HZZ_mumununu_ecm240",
                "wzp6_ee_nunuH_HWW_munumunu_ecm240"
              ]
process = "wzp6_ee_mumuH_HZZ4nu_ecm240"
path = "/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsInvisible/lia/MC_Validation/final/"

selections = ["NoSel", "sel1", "sel2", "sel3", "sel4", "sel5"]

# List of histogram names
histogram_names = [
                    "daughter_higgs_no", 
                    "daughter_higgs_0_pid", 
                    "daughter_higgs_1_pid", 
                    "daughter_higgs_2_pid",
                    "daughter_higgs_3_pid",

                    "daughter_Z_no", 
                    "daughter_Z_0_pid", 
                    "daughter_Z_1_pid", 
                    "daughter_Z_2_pid",
                    "daughter_Z_3_pid",
                    "daughter_Z_4_pid",
                    "daughter_Z_5_pid", 

                    "daughter_Wp_no", 
                    "daughter_Wp_0_pid", 
                    "daughter_Wp_1_pid", 
                    "daughter_Wp_2_pid",
                    "daughter_Wp_3_pid",

                    "daughter_Wm_no", 
                    "daughter_Wm_0_pid", 
                    "daughter_Wm_1_pid", 
                    "daughter_Wm_2_pid",
                    "daughter_Wm_3_pid",

                    "muonp_MC_no",
                    "muonm_MC_no",

                     #muons
                    "muons_p",  
                    "muons_theta",
                    "muons_phi",
                    "muons_no", 
            
                    #electrons
                    "electrons_p",
                    "electrons_theta",
                    "electrons_phi",
                    "electrons_no",

                    #Z
                    "Z_p",
                    "Z_m",
                    "Z_theta",
                    "Z_phi",

                    #recoil
                    "Z_recoil_m",
                    "Z_recoil_p",
                    "Z_recoil_theta",
                    "Z_recoil_phi",

                    #missing
                    "missing_mass",
                    "missing_e",
                    "missing_p",
                    "missing_theta",
                    "missing_phi",
                    "missing_px",
                    "missing_py",
                    "missing_pz",

                    #visible
                    "visible_mass",
                    "visible_e",
                    "visible_p",
                    "visible_theta",
                    "visible_phi",
                    "visible_px",
                    "visible_py",
                    "visible_pz",

                    "ZHChi2",

                    "leps_iso" 
                ]  # Replace with your histogram names

# Define the source and destination paths
files_to_copy = [
    "index.php",
    ".htaccess",
    "README.md"
]

basedir = "/eos/user/l/lia/www/FCC/HiggsInv/MC_Validation_Single"
for process in processList:
    for sel in selections:
        rootpath = path+process+f"_{sel}_histo.root"
        file = ROOT.TFile(rootpath)
        upperdir = os.path.join(basedir,process) 
        outputdir = os.path.join(basedir,process,sel)
        os.makedirs(outputdir, exist_ok=True)

        # Copy files only if they don't exist in the destination
        [shutil.copy(os.path.join(basedir, file), os.path.join(upperdir, file))  for file in files_to_copy if not os.path.exists(os.path.join(upperdir, file))]
        [shutil.copy(os.path.join(basedir, file), os.path.join(outputdir, file)) for file in files_to_copy if not os.path.exists(os.path.join(outputdir, file))]

        # Create a canvas to draw the histograms
        canvas = ROOT.TCanvas("canvas", "Histogram Canvas", 800, 600)

        # Loop over the histogram names and draw each histogram
        for hist_name in histogram_names:
            hist = file.Get(hist_name)
            hist.Scale(Lumi)
            if hist:
                hist.Draw("hist")
                # Save each histogram to a separate PDF file
                canvas.SaveAs(f"{outputdir}/{hist_name}.pdf")
                canvas.SaveAs(f"{outputdir}/{hist_name}.png") 
            else:
                print(f"Histogram {hist_name} not found in the file.")

        # Close the ROOT file
        file.Close()