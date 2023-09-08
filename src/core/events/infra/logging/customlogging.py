import datetime
import getpass
import json
import logging


class UserFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        setattr(record, 'user', getpass.getuser())
        return True


class NoBadWordsFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return not record.getMessage().__contains__('f')


class CustomFormatter(logging.Formatter):
    def __init__(self):
        super().__init__()

    def formatMessage(self, record: logging.LogRecord) -> str:
        super().formatMessage(record)
        log_record = {
            'message': record.message,
            'name': record.name,
            'pathName': record.pathname,
            'funcName': record.funcName,
            'lineNumber': record.lineno,
            'threadId': record.thread,
            'threadName': record.threadName,
            'level': record.levelname,
            'user': record.user,
            'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
        return json.dumps(log_record, indent=4, sort_keys=True)


logging_config: dict = {
    'version': 1,
    'filters': {
        'user': {'()': lambda: UserFilter()},
        'badwords': {'()': lambda: UserFilter()},
    },
    'formatters': {
        'myformatter': {
            '()': lambda: CustomFormatter(),
        },
    },
    'handlers': {
        'console': {
            'filters': ['user', 'badwords'],
            'formatter': 'myformatter',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': '/logs/app.log',
            'filters': ['user', 'badwords'],
            'formatter': 'myformatter',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
        'propagate': False,
    },
    'loggers': {
        'uvicorn.access': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

if __name__ == '__main__':
    import logging.config

    logging.config.dictConfig(logging_config)

    logger = logging.getLogger(__name__)

    logger.info('this is a test')
    logger.error('this is a warning')
    logger.critical('this is a critical error')
