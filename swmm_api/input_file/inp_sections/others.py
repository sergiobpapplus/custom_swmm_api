from numpy import NaN
from pandas import DataFrame, Series

from .identifiers import IDENTIFIERS
from ..helpers.type_converter import infer_type
from ..inp_helpers import BaseSectionObject


class RainGage(BaseSectionObject):
    """
    Section:
        [RAINGAGES]

    Purpose:
        Identifies each rain gage that provides rainfall data for the study area.

    Formats:
        Name Form Intvl SCF TIMESERIES Tseries
        Name Form Intvl SCF FILE       Fname   Sta Units

    PC-SWMM-Format:
        Name Format Interval SCF Source

    Remarks:
        Name
            name assigned to rain gage.
        Form
            form of recorded rainfall, either INTENSITY, VOLUME or CUMULATIVE.
        Intvl
            time interval between gage readings in decimal hours or hours:minutes format (e.g., 0:15 for 15-minute
            readings).
        SCF
            snow catch deficiency correction factor (use 1.0 for no adjustment).
        Tseries
            name of time series in [TIMESERIES] section with rainfall data.
        Fname
            name of external file with rainfall data. Rainfall files are discussed in Section 11.3 Rainfall Files.
        Sta
            name of recording station used in the rain file.
        Units
            rain depth units used in the rain file, either IN (inches) or MM (millimeters).
    """
    identifier =IDENTIFIERS.Name

    class Formats:
        INTENSITY = 'INTENSITY'
        VOLUME = 'VOLUME'
        CUMULATIVE = 'CUMULATIVE'

    class Sources:
        TIMESERIES = 'TIMESERIES'
        FILE = 'FILE'

    class Unit:
        IN = 'IN'
        MM = 'MM'

    def __init__(self, Name, Format, Interval, SCF, Source, *args, Timeseries=NaN, Filename=NaN, Station=NaN,
                 Units=NaN):
        """

        Args:
            Name (str): name assigned to rain gage.
            Format (str): form of recorded rainfall, either INTENSITY, VOLUME or CUMULATIVE.
            Interval (str, Timedelta): time interval between gage readings in decimal hours or hours:minutes format
                                        (e.g., 0:15 for 15-minute readings).
            SCF (float): snow catch deficiency correction factor (use 1.0 for no adjustment).
            Source (str):
            *args:
            Timeseries (str): name of time series in [TIMESERIES] section with rainfall data.
            Filename (str): name of external file with rainfall data.
                            Rainfall files are discussed in Section 11.3 Rainfall Files.
            Station (str): name of recording station used in the rain file.
            Units (str): rain depth units used in the rain file, either IN (inches) or MM (millimeters).
        """
        self.Name = str(Name)
        self.Format = Format
        self.Interval = Interval
        self.SCF = SCF
        self.Source = Source

        self.Timeseries = Timeseries
        self.Filename = Filename
        self.Station = Station
        self.Units = Units

        l = len(args)
        if args:
            if (Source == RainGage.Sources.TIMESERIES) and (l == 1):
                self.Timeseries = args[0]
            elif Source == RainGage.Sources.FILE:

                self.Filename = args[0]
                self.Station = args[1]
                self.Units = args[2]
            else:
                raise NotImplementedError()


class Symbol(BaseSectionObject):
    """
    Section:
        [SYMBOLS]

    Purpose:
        Assigns X,Y coordinates to rain gage symbols.

    Format:
        Gage Xcoord Ycoord

    Remarks:
        Gage
            name of rain gage.
        Xcoord
            horizontal coordinate relative to origin in lower left of map.
        Ycoord
            vertical coordinate relative to origin in lower left of map.
    """
    identifier =IDENTIFIERS.Gage

    def __init__(self, Gage, x, y):
        """Assigns X,Y coordinates to drainage system nodes.

        Args:
            Node (str): name of node.
            x (float): horizontal coordinate relative to origin in lower left of map.
            y (float): vertical coordinate relative to origin in lower left of map.
        """
        self.Gage = str(Gage)
        self.x = x
        self.y = y


