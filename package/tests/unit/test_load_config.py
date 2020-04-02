
from pathlib import Path
from mpg.utils import load_config

import pytest

TEST_DATA_DIR = Path(__file__).parent / 'data'


def test_load_config():

    # When
    config = load_config()

    # Then
    assert type(config) == dict
    assert "datetime_format" in config


@pytest.mark.skip("Work in progress")
def test_load_test_config():

    # Given
    test_file = TEST_DATA_DIR / 'test_config.json'

    # When
    # TODO: add function that uses this

    # Then
    # assert type(config) == dict
    # assert "datetime_format_foo" in config
