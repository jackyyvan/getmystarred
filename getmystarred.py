import urllib2
import json
import os

def get():
    url = 'https://api.github.com/user/starred?page='
    for i in range(1,x):  #这里的x是指你star的项目有多少页，可以自己看看自己的然后填上这个数字
        surl=url+str(i)
        request = urllib2.Request(surl)
        request.add_header('Authorization', 'Bearer xxxxxx') #xxxxxx 指的是你的账户设置的token 怎么设置这个token请自己查github api 文档 v4 
        resp = urllib2.urlopen(request)
        data=json.loads(resp.read())
        for obj in data:
            print(obj['clone_url'])
            cmd= 'git clone '+obj['clone_url']+' data/'+obj['full_name']  ##需要先在此脚本同目录下创建data文件夹
            os.system(cmd)

if __name__ == "__main__":
    get()
