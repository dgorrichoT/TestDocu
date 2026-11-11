import os
import re
import subprocess

# Información del proyecto
project = 'Documentation POC'
copyright = '2026, Tracasa'
author = 'David Gorricho'

docs_section = os.environ.get("DOCS_SECTION", "")
docs_version = os.environ.get("DOCS_VERSION", "")
release_pattern = re.compile(r"^(furo-theme-showcase|use-guidance)-(\d+\.\d+\.\d+)$")
release_tags = subprocess.run(
    ["git", "tag", "--list"], check=True, capture_output=True, text=True
).stdout.splitlines()
versions_by_section = {"furo-theme-showcase": [], "use-guidance": []}

for tag in release_tags:
    match = release_pattern.fullmatch(tag)
    if match:
        versions_by_section[match.group(1)].append(match.group(2))

for versions in versions_by_section.values():
    versions.sort(key=lambda version: tuple(int(part) for part in version.split(".")))

docs_versions = versions_by_section.get(docs_section, [])
latest_versions = {
    section: versions[-1]
    for section, versions in versions_by_section.items()
    if versions
}

html_context = {
    "docs_section": docs_section,
    "docs_version": docs_version,
    "docs_versions": docs_versions,
    "latest_versions": latest_versions,
}

if docs_section and docs_version:
    if docs_version not in docs_versions:
        raise ValueError(f"Tag {docs_section}-{docs_version} is not available in Git")

templates_path = ["_templates"]
html_static_path = ["_static"]
html_logo = "_static/logo.png"

# Extensiones: MyST es para Markdown, rtd es el tema visual
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
]

exclude_patterns = []

# Configuración del tema
html_theme = 'furo'
html_css_files = [
    'custom.css',
]

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
        "sidebar/sections.html",
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