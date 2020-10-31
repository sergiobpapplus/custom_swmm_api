from numpy import NaN
from pandas import DataFrame

from ..inp_helpers import BaseSectionObject, SWMM_VERSION
from .identifiers import IDENTIFIERS


class SubCatchment(BaseSectionObject):
    """
    Section: [**SUBCATCHMENTS**]

    Purpose:
        Identifies each subcatchment within the study area. Subcatchments are land area
        units which generate runoff from rainfall.

    Format:
        ::

            Name Rgage OutID Area %Imperv Width Slope Clength (Spack)

    Format-PCSWMM:
        ``Name RainGage Outlet Area %Imperv Width %Slope CurbLen SnowPack``

    Args:
        Name (str): name assigned to subcatchment.
        RainGage (str): name of rain gage in [RAINGAGES] section assigned to subcatchment. ``Rgage``
        Outlet (str): name of node or subcatchment that receives runoff from subcatchment. ``OutID``
        Area (float): area of subcatchment (acres or hectares).
        Imperv (float): percent imperviousness of subcatchment. ``%Imperv``
        Width (float): characteristic width of subcatchment (ft or meters).
        Slope (float): subcatchment slope (percent).
        CurbLen (float): total curb length (any length units). Use 0 if not applicable. ``Clength``
        SnowPack (str): optional name of snow pack object (from [SNOWPACKS] section) that characterizes snow accumulation and melting over the subcatchment. ``Spack``

    Attributes:
        Name (str): name assigned to subcatchment.
        RainGage (str): name of rain gage in [RAINGAGES] section assigned to subcatchment. ``Rgage``
        Outlet (str): name of node or subcatchment that receives runoff from subcatchment. ``OutID``
        Area (float): area of subcatchment (acres or hectares).
        Imperv (float): percent imperviousness of subcatchment. ``%Imperv``
        Width (float): characteristic width of subcatchment (ft or meters).
        Slope (float): subcatchment slope (percent).
        CurbLen (float): total curb length (any length units). Use 0 if not applicable. ``Clength``
        SnowPack (str): optional name of snow pack object (from [SNOWPACKS] section) that characterizes snow accumulation and melting over the subcatchment. ``Spack``
    """
    identifier =IDENTIFIERS.Name

    def __init__(self, Name, RainGage, Outlet, Area, Imperv, Width, Slope, CurbLen=0, SnowPack=NaN):
        self.Name = str(Name)
        self.RainGage = str(RainGage)
        self.Outlet = str(Outlet)
        self.Area = float(Area)
        self.Imperv = float(Imperv)
        self.Width = float(Width)
        self.Slope = float(Slope)
        self.CurbLen = float(CurbLen)
        self.SnowPack = SnowPack


class SubArea(BaseSectionObject):
    """
    Section: [**SUBAREAS**]

    Purpose:
        Supplies information about pervious and impervious areas for each subcatchment.
        Each subcatchment can consist of a pervious sub-area, an impervious sub-area with
        depression storage, and an impervious sub-area without depression storage.

    Format:
        ::

            Subcat Nimp Nperv Simp Sperv %Zero RouteTo (%Routed)

    Format-PCSWMM:
        ``Subcatchment N-Imperv N-Perv S-Imperv S-Perv PctZero RouteTo PctRouted``

    Args:
        Subcatch (str): subcatchment name. ``Subcat``
        N_Imperv (float): Manning's n for overland flow over the impervious sub-area. ``Nimp``
        N_Perv (float): Manning's n for overland flow over the pervious sub-area. ``Nperv``
        S_Imperv (float): depression storage for impervious sub-area (inches or mm). ``Simp``
        S_Perv (float): depression storage for pervious sub-area (inches or mm). ``Sperv``
        PctZero (float): percent of impervious area with no depression storage. ``%Zero``
        RouteTo (str):

            - ``IMPERVIOUS`` if pervious area runoff runs onto impervious area,
            - ``PERVIOUS`` if impervious runoff runs onto pervious area,
            - ``OUTLET`` if both areas drain to the subcatchment's outlet (default = ``OUTLET``).

        PctRouted (float): percent of runoff routed from one type of area to another (default = 100). ``%Routed``

    Attributes:
        Subcatch (str): subcatchment name. ``Subcat``
        N_Imperv (float): Manning's n for overland flow over the impervious sub-area. ``Nimp``
        N_Perv (float): Manning's n for overland flow over the pervious sub-area. ``Nperv``
        S_Imperv (float): depression storage for impervious sub-area (inches or mm). ``Simp``
        S_Perv (float): depression storage for pervious sub-area (inches or mm). ``Sperv``
        PctZero (float): percent of impervious area with no depression storage. ``%Zero``
        RouteTo (str):

            - ``IMPERVIOUS`` if pervious area runoff runs onto impervious area,
            - ``PERVIOUS`` if impervious runoff runs onto pervious area,
            - ``OUTLET`` if both areas drain to the subcatchment's outlet (default = ``OUTLET``).

        PctRouted (float): percent of runoff routed from one type of area to another (default = 100). ``%Routed``
    """
    identifier =IDENTIFIERS.Subcatch

    class RoutToOption:
        __class__ = 'RoutTo Option'
        IMPERVIOUS = 'IMPERVIOUS'
        PERVIOUS = 'PERVIOUS'
        OUTLET = 'OUTLET'

    def __init__(self, Subcatch, N_Imperv, N_Perv, S_Imperv, S_Perv, PctZero, RouteTo=RoutToOption.OUTLET, PctRouted=100):
        self.Subcatch = str(Subcatch)
        self.N_Imperv = float(N_Imperv)
        self.N_Perv = float(N_Perv)
        self.S_Imperv = float(S_Imperv)
        self.S_Perv = float(S_Perv)
        self.PctZero = float(PctZero)
        self.RouteTo = str(RouteTo)
        self.PctRouted = float(PctRouted)


