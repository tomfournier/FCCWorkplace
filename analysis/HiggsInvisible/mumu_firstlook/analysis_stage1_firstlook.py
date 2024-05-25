#Mandatory: List of processes

processList = {
    #signal
    "wzp6_ee_mumuH_ecm240":{'chunks':20},
    #signal mass
    "wzp6_ee_mumuH_mH-higher-100MeV_ecm240":{'chunks':20},
    "wzp6_ee_mumuH_mH-higher-50MeV_ecm240":{'chunks':20},
    "wzp6_ee_mumuH_mH-lower-100MeV_ecm240":{'chunks':20},
    "wzp6_ee_mumuH_mH-lower-50MeV_ecm240":{'chunks':20},
    #signal syst
    "wzp6_ee_mumuH_BES-higher-1pc_ecm240":{'chunks':20},
    "wzp6_ee_mumuH_BES-lower-1pc_ecm240":{'chunks':20},
    #background: 
    "p8_ee_WW_ecm240":{'chunks':80},
    "p8_ee_ZZ_ecm240":{'chunks':20},
    "wzp6_ee_mumu_ecm240":{'chunks':20},
    "wzp6_ee_tautau_ecm240":{'chunks':20},
    #rare backgrounds:
    "wzp6_egamma_eZ_Zmumu_ecm240":{'chunks':20},
    "wzp6_gammae_eZ_Zmumu_ecm240":{'chunks':20},
    "wzp6_gaga_mumu_60_ecm240":{'chunks':20},
    "wzp6_gaga_tautau_60_ecm240":{'chunks':20},
    "wzp6_ee_nuenueZ_ecm240":{'chunks':20},
    ##test
    #"wzp6_ee_mumuH_ecm240":{'fraction':0.02},
    }
#Mandatory: Production tag when running over EDM4Hep centrally produced events, this points to the yaml files for getting sample statistics
prodTag     = "FCCee/winter2023/IDEA/"

#from userConfig import loc
#outputDir="/afs/cern.ch/work/l/lia/private/FCC/NewWorkFlow/FCCeePhysicsPerformance/case-studies/higgs/mH-recoil/test/flatNtuples_test"
outputDirEos= "/eos/user/l/lia/FCCee/HiggsInv/mumu_firstlook/"
eosType = "eosuser"
#Optional: ncpus, default is 4
nCPUS       = 4

#Optional running on HTCondor, default is False
runBatch    = True
#runBatch    = False
#Optional batch queue name when running on HTCondor, default is workday
batchQueue = "longlunch"

#Optional computing account when running on HTCondor, default is group_u_FCC.local_gen
compGroup = "group_u_FCC.local_gen"

