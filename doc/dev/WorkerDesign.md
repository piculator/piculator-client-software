# Worker 设计思路

## 命令行参数

```
python -m worker command port secret_key [other params]
```

command: 要运行的服务, 暂时只有 jupyter notebook

port: ipc server 的侦听端口

secret_key: ipc server 的 认证密钥

## 两个线程

### 主线程

运行 server ( 譬如 jupyter-notebook ) 来为 app 提供服务

### IPC(Inter-process communication)线程

运行 IPC server 来接受 app 的命令 ( 比如 关闭 jupyter-notebook )

## 如何为 worker 开发功能: 以 jupyter notebook 为例

`jupyter-notebook.py` 中定义了三个函数

- jupyter_notebook_initialize: 初始化
- jupyter_notebook_main: 主函数
- jupyter_notebook_finalize: 清理函数

根据 worker 的设计思路, 启动后解析参数, 然后把控制权交给这三个功能函数

按照要求, 功能函数需要在一个合适的时机启动 IPC server, 即运行 `start_server_thread` 函数

```python
def jupyter_notebook_initialize():
    global app_token, data_bridge_port
    try:
        data_bridge_port = int(sys.argv[4])
        app_token = sys.argv[5]
        global commander
        commander = Commander(data_bridge_port, app_token)
    except:
        print('Invalid arguments!')
        exit(-1)
    global notebook_handler
    notebook_handler = NotebookHandler()
    worker.thread_unsafe_globals['notebook_handler'] = notebook_handler
    ############################
    worker.start_server_thread()
    ############################
```

在本例中, jupyter_notebook 初始化完成后启动了ipc server