class Infiltration(BaseSectionObject):
    identifier =IDENTIFIERS.Subcatch
    table_inp_export = False

    def __init__(self, Subcatch):
        self.Subcatch = str(Subcatch)

    @classmethod
    def from_line(cls, Subcatch, *args, **kwargs):
        n_args = len(args) + len(kwargs.keys()) + 1
        if n_args == 6:  # hortn
            subcls = InfiltrationHorton
        elif n_args == 4:
            subcls = InfiltrationGreenAmpt
        else:
            # TODO
            subcls = InfiltrationCurveNumber

        # _____________________________________
        sub_class_id = None
        if SWMM_VERSION == '5.1.015':
            # NEU in swmm 5.1.015
            last_arg = args[-1]
            cls_args = {
                'HORTON': InfiltrationHorton,
                'MODIFIED_HORTON': InfiltrationHorton,
                'GREEN_AMPT': InfiltrationGreenAmpt,
                'MODIFIED_GREEN_AMPT': InfiltrationGreenAmpt,
                'CURVE_NUMBER': InfiltrationCurveNumber
            }
            if last_arg in cls_args:
                sub_class_id = last_arg
                subcls = cls_args[last_arg]
                args = args[:-1]

        if subcls != InfiltrationHorton:
            args = args[:3]

        # _____________________________________
        o = subcls(Subcatch, *args, **kwargs)
        # _____________________________________
        if sub_class_id is not None:
            o.kind = sub_class_id
        return o


class InfiltrationHorton(Infiltration):

    def __init__(self, Subcatch, MaxRate, MinRate, Decay, DryTime, MaxInf):
        """
        Horton:
            Subcat  MaxRate  MinRate  Decay  DryTime  MaxInf

        PC-SWMM-Format:
            Subcatchment MaxRate MinRate Decay DryTime MaxInfil

        Args:
            line ():

        Returns:

        """
        Infiltration.__init__(self, Subcatch)
        self.MaxRate = MaxRate
        self.MinRate = MinRate
        self.Decay = Decay
        self.DryTime = DryTime
        self.MaxInf = MaxInf
        self.kind = NaN


class InfiltrationGreenAmpt(Infiltration):

    def __init__(self, Subcatch, Psi, Ksat, IMD):
        """
        Green-Ampt:
            Subcat  Psi  Ksat  IMD

        PC-SWMM-Format:
            Subcatchment MaxRate MinRate Decay DryTime MaxInfil

        Args:
            line ():

        Returns:

        """
        Infiltration.__init__(self, Subcatch)
        self.Psi = Psi
        self.Ksat = Ksat
        self.IMD = IMD
        self.kind = NaN


class InfiltrationCurveNumber(Infiltration):

    def __init__(self, Subcatch, CurveNo, Ksat, DryTime):
        """
        Curve-Number:
            Subcat  CurveNo  Ksat  DryTime

        PC-SWMM-Format:
            Subcatchment MaxRate MinRate Decay DryTime MaxInfil

        Args:
            line ():

        Returns:

        """
        Infiltration.__init__(self, Subcatch)
        self.CurveNo = CurveNo
        self.Ksat = Ksat
        self.DryTime = DryTime
        self.kind = NaN


