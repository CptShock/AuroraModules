from willie.module import commands
import urllib2, urllib, optparse, sys, os.path,random
@commands('pasteuserkey')
def ans(bot, trigger):
	username = trigger.group(2)
    from getpass import getpass
    password = getpass()
    bot.say("test")
    request = {"api_dev_key":devkey, "api_user_name":username, "api_user_password":password}

    try:
        reply = urllib2.urlopen("http://pastebin.com/api/api_login.php", urllib.urlencode(request))
    except urllib2.URLError:
        if not options.quiet:
            print "Error uploading", filename + ":", "Network error"
        exit(2)
    else:
        reply = reply.read()
        if "Bad API request" in reply:
            if not options.quiet:
                print "Pastebin login error:", reply
            exit(2)
        else:
            bot.reply(reply)