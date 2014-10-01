# coding=utf8
from __future__ import unicode_literals;from willie import web;from willie.module import commands;import xml.etree.ElementTree as ET
@commands('nieuws')
def nieuws(bot, trigger): bot.say(ET.fromstring(web.get('http://www.demorgen.be/nieuws/rss.xml')).find('channel/item/title').text)
def nieuws(bot, trigger): bot.say(ET.fromstring(web.get('http://www.demorgen.be/nieuws/rss.xml')).find('channel/item/link').text)