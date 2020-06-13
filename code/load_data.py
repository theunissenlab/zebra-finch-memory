import os

import pandas as pd


CODEDIR, _ = os.path.split(__file__)
DATADIR = os.path.join(CODEDIR, "..")


def load_data():
    return pd.read_csv(os.path.join(DATADIR, "TrialData.csv"))
