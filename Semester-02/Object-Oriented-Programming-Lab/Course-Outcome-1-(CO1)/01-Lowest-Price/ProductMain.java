class Product 
{
    String product_code;
    String product_name;
    double product_price;

    Product(String product_code, String product_name, double product_price) {
        this.product_code = product_code;
        this.product_name = product_name;
        this.product_price = product_price;
    }

    String GetLowestPrice(Product p1, Product p2) {
        if (p1.product_price < p2.product_price && p1.product_price < product_price)
            return p1.product_name;
        if (p2.product_price < p1.product_price && p2.product_price < product_price)
            return p2.product_name;
        else
            return product_name;
    }
}

public class ProductMain 
{
    public static void main(String[] args)
     {
        Product p1 = new Product("01", "Apple", 90);
        Product p2 = new Product("02", "Orange", 50);
        Product p3 = new Product("03", "Cherry", 75);

        String item;

        item = p3.GetLowestPrice(p1, p2);

        System.out.println("\nProduct with lowest price is : " +item + "\n");

    }
}