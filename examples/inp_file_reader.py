import os

from swmm_api import read_inp_file, swmm5_run
from swmm_api.input_file import SEC
from swmm_api.input_file.macros.geo import complete_vertices
from swmm_api.run_swmm import (delete_swmm_files,)
from swmm_api.run_swmm.run_epaswmm import infer_swmm_path, get_swmm_version_base, get_swmm_version_epa

inp = read_inp_file('adjust_subcatchemnt_pattern.inp')
inp.force_convert_all()
fn_inp_temp = 'temp.inp'
inp.write_file(fn_inp_temp)
swmm5_run(fn_inp_temp)
delete_swmm_files(fn_inp_temp, including_inp=False)
exit()

inp = read_inp_file('/home/markus/PycharmProjects/swmm_api/examples/internal/2015_06_17_UG_Weiz_OPTI_maxAbk_Ret_3J_60_KW.inp')
# inp = read_inp_file('epaswmm5_apps_manual/Example7-Final.inp')

# inp.RAINGAGES

inp[SEC.RAINGAGES]['RainGage'].interval = '0:01'
inp[SEC.RAINGAGES]['RainGage'].set('interval', '0:01')
inp[SEC.RAINGAGES]['RainGage']['interval'] = '0:01'

print(inp[SEC.RAINGAGES]['RainGage'].to_inp_line())
exit()


complete_vertices(inp)

inp.write_file('temp.inp')
swmm5_run('temp.inp', swmm_path='C:\Program Files (x86)\EPA SWMM 5.1.015\swmm5.exe')

# import time
# t0 = time.perf_counter()
# print(infer_swmm_path())
# print(SWMM_PATH)
# print(get_swmm_version_epa())
# print(time.perf_counter() - t0)
