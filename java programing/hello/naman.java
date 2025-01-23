import java.util.Scanner;
public class naman {

    public static void main(String[] args) {
        // input in java

        Scanner sc = new Scanner(System.in);
        String name = sc.nextLine();
        System.out.println("Hello " + name);

        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println("Before swapping " + a + " " + b);

        b = b + a;
        a = b - a;
        b = b - a;

        System.out.println("After swapping " + a + " " + b);
    }     
}
