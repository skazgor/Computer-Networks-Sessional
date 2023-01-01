package server.httpRequest;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.util.Arrays;
import java.util.Scanner;

public class Response {
    private String response;
    private Status status;
    private String contentType;
    private String contentLength;
    private String htmlBody;
    private byte [] body;
    private final String CRLF = "\r\n";
    public Response() {
        this.contentType = "Content-Type: ";
        this.contentLength = "Content-Length: ";
        this.htmlBody = "";
        this.body = null;
    }
    public String getResponse() {
        return response;
    }


    public String getContentType() {
        return contentType;
    }

    public String getContentLength() {
        return contentLength;
    }

    public String getBody() {
        return htmlBody;
    }

    public void setResponse(String response) {
        this.response = response;
    }

    public void setStatus(Status status) {
        this.status = status;
    }

    public void setContentType(String contentType) {
        this.contentType += contentType;
    }

    public void setContentLength(String contentLength) {
        this.contentLength = contentLength;
    }

    public void setHtmlBodyFromFile(File file) {
        try {
            Scanner scanner =new Scanner(file);
            while(scanner.hasNextLine()){
                htmlBody += scanner.nextLine();
            }
            contentLength+=htmlBody.length();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
    public void setHtmlBody(String htmlBody){
        this.htmlBody = htmlBody;
        contentLength+=htmlBody.length();
    }
    public void readBytes(File file){
        try {
            body = Files.readAllBytes(file.toPath());
            contentLength+=body.length;
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public byte [] getBytes(){
        String response=null;
      if(body==null){
            response = this.response + " " + this.status.status + CRLF +
                  this.contentType + CRLF +
                  this.contentLength + CRLF +
                  CRLF +
                  this.htmlBody+CRLF+CRLF;
      }
      else{
          response = this.response + " " + this.status.status + CRLF +
                  this.contentType + CRLF +
                  this.contentLength + CRLF +
                  CRLF+ new String(body)+CRLF+CRLF;

      }

        System.out.println(response);
        return response.getBytes();
    }
    public void setBody(byte[] body) {
        this.body = body;
    }
}
