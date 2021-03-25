#include <stdio.h>
#include <stdlib.h>

void read(int a[],int *limit)
{
    int i;
    printf("\nEnter the values in sorted order:");
    for ( i = 0; i < *limit; i++)
    {
        scanf("%d", &a[i]);
    }
}
void merge(int arr1[], int arr2[], int *s1, int *s2, int marr[])
{
    int i=0, j=0,k=0;
    while (k < *s1 + *s2)
    {
        if (j < *s2 && i < *s1)
        {
            if (arr1[i] <= arr2[j])
            {
                marr[k] = arr1[i];
                k++;
                i++;
            }
            else
            {
                marr[k] = arr2[j];
                k++;
                j++;
            }
        }
        else
        {
            if (j >= *s2 && i < *s1)
            {
                marr[k] = arr1[i];
                i++;
                k++;
            }
            else if (i >= *s1 && j < *s2)
            {
                marr[k] = arr2[j];
                j++;
                k++;
            }
        }
    }
    printf("\nmerged successfully\n");
}

void display(int arr1[], int arr2[], int *s1, int *s2, int marr[])
{
    int i;
    printf("\nThe elements in first array:\n");
    for(i=0;i<*s1;i++)
    {
        printf(" %d",arr1[i]);
    }
    printf("\nThe elements in second array:\n");
    for(i=0;i<*s2;i++)
    {
        printf(" %d",arr2[i]);
    }
    printf("\nThe array elements after merging:\n");
    for(i=0;i<*s1+*s2;i++)
    {
        printf(" %d",marr[i]);
    }
}

int main()
{
    int arr1[50], arr2[50], marr[100], s1,s2,e=0,ch;
    printf("\nMERGE TWO SORTED ARRAYS\n");
    do
    {
        printf("\n_______________MENU_______________\n");
        printf("\n\t1.Read sorted arrays\n\t2.Merge array\n\t3.Display\n\t4.Exit\n");
        printf("\n__________________________________\n");
        printf("\nEnter your choice:");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1:printf("\nEnter the size of the  array1:");
                    scanf("%d", &s1);
                    read(arr1,&s1);
                    printf("\nEnter the size of the  array2:");
                    scanf("%d", &s2);
                    read(arr2,&s2);
                    break;
            case 2:
                    merge(arr1,arr2,&s1,&s2,marr);
                    break;
            case 3:display(arr1,arr2,&s1,&s2,marr);
                    break;
            case 4:printf("Exiting from the programme");
                    break;
            default:
                    printf("Enter the valid option:");
        }
    }while(ch!=4);


    return 0;
}