class Pattern(BaseSectionObject):
    """
    Section:
        [PATTERNS]

    Purpose:
        Specifies time pattern of dry weather flow or quality in the form of adjustment factors
        applied as multipliers to baseline values.


    Format:
        - Name MONTHLY Factor1 Factor2 ... Factor12
        - Name DAILY Factor1  Factor2  ...  Factor7
        - Name HOURLY Factor1  Factor2  ...  Factor24
        - Name WEEKEND Factor1  Factor2  ...  Factor24

    Remarks:
        - The MONTHLY format is used to set monthly pattern factors for dry weather flow constituents.
        - The DAILY format is used to set dry weather pattern factors for each day of the week, where Sunday is day 1.
        - The HOURLY format is used to set dry weather factors for each hour of the day starting from midnight.
            If these factors are different for weekend days than for weekday days then the WEEKEND format can be used
            to specify hourly adjustment factors just for weekends.
        - More than one line can be used to enter a pattern’s factors by repeating the pattern’s name
            (but not the pattern type) at the beginning of each additional line.
        - The pattern factors are applied as multipliers to any baseline dry weather flows or quality
            concentrations supplied in the [DWF] section.
    """
    identifier =IDENTIFIERS.Name

    class Types:
        __class__ = 'Patter Types'
        MONTHLY = 'MONTHLY'
        DAILY = 'DAILY'
        HOURLY = 'HOURLY'
        WEEKEND = 'WEEKEND'

    def __init__(self, Name, Type, *factors, Factors=None):
        self.Name = str(Name)
        self.Type = Type
        if Factors is not None:
            self.Factors = Factors
        else:
            self.Factors = list(float(f) for f in factors)

    @classmethod
    def convert_lines(cls, lines):
        """multiple lines for one entry"""
        new_lines = list()
        for line in lines:
            if line[1] in ['MONTHLY', 'DAILY', 'HOURLY', 'WEEKEND']:
                new_lines.append(line)
            else:
                new_lines[-1] += line[1:]

        # sec_lines = list()
        for line in new_lines:
            # sec_lines.append()
            yield cls(*line)

        # return sec_lines


class Pollutant(BaseSectionObject):
    """
    Section:
        [POLLUTANTS]

    Purpose:
        Identifies the pollutants being analyzed.

    Format:
        Name Units Crain Cgw Cii Kd (Sflag CoPoll CoFract Cdwf Cinit)

    PC-SWMM-Format:
        Name Units Crain Cgw Crdii Kdecay SnowOnly Co-Pollutant Co-Frac Cdwf Cinit

    Remarks:
        Name
            name assigned to pollutant.
        Units
            concentration units
                MG/L for milligrams per liter
                UG/L for micrograms per liter
                #/L for direct count per liter
        Crain
            concentration of pollutant in rainfall (concentration units).
        Cgw
            concentration of pollutant in groundwater (concentration units).
        Cii
            concentration of pollutant in inflow/infiltration (concentration units).
        Kdecay
            first-order decay coefficient (1/days).
        Sflag
            YES if pollutant buildup occurs only when there is snow cover, NO otherwise (default is NO).
        CoPoll
            name of co-pollutant (default is no co-pollutant designated by a *).
        CoFract
            fraction of co-pollutant concentration (default is 0).
        Cdwf
            pollutant concentration in dry weather flow (default is 0).
        Cinit
            pollutant concentration throughout the conveyance system at the start of the simulation (default is 0).

        FLOW is a reserved word and cannot be used to name a pollutant.

        Parameters Sflag through Cinit can be omitted if they assume their default values.
        If there is no co-pollutant but non-default values for Cdwf or Cinit, then enter an asterisk (*)
        for the co-pollutant name.

        When pollutant X has a co-pollutant Y, it means that fraction CoFract of pollutant Y’s runoff
        concentration is added to pollutant X’s runoff concentration when wash off from a subcatchment is computed.

        The dry weather flow concentration can be overridden for any specific node of the conveyance
        system by editing the node’s Inflows property.
    """
    identifier =IDENTIFIERS.Name

    class Unit:
        MG_PER_L = 'MG/L'
        UG_PER_L = 'UG/L'
        COUNT_PER_L = '#/L'

    def __init__(self, Name, Units, Crain, Cgw, Crdii, Kdecay,
                 SnowOnly=False, Co_Pollutant='*', Co_Frac=0, Cdwf=0, Cinit=0):
        self.Name = str(Name)
        self.Units = Units
        self.Crain = Crain
        self.Cgw = Cgw
        self.Crdii = Crdii
        self.Kdecay = Kdecay
        self.SnowOnly = SnowOnly
        self.Co_Pollutant = Co_Pollutant
        self.Co_Frac = Co_Frac
        self.Cdwf = Cdwf
        self.Cinit = Cinit


