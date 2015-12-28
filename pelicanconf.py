#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jon Moore'
SITENAME = u'offduty pirate'
SITETITLE = u'offdutypirate'
SITESUBTITLE = u'One guys personal blog'
SITEDESCRIPTION = u'%s\'s Personal Blog' % AUTHOR
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Archives', '/archives.html'),)

# Social widget
#SOCIAL = (('Github', 'https://github.com/offdutypirate'),
#         ('Twitter', 'https://twitter.com/offdutypirate'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = ['images']
THEME='./theme/'

# Theme Options
SITELOGO = 'http://s.gravatar.com/avatar/1017f383d5407116b6b468d01aee41ed'
SITEDESCRIPTION = 'My Blog'
MAIN_MENU = False
MENUITEMS = (('Archives', '/archives.html'),)
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

USE_LESS = True