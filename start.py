import subprocess
import monitor_pid
import time

def setting(option):
    
    if option == 1:
        subprocess.run('nvidia-smi')
    if option == 2:
        subprocess.run(['ps','-a'])
def main():
    option = int(input("查看GPU进程（1）或一般进程（2）："))
    while True:
        try:
            setting(option)
            pid = int(input("不要输入类似“1、2、123、222”这种"+"\n"+"请输入要监控的进程PID:"))
            status = monitor_pid.output_status(pid)
            if  status != 0:
                file_path = str(input("请输入要发送的文件路径(可以为空)："))
                if file_path == '':
                    cmd = f"nohup python reminder.py --pid_to_process {pid} > email.log 2>&1 &"
                else:
                    cmd = f"nohup python reminder.py --pid_to_process {pid} --logfile {file_path} > email.log 2>&1 &"
                subprocess.run(cmd,shell=True)
                print("已运行！")
                break
            else:
                print()
                text = '******************不存在这个进程！************************'
                print(text)
                time.sleep(1)
                print()
        except Exception as e:
            print()
            text = f'*********发生了一个错误:{e},请输入正确的整数PID！*********'
            print(text)
            time.sleep(1)
            print()

if __name__ == "__main__":

    main()
