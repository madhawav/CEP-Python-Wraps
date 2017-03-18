import logging
from py4j.java_gateway import JavaGateway, CallbackServerParameters

logging.basicConfig(level=logging.INFO)

#TODO: Add JVM Loader Code

_java_gateway = JavaGateway(callback_server_parameters=CallbackServerParameters(daemonize = True,daemonize_connections=True))

logging.info("Java Gateway Established")
