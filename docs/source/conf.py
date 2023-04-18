# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Koble Systems'
copyright = 'Copyright 2023 |Koble Systems, Inc. | 350 New Holland Ave., Lancaster PA'
author = 'Koble Systems'

release = '0.1'
version = ' '

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
    'recommonmark',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
import sphinx_rtd_theme

html_show_sphinx = False
html_show_sourcelink = False

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
html_css_files = ['custom.css']

# -- Options for EPUB output
epub_show_urls = 'footnote'
