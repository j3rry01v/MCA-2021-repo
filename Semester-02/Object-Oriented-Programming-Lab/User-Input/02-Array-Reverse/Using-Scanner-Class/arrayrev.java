import java.util.Scanner;

public class arrayrev 
{
    static void reverse(int a[], int n)
    {
        int[] b = new int[n];
        int j = n;
        for (int i = 0; i < n; i++) 
        {
            b[j - 1] = a[i];
            j = j - 1;
        }
        System.out.println("Reversed array is: \n");
        for (int k = 0; k < n; k++) {
            System.out.println(b[k]);
        }
    }
  
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
        System.out.println("Elements of array are  \n ");
        for (int i = 0; i < element_count; i++) 
        {
            System.out.println(array[i]);
        }
        reverse(array, element_count);
    }
}