class Transect(BaseSectionObject):
    """
    Section:
        [TRANSECTS]

    Purpose:
        Describes the cross-section geometry of natural channels or conduits with irregular shapes
        following the HEC-2 data format.

    Formats:
        NC Nleft Nright Nchanl
        X1 Name Nsta Xleft Xright 0 0 0 Lfactor Wfactor Eoffset
        GR Elev Station ... Elev Station

    Remarks:
        Nleft:
            Manning’s n of right overbank portion of channel (use 0 if no change from previous NC line).
        Nright:
            Manning’s n of right overbank portion of channel (use 0 if no change from previous NC line.
        Nchanl:
            Manning’s n of main channel portion of channel (use 0 if no change from previous NC line.
        Name:
            name assigned to transect.
        Nsta:
            number of stations across cross-section at which elevation data is supplied.
        Xleft:
            station position which ends the left overbank portion of the channel (ft or m).
        Xright :
            station position which begins the right overbank portion of the channel (ft or m).
        Lfactor:
            meander modifier that represents the ratio of the length of a meandering main channel to the length of the
            overbank area that surrounds it (use 0 if not applicable).
        Wfactor:
            factor by which distances between stations should be multiplied to increase (or decrease)
            the width of the channel (enter 0 if not applicable).
        Eoffset:
            amount added (or subtracted) from the elevation of each station (ft or m).
        Elev:
            elevation of the channel bottom at a cross-section station relative to some fixed reference (ft or m).
        Station:
            distance of a cross-section station from some fixed reference (ft or m).

    Transect geometry is described as shown below, assuming that one is looking in a downstream direction:

    The first line in this section must always be a NC line. After that, the NC line is only needed when a transect has
    different Manning’s n values than the previous one.

    The Manning’s n values on the NC line will supersede any roughness value entered for the conduit which uses the
    irregular cross-section.

    There should be one X1 line for each transect.
    Any number of GR lines may follow, and each GR line can have any number of Elevation-Station data pairs.
    (In HEC-2 the GR line is limited to 5 stations.)

    The station that defines the left overbank boundary on the X1 line must correspond to one of the station entries
    on the GR lines that follow. The same holds true for the right overbank boundary. If there is no match, a warning
    will be issued and the program will assume that no overbank area exists.

    The meander modifier is applied to all conduits that use this particular transect for their cross section.
    It assumes that the length supplied for these conduits is that of the longer main channel.
    SWMM will use the shorter overbank length in its calculations while increasing the main channel roughness to account
    for its longer length.
    """
    identifier =IDENTIFIERS.Name
    table_inp_export = False

    def __init__(self, Name, station_elevations=None, bank_station_left=0, bank_station_right=0,
                 roughness_left=0, roughness_right=0, roughness_channel=0,
                 modifier_stations=0, modifier_elevations=0, modifier_meander=0):
        self.Name = str(Name)

        self.roughness_left = None
        self.roughness_right = None
        self.roughness_channel = None
        self.set_roughness(roughness_left, roughness_right, roughness_channel)

        self.bank_station_left = None
        self.bank_station_right = None
        self.set_bank_stations(bank_station_left, bank_station_right)

        self.modifier_stations = None
        self.modifier_elevations = None
        self.modifier_meander = None
        self.set_modifiers(modifier_meander, modifier_stations, modifier_elevations)

        self.station_elevations = list()

        if station_elevations is not None:
            for s in station_elevations:
                self.add_station_elevation(*s)

    def add_station_elevation(self, station, elevation):
        self.station_elevations.append([float(station), float(elevation)])

    def set_roughness(self, left=0, right=0, channel=0):
        self.roughness_left = float(left)
        self.roughness_right = float(right)
        self.roughness_channel = float(channel)

    def set_bank_stations(self, left=0, right=0):
        self.bank_station_left = float(left)
        self.bank_station_right = float(right)

    def set_modifiers(self, meander=0, stations=0, elevations=0):
        self.modifier_stations = float(stations)
        self.modifier_elevations = float(elevations)
        self.modifier_meander = float(meander)

    def get_number_stations(self):
        """get number of stations"""
        return len(self.station_elevations)

    @classmethod
    def convert_lines(cls, lines):
        """multiple lines for one entry"""
        last_roughness = [0, 0, 0]
        last = None

        for line in lines:
            if line[0] == 'NC':
                last_roughness = line[1:]

            elif line[0] == 'X1':
                if last is not None:
                    yield last
                last = cls(Name=line[1])
                last.set_bank_stations(*line[3:5])
                last.set_modifiers(*line[8:])
                last.set_roughness(*last_roughness)

            elif line[0] == 'GR':
                it = iter(line[1:])
                for station in it:
                    elevation = next(it)
                    last.add_station_elevation(station, elevation)
        yield last

    def inp_line(self):
        s = 'NC {} {} {}\n'.format(self.roughness_left, self.roughness_right, self.roughness_channel)
        s += 'X1 {} {} {} {} 0 0 0 {} {} {}\n'.format(self.Name, self.get_number_stations(),
                                                      self.bank_station_left, self.bank_station_right,
                                                      self.modifier_stations, self.modifier_elevations,
                                                      self.modifier_meander)
        s += 'GR'
        i = 0
        for x, y in self.station_elevations:
            s += ' {} {}'.format(x, y)
            i += 1
            if i == 5:
                i = 0
                s += '\nGR'

        if s.endswith('GR'):
            s = s[:-3]
        s += '\n'
        return s


