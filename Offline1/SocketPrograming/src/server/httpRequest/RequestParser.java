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
//       try {
//         while (inputStream.available() > 0) {
//             int i = inputStream.read();
//             System.out.print(i+" ");
//         }
//       } catch (IOException e) {
//           e.printStackTrace();
//       }
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
            boolean flag=false;
            int  ch ;
            StringBuilder stringBuilder=new StringBuilder();
            while ((ch= inputStream.read())!= -1){
                if(ch=='\r'){
                    if((ch=inputStream.read())=='\n'){
                        if(stringBuilder.isEmpty()){
                            return;
                        }
                        flag=true;
                        if((ch=inputStream.read())=='\r'){
                            if((ch=inputStream.read())=='\n'){
                                break;
                            }
                        }
                    }
                }
                if(flag){
                    stringBuilder.append('\r');
                    stringBuilder.append('\n');
                    flag=false;
                }
                stringBuilder.append((char)ch);
            }
            System.out.println(stringBuilder.toString());
            request.setContentLength(0);
            String [] requestHeaders=stringBuilder.toString().split("\r\n");
            for(String requestHeader:requestHeaders){
                String [] requestHeaderArray=requestHeader.split(": ");
                if(requestHeaderArray[0].equals("Sec-Fetch-Dest")){
                    if(requestHeaderArray[1].equals("image")){
                        request.image=true;
                    }
                }
                if(requestHeaderArray[0].equals("Content-Length")){
                    request.setContentLength(Integer.parseInt(requestHeaderArray[1]));
                }
                if(requestHeaderArray[0].equals("File-Name")){
                    request.setFileName(requestHeaderArray[1]);
                }
                if(requestHeaderArray[0].equals("Status")){
                    System.out.println(requestHeaderArray[1]);
                    request.setStatus(requestHeaderArray[1]);
                }
            }
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
