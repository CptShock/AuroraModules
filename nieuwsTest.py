#!/usr/bin/env python
# -*- coding: latin-1 -*-
import feedparser
@commands('nieuwsT')
def nieuws(bot, trigger):
	python_wiki_rss_url = "http://www.python.org/cgi-bin/moinmoin/" \
                      "RecentChanges?action=rss_rc"
    feed = feedparser.parse( python_wiki_rss_url )
    bot.say(feed)
    