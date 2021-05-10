# -*- coding: utf-8 -*-

import os,time,smtplib
import readConfig
import getpathInfo
from email.mime.text import MIMEText  # 发送正文
from email.mime.multipart import MIMEMultipart  # 发送多个部分
from email.mime.application import MIMEApplication  # 发送附件

read_conf = readConfig.ReadConfig()
mail_host = read_conf.get_email('mail_host')  # 从配置文件中读取，邮件host
mail_user = read_conf.get_email('mail_user')  # 从配置文件中读取，登录邮箱用户名
mail_pass = read_conf.get_email('mail_pass')  # 从配置文件中读取，登录邮箱密码
subject = read_conf.get_email('subject')  # 从配置文件中读取，邮件主题
sender = read_conf.get_email('sender')  # 从配置文件中读取，邮件发送人
receivers = read_conf.get_email('receivers')  # 从配置文件中读取，邮件收件人

mail_path = os.path.join(getpathInfo.get_Path(), './result/report.html')#获取测试报告路径
#logger = logger



class TestMail():
    '''

    def new_report():  # 查找最新的测试报告
        testreport = "/Users/pangjing/PycharmProjects/pxxAutotest1.0/result"
        dirs = os.listdir(testreport)
        dirs.sort()
        newreportname = dirs[-1]
        #print('The new report name: {0}'.format(newreportname))
        file_new = os.path.join(testreport, newreportname)
        return file_new
    '''


    def send_mail(self):

        f = open('/Users/pangjing/PycharmProjects/pxxAutotest1.0/result/report.html', 'rb')
        mail_body = f.read()    #读取测试报告正文
        f.close()

        # 构造一个邮件体：正文、附件
        msg = MIMEMultipart()  # 邮件体
        msg['Subject'] = subject # 邮件主题
        msg['From'] = sender   # 发件人
        msg['To'] = receivers  # 收件人
        msg["Accept-Language"] = "zh-CN"
        msg["Accept-Charset"] = "ISO-8859-1,utf-8"
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))  # 获取系统时间
        #msg['Date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 构建正文
        content = """
                                                    执行测试中……
                                                    测试已完成！！
                                                    生成报告中……
                                                    报告已生成……
                                                    报告已邮件发送！！
                                                    """
        email_body = MIMEText(mail_body, 'html', 'utf-8')
        #email_body['Subject'] = Header('自动化测试报告', 'utf-8')

        msg.attach(email_body)  # 将正文添加到邮件体中
        #构建附件
        att= MIMEApplication(open(mail_path, 'rb').read())  # 打开附件
        att.add_header("Content-Disposition", "attachment", filename='测试报告.html')  # 为附件命名
        msg.attach(att)  # 添加附件到邮件体中

        try:
            smtpObj = smtplib.SMTP()
            smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 使用smtp协议发送邮件，SSL协议来进行加密传输，465为端口号
            smtpObj.login(mail_user, mail_pass)  # 邮箱登录
            smtpObj.sendmail(sender, receivers, msg.as_string())  # 发送邮件
            print('send mail ok')
            smtpObj.quit()
        except smtplib.SMTPException:
            print('send mail fail')




if __name__ == '__main__':# 运营此文件来验证写的send_email是否正确
    print(subject)
    #new_report = TestMail().new_report()
    #TestMail().send_mail(new_report)
    TestMail().send_mail()
    print("send over!!!!!!!!!!")

