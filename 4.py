#!/usr/bin/env python
# -*- coding: utf-8 -*-
# msg 分解

import itchat


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])
    itchat.send('%s, %s' % (u'你是机器人小豆豆，你好', msg['Text']), msg['FromUserName'])
    

itchat.auto_login(hotReload=True)
itchat.run()


