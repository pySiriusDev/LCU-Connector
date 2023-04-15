# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
# import sys
# sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'LCU Connector'
copyright = '2023, Gabriel Viana'
author = 'Gabriel Viana'
release = '1.0.0'
language = "en"


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_autodoc_typehints',
    'autoapi.extension',
    'sphinx_design',
    'sphinx_togglebutton',
    'sphinx.ext.napoleon',
    'sphinx.ext.githubpages',
    'sphinx_copybutton',
    'sphinx_sitemap',
    'myst_parser',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode'
]

autosummary_generate = True

autodoc_typehints = 'description'

autoapi_dirs = ['../../lcu_connector/']
autoapi_root = 'api'
autoapi_keep_files = True
autoapi_python_class_content = 'class'
autoapi_member_order = 'bysource'
autoapi_options = [
    'members',
    'show-inheritance',
    'show-module-summary',
    'imported-members'
]

templates_path = ['_templates']
exclude_patterns = ['riotgames.pem']

html_baseurl = os.environ.get("SPHINX_HTML_BASE_URL", "http://127.0.0.1:8000/")
sitemap_locales = [None]
sitemap_url_scheme = "{link}"

todo_include_todos = True

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
    "strikethrough",
    "substitution",
    "tasklist",
    "attrs_inline",
    "attrs_block",
]

# SWITCHER CONFIG HERE


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ['css/style.css']
html_logo = f'_static/logo.png'
html_favicon = f'_static/logo.png'
html_show_sourcelink = False

html_theme_options = {
    'logo': {
        'image_light': '_static/logo.png',
        'image_dark': '_static/logo.png',
        'text': 'LCU Connector'
    },
    'search_bar_text': 'Search the docs...',
    'navbar_start': ['navbar-logo', 'navbar-nav'],
    'navbar_end': ['theme-switcher', 'navbar-icon-links'],
    'navbar_persistent': ['search-button'],
    'show_nav_level': 2,
    'external_links': [],
    'icon_links_label': 'Social Links',
    'icon_links': [
        {
            'name': 'GitHub',
            'url': 'https://github.com/pySiriusDev',
            'icon': 'fa-brands fa-square-github',
            'type': 'fontawesome',
            'attributes': {
                'target': '_blank'
            }
        },
        {
            'name': 'Instagram',
            'url': 'https://www.instagram.com/biellviana/',
            'icon': 'fa-brands fa-square-instagram',
            'type': 'fontawesome',
            'attributes': {
                'target': '_blank'
            }
        },
        {
            'name': 'Twitter',
            'url': 'https://twitter.com/_siriusbeck',
            'icon': 'fa-brands fa-square-twitter',
            'type': 'fontawesome',
            'attributes': {
                'target': '_blank'
            }
        }
    ],
    'use_edit_page_button': False,
    'pygment_light_style': 'colorful',
    'pygment_dark_style': 'dracula'
}

html_context = {
    'default_mode': 'auto'
}
