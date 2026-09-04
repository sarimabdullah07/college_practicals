import java.util.*;

class practice_1
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        try
        {
            System.out.print("hit '0' to stop & any number to continue: ");
            boolean running=true;
            while (running){
                System.out.print("Continue?");
                int i=sc.nextInt();
                if(i==0){
                    break;} 
                System.out.print("Enter 1st number: ");
                int a = sc.nextInt();
                System.out.print("Enter Operator: ");
                String o=sc.next();
                System.out.print("Enter 2nd number: ");
                int b = sc.nextInt();
                System.out.println("Answer: ");
                switch (o) 
                {
                    case "+" -> System.out.println(a+b); 
                    case "-" -> System.out.println(a-b);
                    case "*" -> System.out.println(a*b);
                    case "/" ->{
                        if(b==0)
                        {
                            System.out.println("Cannot divisible by zero. ");
                        }
                        else;
                        {
                            System.out.println(a/b);
                        }
                    }
                    case "%" -> {
                        if(b==0)
                        {
                            System.out.println("Cannot modulo by zero.");
                        }
                        else;
                        {
                            System.out.println(a%b);
                        }
                    }
                default -> System.out.println("Give suitable data");
                }
            }
        }
        catch (Exception e) 
        {
            System.out.println("Give suitable inputs.");
        }
    }
}

