运行留言板网站
1.新建虚拟环境，安装requirements.txt中的库
pip install requirements.txt
2.确保电脑上有mysql数据库
3.在电脑中新建数据库，并将新数据库信息，修改到config.py文件中
4.在虚拟环境中，运行以下命令，迁移数据库
   python manage.py db migrate
5.运行app.py文件，即运行开发版的服务器。在浏览器上，输入url,即可进入网站。

注意:本软件是开发版本，并不是部署版本。