from tnpConfig import tnpConfig

#### samples
samples={
    
    'data2016a':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2016preVFP/DATA_SkimTree_EGammaTnP/SingleElectron/',
    'mi2016a':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2016preVFP/MC_SkimTree_EGammaTnP/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'mg2016a':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2016preVFP/MC_SkimTree_EGammaTnP/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',

    'data2016b':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2016postVFP/DATA_SkimTree_EGammaTnP/SingleElectron/',
    'mi2016b':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2016postVFP/MC_SkimTree_EGammaTnP/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'mg2016b':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2016postVFP/MC_SkimTree_EGammaTnP/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',

    'data2017':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2017/DATA_SkimTree_EGammaTnP/SingleElectron/',
    'mi2017':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2017/MC_SkimTree_EGammaTnP/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'mg2017':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2017/MC_SkimTree_EGammaTnP/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',

    'data2018':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2018/DATA_SkimTree_EGammaTnP/EGamma/',
    'mi2018':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2018/MC_SkimTree_EGammaTnP/DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos',
    'mg2018':'/gv0/DATA/SKFlat/Run2UltraLegacy_v3/2018/MC_SkimTree_EGammaTnP/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8,'


}

#### binning
binnings = {
    "ID": [
        {"var": "el_eta", "type": "float", "bins":        [-2.5, -2., -1.566, -1.4442, -0.8, 0., 0.8, 1.4442, 1.566, 2., 2.5],  "title": "#eta_{SC}"},
        {"var": "el_pt_cor",   "type": "float",   "bins": [ 10.,15., 20., 25., 30., 35., 50., 70., 100., 200., 500.],  "title": "p_{T} [GeV]"}
    ],
    "Ele23": [
        {"var": "el_eta", "type": "float","bins":     [-2.5, -2., -1.566, -1.4442, -0.8, 0., 0.8, 1.4442, 1.566, 2., 2.5], "title": "#eta_{SC}"},
        {"var": "el_pt_cor", "type": "float", "bins": [ 10.,19.,23., 25., 30., 35., 50., 70., 100., 200.], "title": "p_{T} [GeV]"}
    ],
    "Ele12": [
        {"var": "el_eta", "type": "float", "bins":    [-2.5, -2., -1.566, -1.4442, -0.8, 0., 0.8, 1.4442, 1.566, 2., 2.5], "title": "#eta_{SC}"},
        {"var": "el_pt_cor", "type": "float", "bins": [ 10., 12.,15., 20., 25., 30., 35., 50., 70., 100., 200.], "title": "p_{T} [GeV]"}
    ]
}

loose_mcTrue='mcTrue && ((el_et/mc_probe_et) > 0.5) && ((el_et/mc_probe_et) < 1.5) && (((el_eta-mc_probe_eta)*(el_eta-mc_probe_eta)+(el_phi-mc_probe_phi)*(el_phi-mc_probe_phi))<0.01)'

#### fit parameters

## fits
fit_nominal = [
    "HistPdf::sigPass(x,histPass_genmatching,2)",
    "HistPdf::sigFail(x,histFail_genmatching,2)",
    "RooCMSShape::bkgPass(x,acmsP[50.,40.,80.],betaP[0.1,0.01,0.25],gammaP[0.05, 0.0001, 0.2],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[50.,40.,80.],betaF[0.1,0.01,0.25],gammaF[0.05, 0.0001, 0.2],peakF[90.0])",
    "Fit bkgPass histPass_notgenmatching",
    "Fit bkgFail histFail_notgenmatching",
    "SetConstant acmsP betaP acmsF betaF gammaP gammaF",
]

fit_altsig = [
    "HistPdf::sigPhysPass(x,histPass_genmatching,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching,2)",
    "Gaussian::sigResPass(x,meanP[0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanF[0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x,acmsP[50.,40.,80.],betaP[0.1,0.01,0.25],gammaP[0.05, 0.0001, 0.2],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[50.,40.,80.],betaF[0.1,0.01,0.25],gammaF[0.05, 0.0001, 0.2],peakF[90.0])",
    "Fit bkgPass histPass_notgenmatching",
    "Fit bkgFail histFail_notgenmatching",
    "SetConstant acmsP betaP acmsF betaF gammaP gammaF",
]

