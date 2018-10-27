
public class QuadComp{

 	public static void Quadmethod(int a, int b , int c){
 		 
        double d;
        double e;
        d=(a+Math.sqrt((b*b)-(4*a*c)))/(2*a);
        e=(a-Math.sqrt((b*b)-(4*a*c)))/(2*a);

 		System.out.println("the solutions are : " + d + " and " + e); 

 		



 	}
	public static void main(String[] args){
		int a= Integer.parseInt(args[0]);
		int b= Integer.parseInt(args[1]);
		int c= Integer.parseInt(args[2]);

		
		Quadmethod(a ,b,c );
	}
}