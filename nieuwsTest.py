import feedparser
@commands('nieuwsT')
def nieuws(bot, trigger):
	url = "http://www.demorgen.be/nieuws/rss.xml"
	feed = feedparser.parse(nurl )
	bot.say(feed)
	bot.say("end")
    
    
