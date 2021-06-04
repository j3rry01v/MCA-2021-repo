class Box 
{
    double width ;
    double height ;
    double length ;
}
void volume ()
{
    System.out.println("Volume is ");
    System.out.println(width*height*depth);
}
class boxDemo
{
    public static void main (String args[])
    {
    double volume;
    Box b1 = new Box () ;
    Box b2 = new Box ();
    b1.width = 19;
    b1.length=76;
    b1.height=56;
    System.out.println("Volume is " volume());
    }
}
