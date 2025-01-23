
import java.util.Arrays;
import java.lang.Math;

public class HelloWorld {
    public static void main(String[] args) {
        String name = "Naman ";
        System.out.println("Hello, " + name);
        int age = 20;
        String H = "Katare";
        System.out.println("You are " + age + " years old.");
        System.out.println(name.length());
        String frnd = name + H;
        System.out.println(frnd.length()); 
        System.out.println(frnd.charAt(10)); 
        String K = frnd.replace("N", "n");
        System.out.println(K);
        System.out.println(frnd);
        System.out.println(frnd.substring(6, 12));
        
        int[] arr = new int[3];
        arr[0] = 9;
        arr[1] = 8; 
        arr[2] = 7;
        
        System.out.println("Before sorting");

        System.out.println(arr.length);
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
        
        System.out.println("After sorting");
        Arrays.sort(arr);
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
        System.out.println("Before sorting");
        int[]hell = {3,2,1};
        for (int i = 0; i < hell.length; i++) {
            System.out.println(hell[i]);
        }
        System.out.println("After sorting");

        Arrays.sort(hell);
        for (int i = 0; i < hell.length; i++) {
            System.out.println(hell[i]);
        }
        System.out.println("2D Array");

        // 2D array
        int [][] arr2 = {{2,3,1},{4,5,6}};
        System.out.println(arr2[0][0]);

        // casting
        double price = 100.00;
        double total = 0.18;
        System.out.println(price + total);

        System.out.println("Problem");
        int a = 10;
        double b = (double)10 + 10.0;
        System.out.println(b);
        int c = (int)10.0 + 10;
        System.out.println(c);

        // constants

        // int AGE = 10;
        final int AGE = 10;
        // with final we cannot change the 
        // perticular vlaue of it when we assign it using the final value
        // if we try ti assign it we cannot cooz it fix and denoted it using capital lettes

        // AGE = 20;
        System.out.println(AGE);
        
        // operators;
        System.out.println("operators:");
        int sum = 10 + 12;
        int mul = 10*12;
        int diff = 10-12;
        double div = 10/12;
        double mod = 10%12;
        System.out.println(sum);    
        System.out.println(mul);
        System.out.println(diff);
        // System.out.println(mul);
        System.out.println(div);
        System.out.println(mod);

        // comparison operators
        System.out.println("comparison operators:");
        int x = 10;
        int y = 20;
        System.out.println(x == y);
        System.out.println(x != y);
        System.out.println(x > y);
        System.out.println(x < y);
        System.out.println(x >= y);
        System.out.println(x <= y);

        // logical operators
        System.out.println("logical operators:");
        boolean p = true;
        boolean q = false;
        System.out.println(p && q);
        System.out.println(p || q);
        System.out.println(!p);
        System.out.println(!q);

        // bitwise operators
        System.out.println("bitwise operators:");
        int m = 10;
        int n = 20;
        System.out.println(m & n);
        System.out.println(m | n);
        System.out.println(m ^ n);
        System.out.println(~m);
        System.out.println(m << 2);
        System.out.println(m >> 2);
        System.out.println(m >>> 2);

        // ternary operator
        System.out.println("ternary operator:");
        int num1 = 10;
        int num2 = 20;
        int result = (num1 > num2) ? num1 : num2;
        System.out.println(result);

        // if else
        System.out.println("if else:");
        int num = 10;
        if (num % 2 == 0) {
            System.out.println("Even");
        } else {
            System.out.println("Odd");
        }

        // switch case
        System.out.println("switch case:");

        int day = 3;
        switch (day) {
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday");
                break;
            default:
                System.out.println("Invalid day");
        }
        
        // while loop
        System.out.println("while loop:");
        int i = 1;
        while (i <= 5) {
            System.out.println(i);
            i++;
        }

        // do while loop
        System.out.println("do while loop:");
        int j = 1;
        do {
            System.out.println(j);
            j++;
        } while (j <= 5);

        // for loop
        System.out.println("for loop:");
        for (int k = 1; k <= 5; k++) {
            System.out.println(k);
        }

        // for each loop
        System.out.println("for each loop:");
        int[] numbers = {1, 2, 3, 4, 5};
        for (int number : numbers) {
            System.out.println(number);
        }

        // break statement
        System.out.println("break statement:");
        for (int l = 1; l <= 5; l++) {
            if (l == 3) {
                break;
            }
            System.out.println(l);
        }
        
        // continue statement
        System.out.println("continue statement:");
        for (int l = 1; l <= 5; l++) {
            if (l == 3) {
                continue;
            }
            System.out.println(l);
        }

        // MAths

        System.out.println("Maths Lib:");
        
        System.out.println(Math.random());

    }
}