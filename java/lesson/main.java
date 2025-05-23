import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello");
        System.out.println("I'm here");
        Scanner scn = new Scanner(System.in);
        System.out.println("Enter a number:");
        int num = scn.nextInt();
        scn.close();
        System.out.println("The number is: " + num);
        int countOfChars = 0;
        double averageOfChars = 0.0;
        char temp = "a";
        while(num != 0) 
        {
            countOfChars ++;
            averageOfChars = averageOfChars + num % 10;
            num = num / 10;
        }
        averageOfChars = averageOfChars / countOfChars;
        System.out.println("The amount of chars in the number is: " + countOfChars);
        System.out.println("The average of the chars in the number is: " + averageOfChars);
    }
}