#include<stdio.h>
#define SIZE 10

void read(int a[],int *n)
{
    printf("Enter the number of elements:");
    scanf("%d",n);
    printf("\nEnter the elements:");
    for(int i=0;i<*n;i++)
    {
        scanf("%d",&a[i]);
    }

}
void search(int a[],int *n)
{
    int e,i;
    printf("\nEnter the element to be searched:");
    scanf("%d",&e);
    for(i=0;i<*n;i++)
    {
        if(a[i] == e)
        {
            printf("\n%d is located at position %d\n",e,i+1);
            return;
        }
    }
    printf("\nEntered element is not in the data\n");
}
void display(int a[],int *n){
    printf("\n the  elements are:");
    for(int i=0;i<*n;i++)
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