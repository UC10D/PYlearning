
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itchat
import time



itchat.auto_login()

for i in range(10):  
    itchat.send('Are you ljj ,mmp', toUserName='ljj313974224') 
    time.sleep(3)  


# def hello(): 
# 	itchat.send('Hello, filehelper', toUserName='filehelper')



# if __name__ == "__main__":
#     timer = threading.Timer(2.0, hello())
#     timer.start()


