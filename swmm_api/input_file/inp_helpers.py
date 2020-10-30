from pandas import DataFrame
from numpy import isnan
from copy import deepcopy

from .helpers.type_converter import type2str, infer_type

SWMM_VERSION = '5.1.015'


########################################################################################################################
class UserDict_:
    """imitate UserDict / user class like dict but operations only effect self._data"""

    def __init__(self, d=None, **kwargs):
        if d is None:
            self._data = kwargs
        else:
            if isinstance(d, dict):
                self._data = d
            else:
                self._data = dict(d)

    def __len__(self):
        return self._data.__len__()

    def __getitem__(self, key):
        return self._data.__getitem__(key)

    def __setitem__(self, key, item):
        self._data.__setitem__(key, item)

    def __delitem__(self, key):
        self._data.__delitem__(key)

    def __iter__(self):
        return self._data.__iter__()

    def __contains__(self, key):
        return self._data.__contains__(key)

    def __repr__(self):
        return self._data.__repr__()

    def __str__(self):
        return self._data.__str__()

    def get(self, key, default=None):
        if isinstance(key, list):
            return (self.get(k) for k in key)
        return self._data.get(key) if key in self else default

    def copy(self):
        return type(self)(deepcopy(self._data))

    def values(self):
        return self._data.values()

    def keys(self):
        return self._data.keys()

    def items(self):
        return self._data.items()

    def update(self, d=None, **kwargs):
        self._data.update(d, **kwargs)

    def pop(self, key):
        return self._data.pop(key)

    def __bool__(self):
        return bool(self._data)


########################################################################################################################
class BaseSectionObject:
    """base class for all section objects to unify operations
    sections objects only have __init__ with object parameters

    acts like a dict (getter and setter)"""
    identifier = ''  # attribute of an object which will be used as identifiers
    table_inp_export = True  # if an section is writeable as table. Default ist True

    def get(self, key):
        if isinstance(key, list):
            return tuple([self.get(k) for k in key])
        return self.to_dict_().get(key)

    def set(self, key, value):
        assert key in self.to_dict_()
        vars(self)[key] = value

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, item):
        self.set(key, item)

    def to_dict_(self):
        """
        get all object parameters as dictionary

        Returns:
            dict:
        """
        return vars(self).copy()

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self._to_debug_string()

    def _to_debug_string(self):
        """for debugging purposes

        string is almost equal to python syntax
        so you could copy it and past it into your code

        Returns:
            str: debug string of the object
        """
        args = list()
        for k, d in self.to_dict_().items():
            if isinstance(d, float) and isnan(d):
                args.append('{} = NaN'.format(k))
            elif isinstance(d, str):
                args.append('{} = "{}"'.format(k, d))
            else:
                args.append('{} = {}'.format(k, d))
        return '{}({})'.format(self.__class__.__name__, ', '.join(args))

    def inp_line(self):
        """
        convert object to one line of the .inp file

        for .inp file writing

        Returns:
            str: SWMM .inp file compatible string
        """
        di = self.to_dict_()
        s = ''
        if isinstance(self.identifier, list):
            s += ' '.join([str(di.pop(i)) for i in self.identifier])
        else:
            s += str(di.pop(self.identifier))

        s += ' ' + ' '.join([type2str(i) for i in di.values()])
        return s

    @classmethod
    def from_line(cls, *line):
        """
        convert line in the input file to the object

        Args:
            *line (list[str]): arguments in the line

        Returns:
            BaseSectionObject: object of the input file section
        """
        return cls(*line)

    def copy(self):
        """
        copy object

        Returns:
            BaseSectionObject: copy of the object
        """
        return type(self)(**vars(self).copy())


########################################################################################################################
class InpSectionGeneric:
    """abstract class for input file sections without objects"""
    @classmethod
    def from_lines(cls, lines):
        """abstract function to read input file lines and create an section object"""
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def to_inp(self, fast=False):
        """abstract function to write input file lines of an section object"""
        pass


