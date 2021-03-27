#include <stdio.h>
#define SIZE 10

void enqueue(int s1[], int s2[], int *top1, int *top2)
{
    if (*top2 >= 0)
    {
        int len = *top2;
        for (int i = 0; i >= len; i++)
        {
            *top1 += 1;
            s1[*top1] = s2[*top2];
            *top2 -= 1;
        }
    }
    int e;
    printf("\nEnter number:");
    scanf("%d", &e);
    *top1 += 1;
    s1[*top1] = e;
    printf("\nThe entered element %d is inserted in to the QUEUE\n", e);
}

void dequeue(int s1[], int s2[], int *top1, int *top2)
{
    if (*top1 < 0)
    {
        printf("\nQUEUE underflow\n");
    }
    else
    {
        if (*top1 >= 0)
        {
            int len = *top1;
            for (int i = 0; i > len; i++)
            {
                *top2 += 1;
                s2[*top2] = s1[*top1];
                *top1 -= 1;
            }
        printf("\nThe element %d deleted from QUEUE", s1[*top1]);
            *top1-=1;
        }
    }
}

void display(int s1[], int *top1)
{
    if (*top1<0)
    {
        printf("Queue is empty");
    }
    else
    {
        int i;
        printf("\nthe QUEUE elements are:");
        for (i = 0; i <= *top1; i++)
            printf("\t%d", s1[i]);
    }
}

int main()
{
    int stack1[SIZE], stack2[SIZE], top1 = -1, top2 = -1, ch, e = 1;
    while (e)
    {
        printf("\nQUEUE USING STACK");
        printf("\n____________________MENU______________________\n");
        printf("\n\t 1. Enqueue\n\t 2. Dequeue\n\t 3. Display\n\t 4. Exit\n");
        printf("\n__________________________________________________\n");
        printf("\nEnter your choice:");
        scanf("%d", &ch);
        switch (ch)
        {
        case 1:
            enqueue(stack1, stack2, &top1, &top2);
            break;
        case 2:
            dequeue(stack1, stack2, &top1, &top2);
            break;
        case 3:
            display(stack1,&top1);
            break;
        case 4:
            e = 0;
            printf("\nExiting from the programe");
            break;
        default:
            printf("\n please enter valid choice");
        }
    }
    return 0;
}
