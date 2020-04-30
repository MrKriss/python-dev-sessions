
from pathlib import Path
from mpg.utils import load_config


TEST_DATA_DIR = Path(__file__).parent.parent / 'data'


def test_load_config():

    # When
    config = load_config()

    # Then
    assert type(config) == dict
    assert "datetime_format" in config


def test_load_test_config():

    # Given
    test_config = TEST_DATA_DIR / 'test_config.json'

    # When
    config = load_config(test_config)

    # Then
    assert type(config) == dict
    assert config["datetime_format"] == "%Y-%m-%d %H:%M:%S"