class Polygon(BaseSectionObject):
    """
    Section: [**POLYGONS**]

    Purpose:
        Assigns X,Y coordinates to vertex points of polygons that define a subcatchment boundary.

    Format:
        ::

            Link Xcoord Ycoord

    Remarks:
        Include a separate line for each vertex of the subcatchment polygon, ordered in a
        consistent clockwise or counter-clockwise sequence.

    Args:
        Subcatch (str): name of subcatchment. ``Subcat``
        polygon (list[list[float,float]]): coordinate of the polygon relative to origin in lower left of map.
            - Xcoord: horizontal coordinate of vertex
            - Ycoord: vertical coordinate of vertex

    Attributes:
        Subcatch (str): name of subcatchment. ``Subcat``
        polygon (list[list[float,float]]): coordinate of the polygon relative to origin in lower left of map.
            - Xcoord: horizontal coordinate of vertex
            - Ycoord: vertical coordinate of vertex
    """
    identifier =IDENTIFIERS.Subcatch
    table_inp_export = False

    def __init__(self, Subcatch,  polygon):
        self.Subcatch = str(Subcatch)
        self.polygon = polygon

    @classmethod
    def convert_lines(cls, lines):
        """multiple lines for one entry"""
        polygon = list()
        last = None

        for line in lines:
            Subcatch, x, y = line
            x = float(x)
            y = float(y)
            if Subcatch == last:
                polygon.append([x, y])
            else:
                if last is not None:
                    yield cls(last, polygon)
                last = Subcatch
                polygon = [[x, y]]
        # last
        if last is not None:
            yield cls(last, polygon)

    @property
    def frame(self):
        return DataFrame.from_records(self.polygon, columns=['x', 'y'])

    def inp_line(self):
        return '\n'.join(['{}  {} {}'.format(self.Subcatch, x, y) for x, y in self.polygon])


class Loading(BaseSectionObject):
    """
    Section: [**LOADINGS**]

    Purpose:
        Specifies the pollutant buildup that exists on each subcatchment at the start of a simulation.

    Format:
        ::

            Subcat Pollut InitBuildup Pollut InitBuildup ...

    Format-PCSWMM:
        ``Subcatchment Pollutant Buildup``

    Remarks:
        More than one pair of pollutant - buildup values can be entered per line. If more than
        one line is needed, then the subcatchment name must still be entered first on the
        succeeding lines.

        If an initial buildup is not specified for a pollutant, then its initial buildup is computed
        by applying the DRY_DAYS option (specified in the [OPTIONS] section) to the
        pollutant’s buildup function for each land use in the subcatchment.

    Args:
        Subcatch (str): name of a subcatchment.
        pollutant_buildup (list[list[str, float]]): tuple of

            - Pollut: name of a pollutant.
            - InitBuildup: initial buildup of pollutant (lbs/acre or kg/hectare).

    Attributes:
        Subcatch (str): name of a subcatchment.
        pollutant_buildup (list[list[str, float]]): tuple of

            - Pollut: name of a pollutant.
            - InitBuildup: initial buildup of pollutant (lbs/acre or kg/hectare).

    """
    identifier =IDENTIFIERS.Subcatch
    table_inp_export = False

    def __init__(self, Subcatch,  pollutant_buildup):
        self.Subcatch = str(Subcatch)
        self.pollutant_buildup = pollutant_buildup

    @classmethod
    def convert_lines(cls, lines):
        """multiple lines for one entry"""
        last = None
        pollutant_buildup = list()
        for Subcatch, *line in lines:
            if Subcatch != last:
                # new curve line
                if last is not None:
                    # first return previous curve
                    yield cls(last, pollutant_buildup)
                # reset variables
                pollutant_buildup = list()
                last = Subcatch

            # points in current line
            remains = iter(line)
            for pollutant in remains:
                buildup = next(remains)
                pollutant_buildup.append([pollutant, buildup])

        # last
        if last is not None:
            yield cls(last, pollutant_buildup)

    @property
    def frame(self):
        return DataFrame.from_records(self.pollutant_buildup, columns=['pollutant', 'initial buildup'])

    def inp_line(self):
        return '\n'.join(['{}  {} {}'.format(self.Subcatch, p, b) for p, b in self.pollutant_buildup])
