#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 图灵

import json
import requests

url = 'http://tingapi.ting.baidu.com/v1/restserver/ting?method=baidu.ting.search.common&query=五月天&page_size=1&page_no=1&format=json'
r = requests.get(url)
data = json.loads(r.text)
print data['song_list'][0]['song_id']

song_id = data['song_list'][0]['song_id']
src = 'http://ting.baidu.com/data/music/links?songIds=' + song_id
print src
r2 = requests.get(src)

print r2.text








