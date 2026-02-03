import os
import sys

# Información del proyecto
project = 'Documentation POC'
copyright = '2026, Tracasa'
author = 'David Gorricho'

# Extensiones: MyST es para Markdown, rtd es el tema visual
extensions = [
    'myst_parser',
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']
exclude_patterns = []

# Configuración del tema
html_theme = 'furo'
html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

html_logo = "_static/logo.png"

html_theme_options = {
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
}

# Permitir archivos .md y .rst
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}