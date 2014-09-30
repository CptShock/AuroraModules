from willie.module import commands
import urllib2, urllib, optparse, sys, os.path,random

vardevkey = "e556580a88095cbfb11184fa1a97863b"
vartest = "test123"
varurl = "http://pastebin.com/api/api_post.php"
varpaste = "paste"
varparams = {"api_dev_key":vardevkey,"api_option":varpaste,"api_paste_code":vartest}

@commands('pastabin')
def ans(bot, trigger):
	fetch(url,params,method)
def fetch(url, params):
  varparams = urllib.parse.urlencode(varparams)
  f = urllib.request.urlopen(varurl, varparams)