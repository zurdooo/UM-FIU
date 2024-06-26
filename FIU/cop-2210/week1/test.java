package week1;

import java.util.Scanner;

public class test {
    public static void main(String[] args) {
        int sum;
        int currVal;
        Scanner scnr = new Scanner(System.in);
        sum = 0;
        currVal = scnr.nextInt();
        while (currVal == 0) {
            sum = sum + currVal;
            currVal = scnr.nextInt();
            
        }
        System.out.println("Sum: " + sum);
    }   
}

