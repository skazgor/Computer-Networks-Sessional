package server.httpRequest;

import java.io.File;
import java.io.IOException;
import java.io.OutputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
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
                if(response.getBody()!=null && !response.navigate)
                {   
                    byte [] body=response.getBodyBytes();
                    byte[] temp;
                    for (int i = 0; i < body.length; i=i+1024) {
                       if(i+1024<body.length)
                        {
                            temp=Arrays.copyOfRange(body, i, i+1024);
                            outputStream.write(temp);
                        }
                        else
                        {
                            temp=Arrays.copyOfRange(body, i, body.length);
                            outputStream.write(temp);
                        }
                       outputStream.flush();
                    }
                    outputStream.write(response.getCR());
                    outputStream.flush();
                }
                Thread.sleep(1000);
                outputStream.flush();
            } catch (IOException e) {
                e.printStackTrace();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        else if(request.getRequestType()==RequestType.UPLOAD){
            if(request.isStatus()){
                File file =new File(request.getUrl().substring(1)+"\\"+request.getFileName());

                try {
                    Files.write(Path.of(file.getPath()),request.getBody());

                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            else{
                System.out.println("File not found or not supported");
            }
        }
    }
    private void pathInfo(String path){
        if(Files.exists(Path.of(path))) {
            if (Files.isDirectory(Path.of(path))) {
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
                        htmlBody += "<li><a href=\"http://localhost:5091/" + file.toString() + "\">" + "<i><b>" + file.getFileName() + "</i></b></a></li>";
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
                response.setStatus(Status.OK);
                String extension = path.substring(path.lastIndexOf(".")+1);
                if(extension.contentEquals("jpg")){
                    if(request.image) {
                        response.navigate=false;
                        response.setContentType("image/jpg");
                    }
                    else{
                        response.setContentType("text/html");
                        response.setHtmlBody("<html><body><h1>This image is showing from html document</h1><img src=\"http://localhost:5091/"+path+"\" alt=\"This image is showing from html document\" style=\"width:1024px;height:720px;\"></body></html>");                        return;
                    }
                }
                else if(extension.contentEquals("png")){
                    if(request.image) {
                        response.navigate=false;
                        response.setContentType("image/png");
                    }
                    else{
                        response.setContentType("text/html");
                        response.setHtmlBody("<html><body><h1>This image is showing from html document</h1><img src=\"http://localhost:5091/"+path+"\" alt=\"This image is showing from html document\" style=\"width:1024px;height:720px;\"></body></html>");
                        return;
                    }
                }
                else if(extension.contentEquals("gif")){
                    response.navigate=false;
                    response.setContentType("image/gif");
                }
                else if(extension.contentEquals("html")){
                    response.navigate=false;
                    response.setContentType("text/html");
                }
                else if(extension.contentEquals("css")){
                    response.navigate=false;
                    response.setContentType("text/css");
                }
                else if(extension.contentEquals("js")){
                    response.navigate=false;
                    response.setContentType("text/javascript");
                }
                else if(extension.contentEquals("txt")){
                    response.setContentType("text/html");
                    File file =new File(path);
                    response.setHtmlBodyFromFileForTextDocument(file);
                    return;
                }
                else if(extension.contentEquals("pdf")){
                    response.navigate=false;
                    response.setContentType("application/pdf");
                }
                else if(extension.contentEquals("zip")){
                    response.navigate=false;
                    response.setContentType("application/zip");
                }
                else if(extension.contentEquals("rar")){
                    response.navigate=false;
                    response.setContentType("application/x-rar-compressed");
                }
                else if(extension.contentEquals("doc")){
                    response.navigate=false;
                    response.setContentType("application/msword");
                }
                else if(extension.contentEquals("docx")){
                    response.navigate=false;
                    response.setContentType("application/vnd.openxmlformats-officedocument.wordprocessingml.document");
                }
                else if(extension.contentEquals("xls")){
                    response.navigate=false;
                    response.setContentType("application/vnd.ms-excel");
                }
                else if(extension.contentEquals("xlsx")){
                    response.navigate=false;
                    response.setContentType("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
                }
                else if(extension.contentEquals("ppt")){
                    response.navigate=false;
                    response.setContentType("application/vnd.ms-powerpoint");
                }
                else if(extension.contentEquals("pptx")){
                    response.navigate=false;
                    response.setContentType("application/vnd.openxmlformats-officedocument.presentationml.presentation");
                }
                else if(extension.contentEquals("mp3")){
                    response.navigate=false;
                    response.setContentType("audio/mpeg");
                }
                else if(extension.contentEquals("mp4")){
                    response.navigate=false;
                    response.setContentType("video/mp4");
                }
                else if(extension.contentEquals("wav")){
                    response.navigate=false;
                    response.setContentType("audio/wav");
                }
                else if(extension.contentEquals("avi")){
                    response.setContentType("video/x-msvideo");
                    response.navigate=false;
                }
                else if(extension.contentEquals("wmv")){
                    response.setContentType("video/x-ms-wmv");
                    response.navigate=false;
                }
                else if(extension.contentEquals("flv")){
                    response.setContentType("video/x-flv");
                    response.navigate=false;
                }
                else if(extension.contentEquals("swf")){
                    response.setContentType("application/x-shockwave-flash");
                    response.navigate=false;
                }
                else if(extension.contentEquals("xml")){
                    response.setContentType("application/xml");
                    response.navigate=false;
                }
                else if(extension.contentEquals("json")){
                    response.setContentType("application/json");
                    response.navigate=false;
                }
                File file =new File(path);
                response.readBytes(file);
            }
        }
        else{
            response.setStatus(Status.NOT_FOUND);
            File file =new File("public\\404.html");
            response.setContentType("text/html");
            response.setHtmlBodyFromFile(file);
            System.out.println("404 Page Not Found");
            //send 404
        }
    }

    @Override
    public String toString() {
        return "RequestServer{" +
                "response=\n" + response +
                '}';
    }
}
