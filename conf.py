# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Verizon FiOS Customer Help'
copyright = '2025, Verizon FiOS Help'
author = 'Verizon FiOS Help Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

# Allow raw HTML in .rst files
raw_enabled = True
suppress_warnings = ['raw-html']

# Patterns to ignore
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output settings ----------------------------------------------------

# Title shown in browser and at top of pages
html_title = "Verizon FiOS Customer Service Phone Number for 24-Hour Support"

# Optional short title
html_short_title = "FiOS 24/7 Support Info"

# Favicon file (optional)
html_favicon = 'favicon.ico'

# Use a clean and readable theme
# html_theme = 'sphinx_rtd_theme'

# Hide "View page source"
html_show_sourcelink = False

# Theme customization options
html_theme_options = {
    'display_version': False,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'style_nav_header_background': '#da1f26',  # Verizon red
    'navigation_depth': 3,
}

# Uncomment if you use static files or templates
templates_path = ['_templates']
# html_static_path = ['_static']
