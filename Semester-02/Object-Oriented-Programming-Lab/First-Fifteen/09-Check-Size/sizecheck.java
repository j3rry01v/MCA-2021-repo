

public class sizecheck {
    public static void main(String[] args) {

        int number = 42; //user imput mode will be added later
        String size;
        switch (number) {
    
          case 29:
            size = "Small";
            break;
    
          case 42:
            size = "Medium";
            break;
            
          case 44:
            size = "Large";
            break;
    
          case 48:
            size = "Extra Large";
            break;
          
          default:
            size = "Unknown";
            break;
    
        }
        System.out.println("Size: " + size);
      }
    
}
