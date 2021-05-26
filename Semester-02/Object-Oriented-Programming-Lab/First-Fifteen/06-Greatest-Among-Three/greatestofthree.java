

public class greatestofthree {
    
    public static void main(String[] args) {

        int num1 = 10, num2 = 20, num3 = 30;
  
        if( num1 >= num2 && num1 >= num3)
            System.out.println(num1+" is  Greatest");
  
        else if (num2 >= num1 && num2 >= num3)
            System.out.println(num2+" is Greatest");
  
        else
            System.out.println(num3+" is Greatest");
    }
}
