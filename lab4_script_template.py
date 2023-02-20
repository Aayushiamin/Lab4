import os
import re
import sys

import pandas as pd 

def main():
    log_file = get_log_file_path_from_cmd_line(1)
    dpt_tally = tally_port_traffic(log_file)

    for dpt, count in dpt_tally.items():
        if count > 100:
            generate_port_traffic_report(log_file, dpt)

    pass

    

# TODO: Step 3
def get_log_file_path_from_cmd_line():
    File = open(log_file)
    log_data = File
    File.close()

    


    return

# TODO: Steps 4-7
def filter_log_by_regex(log_file, regex, ignore_case=True, print_summary=False, print_records=False):
    """Gets a list of records in a log file that match a specified regex.
    Args:
        log_file (str): Path of the log file
        regex (str): Regex filter
        ignore_case (bool, optional): Enable case insensitive regex matching. Defaults to True.
        print_summary (bool, optional): Enable printing summary of results. Defaults to False.
        print_records (bool, optional): Enable printing all records that match the regex. Defaults to False.

    Returns:
        (list, list): List of records that match regex, List of tuples of captured data
    """
    records = []

    regex_flags = re.IGNORECASE if ignore_case else 0 

    with open(log_file, 'r') as file:
        for line in file:
            match = re.search(regex, line)
            if match:
                records.append(line)

    if print_records is True:
        print(*records, sep='')

    if print_summary is True:
        print(f'The log file contains {len(records)} records that case-insensitive match the regex "{regex}".')

    return records

# TODO: Step 8
def tally_port_traffic(log_file):
    dest_port_logs = filter_log_by_regex(log_file, 'DPT=(.+?) ')[1]

    dpt_tally = {}
    for dpt_tuple in dest_port_logs:
        dpt_num = dpt_tuple[0]
        dpt_tally[dpt_num] = dpt_tally.get(dpt_num, 0) + 1

    return dpt_tally

# TODO: Step 9
def generate_port_traffic_report(log_file, port_number):
    
    regex = r"^(.{6}) (.{8}).*SRC=(.+?) DST=(.+?) .*SPT=(.+?) " + f"DPT=({port_number})"
    captured_data = filter_log_by_regex(log_file, regex)[1]
    report_df = pd.DataFrame(captured_data)
    report_header = ('Date', 'Time', 'Source IP Address', 'Destination IP Address',)
    report_df.to_csv(f'destination_port_{port_number}_report.csv', index=False, header=False)

    return

# TODO: Step 11
def generate_invalid_user_report(log_file):
    regex = r"^([a-zA-Z]{3} /d+) ([0-9:]{8}).*Invalid user ([a-zA-Z0-9]+) from 9[0-9\.]+)"
    data = filter_log_by_regex(log_file, regex)

    return

# TODO: Step 12
def generate_source_ip_log(log_file, ip_address):
    return

if __name__ == '__main__':
    main()