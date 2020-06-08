import zmail

mail_content = {
    "subject": "自动化测试报告",
    "content": "正文",
    "attachments": "附件路径"    # 附件
}

server = zmail.server("发件人邮箱", "授权码")

server.send_mail("收件人邮箱", mail_content)