########################################################################################################################
class InpSection(UserDict_):
    def __init__(self, section_object):
        """each section of the .inp file is converted to such a section

        Args:
            section_object (BaseSectionObject):
        """
        UserDict_.__init__(self)
        self.section_object = section_object

    @property
    def _identifier(self):
        return self.section_object.identifier

    @property
    def _table_inp_export(self):
        return self.section_object.table_inp_export

    @property
    def data(self):
        # for debugging
        return self._data

    def append(self, item):
        """
        add object(s)/item(s) to section

        Args:
            item (BaseSectionObject | list[BaseSectionObject]):
        """
        if isinstance(item, (list, tuple)):
            for i in item:
                self.append(i)
        else:
            self[item.get(self._identifier)] = item

    @classmethod
    def from_lines(cls, lines, section_class):
        """convert all lines of a section to this class and each line to a object

        for .inp file reading

        Args:
            lines (list[list[str]]): lines of a section in a .inp file
            section_class (BaseSectionObject):

        Returns:
            InpSection: of one section
        """
        inp_section = cls(section_class)

        if isinstance(lines, str):
            lines = txt_to_lines(lines)

        if hasattr(section_class, 'convert_lines'):
            # each object has multiple lines
            for section_class_line in section_class.convert_lines(lines):
                inp_section.append(section_class_line)
            return inp_section

        # -----------------------
        # each line is a object
        for line in lines:
            line = infer_type(line)
            inp_section.append(section_class.from_line(*line))

        return inp_section

    @property
    def frame(self):
        """convert section to a data-frame

        for debugging purposes

        Returns:
            pandas.DataFrame: section as table
        """
        if not self:  # if empty
            return DataFrame()

        return DataFrame([i.to_dict_() for i in self.values()]).set_index(self._identifier)

    # def __repr__(self):
    #     return dataframe_to_inp_string(self.frame)
    #
    # def __str__(self):
    #     return dataframe_to_inp_string(self.frame)

    def to_inp(self, fast=False):
        """section to a multi-line string

        for .inp file writing

        Args:
            fast (bool): don't use any formatting else format as table

        Returns:
            str: .inp file string
        """
        if not self:  # if empty
            return ';; No Data'

        if fast or not self._table_inp_export:
            return '\n'.join(o.inp_line() for o in self.values())
        else:
            return dataframe_to_inp_string(self.frame)

    def copy(self):
        """deep copy the section

        Returns:
            InpSection: copy of the section
        """
        new = type(self)(self.section_object)
        new._data = deepcopy(self._data)
        return new

    def filter_keys(self, keys, by=None):
        """
        filter parts of the section with keys (identifier strings or attribute string)

        Args:
            keys (list): list of names to filter by (ether the identifier or the attribute of "by")
            by (str): attribute name of the section object to filter by

        Returns:
            InpSection: new filtered section
        """
        new = type(self)(self._identifier)
        if by is not None:
            new._data = {k: self[k] for k in self.keys() if self[k][by] in keys}
        else:
            new._data = {k: self[k] for k in set(self.keys()).intersection(keys)}
        return new


########################################################################################################################
class InpData(dict):
    """overall class for an input file"""
    def copy(self):
        """deep copy of an object"""
        return InpData(deepcopy(self))


########################################################################################################################
def dataframe_to_inp_string(df):
    """convert a data-frame into a multi-line string

    used to make a better readable .inp file and for debugging

    Args:
        df (pandas.DataFrame): section table

    Returns:
        str: .inp file conform string for one section
    """
    comment_sign = ';;'
    if df.empty:
        return ';; NO data'

    c = df.copy()
    if c.columns.name is None:
        c.columns.name = comment_sign
    else:
        if not c.columns.name.startswith(comment_sign):
            c.columns.name = comment_sign + c.columns.name

    if c.index.name is not None:
        if not c.index.name.startswith(comment_sign):
            c.index.name = comment_sign + c.index.name

    if c.index._typ == 'multiindex':
        if c.index.names is not None:
            if not c.index.levels[0].name.startswith(comment_sign):
                c.index.set_names(';' + c.index.names[0], level=0, inplace=True)
                # because pandas 1.0
                # c.index.levels[0].name = ';' + c.index.levels[0].name

    return c.applymap(type2str).to_string(sparsify=False, line_width=999999)


########################################################################################################################
def txt_to_lines(content):
    """
    split lines into lists of lists of arguments

    Args:
        content (str): lines in inp file

    Returns:
        list[list[str]]: split lines
    """
    for line in content.split('\n'):
        # ;; section comment
        # ; object comment / either inline(at the end of the line) or before the line
        # if ';' in line:
        #     line
        line = line.split(';')[0]
        line = line.strip()
        if line == '':  # ignore empty and comment lines
            continue
        else:
            yield line.split()
