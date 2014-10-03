import feedparser,time,willie
@commands('nieuwsT')
def nieuws(bot, trigger):
	url = "http://www.demorgen.be/nieuws/rss.xml"
	feed = feedparser.parse( url )
	bot.say(feed)
	bot.say("end")
	time.sleep(20)
