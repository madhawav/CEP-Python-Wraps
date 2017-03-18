from Python_API import _java_gateway #Loads API
from Python_API.InputHandler import InputHandler


class ExecutionPlanRuntime(object):
    def __init__(self,):
        raise NotImplementedError("Initialize ExecutionPlanRuntime using Siddhi Manager")

    def __new__(cls):
        bare_instance = object.__new__(cls)
        bare_instance._execution_plan_runtime_proxy = None
        return bare_instance

    def addCallback(self, queryName, receiveCallback):
        '''
        Assign callback interface to ExecutionPlanRuntime
        :param queryName:
        :param queryCallback:
        :return:
        '''
        class ExecutionPlanCallback(object):
            '''
            Innerclass to wrap around Java Interface
            '''
            def receive(self, timestamp, inEvents, removeEvents):
                receiveCallback(timestamp,inEvents,removeEvents)

            class Java:
                implements = ["org.wso2.siddhi.ExecutionPlanCallbackProxy"]

        _java_gateway.addExecutionPlanRuntimeCallback(self._execution_plan_runtime_proxy,queryName,ExecutionPlanCallback())

    def getInputHandler(self, streamId):
        '''
        Retrieve input handler assigned with a stream
        :param streamId: stream id of stream
        :return: InputHandler
        '''
        input_handler_proxy = self._execution_plan_runtime_proxy.getInputHandler(streamId)
        return InputHandler._fromInputHandlerProxy(input_handler_proxy)

    def start(self):
        '''
        Start ExecutionPlanRuntime
        :return: void
        '''
        self._execution_plan_runtime_proxy.start()

    def shutdown(self):
        '''
        Shutdown ExecutionPlanRuntime
        :return:
        '''
        self._execution_plan_runtime_proxy.shutdown()
        del self._execution_plan_runtime_proxy

    @classmethod
    def _fromExecutionPlanRuntimeProxy(cls, execution_plan_runtime_proxy):
        '''
        Internal Constructor to wrap around JAVA Class ExecutionPlanRuntime
        :param execution_plan_runtime_proxy:
        :return:
        '''
        instance = cls.__new__(cls)
        instance._execution_plan_runtime_proxy = execution_plan_runtime_proxy
        return instance