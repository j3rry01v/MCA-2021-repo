import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;
 
public class addComplex
{
    public static void main(String[] args) 
    {
        double j1 = 0;
        double j2 = 0;
        double i1 =0;
        double i2 = 0;
    //    Scanner scan = new Scanner(System.in);
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("\nEnter the real part and imaginary part of the first complex number");
        try
        {
            i1=Double.parseDouble(br.readLine());
            j1=Double.parseDouble(br.readLine());
        }
        catch (Exception e)
        {
            System.out.println("Check the complex number again ");
            return;
        }
        System.out.println("\nEnter the real part and imaginary part of the second complex number");
        try
        {
            i2=Double.parseDouble(br.readLine());
            j2=Double.parseDouble(br.readLine());
        }
        catch (Exception e)
        {
            System.out.println("Check the complex number again ");
            return;
        }
        System.out.println("\n The first complex number is "+ i1 + "+(" + j1 + ")i");

        System.out.println("\n The second complex number is "+ i2 + " +(" + j2 + ") i");

        System.out.println("\n The sum of the two complex numbers is " + (i1 + i2) + " + i(" + (j1 + j2) + ")");
    }
}