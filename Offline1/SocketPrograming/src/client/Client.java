package client;

import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the full path of the file you want to send to the server:");
        while (true)
        {
            String path = scanner.nextLine();
            String[] pathArray = path.split(" ");
            for(String s : pathArray)
            {
                System.out.println(s);
            }
            if (pathArray.length == 1)
            {
                if (pathArray[0].equals("exit"))
                {
                    break;
                }
                else
                {
                    System.out.println("Invalid input");
                }
            }
            else
            {
                if(pathArray[0].equals("upload"))
                {
                    for (int i = 1; i < pathArray.length; i++) {
                        ClientWorker clientWorker = new ClientWorker(pathArray[i]);
                        clientWorker.start();
                    }
                }
                else
                {
                    System.out.println("Invalid command");
                }
            }
        }
    }
}
