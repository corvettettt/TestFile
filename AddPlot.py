from ROOT import *

if __name__ == '__main__':
  rootfile = TFile('rootfile_moriond16_v1_36fb_moriond17_v2_37fb_1nd_s15_20170127_164251_95_reduced_skim.root')
  treeName = 'rootTupleTree/tree'
  Dir= rootfile.Get(treeName)
  nEntries = Dir.GetEntries()


  h_mjj_passed_MybTag = TH1D('h_mjj_passed_MybTag','h_mjj_passed_MybTag',10000,0,10000)


  for i in range(nEntries):
    Dir.GetEntry(i)
    if Dir.jetCSVAK4_j1 > 0.5 : 
      h_mjj_passed_MybTag.Fill(Dir.mjj)
  
  RootFile = TFile('New.root','recreate')
#  rootfile.Cd()
  h_mjj_passed_MybTag.Write("h_mjj_passed_MybTag")

  RootFile.Close()
