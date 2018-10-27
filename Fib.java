public class Fib{
	public  static void main(String[] args){
		int a =1 ;
		int b=Integer.parseInt(args[0]);
		 int c=0; 
		  int d=1;
		  System.out.println("Fibonancii series up to " +b + " is :");

		while (a<=b){
			System.out.print(c + "+");
			int temp=c+d;
			c=d;
			d=temp;
			a+=1;
		}
	}
}