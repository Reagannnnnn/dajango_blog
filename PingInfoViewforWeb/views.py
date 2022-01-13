from django.shortcuts import render,redirect
from django.http import HttpResponse
import ipaddress
import posix
import subprocess
import threading
import time
import os


def index(request):
    return HttpResponse(str(request.get_host()))

def WelcomePage(request):
    return render(request, "")



class PingThread(threading.Thread):
    def __init__(self, ip):
        threading.Thread.__init__(self)
        self.ip = ip
    def run(self):
        do_ping(self.ip)


def do_ping(ip):
    # 使用命令行ping
    try:
        res = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.PIPE, timeout=1)
        output = res.stdout.decode("gbk")
        # print("%-20s%-20s" % (ip, "success"))
        # Threadlock.acquire()
        pingres[ip] = ip + "       success"
        # print(pingres[ip])
    except subprocess.TimeoutExpired:
        # print("%-20s%-20s" % (ip, "fail"))
        pingres[ip] = ip + "       fail"
        # print(pingres[ip])
    # finally:
        # Threadlock.release()


# if __name__ == "__main__":
#     Target = "180.184.64.0/29"
#     ip_list = []
#     ipaddr = ipaddress.ip_network(Target)
#     pingres = {}
#     for i in ipaddr:
#         ip_list.append(str(i))
#         pingres[str(i)] = {}
#     # print(ip_list)
#     # print(pingres)
#     Threadlock = threading.Lock()
#     threads = []
#
#     while True:
#         failflag = 0
#         for ip in ip_list:
#             # pingthread = PingThread(ip)
#             pingthread = threading.Thread(target=do_ping,args=(ip,))
#             threads.append(pingthread)
#             pingthread.start()
#         for thread in threads:
#             thread.join()
#         for i in ipaddr:
#             print("\r" + str(pingres[str(i)]))
#             if "fail" in pingres[str(i)]:
#                 failflag = 1
#         if failflag == 0:
#             time.sleep(1)
