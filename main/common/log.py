import os;
import logging;
from logging.handlers import TimedRotatingFileHandler
from readconfig import LOG_PATH, Config

class Logger():
    def __init__(self, logger_name="framwork"):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        logConfig = Config().get("log")
        self.log_file_name = logConfig.get("file_name") if logConfig and logConfig.get("file_name") else "test.log"
        logConfig.get("backup") if logConfig and logConfig.get("backup") else 5
        #日志的输出级别
        self.console_output_level = logConfig.get('console_level') if logConfig and logConfig.get('console_level') else 'WARNING'
        self.file_output_level = logConfig.get('file_level') if logConfig and logConfig.get('file_level') else 'DEBUG'
        # 日志输出格式
        pattern = logConfig.get('pattern') if logConfig and logConfig.get('pattern') else '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self.formatter = logging.Formatter(pattern)


        def get_logger(self):
            if not self.logger.handlers:
                console_handler = logging.StreamHandler()
                console_handler.setFormatter(self.formatter)
                console_handler.setLevel(self.console_output_level)
                self.logger.addHandler(console_handler)
                file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH, self.log_file_name),
                                                        when='D',
                                                        interval=1,
                                                        backupCount=self.backup_count,
                                                        delay=True,
                                                        encoding='utf-8'
                                                        )
                file_handler.setFormatter(self.formatter)
                file_handler.setLevel(self.file_output_level)
                self.logger.addHandler(file_handler)
            return self.logger
logger = Logger().get_logger()

