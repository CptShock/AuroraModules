import willie
import random
@willie.module.commands('8')
def ball(bot, trigger):
    """Ask Aurora your questions and she will answer! Usage: !Aurora <question>"""
    messages = ["It is certain"," It is decidedly so","Without a doubt","Yes definitely","You may rely on it","As I see it yes","Most likely","Outlook good","Yes","Signs point to yes","Reply hazy try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Don't count on it","My reply is no","God says no","Very doubtful","Outlook not so good","Wouldn't hope for it","Not in your wildest dreams","Maybe if Arne learns to grow a beard","Not now, not never","Most Definitely"]
    answer = random.randint(0,len(messages))
    bot.say(messages[answer]);