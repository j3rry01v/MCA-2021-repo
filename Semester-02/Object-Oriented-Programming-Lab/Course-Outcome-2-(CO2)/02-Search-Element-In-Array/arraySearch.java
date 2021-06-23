import java.util.*;

class arraySearch
 {
    int count;

    int[] array = new int[10];
   
    public void get_array()
     {
        int count_loop;

        Scanner scan = new Scanner(System.in);

        System.out.print("Enter size of array : ");

        this.count = scan.nextInt();
       
        System.out.print("Enter the elements : ");

        for (count_loop = 0; count_loop < this.count; count_loop++)
        {
                this.array[count_loop] = scan.nextInt();    
        }
    }

    public void search()
    {
        int count_loop,search,flag=0;

        Scanner scan = new Scanner(System.in);

        System.out.print("Enter element to be search in the array : ");

        search = scan.nextInt();

        for(count_loop = 0; count_loop < this.count;count_loop++)
        {
            if(array[count_loop] == search)
            {
                flag=1;
                break;
            }
        }
        if(flag==1)
        {
            System.out.println("Element is present in array");
        }
        else
        {
            System.out.println("Element not present in array");
        }
    }

    public static void main(String[] args)
     {
        arraySearch data = new arraySearch();
        data.get_array();
        data.search();
    }
}