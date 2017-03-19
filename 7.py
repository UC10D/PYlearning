#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 图灵

import json
import requests
import itchat

KEY = 'cdd1bbe660bc4c4ea927879a366df96f'    # change to your API KEY
url = 'http://www.tuling123.com/openapi/api'


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
	print msg['isAt']
	if msg['Content'][0] == '#':
		req_info = msg['Content'].split('#').encode('utf-8')
		query = {'key': KEY, 'info': req_info}
		headers = {'Content-type': 'text/html', 'charset': 'utf-8'}
		r = requests.get(url, params=query, headers=headers)
		res = r.text
		print json.loads(res).get('text').replace('<br>', '\n')
		itchat.send(json.loads(res).get('text').replace('<br>', '\n'), msg['FromUserName'])

itchat.auto_login(hotReload=True)
itchat.run()




