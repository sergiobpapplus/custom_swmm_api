from swmm_api.input_file.macros.gis import convert_inp_to_geo_package

if __name__ == '__main__':
    inp = convert_inp_to_geo_package(inp_fn='epaswmm5_apps_manual/projects/Example1.inp',
                                     gpkg_fn='Example1.gpkg')