#userBatchConfig="/afs/cern.ch/work/l/lia/private/FCC/NewWorkFlow/FCCeePhysicsPerformance/case-studies/higgs/mH-recoil/FCCAnalyses-config/MidTerm/mumu/userBatch.Config"
#USER DEFINED CODE
import ROOT
ROOT.gInterpreter.ProcessLine('''
  TMVA::Experimental::RBDT<> bdt("ZH_Recoil_BDT", "/eos/user/l/lia/FCCee/MidTerm/mumu/BDT/xgb_bdt.root");
  computeModel1 = TMVA::Experimental::Compute<9, float>(bdt);
''')
#"sel0_MRecoil_Mll_73_120_pTll_05":"  Z_leptonic_m  > 73 &&  Z_leptonic_m  < 120 &&zed_leptonic_recoil_m.size()==1 && zed_leptonic_recoil_m[0]  > 120 &&zed_leptonic_recoil_m[0]  <140 && Z_leptonic_pt  > 5",
#Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis():

    #__________________________________________________________
    #Mandatory: analysers funtion to define the analysers to process, please make sure you return the last dataframe, in this example it is df2
    def analysers(df):
        df2 = (
            df
            #############################################
            ## Alias for muon and electron and MC truth informations##
            #############################################
            .Alias("Muon0", "Muon#0.index")
            .Alias("Electron0", "Electron#0.index")
            .Alias("MCRecoAssociations0", "MCRecoAssociations#0.index")
            .Alias("MCRecoAssociations1", "MCRecoAssociations#1.index")
            .Alias("Particle0", "Particle#0.index")
            .Alias("Particle1", "Particle#1.index")
            #############################################
            ## Define the collections of muons ##
            #############################################
            .Define("muons",  "FCCAnalyses::ReconstructedParticle::get(Muon0, ReconstructedParticles)")
            .Define("muons_p", "FCCAnalyses::ReconstructedParticle::get_p(muons)")
            .Define("muons_theta", "FCCAnalyses::ReconstructedParticle::get_theta(muons)")
            .Define("muons_phi", "FCCAnalyses::ReconstructedParticle::get_phi(muons)")
            .Define("muons_q", "FCCAnalyses::ReconstructedParticle::get_charge(muons)")
            .Define("muons_no", "FCCAnalyses::ReconstructedParticle::get_n(muons)")
            
            #############################################
            ## Define the collections of electrons ##
            #############################################
            .Define("electrons",  "FCCAnalyses::ReconstructedParticle::get(Electron0, ReconstructedParticles)")
            .Define("electrons_p", "FCCAnalyses::ReconstructedParticle::get_p(electrons)")
            .Define("electrons_theta", "FCCAnalyses::ReconstructedParticle::get_theta(electrons)")
            .Define("electrons_phi", "FCCAnalyses::ReconstructedParticle::get_phi(electrons)")
            .Define("electrons_q", "FCCAnalyses::ReconstructedParticle::get_charge(electrons)")
            .Define("electrons_no", "FCCAnalyses::ReconstructedParticle::get_n(electrons)")

            #############################################
            ## Define the collections of jets ##
            #############################################
            .Define("jets", "ReconstructedParticle::sel_p(15)(Jet)")
            .Define("jets_p", "FCCAnalyses::ReconstructedParticle::get_p(jets)")
            .Define("jets_theta", "FCCAnalyses::ReconstructedParticle::get_theta(jets)")
            .Define("jets_phi", "FCCAnalyses::ReconstructedParticle::get_phi(jets)")
            .Define("jets_no", "FCCAnalyses::ReconstructedParticle::get_n(jets)")

            #############################################
            # Missing momentum
            #############################################
            .Define("missingEnergy", "HiggsTools::missingEnergy(240., ReconstructedParticles)")
            .Define("MET_e", "FCCAnalyses::ReconstructedParticle::get_p(MissingET)")
            .Define("MET_phi", "FCCAnalyses::ReconstructedParticle::get_phi(MissingET)")
            .Define("MET_p", "FCCAnalyses::ReconstructedParticle::get_p(MissingET)")
            .Define("cosTheta_miss", "HiggsTools::get_cosTheta(MissingET)") 
            
            #############################################
            # Cuts
            #############################################
            .Define("cut0", "0")
            #########
            ### CUT 1: exactly two muons
            #########
            .Filter("muon_no >= 1")
            .Define("cut1", "1")
            #########
            ### CUT 2 :at least 2 leptons, and build the resonance
            #########
            .Filter("leps_no >= 2 && abs(Sum(leps_q)) < leps_q.size()")
            
        )
        
        return df2

    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        branchList = [
            #Reconstructed Particle
            #leptons
            "leading_zll_lepton_p",  
            "leading_zll_lepton_m",  
            "leading_zll_lepton_theta",                    
            "leading_zll_lepton_phi",
            "subleading_zll_lepton_p",
            "subleading_zll_lepton_m",
            "subleading_zll_lepton_theta",
            "subleading_zll_lepton_phi",
            "zll_leptons_acolinearity",
            "zll_leptons_acoplanarity",
            #Zed
            "zll_m",
            "zll_p",
            "zll_theta",
            "zll_phi",
            #Recoil
            "zll_recoil_m",
            #BDT Score
            "BDTscore",
            #Category
            "zll_category",

            #scaleup
            "leading_zll_lepton_p_scaleup",  
            "leading_zll_lepton_m_scaleup",  
            "leading_zll_lepton_theta_scaleup",                    
            "leading_zll_lepton_phi_scaleup",
            "subleading_zll_lepton_p_scaleup",
            "subleading_zll_lepton_m_scaleup",
            "subleading_zll_lepton_theta_scaleup",
            "subleading_zll_lepton_phi_scaleup",
            "zll_leptons_acolinearity_scaleup",
            "zll_leptons_acoplanarity_scaleup",
            #Zed
            "zll_m_scaleup",
            "zll_p_scaleup",
            "zll_theta_scaleup",
            "zll_phi_scaleup",
            #Recoil
            "zll_recoil_m_scaleup",
            #BDT Score
            "BDTscore_scaleup",
            #Category
            "zll_category_scaleup",

            #scaledw
            "leading_zll_lepton_p_scaledw",  
            "leading_zll_lepton_m_scaledw",  
            "leading_zll_lepton_theta_scaledw",                    
            "leading_zll_lepton_phi_scaledw",
            "subleading_zll_lepton_p_scaledw",
            "subleading_zll_lepton_m_scaledw",
            "subleading_zll_lepton_theta_scaledw",
            "subleading_zll_lepton_phi_scaledw",
            "zll_leptons_acolinearity_scaledw",
            "zll_leptons_acoplanarity_scaledw",
            #Zed
            "zll_m_scaledw",
            "zll_p_scaledw",
            "zll_theta_scaledw",
            "zll_phi_scaledw",
            #Recoil
            "zll_recoil_m_scaledw",
            #BDT Score
            "BDTscore_scaledw",
            #Category
            "zll_category_scaledw", 
            
            "zll_recoil_m_sqrtsup",
            "zll_recoil_m_sqrtsdw", 
    
            
            #missing Information
            "cosTheta_miss",
            #Higgsstrahlungness
            "H",
            #number of leptons
            "leps_no"
        ]
        return branchList