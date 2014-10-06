import feedparser,time,willie
@willie.module.commands('nieuwsT')
def nieuws(bot, trigger):
    url = "http://www.demorgen.be/nieuws/rss.xml"
    feed = str(feedparser.parse( url ))
    bot.say(feed)
    bot.say("end")
    time.sleep(20)
