# Example for custom input-file sections
# Based on the new extended section introduced with SWMM 5.2
from numpy import NaN

from swmm_api import SwmmInput
from swmm_api.input_file.helpers import BaseSectionObject
from swmm_api.input_file.sections._identifiers import IDENTIFIERS


STREET = 'STREET'  # cross-section geometry for street conduits | new in SWMM 5.2
INLETS = 'INLETS'  # design data for storm drain inlets | new in SWMM 5.2
INLET_USAGE = 'INLET_USAGE'  # assignment of inlets to street and channel conduits | new in SWMM 5.2


class Street(BaseSectionObject):
    """
    Cross-section geometry for street conduits.

    Section:
        [STREETS]

    Purpose:
        Describes the cross-section geometry of conduits that represent streets.

    Attributes:
        name(str): Name assigned to the street cross-section.
        width_crown (float): Distance from street’s curb to its crown (ft or m).
        height_curb (float): Curb height (ft or m).
        slope (float): Street cross slope (%).
        n_road (float): Manning’s roughness coefficient (n) of the road surface.
        depth_gutter (float | optional): Gutter depression height (in or mm) (default = 0).
        width_gutter (float | optional): Depressed gutter width (ft or m) (default = 0).
        sides (int | optional): 1 for single sided street or 2 for two-sided street (default = 2).
        width_backing (float | optional): Street backing width (ft or m) (default = 0).
        slope_backing (float | optional): Street backing slope (%) (default = 0).
        n_backing (float | optional): Street backing Manning’s roughness coefficient (n) (default = 0).

    Remarks:
        If the street has no depressed gutter (a = 0) then the gutter width entry is ignored. If the
        street has no backing then the three backing parameters can be omitted.
    """
    _identifier = IDENTIFIERS.name
    _table_inp_export = True
    _section_label = STREET

    def __init__(self, name, width_crown, height_curb, slope, n_road, depth_gutter=0, width_gutter=0, sides=2,
                 width_backing=0, slope_backing=0, n_backing=0):
        """
        Cross-section geometry for street conduits.

        Args:
            name(str): Name assigned to the street cross-section.
            width_crown (float): Distance from street’s curb to its crown (ft or m).
            height_curb (float): Curb height (ft or m).
            slope (float): Street cross slope (%).
            n_road (float): Manning’s roughness coefficient (n) of the road surface.
            depth_gutter (float | optional): Gutter depression height (in or mm) (default = 0).
            width_gutter (float | optional): Depressed gutter width (ft or m) (default = 0).
            sides (int | optional): 1 for single sided street or 2 for two-sided street (default = 2).
            width_backing (float | optional): Street backing width (ft or m) (default = 0).
            slope_backing (float | optional): Street backing slope (%) (default = 0).
            n_backing (float | optional): Street backing Manning’s roughness coefficient (n) (default = 0).
        """
        self.name = str(name)
        self.width_crown = float(width_crown)
        self.height_curb = float(height_curb)
        self.slope = float(slope)
        self.n_road = float(n_road)
        self.depth_gutter = float(depth_gutter)
        self.width_gutter = float(width_gutter)
        self.sides = int(sides)
        self.width_backing = float(width_backing)
        self.slope_backing = float(slope_backing)
        self.n_backing = float(n_backing)


