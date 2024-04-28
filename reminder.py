import monitor_pid
import time
import send_email
import datetime
import argparse

def input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pid_to_process","-p",type=int)
    parser.add_argument("--logfile","-f",type=str)
    args = parser.parse_args()
    input_logfile = args.logfile
    input_pid_to_monitor = args.pid_to_process
    return input_logfile,input_pid_to_monitor

def reminder(pid_to_monitor,logfile = None):

    start_time = datetime.datetime.now() # 记录程序开始记录时间

    while True: # 一直循环
        output = monitor_pid.output_status(pid_to_monitor) #监测进程状态，并赋值到output
        if output == 0: # 判断是进程否结束
            end_time = datetime.datetime.now() # 记录程序结束运行的时间
            total_time = end_time -start_time # 计算程序总共运行时间
            start_time_point = start_time.strftime("%Y-%m-%d %H:%M:%S") # 开始时间点
            end_time_point = end_time.strftime("%Y-%m-%d %H:%M:%S") # 结束时间点
            send_email.send_att(logfile,start_time_point,end_time_point,total_time) # 发送邮件
            print(end_time_point)
            exit()

if __name__ == "__main__":
    input_logfile,input_pid_to_monitor = input_args()
    if input_pid_to_monitor is None:
        print("PID为空！")
        exit()
    if input_logfile is None:
        reminder(input_pid_to_monitor)
    else:
        reminder(input_pid_to_monitor,input_logfile)