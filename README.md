# piculator-client-software
Client side software of piculator.



## 树莓派上配置环境

```bash
sudo apt update
sudo apt install python3-pyqt5.qtwebkit python3-pyqt5 python3-jupyter-console python3-bluez
sudo apt install libglib2.0-dev pkg-config libboost-python-dev libboost-thread-dev libbluetooth-dev libglib2.0-dev python-dev
pip3 download gattlib
tar xvzf ./gattlib-*.tar.gz
cd gattlib-*/
sed -ie 's/boost_python-py34/boost_python37/' setup.py
sudo pip3 install .
```