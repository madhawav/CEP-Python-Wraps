from Python_API import _java_gateway #Loads API
from Python_API.ExecutionPlanRuntime import ExecutionPlanRuntime


class SiddhiManager:
    def __init__(self):
        '''
        ''Initialize a new SiddhiManager
        '''
        self._siddhi_manager_proxy =  _java_gateway.jvm.org.wso2.siddhi.core.SiddhiManager()

    def createExecutionPlanRuntime(self,executionPlan):
        '''
        Create an Execution Plan Runtime
        :param executionPlan: SiddhiQuery (string) defining execution plan
        :return: ExecutionPlanRuntime
        '''
        execution_plan_runtime_proxy = self._siddhi_manager_proxy.createExecutionPlanRuntime(executionPlan)
        return ExecutionPlanRuntime._fromExecutionPlanRuntimeProxy(execution_plan_runtime_proxy)

    def shutdown(self):
        '''
        Shutdown SiddhiManager
        :return:
        '''
        self._siddhi_manager_proxy.shutdown()
        del self._siddhi_manager_proxy