import pytest

import matplotlib
matplotlib.use('agg')


def test_read_fastq_scores():
    from plot_fastq_scores import read_fastq_scores
    scores = [
        sum(s)
        for s in read_fastq_scores('test/test_data/small.fastq.gz')
    ]
    assert scores == [1714, 2150, 3288, 1549, 3163]


def test_bin_quality_scores():
    from plot_fastq_scores import (
        bin_quality_scores,
        ReadBase
    )
    bin_data = []
    vals = [44, 127, 900]
    bin_data = bin_quality_scores(bin_data, vals)
    assert bin_data == [
        ReadBase(position=0, quality_score=44),
        ReadBase(position=1, quality_score=127),
        ReadBase(position=2, quality_score=900)
    ]


def test_gather_scores_for_fastq():
    from plot_fastq_scores import (
        gather_scores_for_fastq,
        ReadBase
    )
    count, scores = gather_scores_for_fastq('test/test_data/small.fastq.gz')
    assert count == 4
    assert len(scores) == 384
    assert scores[0] == ReadBase(position=0, quality_score=29)


def test_parse_file_name():
    from plot_fastq_scores import parse_file_name
    assert parse_file_name('../../ABC123.fastq.gz') == 'ABC123'
    assert parse_file_name('../../trimmed.ABC123.fastq.gz') == 'ABC123'
