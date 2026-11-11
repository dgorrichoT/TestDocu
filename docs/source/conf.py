import os
import re
import subprocess

# Información del proyecto
project = 'Documentation POC'
copyright = '2026, Tracasa'
author = 'David Gorricho'

docs_section = os.environ.get("DOCS_SECTION", "")
docs_version = os.environ.get("DOCS_VERSION", "")
docs_versions = []

if docs_section and docs_version:
    tag_pattern = re.compile(rf"^{re.escape(docs_section)}-(\d+\.\d+\.\d+)$")
    tags = subprocess.run(
        ["git", "tag", "--list", f"{docs_section}-*"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    docs_versions = sorted(
        (match.group(1) for tag in tags if (match := tag_pattern.fullmatch(tag))),
        key=lambda version: tuple(int(part) for part in version.split(".")),
    )

html_context = {
    "docs_section": docs_section,
    "docs_version": docs_version,
    "docs_versions": docs_versions,
}

# Extensiones: MyST es para Markdown, rtd es el tema visual
extensions = [
    'myst_parser',
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

html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/version-switcher.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
        "sidebar/variant-selector.html",
    ]
}

# Permitir archivos .md y .rst
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}