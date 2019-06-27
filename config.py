# -*- coding: utf-8 -*-

# 登录方式
LOGIN_TYPE_UID = "LOGIN_TYPE_UID"   # 使用用户和密码登录
LOGIN_TYPE_QR = 'LOGIN_TYPE_QR'     # 使用扫码登录
LOGIN_TYPE = LOGIN_TYPE_UID          # 设置登录方式
USER_NAME = ""                   # 用户名
PASSWD = ""                      # 密码

# 发送设置
TIME_SLOG = 30 * 60                 # 发送微博的时间间隔 (秒)
MAX_IMAGES = 9                      # 允许上传图片的最大数量。如果设置为0，则不上传图片。
ADD_WATERMARK = False               # 是否添加图片水印，为True时，应设置以下两项
WATERMARK_NIKE = "@淘券鼠_"             # 水印名称
WATERMARK_URL = "http://tb.pfinal.club/"         # 水印链接

# 日志设置
LOG_FILE = False                    # 运行日志是否记录文件

# 系统设置
WBCLIENT = 'ssologin.js(v1.4.18)'

USER_AGENT = (
      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.11 (KHTML, like Gecko) '
      'Chrome/20.0.1132.57 Safari/536.11'
)