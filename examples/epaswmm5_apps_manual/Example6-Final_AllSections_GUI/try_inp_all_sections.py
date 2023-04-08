from swmm_api import SwmmInput, SwmmReport, SwmmOutput, SwmmHotstart, CONFIG
from swmm_api.run_swmm import swmm5_run_owa, swmm5_run_epa

# rpt = SwmmReport('Example6-Final_AllSections_GUI.rpt')
# rpt.analyse_end
#
# CONFIG['exe_path'] = r"C:\Program Files\EPA SWMM 5.2.3 (64-bit)\runswmm.exe"
CONFIG['exe_path'] = "/Users/markus/.bin/runswmm"
# CONFIG['encoding'] = 'ISO-8859-1'
# swmm5_run_epa('Example6-Final_AllSections_GUI.inp', init_print=False)

exit()

inp = SwmmInput.read_file('Example6-Final_AllSections_GUI.inp')
inp.force_convert_all()
# inp.copy()

rpt = SwmmReport('Example6-Final_AllSections_GUI.rpt')
out = SwmmOutput('Example6-Final_AllSections_GUI.out')

# not_converted_parts = set(rpt._raw_parts) - set(rpt._converted_parts)
for p in rpt._raw_parts:
 if not hasattr(rpt, p.replace('/', '').replace('-', ' ').replace(' ', '_').lower()):
  print(p)

# rpt.get_simulation_info()

# rpt.groundwater_continuity
# rpt.runoff_quality_continuity
# rpt.get_simulation_info()
# rpt.quality_routing_continuity
# rpt.flow_routing_continuity
# rpt.runoff_quantity_continuity
rpt.street_summary
rpt.time
{
    # 'Groundwater Continuity',
 # 'Runoff Quality Continuity',
 # 'Simulation Infos',
 # 'Street Summary',
 'Most Frequent Nonconverging Nodes',
 # 'Rainfall Dependent I/I',
 # 'Quality Routing Continuity',
 # 'Flow Routing Continuity',
 # 'Street Flow Summary',
 # 'Runoff Quantity Continuity'
}
# print(rpt._raw_parts['Rainfall Dependent I/I'])
print(rpt.street_flow_summary.to_string())
rpt.most_frequent_nonconverging_nodes
print(rpt._raw_parts['Street Flow Summary'])

# inp.to_string(fast=True)
# print()
inp.write_file('Example6-Final_AllSections_python.inp')
# run('Example6-Final_AllSections_GUI.inp')
swmm5_run_epa('Example6-Final_AllSections_python.inp')
