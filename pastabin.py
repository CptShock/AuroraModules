import willie,urllib2, urllib, optparse, sys, os.path,random

@willie.module.commands('pastabin')
def ans(bot, trigger):
	vardevkey = "e556580a88095cbfb11184fa1a97863b"
	vartest = "test123"
	varurl = "http://pastebin.com/api/api_post.php"
	varpaste = "paste"
	varparams = {"api_dev_key":vardevkey,"api_option":varpaste,"api_paste_code":vartest}
	fetch(varurl,varparams)
def fetch(url, params):
  params = urllib.urlencode(varparams)
  f = urllib.urlopen(varurl, params)
  bot.say("uploaded")