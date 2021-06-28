// import java.util.*;

// class stringManipulation
// {
// public class StringManipulations 
// {
//     public static void main(String[] args) 
//     {
// 		// Scanner scan = new Scanner(System.in);
// 		// System.out.println("Enter a  string ");
//         // data =scan.nextLine();
//         stringFunctions str = new stringFunctions();
// 		while(true)
//         {
// 			System.out.println("1.To Uppercase");

// 			System.out.println("2.To Lowercase ");

// 			System.out.println("3.Replace Characters");

// 			System.out.println("4.Reverse");

// 			System.out.println("Enter your choice::");

// 			int choice = scan.nextInt();

// 			switch(choice)
//             {
// 			case 1 :stringToUpperCase();
// 			break;
// 			case 2 :stringToLowerCase();
// 			break;
// 			case 3 :stringReplace(); 
// 			break;
//             case 4 :stringReverse();
// 			default: System.out.println("Invalid option");
// 			}
// 		}
// class stringFunctions 
// {

//   public void stringToUpperCase()
//   {
//    System.out.println("\n Converted to UPPERCASE ");

//    System.out.println(data.toUpperCase());
//    return;
//   }

//  public void  stringToLowerCase()
//   {
//    System.out.println("\n Converted to lowercase ");

//    System.out.println(data.toLowerCase());
//    return;
//   }

//   public String stringReplace (string tempchar , string replace_text)
//   {
//       System.out.println("Which one to replace");

//       tempchar = scan.nextLine();

//       System.out.println("Replace with ?  ");

//       replace_text =scan.nextLine();

//       System.out.println("Replaced...!");

//       System.out.println(data.replace(tempchar, replace_text));

//   }
//  public void stringReverse ()
//   {

//    System.out.println("\n String reversed ");

//    System.out.println(data.reverse());
  
// }
// }

import java.util.*; 
class stringFunctions 
{  
public static void main(String args[]) 
{ 
Scanner scan = new Scanner(System.in);
		System.out.println("Enter a  string ");
        public String data =scan.nextLine();
stringPerform perform=new stringPerform();  
 while(true) 
 {
 			System.out.println("1.To Uppercase");

			System.out.println("2.To Lowercase ");

			System.out.println("3.Replace Characters");

			System.out.println("4.Reverse");

			System.out.println("Enter your choice::");
 int option=scan.nextInt(); 
 switch(option) 
 { 
       case 1: 
 	perform.add();  	
        break;  	
       case 2: 
 	perform.sub();  	
        break;  	
       case 3: 
 	perform.mul();  	
        break;  	
       case 4:  	
    perform.div();  	
        break;  	
       default:
        System.out.println("invalid choice");
        break;
   }  
   } 
 }
} 
class stringPerform
{  
 	public int a=20,b=10; 
 void stringToUpperCase()
  {
   System.out.println("\n Converted to UPPERCASE ");

   System.out.println(data.toUpperCase());
   return;
  }

 void  stringToLowerCase()
  {
   System.out.println("\n Converted to lowercase ");

   System.out.println(data.toLowerCase());
   return;
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
} 