fit_altsig2 = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_genmass,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_genmass,2)",
    "RooCBShape::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[1,0.3,10.0],alphaP[2.0,1.2,3.5],nP[3,-5,5])",
    "RooCBShape::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[1,0.3,10.0],alphaF[2.0,1.2,3.5],nF[3,-5,5])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Fit sigPass histPass_genmatching",
    "Fit sigFail histFail_genmatching",
    "SetConstant alphaP nP alphaF nF",
    "RooCMSShape::bkgPass(x,acmsP[50.,40.,80.],betaP[0.1,0.01,0.25],gammaP[0.05, 0.0001, 0.2],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[50.,40.,80.],betaF[0.1,0.01,0.25],gammaF[0.05, 0.0001, 0.2],peakF[90.0])",
    "Fit bkgPass histPass_notgenmatching",
    "Fit bkgFail histFail_notgenmatching",
    "SetConstant acmsP betaP acmsF betaF gammaP gammaF",
]

fit_altbkg = [
    "HistPdf::sigPass(x,histPass_genmatching,2)",
    "HistPdf::sigFail(x,histFail_genmatching,2)",
    "RooCMSShape::bkgPass(x,acmsP[50.,40.,80.],betaP[0.1,0.01,0.25],gammaP[0.05, 0.0001, 0.2],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[50.,40.,80.],betaF[0.1,0.01,0.25],gammaF[0.05, 0.0001, 0.2],peakF[90.0])",
]

fit_altbkg2 = [
    "HistPdf::sigPass(x,histPass_genmatching,2)",
    "HistPdf::sigFail(x,histFail_genmatching,2)",
    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
    "Exponential::bkgFail(x, alphaF[0.,-5.,5.])",
    "Fit bkgPass histPass_notgenmatching",
    "Fit bkgFail histFail_notgenmatching",
    "SetConstant alphaP alphaF",
]


fit_altbkg2_chebychev = [
    "HistPdf::sigPass(x,histPass_genmatching,2)",
    "HistPdf::sigFail(x,histFail_genmatching,2)",
    "Chebychev::bkgPass(x, {p0P[-0.2.,-1.,1.],p1P[-0.2.,-1.,1.],p2P[0.1,-1.,1.]})",
    "Chebychev::bkgFail(x, {p0F[-0.2.,-1.,1.],p1F[-0.2.,-1.,1.],p2F[0.1,-1.,1.]})",
    "Fit bkgPass histPass_notgenmatching",
    "Fit bkgFail histFail_notgenmatching",
    "SetConstant p0P p1P p2P p0F p1F p2F",
]

fit_nominal_random = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_random,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_random,2)",
    "Gaussian::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "RooCMSShape::bkgPass(x,acmsP[60.,50.,80.],betaP[0.05,0.01,0.08],gammaP[0.1, -1, 1],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[60.,50.,80.],betaF[0.05,0.01,0.08],gammaF[0.1, -1, 1],peakF[90.0])",
]

fit_altsig_random = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_genmass_random,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_genmass_random,2)",
    "RooCBShape::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[1,0.3,10.0],alphaP[2.0,1.2,3.5],nP[3,-5,5])",
    "RooCBShape::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[1,0.3,10.0],alphaF[2.0,1.2,3.5],nF[3,-5,5])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Fit sigPass histPass_genmatching",
    "Fit sigFail histFail_genmatching",
    "SetConstant alphaP nP alphaF nF",
    "RooCMSShape::bkgPass(x,acmsP[60.,50.,80.],betaP[0.05,0.01,0.08],gammaP[0.1, -1, 1],peakP[90.0])",
    "RooCMSShape::bkgFail(x,acmsF[60.,50.,80.],betaF[0.05,0.01,0.08],gammaF[0.1, -1, 1],peakF[90.0])",
]

fit_altbkg_random = [
    "HistPdf::sigPhysPass(x,histPass_genmatching_random,2)",
    "HistPdf::sigPhysFail(x,histFail_genmatching_random,2)",
    "Gaussian::sigResPass(x,meanP[-0.0,-5.0,5.0],sigmaP[0.02,0.02,4.0])",
    "Gaussian::sigResFail(x,meanF[-0.0,-5.0,5.0],sigmaF[0.02,0.02,4.0])",
    "FCONV::sigPass(x, sigPhysPass , sigResPass)",
    "FCONV::sigFail(x, sigPhysFail , sigResFail)",
    "Exponential::bkgPass(x, alphaP[0.,-5.,5.])",
    "Exponential::bkgFail(x, alphaF[0.,-5.,5.])",
]


#### definition

