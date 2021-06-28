public class product {
    String code;
    String name;
    int price;

    public product(String product_code, String product_name, int product_price)
    {
        code = product_code;
        name = product_name;
        price = product_price;
    }

     int price() 
    {
        return price;
    }

    public static void main(String[] args)
    {
        product p1 = new product("", "TV", 2);
        product p2 = new product("B123", "RADIO", 21);
        product p3 = new product("C123", "DVD", 3);

        if (p1.price <= p3.price && p1.price <= p2.price) 
        {
            System.out.println("Lowest product ID is  : " + p1.code);
        }
        if (p3.price <= p1.price && p3.price <= p2.price) 
            System.out.println("Lowest product ID is  : " + p3.code);
        if (p2.price <= p3.price && p2.price <= p1.price) 
            System.out.println("Lowest product ID is  : " + p2.code);
    }
}