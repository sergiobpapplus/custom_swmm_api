from swmm_api import SwmmInput, SwmmReport, SwmmOutput, SwmmHotstart
from swmm_api.run_swmm import swmm5_run_owa

# rpt = SwmmReport('Example6-Final_AllSections_GUI.rpt')
# rpt.analyse_end
#
inp = SwmmInput.read_file('Example6-Final_AllSections_GUI.inp')
inp.force_convert_all()
# inp.copy()
# inp.to_string(fast=True)
# print()

# run('Example6-Final_AllSections_GUI.inp')
