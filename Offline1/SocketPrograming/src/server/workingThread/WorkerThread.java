package server.workingThread;

import server.httpRequest.Request;
import server.httpRequest.RequestParser;
import server.httpRequest.RequestServer;

import java.io.*;
import java.net.Socket;
import java.util.logging.FileHandler;
import java.util.logging.Logger;

public class WorkerThread extends Thread {
  private final Logger logger = Logger.getLogger(String.valueOf(WorkerThread.class));
  private Socket socket;
    public WorkerThread(Socket socket) {
       this.socket = socket;
        FileHandler file = null;
        try {
            file = new FileHandler("Log\\workingThread\\log.txt");
        } catch (IOException e) {
            e.printStackTrace();
        }
        logger.addHandler(file);
    }
    @Override
    public void run() {
        InputStream inputStream=null;
        OutputStream outputStream=null;
          try {
                inputStream = socket.getInputStream() ;
                outputStream =  socket.getOutputStream();
              Request request = new Request();
              logger.info("Request received\n");

              RequestParser requestParser = new RequestParser(inputStream, request);
                requestParser.parse();
                logger.info("Request parsed\n");

              logger.info(request.toString());

              RequestServer requestServer = new RequestServer(request, outputStream);
                requestServer.serve();
                logger.info("Request served\n");

                logger.info(requestServer.toString());
            } catch (Exception e) {
                logger.severe(e.getMessage());
            }
          finally {
                try {
                    Thread.sleep(1000);
                    inputStream.close();
                    outputStream.close();
                    socket.close();
                } catch (Exception e) {
                    logger.severe(e.getMessage());
                }
          }
    }
}

