package client;

import java.io.File;
import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;

public class ClientWorker extends Thread{
    private String path;
    private final String host="localhost";
    private final int port=5091;
    public ClientWorker(String path) {
        this.path = path;
    }
    @Override
    public void run() {
        Socket socket = null;
        OutputStream outputStream = null;
        try {
              socket=new Socket(host,port);
              outputStream=socket.getOutputStream();
            outputStream.write(("UPLOAD /root\\uploaded HTTP/1.1\r\n").getBytes());
            File file=new File(path);
            String extension = path.substring(path.lastIndexOf(".")+1);
            boolean filetype=false;
            if(extension.equals("jpg")||extension.equals("png")||extension.equals("txt")||extension.equals("jpeg")||extension.equals("mp4")) {
                filetype = true;
            }
            if(filetype && file.exists()) {
                outputStream.write(("Content-Length: "+file.length()+"\r\n").getBytes());
                outputStream.write(("File-Name: "+Path.of(path).getFileName()+"\r\n").getBytes());
                outputStream.write("Status: OK\r\n".getBytes());
                outputStream.write("\r\n".getBytes());
                byte [] body=Files.readAllBytes(Path.of(path));
                byte[] temp;
                for (int i = 0; i < body.length; i=i+1024) {
                    if(i+1024<body.length)
                    {
                        temp= Arrays.copyOfRange(body, i, i+1024);
                        outputStream.write(temp);
                    }
                    else
                    {
                        temp=Arrays.copyOfRange(body, i, body.length);
                        outputStream.write(temp);
                    }
                    outputStream.flush();
                }
                outputStream.write("\r\n".getBytes());
                outputStream.flush();
            }
            else{
                System.out.println("File not found or not supported");
                outputStream.write("Status: Not Found\r\n".getBytes());
                outputStream.write("\r\n".getBytes());
                outputStream.flush();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        finally {
            System.out.println("ClientWorker finished");
            try {
                outputStream.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
            try {
                socket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
