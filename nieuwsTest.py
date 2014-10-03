#!/usr/bin/env python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals;from willie import web;from willie.module import commands;import xml.etree.ElementTree as ET;import codecs
@commands('nieuwsT')
def nieuws(bot, trigger):
	text = ET.fromstring(web.get('http://www.demorgen.be/nieuws/rss.xml')).find('channel/item/title').text.encode('ascii', ignore)
	bot.say(text)