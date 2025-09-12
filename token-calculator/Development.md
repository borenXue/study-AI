

* 1、准备 conda 独立环境

```shell
conda config --show
conda config --show channels  # ~/.condarc 文件

conda env create -n token python=3.12.8
conda env list
conda activate token
python --version && pip --version
pip list
```

* 2、安装依赖

```shell
conda activate token

pip install -r requirements.txt
```










conda env create -f environment.yml -n myenv

conda env create -n token-calc python=3.12.8
conda env create -f requirements.txt -n token-calc python=3.12.8

pip install -r requirements.txt

conda create -n your_env_name python=x.x


* 参考命令

```shell





conda env export > environment3.yml


conda config --show channels
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/


```