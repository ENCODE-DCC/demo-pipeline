#!/usr/bin/env python

# Plots quality score boxplot by base position for FASTQ before and after trimming.

import argparse
import logging


def get_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        '-d', '--debug',
        help='Print debug messages.',
        action='store_const',
        dest='log_level',
        const=logging.DEBUG,
        default=logging.WARNING
    )
    parser.add_argument(
        '-u', '--untrimmed',
        help='Path to untrimmed FASTQ.',
    )
     parser.add_argument(
        '-t', '--trimmed',
        help='Path to trimmed FASTQ.',
    )
    return parser.parse_args()


def main():
    args = get_args()
    logging.basicConfig(level=args.log_level)


if __name__ == '__main__':
    main()
