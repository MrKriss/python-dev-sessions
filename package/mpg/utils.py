
from pathlib import Path

import json


def load_config(filepath=None):

    if filepath is None:
        # Specifying the config.json filepath to be in relation to this utils.py file
        filepath = Path(__file__).parent / 'config.json'

    return json.load(open(filepath))
