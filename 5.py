#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 群回复

import itchat


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
	print msg['isAt']
	# itchat.send('%s, %s' % (u'我是机器人小豆豆，你好', (msg['ActualNickName']), msg['FromUserName'])
	itchat.send(u'@%s\u2005 我是机器人小豆豆: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])
    # if msg['isAt']:
    #     itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])


itchat.auto_login(hotReload=True)
itchat.run()