class Control(BaseSectionObject):
    """
    Section:
        [CONTROLS]

    Purpose:
        Determines how pumps and regulators will be adjusted based on simulation time or
        conditions at specific nodes and links.

    Formats:
        Each control rule is a series of statements of the form:
        RULE ruleID
        IF condition_1
        AND condition_2
        OR condition_3
        AND condition_4
        Etc.
        THEN action_1
        AND action_2
        Etc.
        ELSE action_3
        AND action_4
        Etc.
        PRIORITY value

    Remarks:
        RuleID an ID label assigned to the rule.
        condition_n a condition clause.
        action_n an action clause.
        value a priority value (e.g., a number from 1 to 5).

        A condition clause of a Control Rule has the following format:
            Object Name Attribute Relation Value

        where Object is a category of object, Name is the object’s assigned ID name,
        Attribute is the name of an attribute or property of the object, Relation is a
        relational operator (=, <>, <, <=, >, >=), and Value is an attribute value.

        Some examples of condition clauses are:
            NODE N23 DEPTH > 10
            PUMP P45 STATUS = OFF
            SIMULATION TIME = 12:45:00

        The objects and attributes that can appear in a condition clause are as follows:
    """
    identifier =IDENTIFIERS.Name
    table_inp_export = False

    class Clauses:
        __class__ = 'Clauses'
        RULE = 'RULE'
        IF = 'IF'
        THEN = 'THEN'
        PRIORITY = 'PRIORITY'
        AND = 'AND'
        OR = 'OR'

    def __init__(self, Name, conditions, actions, priority=0):
        self.Name = str(Name)
        self.conditions = conditions
        self.actions = actions
        self.priority = int(priority)

    @classmethod
    def convert_lines(cls, lines):
        """multiple lines for one entry"""
        new_lines = list()
        new_obj = list()
        is_condition = False
        is_action = False
        for line in lines:
            if line[0] == cls.Clauses.RULE:
                if new_obj:
                    new_lines.append(new_obj)
                    new_obj = list()
                new_obj.append(line[1])
                is_action = False

            elif line[0] == cls.Clauses.IF:
                new_obj.append([line[1:]])
                is_condition = True

            elif line[0] == cls.Clauses.THEN:
                new_obj.append([line[1:]])
                is_condition = False
                is_action = True

            elif line[0] == cls.Clauses.PRIORITY:
                new_obj.append(line[1])
                is_action = False

            elif is_condition:
                new_obj[-1].append(line)

            elif is_action:
                new_obj[-1].append(line)

        new_lines.append(new_obj)

        # sec_lines = list()
        for line in new_lines:
            # sec_lines.append()
            yield cls(*line)

        # return sec_lines

    def inp_line(self):
        s = '{} {}\n'.format(self.Clauses.RULE, self.Name)
        s += '{} {}\n'.format(self.Clauses.IF, '\n'.join([' '.join(c) for c in self.conditions]))
        s += '{} {}\n'.format(self.Clauses.THEN, '\n'.join([' '.join(a) for a in self.actions]))
        s += '{} {}\n'.format(self.Clauses.PRIORITY, self.priority)
        return s


