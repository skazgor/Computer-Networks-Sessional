package server.httpRequest;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
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
    public boolean navigate=true;
    private final String CRLF = "\r\n";
    public Response() {
        this.contentType = "Content-Type: ";
        this.contentLength = "Content-Length: ";
        this.htmlBody = "";
        this.body = null;
        status=Status.OK;
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
      if(navigate){
            response = this.response + " " + this.status.status + CRLF +
                  this.contentType + CRLF +
                  this.contentLength + CRLF +
                  CRLF +
                  this.htmlBody+CRLF+CRLF;
      }
      else{
          response = this.response + " " + this.status.status + CRLF +
                  this.contentType  + CRLF +
                  this.contentLength + CRLF +
                  CRLF ;
      }

//        System.out.println(response);
        return response.getBytes(StandardCharsets.UTF_8);
    }

    public void setBody(byte[] body) {
        this.body = body;
    }
    public byte[] getBodyBytes(){
        return body;
    }
    public byte[] getCR(){
        return CRLF.getBytes(StandardCharsets.UTF_8);
    }

    public void setHtmlBodyFromFileForTextDocument(File file) {
            try {
                Scanner scanner =new Scanner(file);
                htmlBody="<html><body><h1>this is showing the content of the file</h1><br><br>";
                while(scanner.hasNextLine()){
                    htmlBody += scanner.nextLine();
                }
                htmlBody+="</body></html>";
                contentLength+=htmlBody.length();
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

    @Override
    public String toString() {
        String response=null;
        if(!htmlBody.contentEquals("")){
            response = this.response + " " + this.status.status + CRLF +
                    this.contentType + CRLF +
                    this.contentLength + CRLF +
                    CRLF +
                    this.htmlBody+CRLF+CRLF;
        }
        else{
            response = this.response + " " + this.status.status + CRLF +
                    this.contentType  + CRLF +
                    this.contentLength + CRLF +
                    CRLF ;
        }
        return response;
    }
}
