

import logging

# logging.basicConfig(level=logging.DEBUG,
# 	format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s',
# 	datefmt='%a, %d %b %Y %H:%M:%S',
# 	filename='C:\\Users\\Administrator\\Desktop\\手写识别服务器\\test.log',
# 	filemode='w',
# 	)


logger = logging.getLogger()

# create a handle to write logging file
fh = logging.FileHandler('test.log')

# 再创建一个handler，用于输出控制台
ch = logging.StreamHandler()

# 日志的格式
formatters = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatters)
ch.setFormatter(formatters)

logger.addHandler(fh)
# logger.addHandler(ch)

# 设置日志的级别
logger.setLevel(logging.DEBUG)

logging.debug('debug message')
logging.info('info message')
logging.warning('warnings message')
logging.error('error message')
logging.fatal('fatal message')
logging.critical('critical message')

