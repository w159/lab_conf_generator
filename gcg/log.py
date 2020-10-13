import logging
from gcg.env import DEBUG

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

gcg_logger = logging.getLogger("gcgLogger")
gcg_logger.addHandler(stream_handler)

if DEBUG:
    gcg_logger.setLevel(logging.DEBUG)
else:
    gcg_logger.setLevel(logging.WARNING)
