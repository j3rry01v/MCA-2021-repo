import java.io.*;

public class array 
{
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
        int[] array = new int[10];
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
            System.out.println("\n");
        }
    }
}