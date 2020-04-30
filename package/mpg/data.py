
from pathlib import Path
import pandas as pd


def load(path):
    """Load data from a csv"""

    csv_path = Path(path)
    df = pd.read_csv(csv_path)

    return df


def clean(df):
    """Return cleaned dataset.

    1. Renamed columns to be more memorable

    Reference::
        https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/mtcars.html

    """

    new = df.copy()

    new = rename_columns(new)

    return new


def rename_columns(df):
    """Return dataframe with more interpretable names"""

    new = df.copy()

    new = new.rename(columns={
        "Unnamed: 0": "MakeModel",
        'mpg': 'Mpg',
        'cyl': 'Cylinders',
        'disp': 'Displacement',
        'hp': 'HorsePower',
        'drat': 'RearAxelRatio',
        'wt': 'Weight',
        'qsec': 'QuaterMileTime',
        'vs': 'EngineShape',
        'am': 'Transmission',
        'gear': 'Gears',
        'carb': 'Carburetors'
    })

    return new


def split_make_model_column(df):
    """Return dataframe with make and model in seperate columns"""

    new = df.copy()

    new_columns = new["MakeModel"].str.split(n=1, expand=True)
    new_columns.columns = ["Make", "Model"]
    new = pd.concat([new_columns, new], axis=1)

    return new
