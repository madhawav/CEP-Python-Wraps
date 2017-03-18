package org.wso2.siddhi;

import org.wso2.siddhi.core.event.Event;

/**
 * Proxy callback interface for QueryCallback Abstract Class
 */
public interface ExecutionPlanCallbackProxy {
    void receive(long l, Event[] events, Event[] events1);
}