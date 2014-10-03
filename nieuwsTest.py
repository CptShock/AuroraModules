<<<<<<< HEAD
import feedparser,time,willie
=======
import willie
import feedparser
>>>>>>> 83c99e723d85c8a52066a9da9033c7f200bb9edc
@commands('nieuwsT')
def nieuws(bot, trigger):
	url = "http://www.demorgen.be/nieuws/rss.xml"
	feed = feedparser.parse( url )
	bot.say(feed)
	bot.say("end")
	time.sleep(20)
