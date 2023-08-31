import logging
# logger = logging.getLogger(__name__)    # __name__ = name of the file
# logger.info('Hello from helper')


import logging
logger = logging.getLogger(__name__)
logger.propagate = False
# create handler
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')
# level 
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)
# format
format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(format)
file_handler.setFormatter(format)
# set handler
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning('This is warning')
logger.error('This is an error')