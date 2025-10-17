import sys, os
sys.path.insert(0, os.path.abspath("_ext"))

project = 'PotatoOS'
copyright = '2025, The Potato Corporation'
author = 'The Potato Corporation'

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_copybutton",
    "starch_lexer"
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ["highlight.css"]