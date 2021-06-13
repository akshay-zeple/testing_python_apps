import logging
from loggingpackage import custom_logger as cl

class LoggingDemo2():

    log = cl.cutomLogger(logging.DEBUG)

    def method1(self):

        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warning message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method2(self):
        m2log = cl.cutomLogger(logging.ERROR)

        m2log.debug('debug message')
        m2log.info('info message')
        m2log.warning('warning message')
        m2log.error('error message')
        m2log.critical('critical message')

    def method3(self):
        m3log = cl.cutomLogger(logging.CRITICAL)

        m3log.debug('debug message')
        m3log.info('info message')
        m3log.warning('warning message')
        m3log.error('error message')
        m3log.critical('critical message')

obj = LoggingDemo2()
obj.method1()
obj.method2()
obj.method3()
