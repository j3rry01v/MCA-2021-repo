
public class sumandaverage {
    public static void main(String[] args) {
        int[] arr = {84,50,64,76,78};
        int total = 0;

        for(int i=0; i<4; i++){
        	total = total + arr[i];
        }
        int average = total / 5;
        
        System.out.printf("The average is: ", +average);
    }
    
}
