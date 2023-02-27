import io
import os
from os import path
from pathlib import Path
import zipfile

if(not path.isfile('galaxy-zoo-the-galaxy-challenge.zip')):
    os.system('kaggle competitions download -c galaxy-zoo-the-galaxy-challenge')

if(not path.exists(path.join('galaxy-zoo-the-galaxy-challenge', 'data'))):
    Path(path.join('galaxy-zoo-the-galaxy-challenge', 'data')).mkdir(parents=True, exist_ok=True)

with zipfile.ZipFile('galaxy-zoo-the-galaxy-challenge.zip', 'r') as zip_ref:
    for f in zip_ref.namelist():
        content = io.BytesIO(zip_ref.read(f))
        with zipfile.ZipFile(content, 'r') as zip_file:
            zip_file.extractall(path.join('galaxy-zoo-the-galaxy-challenge', 'data'))