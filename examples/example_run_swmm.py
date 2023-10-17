from swmm_api.run_swmm import swmm5_run_progress, swmm5_run_epa

from swmm_api import CONFIG
CONFIG['exe_path'] = '/Users/markus/Nextcloud/SWMM/bin/mac/runswmm'

# swmm5_run_progress(r'C:\Users\mp\PycharmProjects\swmm_api\examples\temp1.inp')

swmm5_run_epa('./epaswmm5_apps_manual/Example6-Final.inp', init_print=True)