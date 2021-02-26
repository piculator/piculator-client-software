import platform


class Ports:
    # jupyter notebook 的默认运行端口
    jupyter_notebook = 8888
    # worker 端口区间起始
    worker_range_start = 22222
    # 数据桥梁端口
    data_bridge = 40404

    _next_worker_port = worker_range_start

    @classmethod
    def get_worker_port(cls):
        cls._next_worker_port += 1
        return cls._next_worker_port - 1
