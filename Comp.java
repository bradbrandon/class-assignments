public class  Comp{

	public static void  main(String[]   args){
		int a= Integer.parseInt(args[0]);
		int b= Integer.parseInt(args[1]);
		int c= Integer.parseInt(args[2]);
		
		if(a>b){
			System.out.println(" the larger number is  "+ a);

		}
		else if(b>c){
			System.out.println(" the larger number is  "+ b);

		}
		else{
			System.out.println(" the largest number is  " + c);

		}


	}
}