import requests
from pathlib import Path

# Need to specify root CA certificate to get SSL to work.

# https://incognitjoe.github.io/adding-certs-to-requests.html

url = "https://vincentarelbundock.github.io/Rdatasets/csv/datasets/mtcars.csv"
ca_path_in = Path('~/certs/rootca.cer').expanduser()
ca_path_out = ca_path_in.with_suffix('.pem')

# !openssl x509 -inform der -in $ca_path_in -out $ca_path_out

import requests

r = requests.get(url, verify=ca_path_out)

with open('../data/raw/mtcars.csv', 'w') as f:
    f.write(r.content.decode())
