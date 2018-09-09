# import logging
#打印到控制台
# print(logging.debug("调试级别日志"),end="")
# print(logging.info("info级别日志"))
# print(logging.warning("警告级别日志"))
# print(logging.error("错误级别日志"))
# print(logging.critical("崩溃级别程序无法继续运行"))

import logging
# 设置日志级别、日志格式、日志输出位置
logging.basicConfig(filename=r'F:\app.log',   #输出路径、文件名
                    level=logging.DEBUG,    #日志级别
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',    #日志格式
                    datefmt='%Y-%m-%d %H:%M:%S')               #时间格式
logging.info('test info')
logging.debug('test debug')
logging.warning('test warning')
logging.error('test error')
logging.critical('test critical')