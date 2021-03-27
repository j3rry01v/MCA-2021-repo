#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include<unistd.h>

typedef struct node
{
    int data;
    struct node *next;
    struct node *prev;
} node;

node *head;

// inserting value to the doubly linked list
void insert(int *op)
{
    // checking if the entered option is invalid 
    if (*op > 3)
    {
        printf("\nEnter a valid option!!!\n\n");
        return;
    }
    int pos, i, val;
    node *temp = (node *)malloc(sizeof(node *));
    // checking overflow condition
    if (temp == NULL)
    {
        printf("\nList Overflow\n");
    }
    else
    {
        printf("\nEnter the value to be inserted:");
        scanf("%d", &val);
        temp->data = val;
        // inserting value in the front of the doubly linked list
        if (*op == 1)
        {

            if (head == NULL)
            {
                temp->next = NULL;
                temp->prev = NULL;
                head = temp;
            }
            else
            {
                temp->next = head;
                temp->prev = NULL;
                head->prev = temp;
                head = temp;
            }
            printf("\none value entered at front of Doubly linked list\n");
        }
        // inserting value in the last position of the doubly linked list
        else if (*op == 2)
        {

            if (head == NULL)
            {
                temp->next = NULL;
                temp->prev = NULL;
                head = temp;
            }
            else
            {
                node *ptr = head;
                while (ptr->next != NULL)
                {
                    ptr = ptr->next;
                }
                ptr->next = temp;
                temp->next = NULL;
                temp->prev = ptr;
            }
            printf("\none value entered at last of Doubly linked list\n");
        }
        // inserting value in the specified position of the doubly linked list
        else if (*op == 3)
        {
            printf("\nEnter the position where you want to insert the data:");
            scanf("%d", &pos);
            if (pos == 1 && head == NULL)
            {
                temp->next = NULL;
                temp->prev = NULL;
                head = temp;
            }
            else
            {
                node *ptr = head;
                i = 1;
                while (i < pos - 1 && ptr != NULL)
                {
                    ptr = ptr->next;
                    i++;
                }
                if (ptr == NULL)
                {
                    printf("\nNumber of values in the linked list is smaller than the value you entered\n");
                }
                else
                {
                    temp->next = ptr->next;
                    ptr->next->prev = temp;
                    ptr->next = temp;
                    temp->prev = ptr;
                    printf("\nValue entered at position %d ", pos);
                }
            }
        }
    }
}

// function for deleting elements from the doubly linked list
void delete (int *op)
{
    // checking whether the entered choice is valid or not
    if (*op > 3)
    {
        printf("\nplease Enter a valid option!!!\n");
        return;
    }
    int pos, i;
    node *temp = head;
    // checking underflow condition
    if (temp == NULL)
    {
        printf("\nUnderflow!!!\n");
        return;
    }
    else
    {

        // deleting an element from first position of the doubly linked list 
        if (*op == 1)
        {
            if (temp->next == NULL)
            {
                head = NULL;
            }
            else
            {
                head = temp->next;
                head->next = temp->next->next;
            }
            printf("\none value deleted from front of Doubly linked list\n");
        }

        // deleting an element from last position of the doubly linked list
        else if (*op == 2)
        {
            node *ptr = head;
            while (ptr->next != NULL)
            {
                ptr = ptr->next;
            }
            ptr->prev->next = NULL;
            printf("\none value deleted from the last position of Doubly linked list\n");
        }

        // deleting an element from specified position of the doubly linked list
        else if (*op == 3)
        {
            printf("\nEnter the position where you want to delete the data:");
            scanf("%d", &pos);
            node *ptr = head;
            if (pos == 1 && ptr->next == NULL)
            {
                head = NULL;
                printf("\nValue deleted in position %d ", pos);
            }
            else
            {
                i = 1;
                while (i < pos - 1 && ptr != NULL)
                {
                    printf("%d\n", i);
                    ptr = ptr->next;
                    i++;
                }
                if (ptr->next == NULL)
                {
                    printf("\nNumber of values in the linked list is smaller than the value you entered\n");
                }
                else
                {
                    ptr->next = ptr->next->next;
                    printf("\nValue deleted in position %d\n ", pos);
                }
            }
        }
    }
}

// function to display the elements in the doubly linked list
void display()
{
    printf("display function\n");
    if (head == NULL)
    {
        printf("\nlist is empty\n");
    }
    else
    {
        node *temp = head;
        while (temp->next != NULL)
        {
            printf("%d-->", temp->data);
            temp = temp->next;
        }
        printf("%d-->NULL", temp->data);
    }
}

void search(int ele)
{
    if(head==NULL)
    {
        printf("\nList is empty!!!");
        return;
    }
    node *temp= head;
    while(temp!=NULL)
    {
        if(temp->data==ele)
        {
            printf("%d FOUND",ele);
            return;
        }
        temp=temp->next;
    }
    printf("%d NOT FOUND!!!",ele);

}

void sort()
{
    struct node *current,*index;
    for(current=head;current->next!=NULL;current=current->next)
    {
        for(index=current->next;index!=NULL;index=index->next)
        {
            if(current->data>index->data)
            {
                int temp=current->data;
                current->data=index->data;
                index->data=temp;
            }
        }
    }
    printf("\nsorted the list successfully\n");
}

int main()
{
    int ch, e = 1, op,data;
    while (e)
    {
        printf("\n DOUBLY LINKED LIST");
        printf("\n______________MENU______________");
        printf("\n 1.INSERT \n 2.DELETE \n 3.DISPLAY \n 4.SEARCH \n 5.SORT\n 6.EXIT");
        printf("\n_________________________________\n");
        printf("\n Enter your choice:");
        scanf("%d", &ch);
        switch (ch)
        {
        case 1:
            printf("\n__________Insertion option__________\n");
            printf("\n1.Front\n2.Last\n3.In between\n");
            printf("_________________________________\n");
            printf("\nchose your option:");
            scanf("%d", &op);
            insert(&op);
            break;
        case 2:
            printf("\n__________Deletion option__________\n");
            printf("\n1.Front\n2.Last\n3.In between\n");
            printf("_________________________________\n");
            printf("\nchose your option:");
            scanf("%d", &op);
            delete (&op);
            break;
        case 3:
            display();
            break;
        case 4:printf("Enter the data you want to search:");
        scanf("%d",&data);
            search(data);
            break;
        case 5:
            sort();
            break;
        case 6:
            e = 0;
            printf("\n exiting........");
            break;
        default:
            printf("\n please enter valid choice\n");
            break;
        }       
    }
    printf("\n\n\n\t\t\t----------successfully exited----------\n\n");
    return 0;
}