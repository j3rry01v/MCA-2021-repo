import java.util.*;
import java.util.Scanner;

public class matrixaddition
 {
    int row_element;

    int column_element;

    int[][] array = new int[10][10];

    public void build_Matrix()
    {
        int r,c;

        Scanner scan= new Scanner(System.in);

        System.out.print(" \n Enter the number of rows for matrix : ");

        this.row_element = scan.nextInt();

        System.out.print("\n Enter the number of columns for matrix ");

        this.column_element = scan.nextInt();
        
        System.out.print("\n Now enter elements of matrix: ");

        for(r=0;r<this.row_element;r++)
        {
            for(c=0;c<this.column_element;c++)
            {
                this.array[r][c] = scan.nextInt();
            }
        }
    }
// public String alert()
// {
//    System.out.println("Sum of the two matrix is..");
//    return null ;
// }
    
    public static matrixaddition sum_Matrix(matrixaddition matrix1, matrixaddition matrix2)
     {
        int rc, cc;

        matrixaddition temp = new matrixaddition();

        if (matrix1.row_element == matrix2.row_element && matrix1.column_element == matrix2.column_element)
        {
            temp.row_element =matrix1.row_element;

            temp.column_element = matrix1.column_element;

            for (rc = 0; rc < matrix1.row_element; rc++) 
            {
                for (cc = 0; cc < matrix1.column_element; cc++)
                 {
                    temp.array[rc][cc] =  matrix1.array[rc][cc] +  matrix2.array[rc][cc];
                }
            }
        }
        else
         {
            System.out.println("Addition not possible : The matrix must have same number of rows and colums ");
         }

        return temp;
    }

    public void display_Matrix()
    {
        System.out.println("Sum of the two matrix is..");

        int rc,cc;

        for(rc=0;rc<this.row_element;rc++)
        {
            System.out.println(" ");
            
            for(cc=0;cc<this.column_element;cc++)
            {
                System.out.print(this.array[rc][cc] );

                System.out.print(" ");

            }
            System.out.print(" ");
        }
    }
    public static void main(String[] args) 
    {
        matrixaddition first = new matrixaddition();

        matrixaddition second = new matrixaddition();

        matrixaddition temp = sum_Matrix(first, second);

        first.build_Matrix();

        second.build_Matrix();

        temp = sum_Matrix(first,second);
        
        temp.display_Matrix();
    }
}