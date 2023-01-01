package server.httpRequest;

import java.io.IOException;
import java.io.InputStream;

public class RequestParser {
    private InputStream inputStream=null;
    private Request request=null;
    public RequestParser(InputStream inputStream, Request request) {
       this.request=request;
        this.inputStream=inputStream;
    }
   public void  parse(){
        parseRequestLine();
    }
    private void parseRequestLine(){
        try {
            int  ch ;
            StringBuilder stringBuilder=new StringBuilder();
            while ((ch= inputStream.read())!= -1){
                if(ch=='\r'){
                    if(inputStream.read()=='\n'){
                        break;
                    }
                }
                stringBuilder.append((char)ch);
            }
            String requestLine=stringBuilder.toString();
            String[] requestLineArray=requestLine.split(" ");
            request.setMethod(requestLineArray[0]);
            request.setUrl(requestLineArray[1]);
            request.setVersion(requestLineArray[2]);
            parseRequestHeaders();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void parseRequestHeaders(){
        try {
            int  ch ;
            StringBuilder stringBuilder=new StringBuilder();
            while ((ch= inputStream.read())!= -1){
                if(ch=='\r'){
                    if(inputStream.read()=='\n'){
                        break;
                    }
                }
                stringBuilder.append((char)ch);
            }
            request.setContentLength(0);
            parseRequestBody();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void parseRequestBody(){
        try {
            int  ch ;
            int length=request.getContentLength();
            if(length==0){
                return;
            }
            byte[] body=new byte[length];
            while ((ch= inputStream.read())!= -1 && length>0){
                body[body.length-length]=(byte)ch;
                length--;
            }
            request.setBody(body);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
