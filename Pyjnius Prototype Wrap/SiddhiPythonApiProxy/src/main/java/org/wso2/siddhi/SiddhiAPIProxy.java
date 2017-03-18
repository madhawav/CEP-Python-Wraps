package org.wso2.siddhi;

import org.wso2.siddhi.core.ExecutionPlanRuntime;
import org.wso2.siddhi.core.SiddhiManager;
import org.wso2.siddhi.core.event.Event;
import org.wso2.siddhi.core.query.output.callback.QueryCallback;

/**
 * Created by madhawa on 3/17/17.
 */
public class SiddhiAPIProxy {
    /**
     * Initiates a new Siddhi Manager and return instance to Python API
     * @return new SiddhiManager Instance
     */
    public SiddhiManager initSiddhiManager(){
        return new SiddhiManager();
    }

    public void addExecutionPlanRuntimeCallback(ExecutionPlanRuntime executionPlanRuntime, String name, final ExecutionPlanCallbackProxy callback)
    {
        executionPlanRuntime.addCallback(name, new QueryCallback() {
            @Override
            public void receive(long l, Event[] events, Event[] events1) {
                callback.receive(l,events,events1);
            }
        });
    }
}
