
from pathlib import Path
import pandas as pd


def load(path):
    """Load data from a csv"""

    csv_path = Path(path)
    df = pd.read_csv(csv_path)

    return df


def clean(df):

    new = df.copy()

    new.columns = [
        'MakeModel', 'Mpg', 'Cyl', 'Disp', 'Hp', 'Drat',
        'Wt', 'Qsec', 'Vs', 'Am', 'Gear', 'Carb'
    ]

    return new
