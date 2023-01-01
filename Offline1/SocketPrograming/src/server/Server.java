package server;

import server.workingThread.WorkerThread;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.logging.Logger;

public class Server {
    private static Logger logger =Logger.getLogger(String.valueOf(Server.class));
   private static final int PORT = 5091;
    public static void main(String[] args) throws IOException {
        logger.info("Server starting...");
        ServerSocket serverSocket=new ServerSocket(PORT);
        logger.info("Listening on port "+PORT);

        while(serverSocket.isBound() && !serverSocket.isClosed()){
            Socket socket=serverSocket.accept();
            logger.info("New connection from "+socket.getInetAddress());
            WorkerThread thread=new WorkerThread(socket);
            thread.start();
        }
    }
}
