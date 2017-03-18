package org.wso2.siddhi;
import org.wso2.siddhi.core.ExecutionPlanRuntime;
import org.wso2.siddhi.core.event.Event;
import org.wso2.siddhi.core.query.output.callback.QueryCallback;
import org.wso2.siddhi.core.util.EventPrinter;
import py4j.GatewayServer;

import java.util.logging.Logger;

/**
 * Created by madhawa on 3/18/17.
 */
public class EntryPoint {
    public static void main(String[] args) {
        GatewayServer gatewayServer = new GatewayServer(new EntryPoint());
        gatewayServer.start();
        Logger.getAnonymousLogger().info("Server Started");
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

    public void printEvent(long timeStamp, Event[] inEvents, Event[] outEvents)
    {
        EventPrinter.print(timeStamp,inEvents,outEvents);
    }
}
