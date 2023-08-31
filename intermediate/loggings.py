import logging as log
log.basicConfig(
    level=log.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%y %H:%M:%S'
)

# log.debug('this is logging message')
# log.info('this is logging message')
# log.warning('this is logging message')
# log.error('this is logging message')
# log.critical('this is logging message')

import logging_helper as loger
