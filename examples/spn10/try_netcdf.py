from netCDF4 import Dataset

from swmm_api import SwmmOutput
from swmmtonetcdf import create_netcdf_from_swmm


def main():
    out = SwmmOutput('Example6-Final.out')
    out.to_netcdf('first_test.nc')
    # nc = Dataset('Example6-Final.nc', "r", format="NETCDF4")

    # create_netcdf_from_swmm('Example6-Final.out', 'Example6-Final.nc')


if __name__ == '__main__':
    main()
