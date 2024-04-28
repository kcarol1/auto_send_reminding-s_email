import smtplib
from email.mime.text import MIMEText
#发送多种类型的邮件
from email.mime.multipart import MIMEMultipart
def send_att(file_dir,start_time_point,end_time_point,total_time):
    msg_from = '' # 发送方邮箱
    passwd = '' #授权码
    
    to= [''] #接受方邮箱
    
    #设置邮件内容
    #MIMEMultipart类可以放任何内容
    msg = MIMEMultipart()
    conntent="任务已完成"
    #把内容加进去
    msg.attach(MIMEText(conntent + "\n" 
                        "程序开始记录时间：" + str(start_time_point) + "\n" 
                        "程序结束记录时间：" + str(end_time_point) + "\n" 
                        "总共记录时长：" + str(total_time),'plain','utf-8'))
    
    #添加附件
    if file_dir is not None:
        att1=MIMEText(open(file_dir,'rb').read(),'base64','utf-8') #打开附件
        att1['Content-Type']='application/octet-stream'  #设置类型是流媒体格式
        att1['Content-Disposition']='attachment;filename=result.txt' #设置描述信息
    
        msg.attach(att1)  #加入到邮件中
    
    #设置邮件主题
    msg['Subject']="任务已完成"
    
    #发送方信息
    msg['From']=msg_from
    
    #开始发送
    
    #通过SSL方式发送，服务器地址和端口
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    # 登录邮箱
    s.login(msg_from, passwd)
    #开始发送
    s.sendmail(msg_from,to,msg.as_string())
    print("邮件发送成功")
if __name__ == "__main__":
    send_att()
