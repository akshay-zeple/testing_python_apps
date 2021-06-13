import logging

class LoggerDemoConsole():

    def testLog(self):

        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)

        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')

        chandler.setFormatter(formatter)

        logger.addHandler(chandler)

        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
        logger.error('error message')

obj = LoggerDemoConsole()
obj.testLog()