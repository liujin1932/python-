# coding:utf-8
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.read_config import ReadConfig

class SendMail(object):
    def __init__(self):
        rc = ReadConfig(r"D:\Users\Raymond\PycharmProjects\bokeyuan0229\config\config.ini")
        self.smtpserver = rc.get_mail("smtpserver")
        self.port = rc.get_mail("port")
        self.sender = rc.get_mail("sender")
        self.psw = rc.get_mail("psw")
        self.receiver = rc.get_mail("receiver").split(",")

    def new_report(self,testreport):
        dirs = os.listdir(testreport)
        dirs.sort()
        newreportname = dirs[-1]
        print('The new report name: {0}'.format(newreportname))
        file_new = os.path.join(testreport, newreportname)
        print(file_new)
        return file_new

    # new_report(r'D:\report')



    def sendmail(self):
        # ----------2.编辑邮件的内容------
        #读文件
        file_path = self.new_report(r'D:\Users\Raymond\PycharmProjects\bokeyuan0229\report')
        with open(file_path, "rb") as fp:
            mail_body = fp.read()

        msg = MIMEMultipart()
        msg["from"] = self.sender                       # 发件人
        msg["to"] = ";".join(self.receiver)             # 多个收件人list转str
        msg["subject"] = "这个我的主题999"              # 主题

        # 正文
        body = MIMEText(mail_body, "html", "utf-8")
        msg.attach(body)

        # 附件
        att = MIMEText(mail_body, "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename="test_report.html"'
        msg.attach(att)

        # ----------3.发送邮件------
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtpserver)                      # 连服务器
            smtp.login(self.sender, self.psw)
        except:
            smtp = smtplib.SMTP_SSL(self.smtpserver, self.port)
            smtp.login(self.sender, self.psw)                       # 登录
        smtp.sendmail(self.sender, self.receiver, msg.as_string())  # 发送
        smtp.quit()

if __name__ == '__main__':

    ss = SendMail()
    print(ss.receiver)
    ss.sendmail()

