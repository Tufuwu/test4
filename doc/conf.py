# -*- coding: utf-8 -*-

import sys, os

try:
    from unittest.mock import MagicMock
except ImportError:
    try:
        from mock import Mock as MagicMock
    except ImportError as e:
        print("mock is missing: pip install mock")
        raise e

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__), "..")))

# Mock out aerospike,
# see https://docs.readthedocs.io/en/latest/faq.html#i-get-import-errors-on-libraries-that-depend-on-c-modules


class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()


sys.modules.update({"aerospike": Mock()})

# sys.path.append(os.path.abspath('/usr/local/lib/python2.7/site-packages/aerospike-1.0.44-py2.7-macosx-10.9-x86_64.egg/'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
]
napoleon_google_docstring = True
intersphinx_mapping = {"python": ("https://docs.python.org/3.8", None)}

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = u"Aerospike"
copyright = u"2014-2021, Aerospike"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# version = '1.0.40'
# The full version, including alpha/beta/rc tags.
# release = '1.0.40'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
# unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# Alias/type hint configuration.
autodoc_typehints = "signature"
autodoc_type_aliases = {
    "_BaseExpr": "AerospikeExpression",
    "TypeCTX": "TypeCTX",
    "TypeRank": "TypeRank",
    "TypeCount": "TypeCount",
    "TypePolicy": "TypePolicy",
    "TypeValue": "TypeValue",
    "TypeBinName": "TypeBinName",
    "TypeListValue": "TypeListValue",
    "TypeIndex": "TypeIndex",
    "TypeChild": "TypeChild",
    "TypeCompiledOp": "TypeCompiledOp",
    "TypeExpression": "TypeExpression",
    "TypeGeo": "TypeGeo",
    "TypeKey": "TypeKey",
    "TypeKeyList": "TypeKeyList",
    "TypeBitValue": "TypeBitValue",
    "TypeNumber": "TypeNumber",
    "TypeFloat": "TypeFloat",
    "TypeInteger": "TypeInteger",
    "TypeBool": "TypeBool",
    "TypeComparisonArg": "TypeComparisonArg",
    "TypeResultType": "TypeResultType",
    "TypeFixedEle": "TypeFixedEle",
    "TypeFixed": "TypeFixed",
}

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
# Using the Sphinx readthedocs theme, get it first:
# pip3 install sphinx-rtd-theme
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# html_context = {
#    'css_files': [
#        '_static/theme_overrides.css',  # override wide tables in RTD theme
#    ]
# }

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_use_modindex = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = "aerospikehelp"


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
# latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ("index", "aerospike.tex", u"aerospike Documentation", u"Ronen Botzer", "manual"),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_use_modindex = True


# -- Options for sphinx.ext.todo -----------------------------------------------

todo_include_todos = True
