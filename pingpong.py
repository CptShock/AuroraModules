import willie

@willie.module.commands('ping')
def pingpong(bot, trigger):
	bot.say('Pong!')