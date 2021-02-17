import platform


class Ports:
    # jupyter notebook 的默认运行端口
    jupyter_notebook = 8888
    # worker 端口区间起始
    worker_range_start = 22222
    # worker 端口区间终止
    worker_range_end = 22333
    # 数据桥梁端口
    data_bridge = 40404


sage_python_interpreter = r"D:\Non-Green\SageMath 9.2\runtime\bin\python3.7m.exe" if platform.system() == 'Windows' else '/home/pi/sage/sage-9.2/local/bin/python3'
