#include<stdio.h>
#include<stdlib.h>

/* Model of list structure creation */
struct link_list
{
	int data;
	struct link_list *next;
};

typedef struct link_list node;

/* Function for create a list */
void Create(node *p)
{
	int i, num;
	node *temp;
	char ch;
	
	if( p -> data != -999)
	{
	    printf("\n The list already exist.\n");
	    printf(" Do you want to continue? (Y for yes, N for no)\n");
	    scanf(" %c ", &ch);
	    if( ch == 'N'|| ch == 'n')
	        return;
		else
		{
			free(p);
			p->data =-999;
			p->next = NULL;
			Create(p);
		}
		
	}
	printf("\n Enter number of nodes:");
	scanf("%d", &num);
	printf( "\n Enter the elements: " );
	for( i = 0; i < num; i++ )
	{
	    temp = ( node * ) malloc( sizeof ( node ) );
	    if( temp ) /* Memory allocation success full to the node */
	    {
		    scanf( "%d", &temp -> data );
		    temp -> next = NULL;
		
		    if( p -> data != -999 ) /* If, list already contains node(s) */
		    {
			    while( p -> next )
				    p = p -> next;
			    p -> next = temp;
		    }
		    else
			    p -> data = temp -> data; /* If, list is empty, make the newely created node as starting point of the list */				
	    }
	    else
		    printf( "\n Memory overflow\n" ); /* Memory allocation to the node failed */
	}
}

/* Function for add a node to the list */
node *Insert( node *p )
{
	node *q,*temp; 
	int pos, count = 0;
	q = p;
	
	if( p -> data == -999)
	{
	    printf("\n The list is empty. Please create a list first\n");
	    return p;
	}
	
	
	temp = ( node * ) malloc( sizeof ( node ) );
	if( temp ) /* Memory allocation success full to the node */
	{
	    while( q -> next )
	    {
	         count++;
	         q = q -> next;
	    }
	    count++;   
	    printf("\n Enter the position to insert between <1 and %d>:", count + 1);
	    scanf("%d", &pos);
	    if( ( pos < 0 ) || ( pos > (count + 2 ) ) )
	    {
	        printf("\n It is not possible to insert the element at the given position. Position beyond the limit\n");
	        return p;
	    }
	    
		printf( "\n Enter the element: " ); /* Construct a node */
		scanf( "%d", &temp -> data );
		temp -> next = NULL;
		
		if( pos == 1 )
		{
		    printf("\n Inserting the element at the first position.");
		    temp -> next = p;
		    p = temp;
		    return p;
		}
		else
		{
		    q = p;
		    count = 1;
		    while( q -> next )
		    {
		        count++;
		        if( pos == count )
		        {
		            printf("\n Inserting the element in between nodes\n");
		            temp -> next = q -> next;
		            q -> next = temp;
		            return p;
		        }
		        q = q -> next;
		    }
		    printf("\n Inserting the element as last node\n");
		    q -> next = temp;
		    return p;
		    
		}
	}
	else
		printf( "\n Memory overflow\n" ); /* Memory allocation to the node failed */
}

/* Function for list all list elements */
void Display( node *p )
{
	if( p -> data != -999 ) 
	{
		printf( "\n The list elements are: " );
		while( p )
		{
			printf( " %d ", p -> data );
			p = p -> next;
		}
		printf( "\n" );
	}
	else
		printf("\n List is empty \n");
}


/* Function for delete an element from the list */	
node * Delete( node *start )
{
	int ele;
	node *p, *q;
	
	if( start -> data != -999 )
	{
		printf( "\n Enter the element to be dalete:" );
		scanf( "%d", &ele );

		if( start -> data == ele )/* If the element to be delete, is the first element in the list */
		{
			p = start;
			printf( " \nThe element %d is deleted from the list\n ", p -> data );
			if( start -> next == NULL ) /* If list contains only one element */
			{
				q = (node * ) malloc( sizeof( node ) );
				q -> data = -999;
				q -> next = NULL;
				free( p );
				return q;
			}
			start = start -> next;
			free( p );
			return start;
		}
		else /* If the element to be delete, is not the first element of the list */
		{
			p = start;
			while( p -> next ) /* Search for the node */	
			{
				q = p -> next;
				if( q -> data == ele )
				{
					p -> next = q -> next;
					printf( " \nThe element %d is deleted from the list\n ", q -> data );
					free( q );
					return start;
				}
				p = p -> next;
			}
			printf( " \nThe element %d is not present in the list\n ", ele );
			return start;
		}
	}
	else
		printf( "\n Memory underflow\n" );

	return start;
	
}

/* Function for reverse elements of the list */	
node * Reverse( node *start )
{
	node *q, *r, *s;
	q = start;
	r = NULL;
	while( q )
	{
		s = r;
		r = q;
		q = q -> next;
		r -> next = s;
	}
	return r;
	
	
}

/* Function for search an element from the list */
void Search( node *p )
{
    int ele, count = 0;
	if( p -> data != -999 ) 
	{
		printf( "\n Enter the element to search: " );
		scanf("%d", &ele);
		while( p )
		{
		    count++;
		    if( p-> data == ele )
		    {
		        printf("\n The element %d is present in the list at %d position", ele,count);
		        return;
		    }
			p = p -> next;
		}
		printf("\n The element is not present in the list\n" );
	}
	else
		printf("\n List is empty \n");
}


/* Function for sort the list */	
node *Sort(node *start)
{
	node *fnode= start ;
	node *pre1= start;
	node *pre,*t1,*temp;
	if( !start )
		printf("\n The list is empty.");
	else
	{
		node *pre1= start,*pre,*t1,*temp;
		while( start -> next )
		{
			pre = start;
			temp = start -> next;
			while(temp)
			{
				if( start -> data > temp -> data )
				{
					t1 = temp -> next;
					temp -> next = start -> next;
					start -> next = t1;
					if(pre != start )
						pre -> next = start;
					else
						temp -> next = start ;
					if( start == fnode)
						fnode = temp;
					else
						pre1 -> next = temp;
					t1 = start;
					start = temp;
					temp = t1;
				}
			pre = temp;
			temp = temp -> next;
			}
		pre1 = start;
		start = start -> next;
		}
	}
	start = fnode;
	return start;
}

/* Main function */
int main()
{
	
	node *start = ( node * ) malloc( sizeof( node ) ); /* Starting point of the list; Allocate memory for first node */
	start -> data = -999; /* Initialize node, data part with a default value */
	start -> next = NULL; /* Initialize node, next/link part with a default value */
	
	int e = 1, ch;
	
	while( e ) /* Menu implementation for interactively invoke functions for list manipulations */
	{
		printf( "\n--------------MENU--------------\n" );
		printf( "\n\t1. Create\n\t2. Insert\n\t3. Display\n\t4. Delete\n\t5. Reverse\n\t6. Search\n\t7. Sort\n\t8. Exit\n" );
		printf( "\n--------------------------------\n" );
		printf( "\n Enter your choice:" );
		scanf( "%d", &ch );
		
		switch( ch )
		{
			case 1: Create( start );
			     break;
			case 2 : start = Insert( start );
				 break;
			case 3 : Display( start );
				 break;
			case 4 : start = Delete( start );
				 break;
			case 5 : start = Reverse( start );
				 break;
            case 6: Search(start);
                 break;
            case 7: start = Sort( start );
                 break;
			case 8 : e = 0;
				 break;
			default: printf( "\n Invalid choice \n" );
		}
		
	}
	return 0;
} 




