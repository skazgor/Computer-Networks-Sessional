package server.httpRequest;

import java.io.File;
import java.io.IOException;
import java.io.OutputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.stream.Stream;

public class RequestServer {
    private Request request;
    private Response response;
    private OutputStream outputStream = null;

    public RequestServer(Request request, OutputStream outputStream) {
        this.request = request;
        response=new Response();
        this.outputStream = outputStream;
    }

    public void serve() {
        if (request.getRequestType() == RequestType.GET) {
            response.setResponse(request.getVersion());
            if (request.getUrl().equals("/")) {
                response.setStatus(Status.OK);
                File file =new File("public\\root.html");
                response.setHtmlBodyFromFile(file);
                response.setContentType("text/html");

            }
            else{
                pathInfo(request.getUrl().substring(1));
            }
            try {
                outputStream.write(response.getBytes());
                outputStream.flush();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
    private void pathInfo(String path){
        if(Files.exists(Path.of(path))) {
            if (Files.isDirectory(Path.of(path))) {
                System.out.println("Directory"+path);
                //list files
                Stream<Path> files = null;
                try {
                    files = Files.list(Path.of(path));
                } catch (IOException e) {
                    e.printStackTrace();
                }
                String htmlBody = "<html><body><ul>";
                for (Path file : (Iterable<Path>) files::iterator) {
                    if (Files.isDirectory(file)) {
                        htmlBody += "<li><a href=\"http://localhost:5091/" + file.toString() + "\">" + "<i>" + file.getFileName() + "</i></a></li>";
                    } else {
                        htmlBody += "<li><a href=\"http://localhost:5091/" + file.toString() + "\">" + file.getFileName() + "</a></li>";
                    }
                }
                htmlBody += "</ul></body></html>";
                response.setHtmlBody(htmlBody);
                response.setContentType("text/html");
                response.setStatus(Status.OK);
            }
            else{
                 //show file
                File file =new File(path);
                response.readBytes(file);
                response.setContentType("application/pdf");
                response.setStatus(Status.OK);
            }
        }
        else{
            System.out.println("abc");
            response.setStatus(Status.NOT_FOUND);
            File file =new File("public\\404.html");
            response.setHtmlBodyFromFile(file);
            //send 404
        }
    }
}