class Curve(BaseSectionObject):
    """
    Section:
        [CURVES]

    Purpose:
        Describes a relationship between two variables in tabular format.

    Format:
        Name Type X-value Y-value ...

    Format-PCSWMM:
            Name Type X-Value Y-Value

    Remarks:
        Name
            name assigned to table
        Type
            STORAGE / SHAPE / DIVERSION / TIDAL / PUMP1 / PUMP2 / PUMP3 / PUMP4 / RATING / CONTROL
        X-value
            an x (independent variable) value

        Y-value
            the y (dependent variable) value corresponding to x

        Multiple pairs of x-y values can appear on a line. If more than one line is needed,
        repeat the curve's name (but not the type) on subsequent lines. The x-values must
        be entered in increasing order.

        Choices for curve type have the following meanings (flows are expressed in the
        user’s choice of flow units set in the [OPTIONS] section):

        STORAGE
            surface area in ft2 (m2) v. depth in ft (m) for a storage unit node
        SHAPE
            width v. depth for a custom closed cross-section, both normalized with respect to full depth
        DIVERSION
            diverted outflow v. total inflow for a flow divider node
        TIDAL
            water surface elevation in ft (m) v. hour of the day for an outfall node
        PUMP1
            pump outflow v. increment of inlet node volume in ft3 (m3)
        PUMP2
            pump outflow v. increment of inlet node depth in ft (m)
        PUMP3
            pump outflow v. head difference between outlet and inlet nodes in ft (m)
        PUMP4
            pump outflow v. continuous depth in ft (m)
        RATING
            outlet flow v. head in ft (m)
        CONTROL
            control setting v. controller variable

    Examples:
        ;Storage curve (x = depth, y = surface area)
        AC1 STORAGE 0 1000 2 2000 4 3500 6 4200
         8
         5000
        ;Type1 pump curve (x = inlet wet well volume, y = flow )
        PC1 PUMP1
        PC1 100 5 300 10 500 20

    """
    identifier =IDENTIFIERS.Name
    table_inp_export = False

    class TYPES:
        STORAGE = 'STORAGE'
        SHAPE = 'SHAPE'
        DIVERSION = 'DIVERSION'
        TIDAL = 'TIDAL'
        PUMP1 = 'PUMP1'
        PUMP2 = 'PUMP2'
        PUMP3 = 'PUMP3'
        PUMP4 = 'PUMP4'
        RATING = 'RATING'
        CONTROL = 'CONTROL'

    @classmethod
    def _get_names(cls, kind):
        TYPES = cls.TYPES
        if kind == TYPES.STORAGE:
            return ['depth', 'area']
        elif kind == TYPES.SHAPE:
            return ['depth', 'width']
        elif kind == TYPES.DIVERSION:
            return ['inflow', 'outflow']
        elif kind == TYPES.TIDAL:
            return ['hour', 'elevation']
        elif kind == TYPES.PUMP1:
            return ['volume', 'outflow']
        elif kind == TYPES.PUMP2:
            return ['depth', 'outflow']
        elif kind == TYPES.PUMP3:
            return ['head diff', 'outflow']
        elif kind == TYPES.PUMP4:
            return ['depth', 'outflow']
        elif kind == TYPES.RATING:
            return ['head', 'flow']
        elif kind == TYPES.CONTROL:
            return ['variable', 'setting']

    def __init__(self, Name, kind, points):
        self.Name = str(Name)
        self.kind = kind.upper()
        self.points = points

    @classmethod
    def convert_lines(cls, lines):
        last = None
        points = list()
        for name, *line in lines:
            remains = iter(line)

            if name != last:
                # new curve line
                if last is not None:
                    # first return previous curve
                    yield cls(last, kind, points)
                # reset variables
                points = list()
                last = name
                kind = next(remains)

            # points in current line
            for a in remains:
                b = next(remains)
                points.append(infer_type([a, b]))

        # last
        if last is not None:
            yield cls(last, kind, points)

    @property
    def frame(self):
        return DataFrame.from_records(self.points, columns=self._get_names(self.kind))

    def inp_line(self):
        kind = self.kind
        f = ''
        # f = '{}  {}\n'.format(self.Name, self.kind)
        for x, y in self.points:  # [(x,y), (x,y), ...]
            f += '{}  {} {:7.4f} {:7.4f}\n'.format(self.Name, kind, x, y)
            kind = ''
        return f


