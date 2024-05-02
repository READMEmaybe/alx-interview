#!/usr/bin/python3
""" log parser"""
import sys


def print_stats(total_size, status_codes):
    """
    Prints the file size and the count of each status code.

    Args:
        total_size (int): The total size of the file.
        status_codes (dict):
                A dictionary containing the count of each status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line):
    """
    Parses a log line and extracts the status code and file size.

    Args:
        line (str): The log line to parse.

    Returns:
        tuple: A tuple containing the status code and file size,
                    or (None, None) if the line is invalid.
    """
    parts = line.split()
    if len(parts) >= 7:
        status_code = parts[-2]
        file_size = parts[-1]
        if status_code.isdigit() and file_size.isdigit():
            return int(status_code), int(file_size)
    return None, None


def log_parser():
    """
    Parses log lines from standard input and prints statistics.

    Returns:
        None
    """
    total_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            if status_code is not None and file_size is not None:
                total_size += file_size
                status_codes[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


log_parser()
