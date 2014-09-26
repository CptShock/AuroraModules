from willie.module import commands
import random

@commands('conv')
def ans(bot, trigger):
    answers = ['y', 'n']
    message = trigger.group(2)
    fromtype=""
    totype=""
    out=""
    convert = message.split(':')[1]
    if message.find('bin>') != -1:
        out = convert
    if message.find('dec>') != -1:
        out = decbin(int(convert))
    if message.find('hex>') != -1:
        out = decbin(hexdec(convert))
    if message.find('oct>') != -1:
        out = decbin(octdec(convert))
    if message.find('>bin') != -1:
        bot.reply(out)
    if message.find('>dec') != -1:
        bot.reply(bindec(out))
    if message.find('>hex') != -1:
        bot.reply(binhex(out))
    if message.find('>oct') != -1:
        bot.reply(binoct(out))
def decbin(convert):
    hold = []
    j=0
    answer=""
    while convert>0:
        hold.append(str(convert % 2))
        convert = convert/2
        j += 1
    for i in range(0, j):
        k=j-i-1
        answer += str(hold[k])
        i += 1
    return answer
def hexdec(convert):
    answer = 0
    hexa = "0123456789ABCDEF"
    for i in range(0,len(convert)):
        answer += int(hexa.find(convert[(len(convert)-i)-1])*16**i)
        i += 1
    return answer
def octdec(convert):
    answer = 0
    octa = "01234567"
    for i in range(0,len(convert)):
        answer += int(octa.find(convert[(len(convert)-i)-1])*8**i)
        i += 1 
    return answer
def bindec(convert):
    answer=0
    for i in range(0,len(convert)):
        answer += int(convert[len(convert)-i-1])*2**i
        i+=1
    return answer
def binhex(convert):
    hold = []
    var1 = 0
    answer=""
    hexa = "0123456789ABCDEF"
    if len(convert)%4!=0:
        convert="0"+convert
    if len(convert)%4!=0:
        convert="0"+convert
    if len(convert)%4!=0:
        convert="0"+convert
    for i in range(1,len(convert),4):
        var1+=1
        hold.append(int(convert[(len(convert)-i)])+int(convert[(len(convert)-1-i)])*2+int(convert[(len(convert)-2-i)])*4+int(convert[(len(convert)-3-i)])*8)
    for i in range(0,len(hold)):
        answer=hexa[hold[(i)]]+answer
        if i%4==0:
            answer = " " +answer
    return answer
def binoct(convert):
    hold = []
    var1 = 0
    answer=""
    if len(convert)%3!=0:
        convert="0"+convert
    if len(convert)%3!=0:
        convert="0"+convert
    for i in range(1,len(convert),3):
        var1+=1
        hold.append(int(convert[(len(convert)-i)])+int(convert[(len(convert)-1-i)])*2+int(convert[(len(convert)-2-i)])*4)
    for i in range(0,len(hold)):
        answer=str(hold[(i)])+answer
        if i%3==0:
            answer = " " +answer
    return answer