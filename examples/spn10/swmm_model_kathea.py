"""
alle relevanten Parameter, welche im inputfile hinzugefügt werden sollen:

[CONDUITS] (tags [unit])
;; Thickness [m]                 k_Pipe [W/m.K]                k_Soil [W/m.K]         specHcSoil [J/kg.K]           densitySoil  [kg/m3]       AirPattern [pattern]     SoilPattern  [pattern]    thermalEnergy  [K oder kW]

[STORAGE] (tags [unit])
;; Thickness [m]                 k_Pipe [W/m.K]                k_Soil [W/m.K]         specHcSoil [J/kg.K]           densitySoil  [kg/m3]       AirPattern [pattern]     SoilPattern  [pattern]
"""
from numpy import NaN
from swmm_api.input_file.sections import Conduit, Storage, Pattern, Pollutant, DryWeatherFlow
from swmm_api import read_inp_file
from swmm_api.input_file.section_labels import STORAGE, CONDUITS, POLLUTANTS, PATTERNS, DWF


class ConduitKathea(Conduit):
    def __init__(self, name, from_node, to_node, length, roughness, offset_upstream, offset_downstream, flow_initial, flow_max, Thickness,
                 k_Pipe, k_Soil, specHcSoil, densitySoil, AirPattern, SoilPattern, thermalEnergy=NaN):
        """

        Args:
            Thickness (): wall thickness
            k_Pipe (): thermal conductivity pipe (W/m.K)
            k_Soil (): thermal conductivity soil (W/m.K)
            specHcSoil (): specific heat capacity of surrounding soil (J/kg.K)
            densitySoil (): density of surrounding soil (kg/m³)
            AirPattern (): insewer-air pattern
            SoilPattern (): soil pattern
            thermalEnergy (): use of thermal energy (kW or °C)  unit is defined in OPTIONS
        """
        Conduit.__init__(self, name, from_node, to_node, length, roughness, offset_upstream, offset_downstream, flow_initial=flow_initial,
                         flow_max=flow_max)

        self.Thickness = Thickness
        self.k_Pipe = k_Pipe
        self.k_Soil = k_Soil
        self.specHcSoil = specHcSoil
        self.densitySoil = densitySoil
        self.AirPattern = AirPattern
        self.SoilPattern = SoilPattern
        self.thermalEnergy = thermalEnergy


class StorageKathea(Storage):
    def __init__(self, name, elevation, depth_max, depth_init, kind, *args, data=None, depth_surcharge=0, frac_evaporation=0,
                 Thickness=0, k_Pipe=0, k_Soil=0, specHcSoil=0, densitySoil=0, AirPattern=0, SoilPattern=0,
                 suction_head=NaN, hydraulic_conductivity=NaN, moisture_deficit_init=NaN):
        """

        Args:
            Thickness (float): wall thickness
            k_Pipe (float): thermal conductivity pipe (W/m.K)
            k_Soil (float): thermal conductivity soil (W/m.K)
            specHcSoil (float): specific heat capacity of surrounding soil (J/kg.K)
            densitySoil (float): density of surrounding soil (kg/m³)
            AirPattern (str): insewer-air pattern
            SoilPattern (str): soil pattern
        """
        self.name = str(name)
        self.elevation = float(elevation)
        self.depth_max = float(depth_max)
        self.depth_init = float(depth_init)
        self.kind = kind

        if args:
            if kind == Storage.TYPES.TABULAR:
                self._tabular_init(*args)

            elif kind == Storage.TYPES.FUNCTIONAL:
                self._functional_init(*args)

            elif kind in Storage.SHAPES._possible:
                self._shape_init(*args)

            else:
                raise NotImplementedError()
        else:
            self.data = data
            self._optional_args(depth_surcharge, frac_evaporation, Thickness, k_Pipe, k_Soil, specHcSoil, densitySoil, AirPattern, SoilPattern, suction_head, hydraulic_conductivity, moisture_deficit_init)

    def _kathea_args(self, Thickness=0, k_Pipe=0, k_Soil=0, specHcSoil=0, densitySoil=0, AirPattern=0, SoilPattern=0):
        self.Thickness = Thickness
        self.k_Pipe = k_Pipe
        self.k_Soil = k_Soil
        self.specHcSoil = specHcSoil
        self.densitySoil = densitySoil
        self.AirPattern = AirPattern
        self.SoilPattern = SoilPattern

    def _optional_args(self, depth_surcharge=0, frac_evaporation=0,
                       Thickness=None, k_Pipe=None, k_Soil=None, specHcSoil=None, densitySoil=None, AirPattern=None,
                       SoilPattern=None, suction_head=NaN, hydraulic_conductivity=NaN, moisture_deficit_init=NaN):
        self.depth_surcharge = float(depth_surcharge)
        self.frac_evaporation = float(frac_evaporation)
        self._kathea_args(Thickness, k_Pipe, k_Soil, specHcSoil, densitySoil, AirPattern, SoilPattern)
        self._exfiltration_args(suction_head, hydraulic_conductivity, moisture_deficit_init)


