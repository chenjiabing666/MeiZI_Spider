#coding:utf-8
import requests
from bs4 import BeautifulSoup
import threading
import Queue
class Get_ips():
    """
    get_ips:主要用来获得西刺网的第一页的高匿ip,存在ips的文件中
    """
    def __init__(self):
        self.url='http://www.xicidaili.com/nn/1'
        self.header={"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'}
        self.file=open("ips", 'w')
    def get_ips(self):
        res=requests.get(self.url,headers=self.header)
        soup = BeautifulSoup(res.text, 'lxml')
        ips = soup.find_all('tr')
        for i in range(1, len(ips)):
            ip = ips[i]
            tds = ip.find_all("td")
            ip_temp = tds[1].contents[0] + "\t" + tds[2].contents[0] + "\n"
            self.file.write(ip_temp)
        self.file.close()




class Review_ips():
    def __init__(self):
        self.q_1=Queue.Queue()
        self.q_2=Queue.Queue()
        self.file=open('ips','r')
        #self.file_reviewed_ips=open('reviewed_ips','w')
        self.Lock=threading.Lock()
        #self.ip=Get_ips()
    def get_ip(self):
        """
        :return:返回的是所有的队列ip
        """
        lines=self.file.readlines()
        for i in range(0, len(lines)):
            ip = lines[i].strip('\n').split('\t')
            proxy_host = "http://" + ip[0] + ":" + ip[1]
            proxy_temp = {"http": proxy_host}
            self.q_1.put(proxy_temp)
        self.file.close()
        # while not self.q_1.empty():
        #     print self.q_1.get()

    def review_ips(self):
        """
        验证ip
        :return:
        """
        while not self.q_1.empty():
            ip=self.q_1.get()
            try:
                res = requests.get("http://www.baidu.com", proxies=ip, timeout=5)
                if res.status_code == 200:
                    print ip
                    self.Lock.acquire()
                    self.q_2.put(ip)
                    self.Lock.release()
            except Exception:
                pass
    def main(self):
        self.get_ip()  #获得队列ip
        threads = []
        for i in range(0, 40):   #开启多线程验证ip
            threads.append(threading.Thread(target=self.review_ips, args=[]))
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        all_ips=[]
        while not self.q_2.empty():
            ips = self.q_2.get()
            all_ips.append(ips['http'])
            #self.file_reviewed_ips.write(ips['http'] + '\n')
            print ips
        #self.file_reviewed_ips.close()
        print all_ips
if __name__=="__main__":
    my=Get_ips()
    my.get_ips()
    file=Review_ips()
    file.main()


