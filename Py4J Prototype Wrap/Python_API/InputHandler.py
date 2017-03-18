import logging
from Python_API import _java_gateway #Loads API

from Python_API.TypeLong import TypeLong

class InputHandler(object):
    def __init__(self):
        raise NotImplementedError("Initialize InputHandler using ExecutionPlanRuntime")

    def __new__(cls):
        bare_instance = object.__new__(cls)
        bare_instance._input_handler_proxy = None
        return bare_instance

    @classmethod
    def _fromInputHandlerProxy(cls, input_handler_proxy):
        '''
        Internal Constructor to wrap around JAVA Class InputHandler
        :param input_handler_proxy:
        :return:
        '''
        instance = cls.__new__(cls)
        instance._input_handler_proxy = input_handler_proxy
        return instance

    def send(self, data):
        '''
        Sends data to stream
        :param data:
        :return:
        '''

        # Special logic used since Python3.5 doesn't support long

        # TODO: Try to improve the logic here by reducing the number of socket Calls

        i1 = _java_gateway.jvm.org.wso2.siddhi.InputHandlerSendProxy(len(data))
        for d in data:
            if type(d) is float:
                i1.putFloat(d)
            elif type(d) is TypeLong:
                i1.putLong(d)
            elif type(d) is int:
                i1.putInt(d)
            elif type(d) is str:
                i1.putString(d)
            else:
                logging.error("Unknown Type:", type(d))
        i1.send(self._input_handler_proxy)
