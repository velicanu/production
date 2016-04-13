# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: step3 --data --conditions FT_R_53_LV5::All -s RAW2DIGI,RECO --scenario HeavyIons --datatier GEN-SIM-RECO --eventcontent RECODEBUG -n 100 --repacked --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

# Input source
process.source = cms.Source("PoolSource",
                            secondaryFileNames = cms.untracked.vstring(),
                            #fileNames = cms.untracked.vstring('/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/066/14B65DE8-9512-E111-AA9F-BCAEC53296F6.root')
                            fileNames = cms.untracked.vstring(
       '/store/data/Run2011B/Jet/RAW/v1/000/175/832/2C9D83B9-60D9-E011-82BC-001D09F252E9.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/832/D0FEB2F2-56D9-E011-A9FA-003048F1C420.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/833/5CFF0B10-59D9-E011-B256-003048D2C0F0.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/834/22F73656-7AD9-E011-A980-003048F118C4.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/834/7CFA1C0D-67D9-E011-95E8-001D09F29114.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/834/827A7275-69D9-E011-8488-001D09F24259.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/834/905BC54C-5FD9-E011-9F2B-BCAEC518FF8E.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/834/CEC0764A-6CD9-E011-8441-E0CB4E55365C.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/834/ECE8B30D-80D9-E011-89AA-003048D3750A.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/835/8CCD1A39-78D9-E011-B79B-003048F1110E.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/835/C2A7DD83-91D9-E011-AD9E-003048D375AA.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/837/90A1EF1D-82D9-E011-89CD-003048F1182E.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/837/AC2CCA59-92D9-E011-802B-BCAEC5364C4C.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/857/6A2BAEEB-AAD9-E011-84BC-BCAEC518FF4A.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/858/E2E83537-ACD9-E011-A72A-BCAEC5329732.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/860/469629D7-ACD9-E011-8AF6-003048678098.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/860/5EE06746-FCD9-E011-BE7F-BCAEC518FF56.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/863/7661748F-FED9-E011-89E1-BCAEC518FF56.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/863/F0A9332D-FDD9-E011-8734-003048D2BED6.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/865/DC54CE7A-FBD9-E011-9E47-0030487A3DE0.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/866/208EFABD-D2D9-E011-9F5D-BCAEC53296F6.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/866/6CD81B7D-C0D9-E011-9891-0019B9F72D71.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/866/7A0895A6-D0D9-E011-A6D9-0019B9F581C9.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/866/829ADA8C-CED9-E011-BE27-BCAEC5329717.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/866/92190AFA-FCD9-E011-8097-BCAEC5329708.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/866/CEF924BD-CBD9-E011-9C4A-0019B9F707D8.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/872/EED2B9FB-2BDA-E011-BF6C-003048F024DC.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/873/DC17265C-F5D9-E011-B1E3-003048D2C174.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/874/9A97CAFB-FAD9-E011-9601-001D09F23A84.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/874/9C6E5696-F6D9-E011-98AD-003048D2BB58.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/874/A2921446-F5D9-E011-A6AA-001D09F24EE3.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/875/2E873414-04DA-E011-AD67-BCAEC532972C.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/875/64D46196-FED9-E011-B8DB-001D09F29533.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/875/AC7D7D19-FBD9-E011-9246-E0CB4E55367F.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/877/6A8FAF16-10DA-E011-877C-BCAEC518FF56.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/877/E6F96BE0-16DA-E011-96D1-BCAEC518FF7A.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/881/403DCB34-16DA-E011-B643-003048D37580.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/881/BC3B1112-19DA-E011-82A5-BCAEC53296FB.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/881/FCEDB57B-13DA-E011-8974-001D09F2424A.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/886/0EC1A150-18DA-E011-A525-003048F11C58.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/886/42F15563-1ADA-E011-A66E-003048F11C58.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/886/829D769D-1EDA-E011-B6D2-003048F0258C.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/886/AE5B5019-25DA-E011-B85F-003048F118C4.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/887/0EC60375-28DA-E011-BFD5-003048F117EC.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/887/6C69FB79-2FDA-E011-9946-BCAEC5329708.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/888/1CAC49B8-46DA-E011-B2E5-003048D375AA.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/888/28EA18E2-30DA-E011-B056-BCAEC518FF62.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/888/3EDD387C-36DA-E011-9518-003048F01E88.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/888/BA332D1E-3CDA-E011-BCC6-003048F110BE.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/888/DEE7FD22-43DA-E011-B4AC-003048D37580.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/896/3A2269E0-5BDA-E011-A776-003048F118AA.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/906/6231373B-9CDA-E011-B906-001D09F29597.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/906/B07848C0-9DDA-E011-AE3D-001D09F276CF.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/906/FE5A2852-D3DA-E011-9423-003048D3750A.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/910/0284C8DC-A8DA-E011-96E2-BCAEC53296F2.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/916/9A970426-BEDA-E011-91BF-003048D37456.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/921/0C361A5F-D7DA-E011-A0DD-001D09F24D67.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/921/1CD15739-D8DA-E011-8E31-003048F024FA.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/921/3CA885F3-D5DA-E011-9A19-BCAEC53296F4.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/921/4A01EFD2-DFDA-E011-97C8-BCAEC518FF8D.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/921/4AFF0397-DBDA-E011-9231-BCAEC532971D.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/921/5A290FFB-DCDA-E011-BDBE-003048F1110E.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/921/A2FE394D-E8DA-E011-802C-E0CB4E4408E7.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/921/A6773A35-D8DA-E011-B203-003048F118C4.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/921/AEE3B652-E3DA-E011-860E-003048F01E88.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/971/BA72FCB1-39DB-E011-9962-BCAEC5329730.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/971/DE620015-32DB-E011-A786-BCAEC53296FD.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/973/1A2AE3C0-45DB-E011-B353-E0CB4E4408C4.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/973/2CFF31DB-95DB-E011-A7FA-BCAEC518FF63.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/973/9406B15F-41DB-E011-B85E-485B3962633D.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/973/B41A52CE-43DB-E011-916E-003048D2BDD8.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/973/D2A4C638-3FDB-E011-8E70-003048F024FA.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/973/D46B4A26-3CDB-E011-B541-E0CB4E55365C.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/974/007D47CC-47DB-E011-9982-003048F1C832.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/974/96A1CF1C-96DB-E011-8813-BCAEC53296F3.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/975/1051EC61-A1DB-E011-95C6-BCAEC5364C93.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/975/16FCF69E-49DB-E011-A716-001D09F2516D.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/975/1815C39A-4DDB-E011-99C4-BCAEC5329719.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/975/444957D9-4CDB-E011-90CC-0019B9F581C9.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/975/C40CE8F3-4EDB-E011-A228-003048F024F6.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/975/CA0F74DA-9BDB-E011-8F1F-003048F118AA.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/975/D0EE4E52-9BDB-E011-8BD3-BCAEC5364CFB.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/976/240EF6C8-9BDB-E011-A9B2-003048D37538.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/976/24A5BBAE-A4DB-E011-81E7-001D09F24DA8.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/990/0A1D8351-9BDB-E011-8B76-BCAEC518FF67.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/990/1E12DB06-9EDB-E011-AB96-003048F024DE.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/990/34D6A170-9DDB-E011-9AEA-BCAEC53296F2.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/175/990/BA4C492E-9BDB-E011-91CF-BCAEC518FF7A.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/023/7029AAC6-C8DB-E011-A435-001D09F28F0C.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/023/CA69D29D-CADB-E011-956E-BCAEC518FF76.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/023/E82C7CE6-C9DB-E011-AD49-BCAEC518FF50.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/059/C0090D69-3DDC-E011-8A4A-003048D2C020.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/161/B82F1190-43DD-E011-9218-001D09F24FEC.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/163/3E0C56A8-42DD-E011-9872-BCAEC532971F.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/163/46EDA3F4-46DD-E011-992E-BCAEC5329729.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/165/F6F5DEBA-4BDD-E011-93B4-BCAEC518FF62.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/166/DA87CBB9-53DD-E011-830E-003048D2C020.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/167/78FDBC25-51DD-E011-A1C0-E0CB4E4408E3.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/169/26607026-55DD-E011-AD24-BCAEC532972C.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/169/4E0CC673-56DD-E011-A81D-001D09F29533.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/169/622B3274-57DD-E011-A83D-001D09F24FBA.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/169/CCB7C369-52DD-E011-AB75-BCAEC532970D.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/196/088B1021-8ADD-E011-BD91-BCAEC518FF8D.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/201/0834E2A0-A3DD-E011-8CC1-001D09F2546F.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/201/146ACF77-B1DD-E011-8522-003048F024DE.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/201/241111FB-B7DD-E011-AF9E-001D09F253C0.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/201/3A07D2DC-A9DD-E011-ACAB-E0CB4E4408D1.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/201/3C756E1F-ABDD-E011-BF6C-BCAEC5329720.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/201/500D79F6-9FDD-E011-8004-001D09F2910A.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/201/5ED2FAAF-AFDD-E011-BB45-001D09F2426D.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/201/64407B86-ADDD-E011-9969-BCAEC5364C4C.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/201/6ADBDA44-B2DD-E011-965D-BCAEC518FF8A.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/201/7070D154-A7DD-E011-85AE-BCAEC518FF52.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/201/7CA27BCA-A8DD-E011-863B-003048F1C836.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/201/8CAA74C7-AEDD-E011-99B8-BCAEC518FF68.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/201/B82E4312-BDDD-E011-908B-BCAEC532971E.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/201/BE61DE36-A6DD-E011-B8B0-BCAEC518FF3C.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/201/C0571872-BBDD-E011-BBDC-BCAEC532971C.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/201/C05FCF5A-B4DD-E011-8F7D-BCAEC5329732.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/201/C4757654-B3DD-E011-8771-BCAEC518FF91.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/201/EC58A8A9-C1DD-E011-B067-BCAEC5329718.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/202/1C409B38-C4DD-E011-B909-BCAEC518FF8E.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/202/30D60C11-C6DD-E011-A424-E0CB4E4408E7.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/202/56D169EF-C8DD-E011-8C8A-001D09F29321.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/202/A2DA7DE6-CCDD-E011-8200-001D09F253D4.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/202/AC396360-C3DD-E011-AF41-003048F1C832.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/202/ECDF1EDA-C0DD-E011-B8C8-E0CB4E4408D1.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/206/08F96122-CEDD-E011-8ED7-E0CB4E4408C4.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/206/CCE9CBC7-D2DD-E011-BBF2-001D09F2437B.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/207/1E66BE65-D3DD-E011-B5A2-001D09F24448.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/207/5AC16AB9-E1DD-E011-8E70-0030486780AC.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/207/5C33650B-DBDD-E011-B62B-BCAEC5329720.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/207/60BA3143-D8DD-E011-BC87-BCAEC5364C4C.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/286/14CBBA3F-4CDE-E011-B6FE-BCAEC5364CFB.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/286/18BD96B2-48DE-E011-AFC0-003048D374F2.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/286/1AD641D6-4ADE-E011-9CD1-001D09F2305C.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/286/287B2BB1-41DE-E011-9920-003048F1C58C.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/286/425FB682-4BDE-E011-9BD6-BCAEC53296FD.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/286/4661E0E6-43DE-E011-9057-E0CB4E553651.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/286/483CC47A-44DE-E011-92F2-BCAEC5329721.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/286/5C675001-48DE-E011-A382-003048D37456.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/286/765875F1-45DE-E011-B555-003048D2BDD8.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/286/A0466C70-49DE-E011-841F-001D09F242EA.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/286/B2A40550-47DE-E011-9C3F-001D09F23F2A.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/286/C82EF641-51DE-E011-AB34-BCAEC532970F.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/286/F68BC4F1-4CDE-E011-9989-BCAEC53296F7.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/289/4CDEBFD4-52DE-E011-8D2D-BCAEC532971E.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/289/D4513B58-4EDE-E011-8766-BCAEC532970F.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/298/E6AFEED6-56DE-E011-81E7-003048F24A04.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/304/04E1E304-BCDE-E011-90C3-003048F1BF68.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/304/0E8E026D-BFDE-E011-B358-003048D2C174.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/304/286F1561-BDDE-E011-A761-003048F118C2.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/304/2A47942B-BDDE-E011-B1B4-BCAEC518FF50.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/304/32309DD7-BCDE-E011-A251-001D09F2906A.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/304/3A542E2F-BCDE-E011-B7DC-003048F118D4.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/304/4CD15E72-D7DE-E011-B35A-001D09F28D4A.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/304/5CB1B2E3-72DE-E011-A943-003048D3750A.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/304/942B7F61-BCDE-E011-BEF7-BCAEC518FF91.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/304/9CAFB003-BCDE-E011-89ED-003048F117B6.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/304/A2F68B8E-BDDE-E011-B223-001D09F241B9.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/304/B64DCEFA-BCDE-E011-B9C9-BCAEC518FF62.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/304/C4FD9AEC-C2DE-E011-AC9C-BCAEC518FF54.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/304/CC516388-71DE-E011-B7C4-001D09F24EAC.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/304/DA2F7198-C1DE-E011-A144-BCAEC5329729.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/304/EE43CFD0-BCDE-E011-AB22-BCAEC518FF6E.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/304/F8A1F23B-BCDE-E011-A271-BCAEC53296FC.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/308/2C782067-BDDE-E011-AC54-BCAEC518FF7A.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/308/302C5AED-C2DE-E011-BA53-BCAEC518FF89.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/308/6449C5A3-C3DE-E011-A756-BCAEC53296F2.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/308/8A3B978C-D7DE-E011-B864-001D09F2514F.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/308/9845D905-BEDE-E011-8F13-001D09F242EF.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/308/D2149196-C1DE-E011-9DED-BCAEC53296FF.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/308/FEAE2A4F-C2DE-E011-8088-001D09F23A34.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/0458C1DD-D9DE-E011-951C-0019B9F7312C.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/08D1C6D0-C3DE-E011-B1A2-BCAEC53296F6.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/0A86E240-DBDE-E011-ABFE-001D09F24763.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/168518CC-F5DE-E011-AA93-E0CB4E4408D1.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/2EF14CA6-D6DE-E011-B071-001D09F23A34.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/46CECF47-C2DE-E011-B29C-001D09F29524.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/4AC8DC22-C3DE-E011-8D35-BCAEC53296F7.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/4C7308D1-C3DE-E011-B991-001D09F231B0.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/4C740C13-DCDE-E011-A670-001D09F2A690.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/52585E5E-EBDE-E011-A4FD-E0CB4E4408C4.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/5854ED5A-EFDE-E011-AD74-001D09F24259.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/6AAC11DC-DADE-E011-A52A-001D09F252F3.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/78070E20-C3DE-E011-9368-BCAEC5364C62.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/823DAFB8-E9DE-E011-A8B7-003048D2C020.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/ACFAF100-FFDE-E011-BB2A-E0CB4E5536AE.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/AEBA8530-D9DE-E011-AAAA-003048D37456.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/B0763A57-D6DE-E011-BF4A-003048D2C0F0.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/B4803DBC-E7DE-E011-8029-BCAEC518FF6E.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/BE5E9415-DCDE-E011-98BC-001D09F2441B.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/CACEE357-DDDE-E011-9E81-001D09F29533.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/DAE14920-C3DE-E011-98A0-BCAEC5329730.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/DC1C4F57-D6DE-E011-A35D-001D09F23C73.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/DE02C8A1-F3DE-E011-88C6-BCAEC518FF3C.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/F0C993D2-C3DE-E011-BE9F-001D09F251B8.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/F45BE4E6-E6DE-E011-964B-BCAEC5329719.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/309/F6A77E41-DBDE-E011-A5B6-001D09F24EAC.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/461/1AB4B6A2-CADF-E011-B015-003048F024DE.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/461/34CFE2D9-D2DF-E011-B121-003048F118E0.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/461/5A414C0C-CCDF-E011-A4A5-BCAEC532972D.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/463/9E864CA9-D2DF-E011-AD75-BCAEC5329701.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/464/0ADBD71B-D3DF-E011-A816-003048D2C174.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/464/2EB7678A-D9DF-E011-9940-BCAEC518FF54.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/464/6EB46BC7-D3DF-E011-A931-0030487A195C.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/465/7471DD0E-DADF-E011-B8FD-BCAEC54DB5D6.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/466/74CC9127-DADF-E011-BACA-001D09F34488.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/466/884DB2AA-D8DF-E011-BE76-BCAEC518FF5F.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/466/9075B1BF-DFDF-E011-8239-E0CB4E4408C4.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/467/08FF7822-E1DF-E011-9CAE-003048CFB40C.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/467/465BC99D-E4DF-E011-99AD-003048F1182E.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/467/A4A9AE3A-E3DF-E011-9E41-003048F024FE.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/467/D43ABE51-87E0-E011-92C5-001D09F252F3.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/467/FA92A554-DEDF-E011-97BE-001D09F27067.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/468/144F60BE-EDDF-E011-A382-003048F11CF0.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/468/2AB0012A-F6DF-E011-9967-003048D374F2.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/468/2E9AEBF3-EADF-E011-9FEA-001D09F24303.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/468/3C6DA1D7-E8DF-E011-BEE2-001D09F24691.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/468/D0C9A543-F1DF-E011-B59B-003048F11DE2.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/469/F07BA397-F5DF-E011-8266-E0CB4E4408C4.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/470/800530E9-FDDF-E011-B305-BCAEC53296FD.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/545/4CE7B1E0-8FE0-E011-945A-BCAEC532972E.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/547/5AD67E10-96E0-E011-9A8C-BCAEC5329702.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/547/665363CC-99E0-E011-B915-BCAEC5329713.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/547/6C1F8B82-94E0-E011-88DE-BCAEC53296FB.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/547/7A53919B-97E0-E011-BDC1-003048F118C4.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/547/E61CF1FC-A0E0-E011-9365-BCAEC532972D.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/548/00566E6F-A9E0-E011-8CEE-E0CB4E4408D1.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/548/14CA3D1C-A5E0-E011-9B93-BCAEC5329717.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/548/18C7B35F-C7E0-E011-8715-003048D2BED6.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/548/260D4F87-C4E0-E011-9315-0030487CD812.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/548/2821FE46-AEE0-E011-9700-003048D37538.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/548/40B8B04A-B2E0-E011-B39F-BCAEC5364C42.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/548/4A87862D-CBE0-E011-ABC8-BCAEC518FF68.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/548/4CC4C646-B0E0-E011-A693-001D09F24D67.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/548/4E792351-B5E0-E011-A434-001D09F24600.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/548/563DF3D0-B7E0-E011-B26C-BCAEC518FF62.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/548/6CACA63F-9DE0-E011-951D-BCAEC53296F4.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/548/763CB64B-BFE0-E011-BC33-003048F1182E.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/548/7689ADBB-BAE0-E011-9694-001D09F25438.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/548/8AC34EAB-C2E0-E011-9EAF-001D09F231C9.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/548/D2852C37-D6E0-E011-838B-E0CB4E4408E3.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/548/D6622781-A1E0-E011-B60A-BCAEC518FF68.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/548/EEFD7CB3-CFE0-E011-99B8-BCAEC518FF7A.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/548/F43CAD6B-A7E0-E011-9078-BCAEC53296F3.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/570/6AE6F27A-F1E0-E011-92D5-001D09F24259.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/681/ACFC399C-0CE2-E011-AEE1-003048F11C5C.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/697/1C0ACE98-5DE2-E011-8D92-003048F1110E.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/697/645F7082-61E2-E011-AED2-001D09F28E80.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/697/6814C606-60E2-E011-88D2-003048D2BE08.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/697/76D09BE3-65E2-E011-88B4-BCAEC5364C4C.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/697/E25A4E1E-69E2-E011-A339-BCAEC532970F.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/697/E68B8193-6DE2-E011-99AE-BCAEC5329708.root',
       '/store/data/Run2011B/Jet/RAW/v1/000/176/698/3A8B5F45-6CE2-E011-8150-0030487CD6B4.root'
)
                            )

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.28 $'),
    annotation = cms.untracked.string('step3 nevts:100'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RECODEBUGoutput = cms.OutputModule("PoolOutputModule",
                                           splitLevel = cms.untracked.int32(0),
                                           eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
                                           outputCommands = process.RECODEBUGEventContent.outputCommands,
                                           fileName = cms.untracked.string('/tmp/ylai/DATA_RECO.root'),
                                           dataset = cms.untracked.PSet(
    #filterName = cms.untracked.string('MinBiasCollEvtSel'),
    dataTier = cms.untracked.string('RECO')
    ),
                                           )

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'FT_53_LV5_AN1::All', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.hiRecoPFJets = process.hiRecoAllPFJets
process.hiRecoJets = process.hiRecoAllJets
process.reconstruction_step = cms.Path(process.reconstructionHeavyIons)

process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECODEBUGoutput_step = cms.EndPath(process.RECODEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.RECODEBUGoutput_step)

# from Configuration.PyReleaseValidation.ConfigBuilder import MassReplaceInputTag
# MassReplaceInputTag(process)

# process.SimpleMemoryCheck=cms.Service("SimpleMemoryCheck",
#                                       oncePerEventMode=cms.untracked.bool(False))

# process.Timing=cms.Service("Timing",
#                            useJobReport = cms.untracked.bool(True)
#                            )
