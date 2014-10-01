#!/usr/bin/env python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals;from willie import web;from willie.module import commands;import xml.etree.ElementTree as ET
@commands('nieuws')
inputtext = ""
output = ""
def nieuws(bot, trigger): 
	inputtext = ET.fromstring(web.get('http://www.demorgen.be/nieuws/rss.xml')).find('channel/item/title').text.decod('ascii')
	bot.say(inputtext)