kathea_converter = {
    CONDUITS: ConduitKathea,
    STORAGE: StorageKathea,
}

if __name__ == '__main__':
    inp = read_inp_file('basic_model.inp')

    # -----------------------------------------------------
    # converting the conduits and extend the parameters
    for label, obj in inp[CONDUITS].items():
        inp[CONDUITS][label] = ConduitKathea(Thickness=0.18, k_Pipe=1.15, k_Soil=1.5, specHcSoil=1500, densitySoil=2000,
                                             AirPattern="A_GN", SoilPattern="S_GN_3.0", **obj.to_dict_())

    # -----------------------------------------------------
    # converting the storages and extend the parameters
    for label, obj in inp[STORAGE].items():
        inp[STORAGE][label] = StorageKathea(Thickness=0.18, k_Pipe=1.15, k_Soil=1.5, specHcSoil=1500, densitySoil=2000,
                                            AirPattern="A_GN", SoilPattern="S_GN_3.0", **obj.to_dict_())

    # -----------------------------------------------------
    # add temperature as a new pollutant
    if POLLUTANTS not in inp:
        inp[POLLUTANTS] = Pollutant.create_section()

    temperature = Pollutant(name="temperature", unit="CELSIUS", c_rain=0.0, c_gw=0.0, c_rdii=0.0, decay=0.0)
    inp[POLLUTANTS].add_obj(temperature)

    # -----------------------------------------------------
    # add temperature patterns
    if PATTERNS not in inp:
        inp[PATTERNS] = Pattern.create_section()

    T_Hourly = Pattern(name="T_Hourly", cycle=Pattern.CYCLES.HOURLY,
                       factors=[0.984, 0.977, 0.967, 0.957, 0.952, 0.951, 0.953, 0.964, 0.985, 1.011, 1.02, 1.03,
                                1.026, 1.021, 1.015, 1.007, 1.006, 1.007, 1.010, 1.034, 1.043, 1.037, 1.03, 1.01])
    T_Monthly = Pattern(name="T_Monthly", cycle=Pattern.CYCLES.MONTHLY,
                        factors=[0.64, 0.63, 0.67, 0.72, 1.0, 1.0, 1.0, 1.0, 0.978, 0.914, 0.812, 0.71])
    inp[PATTERNS].add_obj(T_Hourly)
    inp[PATTERNS].add_obj(T_Monthly)

    # -----------------------------------------------------
    # add temperature dry weather inflow
    old_dwf = inp[DWF].copy()
    for (node, type_), obj in old_dwf.items():
        new_dwf = DryWeatherFlow(node=node, constituent=temperature.name, base_value=18.95,
                                 pattern1=T_Hourly.name, pattern2=T_Monthly.name)
        inp[DWF].add_obj(new_dwf)

    # -----------------------------------------------------
    # save the new model
    inp.write_file('extended_model.inp', fast=False)

    # -----------------------------------------------------
    inp_kathea = read_inp_file('extended_model.inp', custom_converter=kathea_converter)
