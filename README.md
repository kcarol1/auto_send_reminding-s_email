# 描述
在Linux服务器上跑深度学习代码，跑完后自动发送邮件提醒
# 设置账户
在send_email.py中设置账号和授权码（关于授权码如何获得请自行百度）
# 主要功能
程序结束后发送提示，并且记录了**开始时间**、**结束时间**、**总计时间**以及**监测程序的输出文件（可选项并且需要设置要发送的文件路径）**
<img width="985" alt="PixPin_2024-04-28_22-52-54" src="https://github.com/kcarol1/auto_send_reminding-s_email/assets/97381622/35635b28-7773-4ddd-97bc-33bfbf286399">
# 运行
```
python start.py
```

# 运行2
可以创建`/exp/home/user/.local/bin/reminder`并在其中编辑
```
/exp/home/user/miniconda3/bin/python /exp/home/user/Path/to/start.py
```
即可在命令行直接输入`reminder`运行
