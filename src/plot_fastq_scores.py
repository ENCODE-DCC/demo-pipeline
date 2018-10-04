#!/usr/bin/env python

# Plots quality score boxplot by base position for FASTQ before and after trimming.

import argparse
import gzip
import logging

from Bio import SeqIO
from collections import namedtuple
import matplotlib.pyplot as plt
import seaborn as sns


ReadBase = namedtuple('ReadBase', ['position', 'quality_score'])


def read_fastq_scores(filepath):
    with gzip.open(filepath, 'rt') as f:
        for i, rec in enumerate(SeqIO.parse(f, 'fastq')):
            yield rec.letter_annotations['phred_quality']


def bin_quality_scores(bin_data, vals):
    for pos, qual in enumerate(vals):
        bin_data.append(ReadBase(position=pos, quality_score=qual))
    return bin_data


def gather_scores_for_fastq(filepath):
    bin_data = []
    for vals in read_fastq_scores(filepath):
        bin_data = bin_quality_scores(bin_data, vals)
    return bin_data


def plot_boxplot(bin_data, ax):
    sns.boxplot(
        x=[
            r.position
            for r in bin_data
        ],
        y=[
            r.quality_score
            for r in bin_data
        ],
        color='white',
        ax=ax
    )


def plot_quality_score_by_position(untrimmed_bin_data, trimmed_bin_data):
    sns.set_style('darkgrid')
    fig, axes = plt.subplots(2, 1, sharey=True, sharex=True, figsize=[18, 10])
    plot_boxplot(untrimmed_bin_data, axes[0])
    plot_boxplot(trimmed_bin_data, axes[1])
    axes[0].set_title('Quality score by base position before trimming')
    axes[1].set_title('Quality score by base position after trimming')
    return fig


def save_plot(fig, trimmed_name, untrimmed_name):
    fig.savefig(
        'untrimmed_trimmed_quality_scores_{}_{}.pdf'.format(
            untrimmed_name,
            trimmed_name,
        ),
        bbox_inches='tight'
    )


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
