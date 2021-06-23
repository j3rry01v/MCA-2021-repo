import java.util.*;

class stringManipulation
{
    String data;

    stringManipulation(String data)
    {
        this.data=data;
    }

   void stringToUpperCase()
   {
    System.out.println("\n Converted to UPPERCASE ");

    System.out.println(data.toUpperCase());
   }

   void stringToLowerCase()
   {
    System.out.println("\n Converted to lowercase ");

    System.out.println(data.toLowerCase());
   }

   void stringReplace (string tempchar , string replace_text)
   {
       System.out.println("Which one to replace");

       tempchar = scan.nextLine();

       System.out.println("Replace with ?  ");

       replace_text =scan.nextLine();

       System.out.println("Replaced...!");

       System.out.println(data.replace(tempchar, replace_text));

   }
   void stringReverse ()
   {

    System.out.println("\n String reversed ");

    System.out.println(data.reverse());
   }
}

public class StringManipulations 
{
    public static void main(String[] args) 
    {
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter a  string ");
        data =scan.nextLine();

		while(true)
        {
			System.out.println("1.To Uppercase");

			System.out.println("2.To Lowercase ");

			System.out.println("3.Replace Characters");

			System.out.println("4.Reverse");

			System.out.println("Enter your choice::");

			int choice = scan.nextInt();

			switch(choice)
            {
			case 1 :stringToUpperCase();
			break;
			case 2 :stringToLowerCase();
			break;
			case 3 :stringReplace(); 
			break;
            case 4 :stringReverse();
			default: System.out.println("Invalid option");
			}
		}

	}
}