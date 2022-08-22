import os

from examples.epaswmm5_apps_manual import PATH_EXAMPLES
from swmm_api import SwmmInput
from swmm_api.input_file import SEC
from swmm_api.input_file.macros.compare import compare_inp_objects
from swmm_api.input_file.macros.gis import write_geo_package, gpkg_to_swmm

if __name__ == '__main__':
    inp1 = SwmmInput('Example6-Final.inp')

    from swmm_api.input_file.macros import to_cross_section_maker

    cs = to_cross_section_maker(inp1.XSECTIONS['C3'], inp1)
    _ = cs.profile_figure()
    exit()
    # write_geo_package(inp1, gpkg_fn='Example6-Final.gpkg', driver='GPKG', label_sep='.', crs="EPSG:32633")

    inp2 = gpkg_to_swmm('Example6-Final.gpkg', infiltration_class=inp1._converter[SEC.INFILTRATION])

    for sec in inp1:
        if sec not in inp2:
            inp2[sec] = inp1[sec]

    print(compare_inp_objects(inp1, inp2))
