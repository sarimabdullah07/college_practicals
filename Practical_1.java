
import java.util.Scanner;

class Practical_1
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        
        boolean run = true;
        while (run){
        System.out.println("\n");
        System.out.print("Enter 0 to exit, any num to continue: ");
        int z=sc.nextInt();
        if(z==0)
        {
            System.out.println("Exiting Program...");
            break;
        }

        try 
        {
            System.out.print("Enter 1st number: ");
            int a=sc.nextInt();
            System.out.print("Enter Operator: ");
            String o=sc.next();
            System.out.print("Enter 2nd number: ");
            int b=sc.nextInt();
            System.out.print("Answer: ");
        
            switch (o) 
            {
                case "+" -> System.out.println(a+b);
                case "-" -> System.out.println(a-b);
                case "*" -> System.out.println(a*b);
                case "/" -> 
                {
                    if(b==0)
                    {
                        System.out.println(a/b);
                    }
                    else;
                    {
                        System.out.println("Cannot divided by zero ");
                    }
                }
                case "%" -> 
                {
                    if(b==0)
                    {
                    System.out.println(a%b);
                    }
                    else;
                    {
                        System.out.println("Cannot modulo by zero ");
                    }
                }
                default -> 
                {
                    System.out.println("Enter proper inputs");
                }
            }
        }
        catch (NumberFormatException e) 
        {
            System.out.println("Invalid numeric input! Please enter valid numbers.");
        }}
    }
}
