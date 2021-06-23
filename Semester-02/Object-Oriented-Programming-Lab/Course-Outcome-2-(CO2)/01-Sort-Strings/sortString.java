import java.util.*;

class sortString
 {
    String str;

    public void get_string() 
    {
        Scanner scan = new Scanner(System.in);

        System.out.println("Enter a string  ");

        this.str = scan.nextLine();
    }

    public void sort_print()
     {
        char charArray[] = str.toCharArray();

        Arrays.sort(charArray);

        System.out.println("\n Sorted string is " + new String(charArray));
        System.out.println("");
    }

    public static void main(String[] args) 
    {
        sortString data = new sortString();

        data.get_string();
        
        data.sort_print();
    }

}