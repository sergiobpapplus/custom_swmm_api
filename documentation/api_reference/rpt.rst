==================
Report File Reader
==================
.. currentmodule:: swmm_api

Constructor
~~~~~~~~~~~
.. autosummary::
    :toctree: rpt/

    SwmmReport
    read_rpt_file


Unit Conversion
~~~~~~~~~~~~~~~
.. autosummary::
    :toctree: rpt/

    ~report_file.helpers.ReportUnitConversion


Errors and Warnings
~~~~~~~~~~~~~~~~~~~

.. list-table::

   * - :attr:`SwmmReport.get_warnings`
   * - :attr:`SwmmReport.get_errors`
   * - :attr:`SwmmReport.print_errors`
   * - :attr:`SwmmReport.print_warnings`


Simulation Info
~~~~~~~~~~~~~~~
.. list-table::

    * - :attr:`SwmmReport.analysis_options`
    * - :attr:`SwmmReport.analyse_start`
    * - :attr:`SwmmReport.analyse_end`
    * - :attr:`SwmmReport.analyse_duration`

Helpers
~~~~~~~
.. list-table::

    * - :attr:`SwmmReport.get_version_title`
    * - :attr:`SwmmReport.get_simulation_info`
    * - :attr:`SwmmReport.note`
    * - :attr:`SwmmReport.available_parts`

Unit
~~~~
.. list-table::

    * - :attr:`SwmmReport.flow_unit`
    * - :attr:`SwmmReport.unit`


Continuities
~~~~~~~~~~~~
.. list-table::

    * - :attr:`SwmmReport.runoff_quantity_continuity`
    * - :attr:`SwmmReport.flow_routing_continuity`
    * - :attr:`SwmmReport.quality_routing_continuity`
    * - :attr:`SwmmReport.runoff_quality_continuity`
    * - :attr:`SwmmReport.groundwater_continuity`


Numerics
~~~~~~~~
.. list-table::

    * - :attr:`SwmmReport.highest_continuity_errors`
    * - :attr:`SwmmReport.highest_flow_instability_indexes`
    * - :attr:`SwmmReport.time_step_critical_elements`

Summaries
~~~~~~~~~
.. list-table::

    * - :attr:`SwmmReport.element_count`
    * - :attr:`SwmmReport.conduit_surcharge_summary`
    * - :attr:`SwmmReport.cross_section_summary`
    * - :attr:`SwmmReport.flow_classification_summary`
    * - :attr:`SwmmReport.groundwater_summary`
    * - :attr:`SwmmReport.landuse_summary`
    * - :attr:`SwmmReport.lid_control_summary`
    * - :attr:`SwmmReport.lid_performance_summary`
    * - :attr:`SwmmReport.link_flow_summary`
    * - :attr:`SwmmReport.link_pollutant_load_summary`
    * - :attr:`SwmmReport.link_summary`
    * - :attr:`SwmmReport.node_depth_summary`
    * - :attr:`SwmmReport.node_flooding_summary`
    * - :attr:`SwmmReport.node_inflow_summary`
    * - :attr:`SwmmReport.node_summary`
    * - :attr:`SwmmReport.node_surcharge_summary`
    * - :attr:`SwmmReport.outfall_loading_summary`
    * - :attr:`SwmmReport.pollutant_summary`
    * - :attr:`SwmmReport.pumping_summary`
    * - :attr:`SwmmReport.rainfall_file_summary`
    * - :attr:`SwmmReport.raingage_summary`
    * - :attr:`SwmmReport.routing_time_step_summary`
    * - :attr:`SwmmReport.storage_volume_summary`
    * - :attr:`SwmmReport.subcatchment_runoff_summary`
    * - :attr:`SwmmReport.subcatchment_summary`
    * - :attr:`SwmmReport.subcatchment_washoff_summary`
    * - :attr:`SwmmReport.transect_summary`

Controls
~~~~~~~~
.. list-table::

    * - :attr:`SwmmReport.control_actions_taken`
