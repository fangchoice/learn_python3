# generateCodePdf

1. 安装python依赖

	pip3 install -r requirements.txt
	
	pip install PyMuPDF PyQt5 Cython -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com


2. 配置TEMP

	sudo mkdir /usr/TEMP/
	
	sudo cp ./Tmx*.pdf /usr/TEMP/

3. 执行测试

	python test_cython.py

==================================

不同操作系统，所依赖的系统库有所差异:

ubuntu: apt install libgl1-mesa-dev libglib2.0-0
