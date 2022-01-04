# Usage
git clone https://github.com/supplepentan/penta-white-box-cartoonization.git
cd penta-white-box-cartoonization
wsl
python -m venv venv-wsl
source venv-wsl/bin/activate
python -m pip install -U pip setuptools
python -m pip install nvidia-pyindex
python -m pip install nvidia-tensorflow[horovod]
python -m pip install opencv-python
python -m pip install tqdm
python setup.py
python run.py

# Original
https://github.com/SystemErrorWang/White-box-Cartoonization/blob/master/paper/06791.pdf
