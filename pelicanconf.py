#!/usr/bin/env python
"""This is the configuration file of the blog """
from __future__ import unicode_literals

# pylint: disable=unused-wildcard-import
# -*- coding: utf-8 -*- #

AUTHOR = u'flety'
SITENAME = u'myawesomeblog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('My real blog that I don\'t maintain', 'https://damfle.github.io/'),
         ('Test repo', 'https://gitlab.com/flety1/myawesomeblog'),
         ('This but built htmls', 'https://github.com/flety/flety.github.io'),)


# Social widget
SOCIAL = None
DEFAULT_PAGINATION = 10
REVERSE_CATEGORY_ORDER = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
