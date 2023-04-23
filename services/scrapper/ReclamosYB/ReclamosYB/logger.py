import logging
from logging.handlers import RotatingFileHandler

log_file = "reclamosyb.log"
log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(log_file, maxBytes=100000, backupCount=1)
handler.setLevel(logging.INFO)

formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)

logger.addHandler(handler)
