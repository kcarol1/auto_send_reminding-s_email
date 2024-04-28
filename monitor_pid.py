import psutil
import time

def check_process(pid):
    """检查进程是否正在运行"""
    try:
        # 获取进程信息
        process = psutil.Process(pid)
        # 如果进程正在运行，返回1
        if process.is_running():
            return 1
    except psutil.NoSuchProcess:
        # 如果进程不存在，返回0
        return 0

def output_status(PID_TO_MONITOR):
    status = check_process(PID_TO_MONITOR)
    return(status)

if __name__ == "__main__":
    output_status()