class Timeseries(BaseSectionObject):
    """
    Section:
        [TIMESERIES]

    Purpose:
        Describes how a quantity varies over time.

    Formats:
        - Name ( Date ) Hour Value ...
        - Name Time Value ...
        - Name FILE Fname

    Remarks:
        - Name: name assigned to time series.
        - Date: date in Month/Day/Year format (e.g., June 15, 2001 would be 6/15/2001).
        - Hour: 24-hour military time (e.g., 8:40 pm would be 20:40) relative to the last date specified
               (or to midnight of the starting date of the simulation if no previous date was specified).
        - Time: hours since the start of the simulation, expressed as a decimal number or as hours:minutes.
        - Value: value corresponding to given date and time.
        - Fname: name of a file in which the time series data are stored

        There are two options for supplying the data for a time series:
        i.: directly within this input file section as described by the first two formats
        ii.: through an external data file named with the third format.

        When direct data entry is used, multiple date-time-value or time-value entries can
        appear on a line. If more than one line is needed, the table's name must be repeated
        as the first entry on subsequent lines.

        When an external file is used, each line in the file must use the same formats listed
        above, except that only one date-time-value (or time-value) entry is allowed per line.
        Any line that begins with a semicolon is considered a comment line and is ignored.
        Blank lines are not allowed.

        Note that there are two methods for describing the occurrence time of time series data:

        - as calendar date/time of day (which requires that at least one date, at the start of the series, be entered)
        - as elapsed hours since the start of the simulation.

        For the first method, dates need only be entered at points in time when a new day occurs.

    Examples:
        ;Rainfall time series with dates specified
        TS1 6-15-2001 7:00 0.1 8:00 0.2 9:00 0.05 10:00 0
        TS1 6-21-2001 4:00 0.2 5:00 0 14:00 0.1 15:00 0 335

        ;Inflow hydrograph - time relative to start of simulation
        HY1 0 0 1.25 100 2:30 150 3.0 120 4.5 0
        HY1 32:10 0 34.0 57 35.33 85 48.67 24 50 0
    """
    identifier =IDENTIFIERS.Name
    table_inp_export = False

    class TYPES:
        FILE = 'FILE'

    def __init__(self, Name):
        """
        Describes how a quantity varies over time.

        Args:
            Name (str): name assigned to time series.
        """
        self.Name = str(Name)

    @classmethod
    def convert_lines(cls, lines):
        """
        convert the input file section
        an object uses multiple lines

        Args:
            lines (str | list[list[str]]): lines in the input file section

        Yields:
            TimeseriesData | TimeseriesFile: Timeseries objects
        """
        data = list()
        last = None

        for name, *line in lines:
            # ---------------------------------
            if line[0].upper() == cls.TYPES.FILE:
                yield TimeseriesFile(name, ' '.join(line[1:]))
                last = name

            # ---------------------------------
            else:
                if name != last:
                    if last is not None:
                        yield TimeseriesData(last, data)
                    data = list()
                    last = name

                # -------------
                iterator = iter(line)
                for part in iterator:
                    if '/' in part:
                        date = part
                        time = next(iterator)
                        i = ' '.join([date, time])

                    else:
                        i = part

                    v = float(next(iterator))
                    data.append([i, v])

        # last
        if line[0].upper() != cls.TYPES.FILE:
            yield TimeseriesData(last, data)


class TimeseriesFile(Timeseries):
    def __init__(self, Name, filename):
        """
        Describes how a quantity varies over time.

        Args:
            Name (str): name assigned to time series.
            filename (str): name of a file in which the time series data are stored
        """
        Timeseries.__init__(self, Name)
        self.kind = self.TYPES.FILE
        self.filename = filename


class TimeseriesData(Timeseries):
    def __init__(self, Name, data):
        """
        Describes how a quantity varies over time.

        Args:
            Name (str): name assigned to time series.
            data (list[tuple]): list of index/value tuple
        """
        Timeseries.__init__(self, Name)
        self.data = data

    @property
    def frame(self):
        """
        convert object to pandas Series

        Returns:
            pandas.Series: Timeseries
        """
        datetime, values = zip(*self.data)
        return Series(index=datetime, data=values, name=self.Name)

    def inp_line(self):
        f = ''
        for datetime, value in self.data:
            f += '{} {} {}\n'.format(self.Name, datetime, value)
        return f