LowPtCut    = ""
#"(el_pt_cor > 20 || (tag_Ele_IsoMVA94XV2 > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt_cor*(1-cos(event_met_pfphi-tag_Ele_phi)))  < 45))"
TagGAP      = ""
#"&& !(fabs(tag_sc_eta)>1.4442&&fabs(tag_sc_eta)<1.566) "
Tag16Cut    = "(tag_passingCutBasedTight94XV2  && tag_passHltEle27WPTightGsf         &&  tag_Ele_pt_cor > 30    && abs(tag_sc_eta) < 2.17 "+TagGAP +" && el_q*tag_Ele_q < 0 && "+LowPtCut+")"
Tag16CutAlt = "(tag_passingCutBasedTight94XV2  && tag_passHltEle27WPTightGsf         &&  tag_Ele_pt_cor > 35    && abs(tag_sc_eta) < 2.17 "+TagGAP +" && el_q*tag_Ele_q < 0 &&  "+LowPtCut+")"
Tag17Cut    = "(tag_passingCutBasedTight94XV2  && tag_passHltEle32DoubleEGWPTightGsf &&  tag_passEGL1SingleEGOr &&  tag_Ele_pt_cor > 35 && abs(tag_sc_eta) < 2.17 "+TagGAP +" && el_q*tag_Ele_q < 0 &&  "+LowPtCut+")"
Tag17CutAlt = "(tag_passingCutBasedTight94XV2  && tag_passHltEle32DoubleEGWPTightGsf && tag_passEGL1SingleEGOr &&  tag_Ele_pt_cor > 40 && abs(tag_sc_eta) < 2.17 "+TagGAP +" && el_q*tag_Ele_q < 0 &&  "+LowPtCut+")"
Tag18Cut    = "(tag_passingCutBasedTight94XV2  && tag_passHltEle32WPTightGsf &&  tag_Ele_pt_cor > 35 && abs(tag_sc_eta) < 2.17 "+TagGAP +"  && el_q*tag_Ele_q < 0 &&  "+LowPtCut+")"
Tag18CutAlt = "(tag_passingCutBasedTight94XV2  && tag_passHltEle32WPTightGsf &&  tag_Ele_pt_cor > 40 && abs(tag_sc_eta) < 2.17 "+TagGAP +" && el_q*tag_Ele_q < 0 &&  "+LowPtCut+")"

HLTEl23     = 'passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1 && el_l1et > L1ThresholdHLTEle23Ele12CaloIdLTrackIdLIsoVL'
HLTEl23v2   = 'passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1'
HLTEl12     = 'passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2'

POGTIGHT= "(passingCutBasedTight94XV2)"
HNL_ULID = '(passingHNLMVA)'
HNLMVACF= "(passingHNLMVACF)"
HNLMVACFTight="(scoreHNLMVACF > 0.5)"
HNLMVACFMedium="(scoreHNLMVACF > 0.4)"
HNLMVACFLoose="(scoreHNLMVACF > 0.3)"
HNLMVAFAKE= "(passingHNLMVAFake)"
HNLMVAFAKELoose= "(scoreHNLMVAFake > 0.2)"
HNLMVACONV= "(passingHNLMVAConv)"
HNLMVACONVTight="(scoreHNLMVAConv > -0.7)"
HNLMVACONVMedium="(scoreHNLMVAConv > -0.4)"
HNLMVACONVLoose="(scoreHNLMVAConv > -0.2)"

#### configs
Configs = {}
config = tnpConfig(
    data = samples["data2016a"],
    sim = samples["mi2016a"],
    sim_weight='weight*PUweight*prefireweight*zptweight',
    sim_maxweight = 1e5,
    sim_genmatching=loose_mcTrue,
    sim_notgenmatching='el_q*tag_Ele_q<0 && !('+loose_mcTrue+')',
    sim_genmass="mcMass",
    tree = "tnpEleIDs/fitter_tree",
    mass="pair_mass_cor",
    bins = binnings['ID'],
    expr = Tag16Cut,
    test = HNL_ULID,
    hist_nbins = 98,
    hist_range = (52, 150),
    method = "fit",
    fit_parameter = fit_nominal,
    fit_range = (70, 112),
    count_range=(80,102),

    systematic = [[{"title": "altsig", "fit_parameter": fit_altsig}],
                  [{"title": "altbkg", "fit_parameter": fit_altbkg}],
                  #[{"title": "altmc", "sim": samples["mg2016a"]}],
                  #[{"title": "altTag", "expr": Tag16CutAlt}],
                  #[{'title':'PUweight_up'},{'title':'PUweight_down'}],
                  #[{'title':'prefireweight_up'},{'title':'prefireweight_down'}],
                  #[{'title':'massbroad','fit_range':(52,150)}, {'title':'massnarrow','fit_range':(76,106)}],
                  #[{'title':'massbinmore','hist_nbins':196},{'title':'massbinless','hist_nbins':49}],
              ],
    option="fix_ptbelow20",

)

