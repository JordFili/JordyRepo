import FWCore.ParameterSet.Config as cms
from Configuration.Generator.PythiaUEZ2Settings_cfi import *
from GeneratorInterface.ExternalDecays.TauolaSettings_cff import *

generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    comEnergy = cms.double(8000.0),
    crossSection = cms.untracked.double(1.1),
    ExternalDecays = cms.PSet(
        Tauola = cms.untracked.PSet(
            TauolaPolar,
            TauolaDefaultInputCards
        ),
        parameterSets = cms.vstring('Tauola')
    ),
    UseExternalGenerators = cms.untracked.bool(True),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring('MSEL=0         ! User defined processes',
            'MSUB(186)= 1   ! gg->QQbarA (MSSM)',
            'KFPR(186,2)= 5 ! Q = b',  
            # MSSM settings
            'IMSS(4)= 2     ! masses fixed by user',
            'RMSS(5)= 30.   ! tan beta', 
            'RMSS(19)= 30. ! m_A', 
            'RMSS(1)= 100.  ! M1',   
            'RMSS(2)= 200.  ! M2',   
            'RMSS(3)= 800.  ! Mg',   
            'RMSS(4)= 200.  ! mu',   
            'RMSS(6)= 1000.  ! MS',
            'RMSS(7)= 1000.  ! MS',
            'RMSS(8)= 1000.  ! MS',
            'RMSS(9)= 1000.  ! MS',
            'RMSS(10)= 1000.  ! MS',
            'RMSS(11)= 1000.  ! MS',
            'RMSS(12)= 1000.  ! MS',
            'RMSS(13)= 1000.  ! MS',
            'RMSS(14)= 1000.  ! MS',
            'RMSS(15)= 2000.  ! Ab',
            'RMSS(16)= 2000.  ! At',
            'RMSS(17)= 2000.  ! Atau',
            # Higgs masses
            # 'PMAS(25,1)=125.   ! mh',
            # 'PMAS(35,1)=125.  ! mH',
            'PMAS(36,1)=60.  ! mA',
            # Switch off / on desirable channels for A->tautau
            'MDME(420,1)=0  ! Higgs(H) decay into d              dbar', 
            'MDME(421,1)=0 ', 
            'MDME(422,1)=0 ', 
            'MDME(423,1)=0 ', 
            'MDME(424,1)=0 ', 
            'MDME(425,1)=0 ', 
            'MDME(426,1)=0 ', 
            'MDME(427,1)=0 ', 
            'MDME(428,1)=0 ', 
            'MDME(429,1)=1  ! decay to mu+mu-', 
            'MDME(430,1)=0  ', 
            'MDME(431,1)=0 ', 
            'MDME(432,1)=0 ', 
            'MDME(433,1)=0 ', 
            'MDME(434,1)=0 ', 
            'MDME(435,1)=0 ', 
            'MDME(436,1)=0 ', 
            'MDME(437,1)=0 ', 
            'MDME(438,1)=0 ', 
            'MDME(439,1)=0 ', 
            'MDME(440,1)=0 ', 
            'MDME(441,1)=0 ', 
            'MDME(442,1)=0 ', 
            'MDME(443,1)=0 ', 
            'MDME(444,1)=0 ', 
            'MDME(445,1)=0 ', 
            'MDME(446,1)=0 ', 
            'MDME(447,1)=0 ', 
            'MDME(448,1)=0 ', 
            'MDME(449,1)=0 ', 
            'MDME(450,1)=0 ',
            'MDME(451,1)=0 ', 
            'MDME(452,1)=0 ', 
            'MDME(453,1)=0 ', 
            'MDME(454,1)=0 ', 
            'MDME(455,1)=0 ', 
            'MDME(456,1)=0 ', 
            'MDME(457,1)=0 ', 
            'MDME(458,1)=0 ', 
            'MDME(459,1)=0 ', 
            'MDME(460,1)=0 ', 
            'MDME(461,1)=0 ', 
            'MDME(462,1)=0 ', 
            'MDME(463,1)=0 ', 
            'MDME(464,1)=0 ', 
            'MDME(465,1)=0 ', 
            'MDME(466,1)=0 ', 
            'MDME(467,1)=0 ', 
            'MDME(468,1)=0 ', 
            'MDME(469,1)=0 ', 
            'MDME(470,1)=0 ', 
            'MDME(471,1)=0 ', 
            'MDME(472,1)=0 ', 
            'MDME(473,1)=0 ', 
            'MDME(474,1)=0 ', 
            'MDME(475,1)=0 ', 
            'MDME(476,1)=0 ', 
            'MDME(477,1)=0 ', 
            'MDME(478,1)=0 ', 
            'MDME(479,1)=0 ', 
            'MDME(480,1)=0 ', 
            'MDME(481,1)=0 ', 
            'MDME(482,1)=0 ', 
            'MDME(483,1)=0 ', 
            'MDME(484,1)=0 ', 
            'MDME(485,1)=0 ', 
            'MDME(486,1)=0 ', 
            'MDME(487,1)=0 ', 
            'MDME(488,1)=0 ', 
            'MDME(489,1)=0 ', 
            'MDME(490,1)=0 ', 
            'MDME(491,1)=0 ', 
            'MDME(492,1)=0 ', 
            'MDME(493,1)=0 ', 
            'MDME(494,1)=0 ', 
            'MDME(495,1)=0 ', 
            'MDME(496,1)=0 ', 
            'MDME(497,1)=0 ', 
            'MDME(498,1)=0 ', 
            'MDME(499,1)=0 ', 
            'MDME(500,1)=0 ', 
            'MDME(501,1)=0 ', 
            'MDME(502,1)=0 '),
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)

