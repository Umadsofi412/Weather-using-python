# -*- coding: utf-8 -*-
"""requests.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w2dZ-BCWygyPSk2SXfxv3suHS3ucysr0
"""

import requests

r = requests.get('https://imgs.xkcd.com/comics/circuit_diagram.png')

with open('comic.png','wb') as f: 
        f.write(r.content)