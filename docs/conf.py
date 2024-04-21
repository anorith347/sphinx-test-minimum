# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# ソースコードのパスを指定
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "mymodule"
copyright = "2024, anorith347"
author = "anorith347"
release = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # ソースコード読み込み用
    "numpydoc",  # docstring パース用
    "sphinx_rtd_theme",  # Read the Docs テーマ
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Read the Docs テーマを設定
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