Configs["HNL_ULID_2016a"] = config.clone()
Configs["HNL_ULID_2016b"] = config.clone(
    data = samples["data2016b"],
    sim = samples["mi2016b"],
    systematic = [[{"title": "altsig", "fit_parameter": fit_altsig}],
                  [{"title": "altbkg", "fit_parameter": fit_altbkg}],
                  #[{"title": "altmc", "sim": samples["mg2016b"]}],
                  [{"title": "altTag", "expr": Tag16CutAlt}],
                  #[{'title':'PUweight_up'},{'title':'PUweight_down'}], 
                  #[{'title':'prefireweight_up'},{'title':'prefireweight_down'}], 
                  #[{'title':'massbroad','fit_range':(52,150)}, {'title':'massnarrow','fit_range':(76,106)}], 
                  #[{'title':'massbinmore','hist_nbins':196},{'title':'massbinless','hist_nbins':49}],                                                                                                                                                                        
              ],

)
Configs["HNL_ULID_2017"] = config.clone(
    data = samples["data2017"],
    sim = samples["mi2017"],
    expr = Tag17Cut,
    systematic = [[{"title": "altsig", "fit_parameter": fit_altsig}],
                  [{"title": "altbkg", "fit_parameter": fit_altbkg}],
                  #[{"title": "altmc", "sim": samples["mg2017"]}],
                  [{"title": "altTag", "expr": Tag17CutAlt}],
              ],

)
Configs["HNL_ULID_2018"] = config.clone(
    data = samples["data2018"],
    sim = samples["mi2018"],
    expr = Tag18Cut,
    systematic = [[{"title": "altsig", "fit_parameter": fit_altsig}],
                  [{"title": "altbkg", "fit_parameter": fit_altbkg}],
                  #[{"title": "altmc", "sim": samples["mg2018"]}],
                  [{"title": "altTag", "expr": Tag18CutAlt}],
              ],
)

####2017 

Eras = ["16a","16b","17","18"]

for Era in Eras:

    TagCut   = "(tag_passingCutBasedTight94XV2  && tag_passHltEle27WPTightGsf &&  tag_Ele_pt_cor > 30 && abs(tag_sc_eta) < 2.17 "+TagGAP+"&& el_q*tag_Ele_q < 0 && "+LowPtCut+")"
    TagCutAlt = "(tag_passingCutBasedTight94XV2  && tag_passHltEle27WPTightGsf &&  tag_Ele_pt_cor > 35 && abs(tag_sc_eta) < 2.17 "+TagGAP+"&& el_q*tag_Ele_q < 0 &&  "+LowPtCut+")"
     
    if Era == "17":
        TagCut = "(tag_passingCutBasedTight94XV2  && tag_passHltEle32DoubleEGWPTightGsf && tag_passEGL1SingleEGOr &&  tag_Ele_pt_cor > 35 && abs(tag_sc_eta) < 2.17 "+TagGAP+"&& el_q*tag_Ele_q < 0 &&  "+LowPtCut+")"
        TagCutAlt = "(tag_passingCutBasedTight94XV2  && tag_passHltEle32DoubleEGWPTightGsf && tag_passEGL1SingleEGOr &&  tag_Ele_pt_cor > 40 && abs(tag_sc_eta) < 2.17 "+TagGAP+" && el_q*tag_Ele_q < 0 &&  "+LowPtCut+")"
    if Era == "18":
        TagCut = "(tag_passingCutBasedTight94XV2  && tag_passHltEle32WPTightGsf &&  tag_Ele_pt_cor > 35 && abs(tag_sc_eta) < 2.17 "+TagGAP+" && el_q*tag_Ele_q < 0 &&  "+LowPtCut+")"
        TagCutAlt = "(tag_passingCutBasedTight94XV2  && tag_passHltEle32WPTightGsf &&  tag_Ele_pt_cor > 40 && abs(tag_sc_eta) < 2.17 "+TagGAP+" && el_q*tag_Ele_q < 0 &&  "+LowPtCut+")"
        
    print ("TAG = " + TagCut)
    Configs["POGTIGHT_"+Era]         = config.clone(    data = samples["data20"+Era],    sim = samples["mi20"+Era],    expr = TagCut,  test = POGTIGHT)
    Configs["HNLMVACF_"+Era]         = config.clone(    data = samples["data20"+Era],    sim = samples["mi20"+Era],    expr = TagCut,  test = HNLMVACF)
    Configs["HNLMVACFLoose_"+Era]    = config.clone(    data = samples["data20"+Era],    sim = samples["mi20"+Era],    expr = TagCut,    test = HNLMVACFLoose)
    Configs["HNLMVACFMedium_"+Era]   = config.clone(    data = samples["data20"+Era],    sim = samples["mi20"+Era],    expr = TagCut,    test = HNLMVACFMedium)
    Configs["HNLMVACFTight_"+Era]   = config.clone(    data = samples["data20"+Era],    sim = samples["mi20"+Era],    expr = TagCut,    test = HNLMVACFTight)
    Configs["HNLMVAFAKE_"+Era]       = config.clone(    data = samples["data20"+Era],    sim = samples["mi20"+Era],    expr = TagCut,    test = HNLMVAFAKE)
    Configs["HNLMVAFAKELoose_"+Era]  = config.clone(    data = samples["data20"+Era],    sim = samples["mi20"+Era],    expr = TagCut,    test = HNLMVAFAKELoose)
    Configs["HNLMVACONV_"+Era]       = config.clone(    data = samples["data20"+Era],    sim = samples["mi20"+Era],    expr = TagCut,    test = HNLMVACONV)
    Configs["HNLMVACONVLoose_"+Era]  = config.clone(    data = samples["data20"+Era],    sim = samples["mi20"+Era],    expr = TagCut,    test = HNLMVACONVLoose)
    Configs["HNLMVACONVMedium_"+Era] = config.clone(    data = samples["data20"+Era],    sim = samples["mi20"+Era],    expr = TagCut,    test = HNLMVACONVMedium)
    Configs["HNLMVACONVTight_"+Era]  = config.clone(    data = samples["data20"+Era],    sim = samples["mi20"+Era],    expr = TagCut,    test = HNLMVACONVTight)
