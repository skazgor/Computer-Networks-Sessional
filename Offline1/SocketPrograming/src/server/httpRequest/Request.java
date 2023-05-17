package server.httpRequest;

public class Request {
   private RequestType requestType;
    private String url;
    private String version;
    private String host;
    private String userAgent;
    private String contentType;
    private byte[] body;
    private int contentLength;
    private boolean status;
    private String fileName;
    public boolean image = false;
    public boolean isStatus() {
        return status;
    }

    public void setStatus(String status) {
        if(status.equals("OK")){
            this.status=true;
        }
        else{
            this.status=false;
        }
    }

    public String getFileName() {
        return fileName;
    }

    public void setFileName(String filename) {
        this.fileName = filename;
    }
    public RequestType getRequestType() {
        return requestType;
    }

    public byte[] getBody() {
        return body;
    }

    public void setBody(byte[] body) {
        this.body = body;
    }

    public int getContentLength() {
        return contentLength;
    }

    public void setContentLength(int contentLength) {
        this.contentLength = contentLength;
    }

    public void setMethod(String requestType) {
        if(requestType.equals("GET")){
            this.requestType=RequestType.GET;
        }
        else if(requestType.equals("UPLOAD")){
            this.requestType=RequestType.UPLOAD;
        }
        else if(requestType.equals("POST")){
            this.requestType=RequestType.POST;
        }
        else if(requestType.equals("PUT")){
            this.requestType=RequestType.PUT;
        }
        else if(requestType.equals("DELETE")){
            this.requestType=RequestType.DELETE;
        }
        else if(requestType.equals("HEAD")){
            this.requestType=RequestType.HEAD;
        }
        else if(requestType.equals("OPTIONS")){
            this.requestType=RequestType.OPTIONS;
        }
        else if(requestType.equals("TRACE")){
            this.requestType=RequestType.TRACE;
        }
        else if(requestType.equals("CONNECT")){
            this.requestType=RequestType.CONNECT;
        }
    }

    public void setRequestType(RequestType requestType) {
        this.requestType = requestType;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public String getHost() {
        return host;
    }

    public void setHost(String host) {
        this.host = host;
    }

    public String getUserAgent() {
        return userAgent;
    }

    public void setUserAgent(String userAgent) {
        this.userAgent = userAgent;
    }

    public String getContentType() {
        return contentType;
    }

    public void setContentType(String contentType) {
        this.contentType = contentType;
    }

    @Override
    public String toString() {
        String s= "Request{\n" +
                "requestType=" + requestType +
                "\nurl=" + url   +
                ",\nversion=" + version + '\n';
        if(image){
            s+="Sec-Fetch-Dest: image\n";
        }
        else {
            s+="Sec-Fetch-Dest: document\n";
        }
        s+= '}';
        return s;
    }
}
