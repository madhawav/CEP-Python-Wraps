import Python_API #Initializes Runtime
from Python_API import _java_gateway


def PrintEvent(timestamp, inEvents, outEvents):
    '''
    Prints Stream Event to Log
    :param timestamp:
    :param inEvents:
    :param outEvents:
    :return:
    '''

    _java_gateway.entry_point.printEvent(timestamp,inEvents,outEvents)

    # NOTE: We are unable to call org.wso2.siddhi.core.util.EventPrinter.print directly because print is a keyword of python
