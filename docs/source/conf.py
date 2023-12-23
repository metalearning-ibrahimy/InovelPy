# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'InovelPy'
copyright = '2023, Rahman'
author = 'Rahman'

release = '1.0'
version = '1.0.1'

# -- General configuration

autosectionlabel_prefix_document = True

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.bibtex',
]

bibtex_bibfiles = ['refs.bib']
bibtex_default_style = 'unsrt'
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
