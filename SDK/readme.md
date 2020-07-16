

# MAC电脑下安装hid的说明

# python3.6

# requirement.txt
hid==1.0.4
hidapi==0.9.0.post3
PyQt5==5.14.2


# 如果是python3.8可能与hid不兼容，会导致hid不能加载一些库文件

ImportError: Unable to load any of the following libraries:libhidapi-hidraw.so
libhidapi-hidraw.so.0 libhidapi-libusb.so libhidapi-libusb.so.0 libhidapi-iohidmanager.so
libhidapi-iohidmanager.so.0 libhidapi.dylib hidapi.dll libhidapi-0.dll

更多信息可参考
https://pypi.org/project/hid/
https://github.com/libusb/hidapi






