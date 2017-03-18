import logging
logging.basicConfig(level=logging.INFO)

#Add Java library to class path of jvm
import jnius_config
jnius_config.set_classpath('.','../SiddhiPythonApiProxy/out/artifacts/SiddhiPythonApiProxy_jar/*')

logging.info("Classpath Configured")

#Start JVM
from jnius import autoclass

#Retrieve access
siddhi_manager_api = autoclass("org.wso2.siddhi.SiddhiAPIProxy")
siddhi_manager_api_inst = siddhi_manager_api()


