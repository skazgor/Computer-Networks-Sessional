package server.workingThread;

import server.httpRequest.Request;
import server.httpRequest.RequestParser;
import server.httpRequest.RequestServer;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.util.logging.Logger;

public class WorkerThread extends Thread {
  private final Logger logger = Logger.getLogger(String.valueOf(WorkerThread.class));
  private Socket socket;
    public WorkerThread(Socket socket) {
       this.socket = socket;
    }
    @Override
    public void run() {
        InputStream inputStream=null;
        OutputStream outputStream=null;
          try {
                inputStream = socket.getInputStream() ;
                outputStream =  socket.getOutputStream();
              Request request = new Request();
              RequestParser requestParser = new RequestParser(inputStream, request);
                requestParser.parse();
              System.out.println(request);
              RequestServer requestServer = new RequestServer(request, outputStream);
                requestServer.serve();
            } catch (Exception e) {
                logger.severe(e.getMessage());
            }
          finally {
                try {
                    inputStream.close();
                    outputStream.close();
                    socket.close();
                } catch (Exception e) {
                    logger.severe(e.getMessage());
                }
          }
    }
}

