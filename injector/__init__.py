import coloredlogs

coloredlogs.install()
custom_logger = logging.getLogger(name)
coloredlogs.install(level="INFO", logger=custom_logger)
