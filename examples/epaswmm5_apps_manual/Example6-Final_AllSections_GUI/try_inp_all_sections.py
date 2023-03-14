from swmm_api import SwmmInput, SwmmReport, SwmmOutput, SwmmHotstart, CONFIG
from swmm_api.run_swmm import swmm5_run_owa, swmm5_run_epa

# rpt = SwmmReport('Example6-Final_AllSections_GUI.rpt')
# rpt.analyse_end
#
CONFIG['exe_path'] = r"C:\Program Files\EPA SWMM 5.2.3 (64-bit)\runswmm.exe"
CONFIG['encoding'] = 'ISO-8859-1'

inp = SwmmInput.read_file('Example6-Final_AllSections_GUI.inp')
inp.force_convert_all()
# inp.copy()
# inp.to_string(fast=True)
# print()
inp.write_file('Example6-Final_AllSections_python.inp')
# run('Example6-Final_AllSections_GUI.inp')
swmm5_run_epa('Example6-Final_AllSections_python.inp')
