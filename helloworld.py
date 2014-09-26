import willie

@willie.module.commands('helloworld')
def helloworld(bot, trigger):
	bot.say('Hello World!')