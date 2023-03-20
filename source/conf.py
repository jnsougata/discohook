import os
import sys

sys.path.insert(0, os.path.abspath('..'))

project = 'Discohook'
copyright = '2023, Sougata Jana'
author = 'Sougata Jana'
release = '0.0.5'


templates_path = ['_templates']
exclude_patterns = []

html_theme = 'furo'
html_static_path = ['_static']

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx.ext.napoleon']
