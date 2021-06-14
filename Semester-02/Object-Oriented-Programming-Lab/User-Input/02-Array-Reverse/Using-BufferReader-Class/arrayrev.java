import java.io.*;

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
        element_count =10;
        BufferedReader br = new BufferedReader(new
        InputStreamReader(System.in));
        System.out.print("Enter the number of elements  for the array ");
        try
        {
         element_count = Integer.parseInt(br.readLine());
        }
        catch (IOException e) 
        {
            e.printStackTrace();
        }
        int[] array = new int[element_count];
        System.out.println("Now enter array elements ");
        for (int i = 0; i < element_count; i++) 
        {
            try
            {
            array[i] = Integer.parseInt(br.readLine());
            }
            catch (IOException e)
             {
                e.printStackTrace();
              } 
            }
        System.out.println("Elements of array are ");
        for (int i = 0; i < element_count; i++) 
        {
            System.out.println(array[i]); 
        }
        reverse(array, array.length); //bug in array length displays element count as 10 ,
        //absent array elements will be displayed as 0
    }
} 