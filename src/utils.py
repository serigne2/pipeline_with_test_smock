import logging

def log_message(message: str, level: str = 'info'):
    logger = logging.getLogger('etl_logger')
    level = level.lower()
    if level == 'info':
        logger.info(message)
    elif level == 'warning':
        logger.warning(message)
    elif level == 'error':
        logger.error(message)
    else:
        raise ValueError(f"Unknown log level: {level}")
