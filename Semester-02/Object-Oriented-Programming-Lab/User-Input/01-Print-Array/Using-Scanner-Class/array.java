import java.util.Scanner;

public class array 
{
    public static void main(String[] args)
     {
        int element_count;
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the number of elements  for the array ");
        element_count = scan.nextInt();
        int[] array = new int[10];
        System.out.println("Now enter array elements ");
        for (int i = 0; i < element_count; i++) 
        {
            array[i] = scan.nextInt();
        } 
        System.out.println("Elements of array are ");
        for (int i = 0; i < element_count; i++) 
        {
            System.out.println(array[i]);
            System.out.println("\n");
        }
    }
}