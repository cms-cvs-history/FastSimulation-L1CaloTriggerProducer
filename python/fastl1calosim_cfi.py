import FWCore.ParameterSet.Config as cms

fastL1CaloSim = cms.EDFilter("FastL1CaloSim",
    TowerEEScale = cms.double(1.0),
    HcalLUT = cms.FileInPath('CalibCalorimetry/CaloTPG/data/TPGcalcDecompress2.txt'),
    TowerEMLSB = cms.double(0.5),
    JetSeedEtThreshold = cms.double(0.01),
    JetLSB = cms.double(0.5),
    DoJetCorr = cms.bool(True),
    EMActiveLevel = cms.double(3.0),
    EMSeedEnThreshold = cms.double(0.01),
    CrystalEEThreshold = cms.double(0.0), ##0.45

    TowerHadLSB = cms.double(0.5),
    FGEEThreshold = cms.double(0.5),
    HcalTPInput = cms.InputTag("hcalTriggerPrimitiveDigis"),
    TowerEBScale = cms.double(1.0),
    IsolationEt = cms.double(3.0),
    TowerHBScale = cms.double(1.0),
    TowerHBThreshold = cms.double(0.0),
    GctIso = cms.bool(False),
    hOeThreshold = cms.double(0.05),
    noFGThreshold = cms.double(50.0),
    TowerInput = cms.InputTag("towerMaker"),
    CrystalEBThreshold = cms.double(0.0), ##0.09

    EmInputs = cms.VInputTag(cms.InputTag("ecalRecHit","EcalRecHitsEB"), cms.InputTag("ecalRecHit","EcalRecHitsEE")),
    HadActiveLevel = cms.double(3.0),
    TowerHEScale = cms.double(1.0),
    # Defaults
    # "RecHits" or "TrigPrims" 
    AlgorithmSource = cms.string('TrigPrims'),
    EMLSB = cms.double(0.5),
    TowerHEThreshold = cms.double(0.0),
    TowerEEThreshold = cms.double(0.0),
    MuonNoiseLevel = cms.double(2.0),
    noTauVetoLevel = cms.double(10000.0),
    EMNoiseLevel = cms.double(2.0),
    DoEMCorr = cms.bool(True),
    FGEBThreshold = cms.double(0.8),
    QuietRegionThreshold = cms.double(3.0),
    EcalTPInput = cms.InputTag("ecalTriggerPrimitiveDigis"),
    TowerEBThreshold = cms.double(0.0),
    DoBitInfo = cms.bool(False),
    HadNoiseLevel = cms.double(2.0)
)


