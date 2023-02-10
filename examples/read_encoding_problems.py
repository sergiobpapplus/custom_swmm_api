from swmm_api import SwmmReport, SwmmInput, SwmmOutput, SwmmHotstart
from swmm_api.run_swmm import get_result_filenames

from swmm_api import CONFIG
# CONFIG['encoding'] = 'iso-8859-1'

# fn_inp = 'inp_test_encoding_iso-8859-1.inp'
fn_inp = 'inp_test_encoding_utf-8.inp'

fn_rpt, fn_out = get_result_filenames(fn_inp)
# fn_hst = fn_inp.replace('.inp', '.hst')

inp = SwmmInput(fn_inp)
rpt = SwmmReport(fn_rpt)
out = SwmmOutput(fn_out)
# hst = SwmmHotstart(fn_hst, inp)

print()
