from swmm_api import SwmmInput
from swmm_api.input_file.sections import Control

inp = SwmmInput.read_file('example_controls.inp')
c = inp.CONTROLS
print(c['ARA_INFLOW'].to_inp_line())
# print(c.to_inp_lines())

control_object = Control(name='test_rule',
                         conditions=[Control._Condition('IF', 'SIMULATION', 'TIME', '›', 0)],
                         actions_if=[Control._Action('PUMP', 'FVSanPump4', 'STATUS', '=', 'OFF')],
                         priority=5)
control_object

inp2 = SwmmInput()
inp.add_obj(control_object)
