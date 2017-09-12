#! -*- coding:utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        PortScan
# Purpose:     扫描网段主机的端口开放情况
# -------------------------------------------------------------------------------
import socket


def main():
    ip_start = input('请输入开始IP：(默认:127.0.0.1)')
    if ip_start == '':
        ip_start = '127.0.0.1'
        ip_end = '127.0.0.1'
    else:
        ip_end = input('请输入结束IP：')
        if ip_end == '':
            ip_end = '127.0.0.1'

    s = input('请输入目标主机开始端口：(默认扫描常用端口)')
    if s == '':
        portList = [21, 22, 23, 25, 80, 135, 137, 139, 445, 1433, 1502, 3306, 3389, 8080, 9015]
    else:
        startport = int(s)
        s = input('请输入目标主机结束端口：(默认:65535)')
        if s == '':
            endport = 65535
        else:
            endport = int(s)
        portList = [i for i in range(startport, endport + 1)]

    while 1:
        # ip_start<ip_end
        x1 = ip_start.rfind('.');
        x2 = ip_end.rfind('.')
        if int(ip_start[x1 + 1:]) > int(ip_end[x2 + 1:]):
            break;

            # 开始扫描端口
        for port in portList:
            print('正在扫描%s ：%d' % (ip_start, port))
            try:
                sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sk.settimeout(10)
                sk.connect((ip_start, port))
                sk.settimeout(None)
                print 'Server %s port %d OK!' % (ip_start, port)
                sk.close()

                # 结果保存在文件中
                f = open("IP_Port.txt", 'a')
                f.write(ip_start + ' : ' + str(port) + '\n')
                f.close()
            except Exception:
                print 'Server %s port %d is not connected!' % (ip_start, port)

                # 更新ip_start
        i = ip_start.rfind('.')
        x = int(ip_start[i + 1:]) + 1
        ip_start = ip_start[:i + 1] + str(x)

    print '扫描完成，结果保存在IP_Port.txt文件中'


if __name__ == '__main__':
    main()