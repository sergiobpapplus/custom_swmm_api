from swmm_api import read_out_file, swmm5_run
from swmm_api.output_file import OBJECTS, VARIABLES


# Example for OUT File Reader

# swmm5_run('epaswmm5_apps_manual/Example6-Final.inp')

out = read_out_file('epaswmm5_apps_manual/Example6-Final.out')

# read all node heads using the python engine (slower but able to read huge files)
d = out.get_part(OBJECTS.NODE, None, VARIABLES.NODE.HEAD, slim=True)

# read all node heads using the numpy (C) engine (faster but uses a lot of memory for huge file and thus may fail)
d2 = out.get_part(OBJECTS.NODE, None, VARIABLES.NODE.HEAD, slim=False)

# testing start and end times for sliced reading
start = d.index[123]
end = d.index[982]

# reading data for a specific time range
d2_ = out.get_part(OBJECTS.NODE, None, VARIABLES.NODE.HEAD, slim=False, start=start, end=end)

d_ = out.get_part(OBJECTS.NODE, None, VARIABLES.NODE.HEAD, slim=True, start=start, end=end)
exit()
# n_cols = 1612
# c: 10s
# py: 28s
# ---
# n_cols = 9672
# c: 51s
# py: 2m 40s

out.get_part(OBJECTS.NODE, 'J1', VARIABLES.NODE.HEAD, slim=True, processes=2)

out.get_part(OBJECTS.NODE, 'J1', VARIABLES.NODE.HEAD).to_frame()
out.get_part(OBJECTS.NODE, ['J1', 'J23fsd'], VARIABLES.NODE.HEAD).to_frame()
out.get_part(OBJECTS.NODE, ['J1', 'J23fsd'], [VARIABLES.NODE.HEAD, 'fj1e']).to_frame()

# get all data as pandas.DataFrame
out.to_frame()

# get a specific part of the out data as pandas.Series
out.get_part(OBJECTS.NODE, 'J1', VARIABLES.NODE.HEAD).to_frame()

# to get all data of a node, just remove the variable part
out.get_part(OBJECTS.NODE, 'J1')

# other functions
out.filename

out.variables

out.labels

out.number_columns

type(out.to_numpy())