#### Trigger

config_HLT = tnpConfig(
    data = samples["data2016a"],
    sim = samples["mi2016a"],
    expr = Tag16Cut+" && "+HNL_ULID,
    test = HLTEl23,
    sim_weight='weight*PUweight*prefireweight*zptweight',
    sim_maxweight = 1e5,
    sim_genmatching=loose_mcTrue,
    sim_notgenmatching='el_q*tag_Ele_q<0 && !('+loose_mcTrue+')',
    sim_genmass="mcMass",
    tree = "tnpEleTrig/fitter_tree",
    mass="pair_mass_cor",
    bins = binnings["Ele23"],
    hist_nbins = 70,
    hist_range = (55, 125),
    method = "fit",
    fit_parameter = fit_nominal,
    fit_range = (60, 120),

    systematic = [
        [{"title": "altsig", "fit_parameter": fit_altsig}],
        #[{"title": "altbkg", "fit_parameter": fit_altbkg}],
        #[{"title": "altmc", "sim": samples["mg2016a"]}],
        #[{"title": "altTag", "expr": Tag16Cut+" && "+HNL_ULID}],
        #[{"title": "fitwindowup", "fit_range": (63, 123)},
        # {"title": "fitwindowdown", "fit_range": (57, 117)}],
    ],
)
Configs["HLTEl23_2016a"] = config_HLT.clone()
Configs["HLTEl23_2016b"] = config_HLT.clone(
    data = samples["data2016b"],
    sim = samples["mi2016b"],
)
Configs["HLTEl23_2017"] = config_HLT.clone(
    data = samples["data2017"],
    sim = samples["mi2017"],
    expr = Tag17Cut+" && "+HNL_ULID,
)
Configs["HLTEl23_2018"] = config_HLT.clone(
    data = samples["data2018"],
    sim = samples["mi2018"],
    expr = Tag18Cut+" && "+HNL_ULID,
)
Configs["HLTEl12_2016a"] = config_HLT.clone(
    bins = binnings["Ele12"],
    test = HLTEl12
)
Configs["HLTEl12_2016b"] = config_HLT.clone(
    data = samples["data2016b"],
    sim = samples["mi2016b"],
    bins = binnings["Ele12"],
    test = HLTEl12,
)   
Configs["HLTEl12_2017"] = config_HLT.clone(
    data = samples["data2017"],
    sim = samples["mi2017"],
    bins = binnings["Ele12"],
    test = HLTEl12,
    expr = Tag17Cut+" && "+HNL_ULID,

)
Configs["HLTEl12_2018"] = config_HLT.clone(
    data = samples["data2018"],
    sim = samples["mi2018"],
    bins = binnings["Ele12"],
    test = HLTEl12,
    expr = Tag18Cut+" && "+HNL_ULID,
)


if __name__ == "__main__":
    for key in sorted(Configs.keys()):
        print key
