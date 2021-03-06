package org.wso2.siddhi;

/**
 * Created by madhawa on 3/18/17.
 */

import org.wso2.siddhi.core.event.Event;
import org.wso2.siddhi.core.util.EventPrinter;

/**
 * Proxy class used to interface with org.wso2.siddhi.core.util.EventPrinter
 */
public class EventPrinterProxy {
    private EventPrinterProxy(){}

    public static void printEvent(long timeStamp, Event[] inEvents, Event[] outEvents)
    {
        EventPrinter.print(timeStamp,inEvents,outEvents);
    }
}
