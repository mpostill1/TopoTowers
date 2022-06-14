#BasicEventslection fliter clean events 
#JetHistsAlgo plots the jets

from xAODAnaHelpers import Config
c = Config()

c.algorithm("BasicEventSelection", {"m_truthLevelOnly": False,
                                    "m_applyGRLCut": True,
                                    "m_GRLxml": "/cvmfs/atlas.cern.ch/repo/sw/database/GroupData/GoodRunsLists/data18_13TeV/20180518/data18_13TeV.periodAllYear_HEAD_Unknown_PHYS_StandardGRL_All_Good_25ns_Triggerno17e33prim.xml",
                                    "m_doPUreweighting": False,
                                    "m_vertexContainerName": "PrimaryVertices",
                                    "m_PVNTrack": 2,
                                    "m_name": "myBaseEventSel"})
c.algorithm("ClusterHistsAlgo", {"m_inContainerName":"CaloCalFwdTopoTowers",
                                 "m_detailStr": "dummy"})
