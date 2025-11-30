from loguru import logger

def configure_logging():
    logger.remove()
    logger.add(
        "backend_log.log",
        rotation="10 MB",
        retention="10 days",
        level="INFO",
        format="{time} {level} {message}"
    )
    logger.add(
        "stderr",
        level="WARNING",
        format="<red>{time}</red> <level>{level}</level> <green>{message}</green>",
        colorize=True,
    )
