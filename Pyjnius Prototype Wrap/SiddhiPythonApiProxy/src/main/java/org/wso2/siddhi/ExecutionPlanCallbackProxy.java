package org.wso2.siddhi;

import org.wso2.siddhi.core.event.Event;

/**
 * Created by madhawa on 3/18/17.
 */
public interface ExecutionPlanCallbackProxy {
    void receive(long l, Event[] events, Event[] events1);
}
