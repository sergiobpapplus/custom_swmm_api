from swmm_api import SwmmInput
from swmm_api.input_file.macros import remove_empty_sections

inp = SwmmInput.read_file('GisToSWMM5/demo_catchment/out/SWMM_in/demo_catchment_adap.inp')
remove_empty_sections(inp)
inp.write_file('demo_catchment_adap_py.inp', fast=False)

import geopandas as gpd

gdf = gpd.read_file('GisToSWMM5/demo_catchment/GIS/conduits.shp')

gdf.columns

from swmm_api.input_file.sections import Conduit

help(Conduit.__init__)

# name, from_node, to_node, length, roughness, offset_upstream=0, offset_downstream=0, flow_initial=0, flow_max=nan
# 'name', 'junc_in', 'junc_out', 'length', 'roughness', 'elev_in_of', 'elev_ou_of'
conduit_section = Conduit.create_section(gdf[['name', 'junc_in', 'junc_out', 'length', 'roughness', 'elev_in_of', 'elev_ou_of']].values)

inp2 = SwmmInput()
inp2.add_new_section(conduit_section)