#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 图灵

import json
import requests

url = 'http://s.music.qq.com/fcgi-bin/music_search_new_platform?t=0&n=1&aggr=1&cr=1&loginUin=0&format=json&inCharset=GB2312&outCharset=utf-8&notice=0&platform=jqminiframe.json&needNewCode=0&p=1&catZhida=0&remoteplace=sizer.newclient.next_song&w=五月天'


r = requests.get(url)



data = json.loads(r.text)
print data['data']['song']['list'][0]['grp'][0]['f'].split('|')[0]

song_id = data['data']['song']['list'][0]['grp'][0]['f'].split('|')[0]


# req_info = ''.encode('utf-8')


# query = {'info': req_info}
headers = {'Content-type': 'text/html', 'charset': 'utf-8'}

srcUrl = 'http://ws.stream.qqmusic.qq.com/4931916.m4a?fromtag=46'

src = 'http://music.qq.com/miniportal/static/lyric/".($song_id%100)."/{$song_id}.xml'
# 方法一、用requests模块已get方式获取内容
r2 = requests.post(src, headers=headers)


print r2






