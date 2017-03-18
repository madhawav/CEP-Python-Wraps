from time import sleep
from Python_API.EventPrinter import PrintEvent
from Python_API.SiddhiManager import SiddhiManager

# Creating SiddhiManager
siddhiManager = SiddhiManager()
executionPlan = "" + "define stream cseEventStream (symbol string, price float, volume long); " + "" +"@info(name = 'query1') " +"from cseEventStream[volume < 150] " +"select symbol,price " + "insert into outputStream ;"

# Generating runtime
executionPlanRuntime = siddhiManager.createExecutionPlanRuntime(executionPlan)

# Adding callback to retrieve output events from query
def executionPlanRuntimeCallback(timestamp, inEvents, outEvents):
    PrintEvent(timestamp, inEvents,outEvents)

executionPlanRuntime.addCallback("query1",executionPlanRuntimeCallback)

# Retrieving input handler to push events into Siddhi
inputHandler = executionPlanRuntime.getInputHandler("cseEventStream")

# Starting event processing
executionPlanRuntime.start()

# Sending events to Siddhi
inputHandler.send(["IBM",700.0,100l])
inputHandler.send(["WSO2", 60.5, 200l])
inputHandler.send(["GOOG", 50, 30l])
inputHandler.send(["IBM", 76.6, 400l])
inputHandler.send(["WSO2", 45.6, 50l])
sleep(0.5)

# shutting down the runtime
executionPlanRuntime.shutdown()

# shutting down Siddhi
siddhiManager.shutdown()