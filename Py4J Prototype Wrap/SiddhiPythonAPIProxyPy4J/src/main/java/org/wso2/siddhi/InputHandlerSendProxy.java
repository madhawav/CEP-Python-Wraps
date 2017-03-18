package org.wso2.siddhi;

import org.wso2.siddhi.core.stream.input.InputHandler;

/**
 * Proxy class used to interface with InputHandler.send method
 */
public class InputHandlerSendProxy {
    private Object[] data;
    private int index = 0;
    public InputHandlerSendProxy(int size)
    {
        data = new Object[size];
    }
    public void putLong(long l)
    {
        data[index++] = l;
    }
    public void putInt(int i)
    {
        data[index++] = i;
    }

    public void putString(String s){
        data[index++] = s;
    }
    public void putFloat(float f){
        data[index++] = f;
    }

    public void putDouble(double d){
        data[index++] = d;
    }

    public void send(InputHandler inputHandler) throws InterruptedException {
        inputHandler.send(data);
    }
}

