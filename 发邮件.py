
# 方案2：使用第三方工具包zmail      注意:是否安装了zmail包

import zmail

# 你的邮件内容
mail_content = {
    'subject': 'Success!',  # 随便填写
    'content': 'This message from zmail!',  # 随便填写
    'attachments': 'movie.csv'
}
# 使用你的邮件账户名和密码登录服务器
server = zmail.server('名', '密码')
# 发送邮件
server.send_mail('864071694@qq.com', mail_content)
