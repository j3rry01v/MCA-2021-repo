#include<stdio.h>
#include<stdlib.h>
#define SIZE 10

void read(int a[],int *top)
{
    int n;
    printf("\nEnter the number of elements:");
    scanf("%d",&n);
    printf("\nEnter the array elements in sorted order:");
    for (int i=0;i<n;i++)
    {
        *top+=1;
        scanf("%d",&a[*top]);
    }
}

void search(int a[],int *top)
{ 
    int ele,first,last,mid;
    printf("\nEnter the element to be searched:");
    scanf("%d",&ele);
    first=0;
    mid=*top/2;
    last=*top;
    while(first<=last)
    {
        if(a[mid] == ele)
        {
            printf("\nThe location of entered element is %d",mid+1);
            return;
        }
        else if (a[mid]>ele)
        {
            last=mid-1;
        }
        else
        {
            first=mid+1;
        }
        mid=(first+last)/2;
        
    }
    printf("\n Entered element is not in the list");
}

void display(int a[],int *n){
    printf("\n the  elements are:");
    for(int i=0;i<=*n;i++)
        printf("%d ",a[i]);
}

int main()
{
    int arr[SIZE],ch,e=1;
    int n=-1;
    while(e)
    {
        printf("\n\n____________________MENU______________________\n");
        printf("\n\t 1. read\n\t 2. search\n\t 3. Display\n\t 4. Exit\n");
        printf("\n__________________________________________________\n");
        printf("\nEnter your choice:");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1:read(arr, &n);
                    break;
            case 2:search(arr,&n);
                    break;
            case 3:display(arr,&n);
            break;
            case 4:e=0;
                printf("\nExiting from the programe\n");
                break;
            default:printf("\n please enter valid choice\n");
        }
    }
    return 0;

}