class Inlet(BaseSectionObject):
    """
    Design data for storm drain inlets.

    Section:
        [INLETS]

    Purpose:
        Defines inlet structure designs used to capture street and channel flow that are sent to below
        ground sewers.

    Format:
        ::

            Name GRATE/DROP_GRATE Length Width Type (Aopen Vsplash)
            Name CURB/DROP_CURB Length Height (Throat)
            Name SLOTTED Length Width
            Name CUSTOM Dcurve/Rcurve

    Parameters:
        name (str): name assigned to the inlet structure.
        length (float): length of the inlet parallel to the street curb (ft or m).
        width (float): width of a GRATE or SLOTTED inlet (ft or m).
        height (float): height of a CURB opening inlet (ft or m).
        grate_type (str): type of GRATE used (see below).
        area_open (float): fraction of a GENERIC grate’s area that is open.
        velocity_splash (float): splash over velocity for a GENERIC grate (ft/s or m/s).
        throat_angle (str): the throat angle of a CURB opening inlet (HORIZONTAL, INCLINED or VERTICAL).
        curve (str): one of:
            - name of a Diversion-type curve (captured flow v. approach flow) for a CUSTOM inlet.
            - name of a Rating-type curve (captured flow v. water depth) for a CUSTOM inlet.

    Remarks:
        See Section 3.3.7 for a description of the different types of inlets that SWMM can model.

        Use one line for each inlet design except for a combination inlet where one GRATE line
        describes its grated inlet and a second CURB line (with the same inlet name) describes its curb
        opening inlet.

        GRATE, CURB, and SLOTTED inlets are used with STREET conduits, DROP_GRATE and
        DROP_CURB inlets with open channels, and a CUSTOM inlet with any conduit.

        GRATE and DROP_GRATE types can be any of the following:

            - ``P_BAR``-50: Parallel bar grate with bar spacing 17⁄8” on center
            - ``P_BAR``-50X100: Parallel bar grate with bar spacing 17⁄8” on center and 3⁄8” diameter lateral rods spaced at 4” on center
            - ``P_BAR``-30: Parallel bar grate with 11⁄8” on center bar spacing
            - ``CURVED_VANE``: Curved vane grate with 31⁄4” longitudinal bar and 41⁄4” transverse bar spacing on center
            - ``TILT_BAR``-45: 45 degree tilt bar grate with 21⁄4” longitudinal bar and 4” transverse bar spacing on center
            - ``TILT_BAR``-30: 30 degree tilt bar grate with 31⁄4” and 4” on center longitudinal and lateral bar spacing respectively
            - ``RETICULINE``: "Honeycomb" pattern of lateral bars and longitudinal bearing bars
            - ``GENERIC``: A generic grate design.

        Only a GENERIC type grate requires that Aopen and Vsplash values be provided.
        The other standard grate types have predetermined values of these parameters.
        (Splash over velocity is the minimum velocity that will cause some water to shoot over the inlet thus
        reducing its capture efficiency).

        A CUSTOM inlet takes the name of either a Diversion curve or a Rating curve as its only
        parameter (see the [CURVES] section). Diversion curves are best suited for on-grade
        inlets and Rating curves for on-sag inlets.

    Examples:
        ::

            ; A 2-ft x 2-ft parallel bar grate
            InletType1 GRATE 2 2 P-BAR-30

            ; A combination inlet
            InletType2 GRATE 2 2   CURVED_VANE
            InletType2 CURB  4 0.5 HORIZONTAL

            ; A custom inlet using Curve1 as its capture curve
            InletType3 CUSTOM Curve1
    """
    _identifier = IDENTIFIERS.name
    _table_inp_export = False
    _section_label = INLETS

    class TYPES:
        GRATE = 'GRATE'
        CURB = 'CURB'
        DROP_GRATE = 'DROP_GRATE'
        DROP_CURB = 'DROP_CURB'
        SLOTTED = 'SLOTTED'
        CUSTOM = 'CUSTOM'

    class THROAT:
        HORIZONTAL = 'HORIZONTAL'
        INCLINED = 'INCLINED'
        VERTICAL = 'VERTICAL'

    def __init__(self, name, kind,
                 # length, width, height, grate_type, area_open, velocity_splash, throat_angle
                 ):
        """Design data for storm drain inlets."""
        self.name = name
        self.kind = kind
        # self.length = length
        # self.width = width
        # self.height = height
        # self.grate_type = grate_type
        # self.area_open = area_open
        # self.velocity_splash = velocity_splash
        # self.throat_angle = throat_angle

    # def __new__(cls, *args, **kwargs):
    #     pass


class InletGrate(Inlet):
    def __init__(self, name, kind=Inlet.TYPES.GRATE, length=None, width=None, grate_type=None, area_open=NaN,
                 velocity_splash=NaN):
        super().__init__(name, kind)
        self.length = length
        self.width = width
        self.grate_type = grate_type
        self.area_open = area_open
        self.velocity_splash = velocity_splash


class InletCurb(Inlet):
    def __init__(self, name, kind=Inlet.TYPES.CURB, length=None, height=None):
        super().__init__(name, kind)
        self.length = length
        self.height = height


class InletSlotted(Inlet):
    def __init__(self, name, kind=Inlet.TYPES.SLOTTED, length=None, width=None):
        super().__init__(name, kind)
        self.length = length
        self.width = width


