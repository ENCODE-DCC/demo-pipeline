#!/usr/bin/env python3

# Plots quality score boxplot by base position for FASTQ before and after trimming.

import argparse
import gzip
import logging

from Bio import SeqIO
from collections import namedtuple
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns


ReadBase = namedtuple('ReadBase', ['position', 'quality_score'])


def read_fastq_scores(filepath):
    logging.debug('Opening FASTQ {}'.format(filepath))
    with gzip.open(filepath, 'rt') as f:
        for i, rec in enumerate(SeqIO.parse(f, 'fastq')):
            # Only sample first 10,000.
            if i == 10000:
                break
            yield rec.letter_annotations['phred_quality']


def bin_quality_scores(bin_data, vals):
    for pos, qual in enumerate(vals):
        bin_data.append(ReadBase(position=pos, quality_score=qual))
    return bin_data


def gather_scores_for_fastq(filepath):
    logging.debug('Gathering scores for {}'.format(filepath))
    bin_data = []
    for i, vals in enumerate(read_fastq_scores(filepath)):
        bin_data = bin_quality_scores(bin_data, vals)
    return i, bin_data


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


def space_xticklabels(ax):
    for i, label in enumerate(ax.get_xticklabels()):
        if i % 5 != 0:
            label.set_visible(False)


def set_x_axis(ax0, ax1):
    ax0_ticks = ax0.get_xticks()
    ax0_ticklabels = ax0.get_xticklabels()
    ax1_ticks = ax1.get_xticks()
    ax1_ticklabels = ax1.get_xticklabels()
    if len(ax0_ticks) >= len(ax1_ticks):
        ax1.set_xticks(ax0_ticks)
        ax1.set_xticklabels(ax0_ticklabels)
    else:
        ax0.set_xticks(ax1_ticks)
        ax0.set_xticklabels(ax1_ticklabels)


def plot_quality_score_by_position(untrimmed_bin_data, trimmed_bin_data):
    logging.debug('Creating plot')
    sns.set_style('darkgrid')
    fig, axes = plt.subplots(2, 1, sharey=True, figsize=[18, 10])
    plot_boxplot(untrimmed_bin_data, axes[0])
    plot_boxplot(trimmed_bin_data, axes[1])
    axes[0].set_title('Quality score by base position before trimming')
    axes[1].set_title('Quality score by base position after trimming')
    axes[0].get_shared_x_axes().join(axes[0], axes[1])
    set_x_axis(axes[0], axes[1])
    space_xticklabels(axes[0])
    space_xticklabels(axes[1])
    axes[0].xaxis.set_tick_params(which='both', labelbottom=False)
    return fig


def parse_file_name(filepath):
    return '_'.join(
        [
            f.split('.')[0]
            for f in filepath.split('/')
            if 'fastq' in f
        ]
    )


def save_plot(figure, untrimmed_name, trimmed_name):
    logging.debug('Saving plot')
    figure.savefig(
        '{}_untrimmed_{}_trimmed_quality_scores.pdf'.format(
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
        required=True,
    )
    parser.add_argument(
        '-t', '--trimmed',
        help='Path to trimmed FASTQ.',
        required=True,
    )
    return parser.parse_args()


def main():
    args = get_args()
    logging.basicConfig(level=args.log_level)
    untrimmed_count, untrimmed_bin_data = gather_scores_for_fastq(args.untrimmed)
    trimmed_count, trimmed_bin_data = gather_scores_for_fastq(args.trimmed)
    print('Count', untrimmed_count, trimmed_count)
    figure = plot_quality_score_by_position(untrimmed_bin_data, trimmed_bin_data)
    save_plot(figure, parse_file_name(args.untrimmed), parse_file_name(args.trimmed))


if __name__ == '__main__':
    main()
