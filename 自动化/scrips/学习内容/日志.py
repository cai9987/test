import logging

# # 设置日志级别
# logging.basicConfig(level=logging.DEBUG)
#
# logging.debug("debug")
# logging.info("info")
# # 默认为waring
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")


logger = logging.getLogger()

logger.setLevel(logging.INFO)


sh = logging.StreamHandler()

logger.addHandler(sh)

logger.info("info")
logger.debug("debug")
