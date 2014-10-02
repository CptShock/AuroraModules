import urllib,willie
_base_domain = 'pastebin.com'
_prefix_url = 'http://%s/' % _base_domain
_subdomain_url = 'http://%%s.%s/' % _base_domain
_api_url = 'http://%s/api/api_post.php' % _base_domain

@willie.module.commands('pb')
def ans(bot, trigger):
    url = submit(trigger.group(2))
    bot.say(url)
    
def submit(api_paste_code,api_paste_name = None, api_paste_private = None,api_paste_expire_date = None, api_paste_format = None):
    argv = { 'api_paste_code' : str(api_paste_code) }
    if api_paste_name is not None:
        argv['api_paste_name'] = str(api_paste_name)
    if api_paste_private is not None:
        argv['api_paste_private'] = int(bool(int(api_paste_private)))
    if api_paste_expire_date is not None:
        api_paste_expire_date = str(api_paste_expire_date).strip().upper()
        argv['api_paste_expire_date'] = api_paste_expire_date
    if api_paste_format is not None:
        api_paste_format = str(paste_format).strip().lower()
        argv['api_paste_format'] = api_paste_format
    argv['api_dev_key'] = "e556580a88095cbfb11184fa1a97863b"
    argv['api_option'] = "paste"
    fd = urllib.urlopen(_api_url, urllib.urlencode(argv))
    try:
        response = fd.read()
    finally:
        fd.close()
    del fd
    return response