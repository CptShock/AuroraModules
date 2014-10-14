import feedparser,time,willie
@willie.module.commands('nieuwsT')
def nieuws(bot,trigger):
    url = 'http://www.demorgen.be/nieuws/rss.xml'
    feed = feedparser.parse(url)
    bot.say(str(feed.feed.title))
    try:
        bot.say(str(feed.entries[int(trigger.group(2))].title))
        bot.say(str(feed.entries[int(trigger.group(2))].link))
    except:
        bot.say("try another number")
