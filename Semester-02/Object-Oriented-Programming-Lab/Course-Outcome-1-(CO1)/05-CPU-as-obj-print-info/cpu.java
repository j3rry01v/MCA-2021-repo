class cpu 
{
    int price;

    cpu(int p)
     {
        this.price = p;
    }

    class Processor 
    {
        int cores;

        String manufacturer;

        Processor(int n, String m) 
        {
            this.cores = n;

            this.manufacturer = m;
        }

        void display() 
        {
            System.out.println("\nNo of Cores : " + this.cores);  

            System.out.println("\nProcessor manufacturer: " + this.manufacturer);
        }
    }

    static class Ram 
    {
        int memory;

        String manufacturer;

        Ram(int n, String m) 
        {
            this.memory = n;  

            this.manufacturer = m;
        }

        void display()
         {
            System.out.println("\n Memory Size : " + this.memory); 

            System.out.println("\nMemory manufacturer : " + this.manufacturer);
        }
    }

    void display()
     {
        System.out.println("\n Price of Cpu : " + this.price);
    }

    public static void main(String[] args) 
    {
        cpu M1 = new cpu(40000);
        cpu.Processor Processor_new = M1.new Processor(8, "Samsung");
        cpu.Ram ram_new = new Ram(8000, "Apple");
        M1.display();
        Processor_new.display();
        ram_new.display();
    }
}