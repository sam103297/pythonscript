import os
import sys


print ("===============欢迎使用Docker自动更新网站工具===============")
print ("\r\n")
rongqi = input("请输入当前网站容器名称：")

#停止当前容器
os.system("docker stop %s" %(rongqi))
#删除当前容器
os.system("docker rm %s" %(rongqi))
#删除当前镜像
os.system("docker rmi %s" %(rongqi))
#创建镜像
os.system("docker image build -t /wwwroot/PanguVideo/ %s ." %(rongqi))
#运行容器
os.system("docker run --name=%s -p 7777:80 -d %s" %(rongqi,rongqi))

print("Success！")
sys.exit()