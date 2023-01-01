package server.httpRequest;

public enum Status {
    OK("200 OK"),NOT_FOUND("404 Not Found");
    public String status;
    private Status(String status){
        this.status = status;
    }
}
