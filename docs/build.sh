#!/usr/bin/env bash
rm -rf _build
pyenv activate env2.7.11
make gettext
sphinx-intl update -l fa -p _build/locale

sphinx-intl build
make -e SPHINXOPTS="-D language='fa'" html
