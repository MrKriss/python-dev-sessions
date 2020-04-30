
import pytest
import pandas as pd

from mpg.data import split_make_model_column


@pytest.fixture(scope='session')
def test_data():
    return pd.DataFrame({
        'MakeModel': [
            'Mazda RX4',
            'Mazda RX4 Wag',
            'Datsun 710',
            'Hornet 4 Drive',
            'Hornet Sportabout',
        ],
        'Mpg': [21.0, 21.0, 22.8, 21.4, 18.7],
        'Cylinders': [6, 6, 4, 6, 8],
        'Displacement': [160.0, 160.0, 108.0, 258.0, 360.0],
        'HorsePower': [110, 110, 93, 110, 175],
        'RearAxelRatio': [3.9, 3.9, 3.85, 3.08, 3.15],
        'Weight': [2.62, 2.875, 2.32, 3.215, 3.44],
        'QuaterMileTime': [16.46, 17.02, 18.61, 19.44, 17.02],
        'EngineShape': [0, 0, 1, 1, 0],
        'Transmission': [1, 1, 1, 0, 0],
        'Gears': [4, 4, 4, 3, 3],
        'Carburetors': [4, 4, 1, 1, 2]
    })


def test_split_make_model(test_data):

    # When
    new = split_make_model_column(test_data)

    # Then
    assert "Make" in new.columns
    assert "Model" in new.columns

    assert new["Make"].tolist() == [
        'Mazda',
        'Mazda',
        'Datsun',
        'Hornet',
        'Hornet',
    ]
