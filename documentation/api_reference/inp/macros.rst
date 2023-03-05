Input File Manipulation - Macros
--------------------------------

Check
~~~~~

.. currentmodule:: swmm_api.input_file.macros.check
.. autosummary::
    :toctree: macros/

    check_for_nodes_old
    check_for_nodes
    check_for_duplicate_nodes
    check_for_duplicate_links
    check_for_duplicates
    check_for_subcatchment_outlets_old
    check_for_subcatchment_outlets
    check_for_curves
    check_outfall_connections

Collection
~~~~~~~~~~

.. currentmodule:: swmm_api.input_file.macros.collection
.. autosummary::
    :toctree: macros/

    nodes_dict
    nodes_subcatchments_dict
    links_dict
    subcatchments_per_node_dict

Compare
~~~~~~~

.. currentmodule:: swmm_api.input_file.macros.compare
.. autosummary::
    :toctree: macros/

    compare_sections
    compare_inp_files
    compare_inp_objects
    inp_version_control

Convert model
~~~~~~~~~~~~~

.. currentmodule:: swmm_api.input_file.macros.convert_model
.. autosummary::
    :toctree: macros/

    to_kinematic_wave

Convert object
~~~~~~~~~~~~~~

.. currentmodule:: swmm_api.input_file.macros.convert_object
.. autosummary::
    :toctree: macros/

    junction_to_divider
    junction_to_outfall
    junction_to_storage
    storage_to_outfall
    conduit_to_orifice

Cross section curve
~~~~~~~~~~~~~~~~~~~

.. currentmodule:: swmm_api.input_file.macros.cross_section_curve
.. autosummary::
    :toctree: macros/

    get_cross_section_maker
    to_cross_section_maker
    profil_area

Curve
~~~~~

.. currentmodule:: swmm_api.input_file.macros.curve
.. autosummary::
    :toctree: macros/

    curve_figure

Edit
~~~~

.. currentmodule:: swmm_api.input_file.macros.edit
.. autosummary::
    :toctree: macros/

    delete_node
    move_flows
    reconnect_subcatchments
    delete_link
    delete_subcatchment
    split_conduit
    combine_vertices
    combine_conduits
    combine_conduits_keep_slope
    dissolve_conduit
    rename_node
    rename_link
    rename_subcatchment
    rename_timeseries
    flip_link_direction
    remove_quality_model
    delete_pollutant

Filter
~~~~~~

.. currentmodule:: swmm_api.input_file.macros.filter
.. autosummary::
    :toctree: macros/

    filter_tags
    filter_nodes
    filter_links_within_nodes
    filter_links
    filter_subcatchments
    create_sub_inp

Geo
~~~

.. currentmodule:: swmm_api.input_file.macros.geo
.. autosummary::
    :toctree: macros/

    transform_coordinates
    complete_link_vertices
    complete_vertices
    reduce_vertices
    simplify_link_vertices
    simplify_vertices

Gis
~~~

.. currentmodule:: swmm_api.input_file.macros.gis
.. autosummary::
    :toctree: macros/

    set_crs
    convert_inp_to_geo_package
    write_geo_package
    get_subcatchment_connectors
    links_geo_data_frame
    nodes_geo_data_frame
    gpkg_to_swmm
    update_length
    update_area

Graph
~~~~~

.. currentmodule:: swmm_api.input_file.macros.graph
.. autosummary::
    :toctree: macros/

    inp_to_graph
    get_path
    get_path_subgraph
    next_nodes
    previous_nodes
    next_links_labels
    next_links
    previous_links_labels
    previous_links
    links_connected
    number_in_out
    downstream_nodes
    upstream_nodes
    subcatchments_connected
    get_network_forks
    split_network
    conduit_iter_over_inp

Macros
~~~~~~

.. currentmodule:: swmm_api.input_file.macros.macros
.. autosummary::
    :toctree: macros/

    find_node
    find_link
    calc_slope
    conduit_slopes
    conduits_are_equal
    update_no_duplicates
    increase_max_node_depth
    set_times
    combined_subcatchment_frame
    combined_nodes_frame
    nodes_data_frame
    iter_sections
    delete_sections
    set_absolute_file_paths

Plotting longitudinal
~~~~~~~~~~~~~~~~~~~~~

.. currentmodule:: swmm_api.input_file.macros.plotting_longitudinal
.. autosummary::
    :toctree: macros/

    get_longitudinal_data
    get_water_level
    iter_over_inp_
    iter_over_inp
    get_node_station
    set_zero_node
    plot_longitudinal
    animated_plot_longitudinal

Plotting map
~~~~~~~~~~~~

.. currentmodule:: swmm_api.input_file.macros.plotting_map
.. autosummary::
    :toctree: macros/

    get_matplotlib_colormap
    get_color_mapper
    custom_color_mapper
    get_discrete_colormap
    set_inp_dimensions
    init_empty_map_plot
    get_auto_size_function
    add_link_map
    add_subcatchment_map
    add_node_map
    add_node_labels
    plot_map
    add_custom_legend
    add_backdrop

Reduce unneeded
~~~~~~~~~~~~~~~

.. currentmodule:: swmm_api.input_file.macros.reduce_unneeded
.. autosummary::
    :toctree: macros/

    reduce_curves
    reduce_pattern
    reduce_controls
    simplify_curves
    reduce_raingages
    remove_empty_sections
    reduce_timeseries

Split inp file
~~~~~~~~~~~~~~

.. currentmodule:: swmm_api.input_file.macros.split_inp_file
.. autosummary::
    :toctree: macros/

    split_inp_to_files
    read_split_inp_file

Summarize
~~~~~~~~~

.. currentmodule:: swmm_api.input_file.macros.summarize
.. autosummary::
    :toctree: macros/

    print_summary

Tags
~~~~

.. currentmodule:: swmm_api.input_file.macros.tags
.. autosummary::
    :toctree: macros/

    get_node_tags
    get_link_tags
    get_subcatchment_tags
    filter_tags
    delete_tag_group
