"""Commonly-used functions
"""

import sys
import json
import numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer

RANDOM_SEED = 1337
DATA_PATH = None


def load_raw():
    """Load tsv into raw DataFrame
    """
    df = pd.read_table(DATA_PATH)
    return df


def append_kmer_dict_df(df, seq_colname):
    """Given the data frame and the name of the column containing sequence data
    returns a sparse two-dimensional matrix
    """
    seqs = df[seq_colname]
    kmerdicts = map(lambda x: get_kmer_freqs(x), seqs)
    vec = DictVectorizer()
    kmervectorized = vec.fit_transform(kmerdicts)
    return kmervectorized


def get_kmer_freqs(seq, k=3):
    """Return a dictionary of all k-mers in a sequence
    """
    kmer_freqs = dict()
    stop_idx = len(seq) - 2
    for seq_idx in range(0, stop_idx):
        kmer = seq[seq_idx:seq_idx + k]
        if kmer not in kmer_freqs:
            kmer_freqs[kmer] = 1
        else:
            kmer_freqs[kmer] += 1
    return kmer_freqs


def load_and_group_by(df, colname):
    """Wrapper around df group by column name
    """
    return df.groupby(colname)


if __name__ == "__main__":
    """Just for debugging (won't run if imported from somewhere else).
    Could alternatively debug in an IPython REPL.
    """
    DATA_PATH = sys.argv[1]
    df = load_raw()
    grouped = load_and_group_by(df, "gene_name")
    print df.head()
    print(json.dumps(grouped,
                     default=lambda obj: vars(obj),
                     indent=1))
