from swmm_api import SwmmInput

inp = SwmmInput.read_file('example_controls.inp')
c = inp.CONTROLS
print(c['ARA_INFLOW'].to_inp_line())
# print(c.to_inp_lines())
