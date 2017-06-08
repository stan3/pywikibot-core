# -*- coding: utf-8 -*-
"""Family module for Wikimedia Commons Beta."""
#
# (C) Pywikibot team, 2005-2015
#
# Distributed under the terms of the MIT license.
#
from __future__ import absolute_import, unicode_literals

__version__ = '$Id$'

import commons_family


# The Wikimedia Commons Beta family
class Family(commons_family.Family):

    """Family class for Wikimedia Commons Beta."""

    name = 'betacommons'
    domain = 'commons.wikimedia.beta.wmflabs.org'
