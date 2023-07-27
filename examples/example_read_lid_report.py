import pandas as pd

from swmm_api.report_file.lid_rpt import read_lid_report


def main():
    df = read_lid_report(r'epaswmm5_apps_manual\Example6-Final_AllSections_GUI\Example6-Final_AllSections_GUI_S5_LID_report.txt')
    elapsed_time = pd.to_timedelta(df['Elapsed_Time_Hours'], unit='h')
    print(df)


if __name__ == '__main__':
    main()
