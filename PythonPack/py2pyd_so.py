
# pip install cython
# 在window下生成 pyd文件，相当于dll
# 在Linux下生成 so文件


from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize(["registration.py", "decorate01.py"]))

