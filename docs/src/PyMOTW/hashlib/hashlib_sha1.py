#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Simple SHA1 generation.
"""

__version__ = "$Id$"
#end_pymotw_header

import hashlib

from hashlib_data import lorem

h = hashlib.sha1()
h.update(lorem)
print h.hexdigest()