class InletCustom(Inlet):
    def __init__(self, name, kind=Inlet.TYPES.CUSTOM, curve=None):
        super().__init__(name, kind)
        self.curve = curve


class InletUsage(BaseSectionObject):
    """
    Assignment of inlets to street and channel conduits.

    Section:
        [INLET_USAGE]

    Purpose:
        Assigns inlet structures to specific street and open channel conduits.

    Attributes:
        conduit (str): name of a street or open channel conduit containing the inlet.
        inlet (str): name of an inlet structure (from the [``INLETS``] section (:class:`Inlet`)) to use.
        node (str): name of the sewer node receiving flow captured by the inlet.
        num (int | optional): number of replicate inlets placed on each side of the street.
        clogged_pct (float | optional): degree to which inlet capacity is reduced due to clogging (%).
        flow_max (float | optional): maximum flow that the inlet can capture (flow units).
        height_gutter (float | optional): height of local gutter depression (in or mm).
        width_gutter (float | optional): width of local gutter depression (ft or m).
        placement (str | optional): One of ``AUTOMATIC``, ``ON_GRADE``, or ``ON_SAG`` (:attr:`InletUsage.PLACEMENTS`).

        PLACEMENTS: Enum-like for the attribute :attr:`InletUsage.placement` with following members -> {``AUTOMATIC`` | ``ON_GRADE`` | ``ON_SAG``}

    Remarks:
        Only conduits with a ``STREET`` cross section can be assigned a curb and gutter inlet while
        drop inlets can only be assigned to conduits with a ``RECT_OPEN`` or ``TRAPEZOIDAL`` cross
        section.

        Only the first three parameters are required. The default number of inlets is 1 (for each side
        of a two-sided street) while the remaining parameters have default values of 0.

        A :attr:`InletUsage.flow_max` value of 0 indicates that the inlet has no flow restriction.

        The local gutter depression applies only over the length of the inlet unlike the continuous
        depression for a ``STREET`` cross section which exists over the full curb length.

        The default inlet placement is AUTOMATIC, meaning that the program uses the network
        topography to determine whether an inlet operates on-grade or on-sag. On-grade means the
        inlet is located on a continuous grade. On-sag means the inlet is located at a sag or sump point
        where all adjacent conduits slope towards the inlet leaving no place for water to flow except
        into the inlet.
    """
    _identifier = 'conduit'  # inlet
    _table_inp_export = True
    _section_label = INLET_USAGE

    class PLACEMENTS:
        AUTOMATIC = 'AUTOMATIC'
        ON_GRADE = 'ON_GRADE'
        ON_SAG = 'ON_SAG'

    def __init__(self, conduit, inlet, node, num=NaN, clogged_pct=NaN, flow_max=NaN, height_gutter=NaN,
                 width_gutter=NaN, placement=NaN):
        """
        Assignment of inlets to street and channel conduits.

        Args:
            conduit (str): name of a street or open channel conduit containing the inlet.
            inlet (str): name of an inlet structure (from the [INLETS] section (:class:`Inlet`)) to use.
            node (str): name of the sewer node receiving flow captured by the inlet.
            num (int | optional): number of replicate inlets placed on each side of the street.
            clogged_pct (float | optional): degree to which inlet capacity is reduced due to clogging (%).
            flow_max (float | optional): maximum flow that the inlet can capture (flow units).
            height_gutter (float | optional): height of local gutter depression (in or mm).
            width_gutter (float | optional): width of local gutter depression (ft or m).
            placement (str | optional):  One of ``AUTOMATIC``, ``ON_GRADE``, or ``ON_SAG`` (:attr:`InletUsage.PLACEMENTS`).
        """
        self.conduit = str(conduit)
        self.inlet = str(inlet)
        self.node = str(node)
        self.num = int(num)
        self.clogged_pct = float(clogged_pct)
        self.flow_max = float(flow_max)
        self.height_gutter = float(height_gutter)
        self.width_gutter = float(width_gutter)
        self.placement = placement


def main():
    inp = SwmmInput(custom_section_handler={
        STREET: Street,
        INLETS: Inlet,
        INLET_USAGE: InletUsage,
    })


if __name__ == '__main__':
    main()
