import os
from logging import getLogger, StreamHandler,FileHandler, DEBUG
if os.name == 'posix':
    from logging import SysLogHandler
logger = getLogger(__name__)
#handler = StreamHandler()
handler=FileHandler('test.log',mode='a',encoding='UTF-8')
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

logger.debug('hello')
