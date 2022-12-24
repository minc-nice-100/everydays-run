import os
import time
import sys

#输出路径
def databe():
    databe = sys.argv[0]
    databe = databe.replace("evedays-run.py","",1)
    return(databe)
#创建文件
def newdoc(stay = "",name = "test",last = ".log"):
    print("newdoc in " + databe() + stay + "\\" + name + last)
    file = open(databe() + stay + "\\" + name + last,'w')
    file.close()
    return(databe() + stay + "\\" + name + last)
#写文件
def writedoc(con = "",doc ="test.log"):
    file = open(doc,"a")
    for temp in con:
        file.write(str(temp))
    file.close
    return(doc)
#运行py，抓输出
def rundoc(doc = []):
    ret = []
    for run in doc:
        print("run "+ databe() + run)
        r = os.popen(databe() + run, 'r')
        re = r.readlines()		# re接受返回结果
        r.close()
        ret.append(re)
    return(ret)
#获取格式化时间
def gtime(sth = ""):
    u = "%Y"+sth+"%m"+sth+"%d"
    time1 = time.localtime()
    ret = time.strftime(u,time1) 
    return(ret)


#主程序
name = gtime()
logstay = newdoc("log",name,".log")
run = ["runs/60s.py","runs/FNplus.py -u wu01768@gmail.com -p wzc315201"]
runlog = rundoc(run)
for writcon in runlog:
    writedoc(writcon,logstay)
