from ROOT import *
import array

if __name__=='__main__':


   CSV_bg=[100,150,200,250,300,350,400,450,460,500,550]
   CSV_bb=[100,150,200,250,300,350,400,450,460,500,550,600,650,700,750,800,850,900,935,950]
   value_bb=[4454.25,4454.25,5524.25,5270.75,5075.75,4841.75,4652.75,4492.75,4485.25,4330.75,4188.75,4035.25,3876.75,3691.25,3548.25,3371.75,3121.25,2787.75,2421.75,2287.75]
   value_bg=[1654.75,1663.75,2468.25,2252.25,2024.75,1948.75,1864.75,1812.25,1780.25,1752.25,1640.75]

   CSV_bg_a=array.array('f',CSV_bg)
   CSV_bb_a=array.array('f',CSV_bb)
   value_bg_a=array.array('f',value_bg)
   value_bb_a=array.array('f',value_bb)

   c1 = TCanvas('c1','Scan over btag of bg',200,10,700,500)
   scanbg = TGraph(len(CSV_bg_a),CSV_bg_a,value_bg_a)
   scanbg.Draw('AC*')
   c1.Print('Scan_over_btag_of_bg.pdf')

   c1 = TCanvas('c1','Scan over btag of bg',200,10,700,500)
   scanbb = TGraph(len(CSV_bb_a),CSV_bb_a,value_bb_a)
   scanbb.Draw('AC*')
   c1.Print('Scan_over_btag_of_bb.pdf')
