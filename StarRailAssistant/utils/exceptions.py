'''
Author: Night-stars-1 nujj1042633805@gmail.com
Date: 2023-05-13 13:05:56
LastEditors: Night-stars-1 nujj1042633805@gmail.com
LastEditTime: 2023-07-22 17:53:06
FilePath: \Honkai-Star-Rail-beta-2.4h:\Download\Zip\Honkai-Star-Rail-beta-2.7\tool\exceptions.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
from widgets import log as log_widget
import traceback


class Exception(Exception):

    def __init__(self, message):
        super().__init__(message)
        log_widget.transmitDebugLog(message, level=3)
        log_widget.transmitDebugLog(traceback.format_exc(), level=2)


class TypeError(Exception):

    def __init__(self, message):
        super().__init__(message)
        log_widget.error(message)