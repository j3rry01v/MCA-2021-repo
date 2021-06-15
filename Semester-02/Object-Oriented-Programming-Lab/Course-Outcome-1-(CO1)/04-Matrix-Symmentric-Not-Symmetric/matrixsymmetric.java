import java.util.*;

import java.util.Scanner;
 
public class matrixsymmetric
{   
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
         
        System.out.println("Enter the number of rows: ");
         
        int row_element = scan.nextInt();
         
        System.out.println("Enter the number of columns : ");
         
        int column_element = scan.nextInt();
         
        int matrix[][] = new int[row_element][column_element];
         
        System.out.println("Enter the elements :");
         
        for (int i = 0; i < row_element; i++)
        {
            for (int j = 0; j < column_element; j++)
            {
                matrix[i][j] = scan.nextInt();
            }
        }
         
        System.out.println("Entered Matrix is :");
         
        for (int i = 0; i < row_element; i++)
        {
            for (int j = 0; j < column_element; j++)
            {
                System.out.print(matrix[i][j]+"\t");
            }
             
            System.out.println("");
        }
         
        //Checking the input matrix for symmetric
         
        if(row_element != column_element)
        {
            System.out.println("The given matrix is not square matrix, so it is not symmetric ");
        }
        else
        {
            boolean symmetric = true;
             
            for (int i = 0; i < row_element; i++)
            {
                for (int j = 0; j < column_element; j++)
                {
                    if(matrix[i][j] != matrix[j][i])
                    {
                        symmetric = false;
                        break;
                    }
                }
            }
             
            if(symmetric)
            {
                System.out.println("\nThe given matrix is symmetric");
            }
            else
            {
                System.out.println("\nThe given matrix is not symmetric");
            }
        }
    }
}