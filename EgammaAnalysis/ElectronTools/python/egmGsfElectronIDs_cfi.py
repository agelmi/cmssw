import FWCore.ParameterSet.Config as cms
from PhysicsTools.SelectorUtils.centralIDRegistry import central_id_registry

from PhysicsTools.SelectorUtils.trivialCutFlow_cff import *

trivialCutFlowMD5 = central_id_registry.getMD5FromName(trivialCutFlow.idName)

egmGsfElectronIDs = cms.EDProducer(
    "VersionedElectronIdProducer",
    electronSrc = cms.InputTag('gedGsfElectrons'),
    electronsArePAT = cms.bool(False),
    electronIDs = cms.VPSet( cms.PSet( idDefinition = trivialCutFlow,
                                       idMD5 = cms.string(trivialCutFlowMD5) )
                           )
)
    
