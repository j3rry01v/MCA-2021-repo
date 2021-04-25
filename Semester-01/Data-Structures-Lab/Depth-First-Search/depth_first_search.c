#include<stdio.h>
#include<stdlib.h>
struct node {
int vertex;
    struct node* next;
};
typedef struct node node;
struct Graph
{
    int numVertices;
    int *visited;
    node **adjLists;
};
typedef struct Graph Graph;
node *createNode(int v)
{
    node *newNode = (node *)malloc(sizeof(node));
    newNode -> vertex = v;
    newNode -> next = NULL;
    return newNode;
}
void addEdge(Graph* graph, int src, int dest) {
    node *newNode = createNode(dest);
    newNode -> next = graph -> adjLists[src];
    graph -> adjLists[src] = newNode;
    newNode = createNode(src);
    newNode -> next = graph -> adjLists[dest];
    graph -> adjLists[dest] = newNode;
}
Graph *createGraph(int vertices, int edges)
{
    int i;
    int src,dest;
    Graph *graph =(Graph *) malloc(sizeof(Graph));
    graph -> numVertices = vertices;
    graph -> adjLists = malloc(vertices * sizeof(node*));
    graph -> visited = malloc(vertices * sizeof(int));

    for(i = 0; i < vertices; i++)
    {
        graph -> adjLists[i] = NULL;
        graph -> visited[i] = 0;
    }
    printf("\nEnter Edges...\n");
    printf("\n<source,destination> (Between 0 to %d)", vertices - 1);
    for(i = 0; i < edges; i++)
    {
        printf("\nEnter edge %d:", i+1);
        scanf("%d%d", &src,&dest);
        addEdge(graph,src,dest);
}
    return graph;
}
void DFS(Graph *graph, int vertex)
{
    node *adjList = graph -> adjLists[vertex];
    node *temp = adjList;
    graph -> visited[vertex] = 1;
    printf("%d -> ", vertex);
    while(temp != NULL)
    {
        int connectedVertex = temp->vertex;
        if(graph -> visited[connectedVertex] == 0)
        {
            DFS(graph, connectedVertex);
        }
        temp = temp -> next;
    }
}
void displayGraph(Graph *graph)
{
    int v;
    for(v = 0; v < graph -> numVertices; v++)
    {
node *temp = graph -> adjLists[v];
printf("\n Adjacency list of vertex %d\n ", v); while(temp)

        {
            printf("%d -> ", temp -> vertex);
            temp = temp -> next;
}
        printf("\n");
    }
}
int main() {
        Graph   *graph = NULL;
        int nv, ne;
        int start = 0;
        int e = 1, ch;
while( e ) {
                printf( "\n--------------MENU--------------\n" );
                printf( "\n\t1. Create Graph\n\t2. Display\n\t3. Depth First Search
(DFS) Algorithm\n\t4. Exit\n" );
0): ");
}
return 0; }
case 1: printf("\nEnter number of verices and edges: ");
        scanf("%d%d", &nv,&ne);
        graph = createGraph(nv,ne);
     break;
case 2: displayGraph(graph);
         break;
case 3: printf("\nSearched in the order (from the vertex
        DFS(graph,start);
     break;
case 4 : e = 0;
         break;
default: printf( "\n Invalid choice \n" );
printf( "\n--------------------------------\n" );
printf( "\n Enter your choice:" );
scanf( "%d", &ch );
switch( ch ) {
}
