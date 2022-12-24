# everydays-run


## 开发

首先，创建一个文件，要求该文件可以执行程序并记录输出
![](https://ited.ml/content/uploadfile/202212/0eba1671865691.png)
然后打开ta，开始开发
![](https://ited.ml/content/uploadfile/202212/thum-320f1671865833.png)
因为这次要与系统交互，所以引入os模块
```python
import os
```
要用时间，引入time模块
```python
import time
```
要路径，引入sys模块
```python
import sys
```

之后定义关键的模块

- 输出当前路径
```python
def databe():
    databe = sys.argv[0]
    databe = databe.replace("evedays-run.py","",1)
    return(databe)
```

- 创建文件，返回文件路径（相对）
```python
def newdoc(stay = "",name = "test",last = ".log"):
    print("newdoc in " + databe() + stay + "\\" + name + last)
    file = open(databe() + stay + "\\" + name + last,'w')
    file.close()
    return(databe() + stay + "\\" + name + last)
```

- 写文件，返回文件路径（相对）
```python
def writedoc(con = "",doc ="test.log"):
    file = open(doc,"a")
    for temp in con:
        file.write(str(temp))
    file.close
    return(doc)
```

- 运行东西，输入路径列表，返回输出列表
```python
def rundoc(doc = []):
    ret = []
    for run in doc:
        print("run "+ databe() + run)
        r = os.popen(databe() + run, 'r')
        re = r.readlines()		# re接受返回结果
        r.close()
        ret.append(re)
    return(ret)
```

- 获取格式化时间
```python
def gtime(sth = ""):
    u = "%Y"+sth+"%m"+sth+"%d"
    time1 = time.localtime()
    ret = time.strftime(u,time1) 
    return(ret)
```

建立项目基本文件结构
![](https://ited.ml/content/uploadfile/202212/thum-457d1671868155.png)

编写主程序，无非就是轮番执行而已，拆了两次列表
```python
name = gtime()    #获取时间
logstay = newdoc("log",name,".log")      #创建日志
run = ["runs/60s.py","runs/FNplus.py -u 邮箱 -p 密码"]      #运行两个文件
runlog = rundoc(run)      #记录日志
for writcon in runlog:      #拆日志列表
    writedoc(writcon,logstay)      #写入日志
```

## 部署
首先把这个文件拖到服务器上
![](https://ited.ml/content/uploadfile/202212/ef3d1671874280.png)

然后添加计划任务即可，无需额外参数
![](https://ited.ml/content/uploadfile/202212/64811671874618.png)


原帖地址：[https://ited.ml/post/123](https://ited.ml/post/123)
