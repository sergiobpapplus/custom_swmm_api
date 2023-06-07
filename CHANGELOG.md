# Changelog

<!--next-version-placeholder-->

## v0.4.22 (2023-06-07)
### Fix
* Added function for adding layers to LIDcontrol ([`d31a3d2`](https://gitlab.com/markuspichler/swmm_api/-/commit/d31a3d296325b02c01255fb790f18f7e2289cc05))

## v0.4.21 (2023-05-04)
### Fix
* Set back to default locale in timeseries data converter ([`56d1af7`](https://gitlab.com/markuspichler/swmm_api/-/commit/56d1af71beb4a704a72c5ff9963c98498d38a6e5))
* Optional show progressbar in compare_inp_files ([`d2661f2`](https://gitlab.com/markuspichler/swmm_api/-/commit/d2661f2aabd6cd826a28370881ddc3ffbe8dde0c))

## v0.4.20 (2023-04-17)
### Fix
* Fixed errors in the `Control` object implementation. `actions` attribute is now split into `actions_if` and `actions_else`. Actions don't need the parameter `logic`. ([`2aa71a9`](https://gitlab.com/markuspichler/swmm_api/-/commit/2aa71a90427e978baf8af0736f065bc908fa2062))

## v0.4.19 (2023-04-13)
### Fix
* Weir road surface parameter not used, was a string, now its a nan and will not be written into the new inp file. ([`25d665b`](https://gitlab.com/markuspichler/swmm_api/-/commit/25d665bb46a2bfc4c82a4446bc590f3b92a58f88))

## v0.4.18 (2023-04-08)
### Fix
* Raise error when swmm run failed with owa swmm ([`0aa9743`](https://gitlab.com/markuspichler/swmm_api/-/commit/0aa97438c32bcdb20358ebf8bc16dc5b7ff970b4))
* Optimize polygon import for large models ([`52d1f53`](https://gitlab.com/markuspichler/swmm_api/-/commit/52d1f53c0bd5d99ce8a0bbf5a0006c2e6099b87f))

### Documentation
* Extended the testing swmm inp model ([`39c08f2`](https://gitlab.com/markuspichler/swmm_api/-/commit/39c08f23a72c6bf538dc030fb017b92a6d75ea1d))
* Update out file example ([`cdbce04`](https://gitlab.com/markuspichler/swmm_api/-/commit/cdbce04384007dc6dba8d532fa0914c0d53360b0))
* Update out file example ([`d746ce3`](https://gitlab.com/markuspichler/swmm_api/-/commit/d746ce39bab919273b42390e635d265febd504fb))

## v0.4.17 (2023-04-06)
### Fix
* Added rainfall_dependent_ii, street_flow_summary, shape_summary and street_summary as property to the SwmmReport class ([`70ff5aa`](https://gitlab.com/markuspichler/swmm_api/-/commit/70ff5aa3b044a670447d1d8d754d65c8a062bbaf))

## v0.4.16 (2023-04-04)
### Fix
* Added to_parquet_chunks for SwmmOutput to write parquet files in chunks to prevent out of memory error for huge out files. ([`6ac200b`](https://gitlab.com/markuspichler/swmm_api/-/commit/6ac200b74b51f216d564adffaae3e8f52e994e66))

### Documentation
* Polygon size is limited in gui ([`68b84dc`](https://gitlab.com/markuspichler/swmm_api/-/commit/68b84dc20bd54bcef6ef97575845f5948f81e270))

## v0.4.15 (2023-03-28)
### Fix
* Run swmm in temporary folder and get results ([`e79b355`](https://gitlab.com/markuspichler/swmm_api/-/commit/e79b355bff1732022e1aa3d36a8fa230ed66790a))

## v0.4.14 (2023-03-27)
### Fix
* Enhanced swmm exe search ([`1401b56`](https://gitlab.com/markuspichler/swmm_api/-/commit/1401b568599beaee9bfdae6ccd72089ed9c92f27))
* Error due to locale in combine dw-flows ([`d118b3b`](https://gitlab.com/markuspichler/swmm_api/-/commit/d118b3be4e5e3dfe91b857231990d5ad4ce49d0f))

## v0.4.13 (2023-03-27)
### Fix
* Finding correct swmm executable ([`3a8301f`](https://gitlab.com/markuspichler/swmm_api/-/commit/3a8301f713c789985ff918cf19924ea91c1b4569))
* Setting locale with macOS for timeseries date format conversion ([`e55c1ff`](https://gitlab.com/markuspichler/swmm_api/-/commit/e55c1ff86752591f4b1cf1b3453a39d3c30f13c0))

## v0.4.12 (2023-03-24)
### Fix
* Input_file.macros.move_flows now takes the pattern of the dominant node ([`bf6612a`](https://gitlab.com/markuspichler/swmm_api/-/commit/bf6612a98f400346017a266fe7dcd699448c7eee))

## v0.4.11 (2023-03-14)
### Fix
* Timeseries conversion when locale is not english ([`1cd934e`](https://gitlab.com/markuspichler/swmm_api/-/commit/1cd934ef29507112d93ee2feeee78c7b9f3e0c23))
* Wrong identifies in Groundwater object ([`347b0a2`](https://gitlab.com/markuspichler/swmm_api/-/commit/347b0a20f922540d5a2e727b4d6c7198ddd63c77))
* Added function swmm_api.input_file.macros.get_downstream_path ([`dca930b`](https://gitlab.com/markuspichler/swmm_api/-/commit/dca930b7a7906e08c8fe5b6d962d2174d6be99b5))

### Documentation
* Extended gis to swmm example ([`4051127`](https://gitlab.com/markuspichler/swmm_api/-/commit/4051127550eff2c750e2c6a26d0a36e6125678af))
* Swmm5_run_epa function: paths as string or Path ([`0e7eceb`](https://gitlab.com/markuspichler/swmm_api/-/commit/0e7eceb91a250c094c2987c6b4bceccf88210d01))
* Extended gis to swmm example ([`202dab8`](https://gitlab.com/markuspichler/swmm_api/-/commit/202dab87e478f89719deff861c622ae1e2d86c21))

## v0.4.10 (2023-03-13)
### Fix
* Error with function SwmmInput.check_for_section [Issue #6](https://gitlab.com/markuspichler/swmm_api/-/issues/6) ([`ddeb730`](https://gitlab.com/markuspichler/swmm_api/-/commit/ddeb730d4782b999653c445e3f39e6a638c3a50f))

## v0.4.9 (2023-03-09)
### Fix
* Added option to not show progressbar in selective out-file reader ([`ea8b666`](https://gitlab.com/markuspichler/swmm_api/-/commit/ea8b6667f1ebb8944f10db9056e19f90a3e86910))

## v0.4.8 (2023-03-09)
### Fix
* Added InpSectionDummy and DummySectionObject classes for unknown sections in the inp-file ([`1949f6a`](https://gitlab.com/markuspichler/swmm_api/-/commit/1949f6ac43e4e445e2e229c78aba64562f3115bc))
* Added setter for OPTIONS section ([`d361916`](https://gitlab.com/markuspichler/swmm_api/-/commit/d361916f5249da5dd32ad74ec5d12d7e647eb72c))
* Inlet object was broken in the reader ([`9a08149`](https://gitlab.com/markuspichler/swmm_api/-/commit/9a08149c1565a68055a2b84c49c9b5661f7dc6e5))
* Added swmm-version to CONFIG for syntax differences in inp-file creation ([`8c08851`](https://gitlab.com/markuspichler/swmm_api/-/commit/8c0885109eda84e31b5664a5a633b2f82b4d8a63))

### Documentation
* Added example for custom inp section ([`f797dac`](https://gitlab.com/markuspichler/swmm_api/-/commit/f797dac6bbe25018c264a81ef2fc357db8be8110))

## v0.4.7 (2023-03-08)
### Fix
* Added lost swmm 5.2 sections to input converter ([`7249f72`](https://gitlab.com/markuspichler/swmm_api/-/commit/7249f72eeb6eb934fc53ad760818feaf9243c5aa))

## v0.4.6 (2023-03-07)
### Fix
* Added config for path to default swmm exe ([`2807d8f`](https://gitlab.com/markuspichler/swmm_api/-/commit/2807d8f68842fcddbd397614c39411dee088b81d))
* Raise FileNotFoundError when file is not available ([`4ae6dd1`](https://gitlab.com/markuspichler/swmm_api/-/commit/4ae6dd15f733051f7099309445298b616f9e9967))

## v0.4.5 (2023-03-05)
### Fix
* Add gis_decimals to swmm-api-config ([`c85aeba`](https://gitlab.com/markuspichler/swmm_api/-/commit/c85aeba364bc14ff730c01461b1478a01a829904))

### Documentation
* Fixed doc creation ([`d32cde3`](https://gitlab.com/markuspichler/swmm_api/-/commit/d32cde3184e098055a025b55d03932e561199050))

## v0.4.4 (2023-03-03)
### Fix
* Added macro `subcatchments_connected` ([`8fa7dc9`](https://gitlab.com/markuspichler/swmm_api/-/commit/8fa7dc94e96a97f940fc8fd3769b288547c48982))

### Documentation
* Minor doc fixes ([`081205d`](https://gitlab.com/markuspichler/swmm_api/-/commit/081205d454901b5e2a41d0c6ee2e22a91ea047d6))
* Minor doc fixes ([`059902c`](https://gitlab.com/markuspichler/swmm_api/-/commit/059902c5d0fa06b73354354958fd87ca1706d027))
* Enhanced doc build ([`ff09a2d`](https://gitlab.com/markuspichler/swmm_api/-/commit/ff09a2deef68f94590675f84e92ae75af09e50df))

## v0.4.3 (2023-02-24)
### Fix
* Added setter to OptionSection ([`3d927ce`](https://gitlab.com/markuspichler/swmm_api/-/commit/3d927cec2e85333e36fea6a20986b67f491aec79))
* Fixed wrong outfile data index ([`34f7350`](https://gitlab.com/markuspichler/swmm_api/-/commit/34f735034d694af54b3f6580271a727080995526))
* Fixed wrong outfile data index ([`aebc9e5`](https://gitlab.com/markuspichler/swmm_api/-/commit/aebc9e50993ee1b76e58b5d8dc18982e217b2095))
* Added function write_calibration_files ([`b2f52e6`](https://gitlab.com/markuspichler/swmm_api/-/commit/b2f52e6d93b32a26bfe235376d555c6b8c60306c))
* Added function animated_plot_longitudinal ([`f19915e`](https://gitlab.com/markuspichler/swmm_api/-/commit/f19915ebcd7df9a7eba5b27cc2c84486950231ab))

### Documentation
* Inp write file also possible as Path-type ([`f327d55`](https://gitlab.com/markuspichler/swmm_api/-/commit/f327d557d31d6b74f4825d6600856bc937880c32))

## v0.4.2 (2023-02-15)
### Fix
* Input-file class copy function also copies the converter classes, the encoding and the section ordering ([`03ad15b`](https://gitlab.com/markuspichler/swmm_api/-/commit/03ad15b9eb742609dbd308dacf35604eaadfb905))
* Owa-swmm-api only takes string for the input-filename ([`31ebf60`](https://gitlab.com/markuspichler/swmm_api/-/commit/31ebf603ac22bce95c8b755ed4e049d374bc2d9a))

## v0.4.1 (2023-02-13)
### Fix
* Inp_to_graph adds now the swmm-objects to the graph object ([`444fb4f`](https://gitlab.com/markuspichler/swmm_api/-/commit/444fb4fb3957bab2964aed12898ec855d1f00ccd))
* Improvements for delete_node(), move_node(), reconnect_subcatchments(), combine_conduits() ([`9a81ba9`](https://gitlab.com/markuspichler/swmm_api/-/commit/9a81ba9216b36c49bc784f2d7654a25cfb961dd1))
* Remove empty sections before gis export ([`6a244c7`](https://gitlab.com/markuspichler/swmm_api/-/commit/6a244c73fd0cba47dbfc557ef2c69e6f93ce1738))
* Get_result_filename accepts now a `Path` as parameter ([`6f78982`](https://gitlab.com/markuspichler/swmm_api/-/commit/6f78982711b44dfba3d84df4926d0acbf90efe6a))
* Pyswmm only takes string for the input-filename ([`82603c7`](https://gitlab.com/markuspichler/swmm_api/-/commit/82603c7a57b15041692bfc1176816871239156f3))

### Documentation
* Allow path and string ([`ff62215`](https://gitlab.com/markuspichler/swmm_api/-/commit/ff6221565add779d1cf0eced9fd4d06b5dbefa43))
* Minor documentation fixes ([`adf4d9b`](https://gitlab.com/markuspichler/swmm_api/-/commit/adf4d9bf9aa8a71baa3219f896d24c9c02588292))

## v0.4.0 (2023-02-10)
### Feature
* Adding warning to out-file-reader when request is not found. ([`baaaa58`](https://gitlab.com/markuspichler/swmm_api/-/commit/baaaa583832a462d9f004d538a8928cd364b924b))
* Ability to set global default encoding for reading inp, out, and report files. ([`8365ba8`](https://gitlab.com/markuspichler/swmm_api/-/commit/8365ba85dd272fd229c8dc53da867c9000efdde5))

### Documentation
* New docker image for the website generation ([`6333ccc`](https://gitlab.com/markuspichler/swmm_api/-/commit/6333ccca6fbd7d6f4286e7fc574a687936b00308))
* Into + joss-paper ([`2bacb27`](https://gitlab.com/markuspichler/swmm_api/-/commit/2bacb279c1ca6cb2b51f0b04f8b1a4f238b5c26c))
* Typo ([`2f35161`](https://gitlab.com/markuspichler/swmm_api/-/commit/2f35161aeb42dc68a5af2c76aff8495351e53826))
* Typo ([`cbc9f3a`](https://gitlab.com/markuspichler/swmm_api/-/commit/cbc9f3a824aa41b98f44ade7d4e705a53126aee5))
* Changes in readme ([`3a240b6`](https://gitlab.com/markuspichler/swmm_api/-/commit/3a240b6440fbae9f87d5fad97a0ce2f24af988e6))
* Changes in readme ([`cea2da5`](https://gitlab.com/markuspichler/swmm_api/-/commit/cea2da5fc3bc43cf5855cf1b8e458bdb6a217c28))
* Changes in readme ([`9b069dd`](https://gitlab.com/markuspichler/swmm_api/-/commit/9b069ddf966f7ad3e22f32cfade10a1b658369e1))
* Added reference to readme ([`6da8f41`](https://gitlab.com/markuspichler/swmm_api/-/commit/6da8f411fd90d51eccecb5386365f9977bdaabd4))
* Typo in readme ([`255132f`](https://gitlab.com/markuspichler/swmm_api/-/commit/255132f92eefc6b2f35c191654a09ba8a73aa061))

## v0.3.3 (2023-02-03)

### Fix

* Added keyword arguments to control condition and action init ([`bf1ad7a`](https://gitlab.com/markuspichler/swmm_api/-/commit/bf1ad7a166002e2562831f64332c12a8075b7ace))

### Documentation

* Tutorial How to add control rules ([`0ca1d9c`](https://gitlab.com/markuspichler/swmm_api/-/commit/0ca1d9cef327c18d5447af8db977b179c1310668), [`b8d652f`](https://gitlab.com/markuspichler/swmm_api/-/commit/b8d652f02402f56d9cf0c3948014bf998296b076), [`9442147`](https://gitlab.com/markuspichler/swmm_api/-/commit/9442147211cbed03fbb45a3a6b0489a317ed8659))
* Adding example to import gis data ([`e2c148e`](https://gitlab.com/markuspichler/swmm_api/-/commit/e2c148e5eb35dbf93ddc759aed6b325cb49eb66c))
* Adding publications mentioning swmm-api to readme ([`4d209ab`](https://gitlab.com/markuspichler/swmm_api/-/commit/4d209aba439ae3d1cc55bcbe6b5613743441ac6d))

### Style

* matplotlib constrained layout

## v0.3.2 (2023-01-09)

### Fix

* Added ability to set * as offset for "offset measured as elevation"-option. ([`6994640`](https://gitlab.com/markuspichler/swmm_api/-/commit/699464091dacfc67283a7ea7b6a84bee8d105e8f))
* case insensitive string comparison for type convertion of "YES", "NO" and "NONE"
* infer_offset_elevation function (only internal)

### Documentation

* added warning in readme
* added some icons to headers
* capital letter at beginning

## v0.3.1 (2022-12-16)

### Fix

* Ci-test ([`189d64c`](https://gitlab.com/markuspichler/swmm_api/-/commit/189d64c958426679339cfb781b7fd64755647931))

### added

* get_geo_length to Vertices object
* possibility to set path as a pathlib.Path-object
* parameter for minimum length to simplify vertices function 

## 0.3.post3 (Nov 21, 2022)

### Fix

- HotstartFileReader fixed if not all sections in .inp-file

## 0.3.post2 (Oct 18, 2022)

### Fix

- added needed package data-file

## 0.3.post1 (Oct 17, 2022)

### changed

- running swmm functions are reordered
- internal package structure

### added

- reading .rpt-file with encoding

## 0.3 (Sep 06, 2022)

### removed

- CoordinatesGeo (functionality included in Coordinate)
- VerticesGeo (functionality included in Vertices)
- PolygonGeo (functionality included in Polygon)
- SwmmInputGeo (functionality included in SwmmInput)

### changed

- SwmmInput init is equal to SwmmInput.read_file
- better repr for SwmmInput and InpSections
- map plot function is separated in several function for better customization

### new

- swmm_api.input_file.macros.compare_inp_objects()
- add_backdrop to map plot
- Astlingen model in examples
- Examples for SNP10 conference
- get_used_curves
- check_outfall_connections
- detect_encoding for reading the inp-file and the rpt-file (default=utf-8)
- SwmmInput.read_text
- read out file as buffer
- input_file.macros.update_area
- error message when swmm is not found

### Fix

- inp update error
- minor issues with GIS import end export
- sort warnings in report by natural order
- minor issues with SwmmReport
- issue with networkx with parallel links
- possibility to have multiple times the same section in the inp-file
- swmm error when inline timeseries is on the end of the file
- error in controls
- error in timerseries, for specific orders

An error will be raised when calling a geo-function and the proper packages are not installed.

Renamed every parameter of the base Objects of the inp-sections.
The reason for the renaming is that the naming was previously very inconsistent and did not comply with the pip-standard.

## 0.2.0.18.3 (Mar 01, 2022)

Minor fixes
Fixed Error when using Timeseries past the year 3000.

## 0.2.0.18 (Feb 22, 2022)

### Fix

- type in swmm_api.input_file.macros.collection.subcachtment_nodes_dict > subcatchment_nodes_dict
- copy error for swmm_api.input_file.sections.lid.LIDControl, swmm_api.input_file.sections.others.Hydrograph, SnowPack
- reduce_controls now works
- error when reading a RDII
- infiltration object type recognition
- error when reading the report section "routing time step summary"

### renamed
- in swmm_api.input_file.macros.collection subcatchment_nodes_dict to subcatchments_per_node_dict

### added
- function swmm_api.input_file.macros.edit.remove_quality_model
- swmm_api.input_file.section_list.POLLUTANT_SECTIONS
- missing report sections
- swmm_api.input_file.macros.check.check_for_subcatchment_outlets
- swmm_api.input_file.macros.collection.nodes_subcatchments_dict
- InpSection and InpSectionGeneric have now _label for the section label
- add_new_section to SwmmInput
- SwmmInputGeo as alias of SwmmInput with geo_section_converter as custom_converter
- example for sorting in the inp-file-writer
- possibility to turn off sorting in inp-file write_file (`sort_objects_alphabetical=False`)
- SwmmHotstart file reader

### moved
- SEC from swmm_api.input_file.section_abr to swmm_api.input_file

### improved
- performance for reading bis inp-files
- natural sorting for objects. (i.e. the object names \[J1, J2, J10\] were previously sorted as  \[J1, J10, J2\])
- sections will be sorted as in the read file
- default sorting is based on sorting of the EPA SWMM GUI / PCSWMM
- copy unconverted inp file as string

### changed
- in swmm_api.input_file.macros.check the functions check_for_nodes, check_for_duplicates now return set of error and don't print
- BaseSectionObject are now hashable
- Control object has now objects as action and condition for better usability


## 0.2.0.17 (Feb 11, 2022)
### fixed
- error in copy Pollutant
- error in TimeseriesData when datetime is a float

### renamed
- in swmm_api.input_file.macros.geo update_vertices to complete_vertices 

### added
- swmm_api.input_file.macros.edit.flip_link_direction
- swmm_api.input_file.macros.geo.complete_link_vertices
- swmm_api.input_file.macros.geo.simplify_link_vertices
- swmm_api.input_file.macros.geo.simplify_vertices
- automatic creation for sections when getter is called and not in inp-data

### moved
- reduce_vertices from swmm_api.input_file.macros.reduce_unneeded to geo

## 0.2.0.16 (Jan 7, 2022)
- moved predefined output file variables (VARIABLES, OBJECTS) to swmm_api.output_file.definitions
- new functions:
- swmm_api.input_file.macros.iter_sections
- swmm_api.input_file.macros.delete_sections
- added functions `add_obj` and `add_multiple` to SwmmInput object
- added function `delete_tag_group` to delete tags for specific objects i.e. all node tags
- `SEC` as reference for inp-sections
- remove ignore_sections, convert_sections and ignore_gui_sections parameters of swmm_api.SwmmInput.read_file
  - sections with be converted wenn needed.
- added function
  - SwmmInput.force_convert_all()
- added `SUBCATCHMENT_SECTIONS` to `swmm_api.input_file.section_lists`
- 

## 0.2.0.15 (Nov 19, 2021)
- added functions in swmm_api.input_file.macros.*
- added documentation for marcos
- minor changes

## 0.2.0.14 (Nov 11, 2021)
- New `TITLE` Section `TitleSection` based on `UserString`
- Default Infiltration based on `OPTIONS` - `INFILTRATION` parameter (function: `SwmmInput.set_default_infiltration`)
- added `InpSection.set_parent_inp` and `InpSection.get_parent_inp` to InpSections

## 0.2.0.13 (Oct 21, 2021)
- SwmmOutExtract.get_selective_results small performance boost
- new function: update_length
- updated and add example files
- resorted macros
- added macros with package `SWMM_xsections_shape_generator`
- added Summary tables to SwmmReport reader
- fixed some issued with SwmmReport
- new function: `check_for_duplicates`

## 0.2.0.12 (Sep 28, 2021)
- fixed out reader for custom pollutant unit
- gis import example
- LINK_SECTIONS, NODE_SECTIONS as section list
- SnowPack as new Class for reader
- datetime format fixed for import and export
- new "check_for_duplicates" macro
- fixed run for linux
- new get_swmm_version function
- pyswmm runner (not stable)
- fixed docker for documentation site

## 0.2.0.6 (Sep 15, 2021)
- better gis export
- compare inp files
- macro documentations

## 0.2.0.5 (Sep 10, 2021)
- gis export of all nodes, links as separate function
- added subcatchment connector to gis export
- added inp write and inp to string to SwmmInput class
- abstract class for nodes and links

## 0.2.0.4 (May 27, 2021)

- fixed errors when object labels start with a number
- rewritten out-file-reader

## 0.2.0.3 (May 18, 2021)

- fixed errors when `-nan(ind)` in report file

## 0.2.0.2 (May 5, 2021)

- added polygons to transform coordinated function
- added geopandas_to_polygons
- fixed some documentation errors
- fixed tag error (spaces in tag)
- fixed undefined types in some objects
- added function "add_inp_lines" to add a collection of lines to an existing section
- set default of "ignore_gui_sections" in "SwmmInput.read_file" to False
- added "delete_subcatchment" to macros
- fixed faulty tag filter in filter_nodes/_links/_subcatchments

## 0.2 (Apr 6, 2021)

## 0.1a25  (Apr 1, 2021)

## 0.1a24  (Mar 30, 2021)

## 0.1a23  (Feb 19, 2021)

## 0.1a22  (Dec 15, 2020)

## 0.1a21  (Nov 18, 2020)

Changes Including:
- 0.1a20  (Nov 9, 2020)
- 0.1a19  (Nov 6, 2020)
- 0.1a18  (Nov 6, 2020)

## 0.1a17  (Oct 16, 2020)

Changes Including:
- 0.1a16  (Sep 30, 2020)
- 0.1a15  (Sep 24, 2020)
- 0.1a14  (Sep 23, 2020)
- 0.1a13  (Sep 23, 2020)
- 0.1a12  (Sep 23, 2020)
- 0.1a11  (Sep 14, 2020)

## 0.1a10  (Aug 27, 2020)

Changes Including:
- 0.1a9  (Aug 27, 2020)

## 0.1a8  (Apr 19, 2020)

Changes Including:
- 0.1a7  (Apr 19, 2020)

## 0.1a6  (Nov 13, 2019)

Changes Including:
- 0.1a5  (Nov 8, 2019)
- 0.1a4  (Nov 4, 2019)
- 0.1a3  (Oct 28, 2019)
- 0.1a2  (Oct 3, 2019)
- 0.1a0  (Oct 2, 2019)