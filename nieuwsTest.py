#!/usr/bin/env python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals;from willie import web;from willie.module import commands;import xml.etree.ElementTree as ET
@commands('nieuwsT')
def nieuws(bot, trigger):
	content = unicode((ET.fromstring(web.get('http://www.demorgen.be/nieuws/rss.xml')).find('channel/item/title').text).content.strip(codecs.BOM_UTF8), 'utf-8')
	parser.parse(StringIO.StringIO(content))
	bot.say(content)