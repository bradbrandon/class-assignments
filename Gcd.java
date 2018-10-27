public class Gcd{
	public void gcd(int nums[]){
		int a= nums[1];
		int b=nums[2];
		int c=nums[3];


		 for (int i=1; i<c;i+=1){
		 	if(a%i==0 && b%i==0 && c%i==0){
		 		System.out.println(i);
		 	}
		 }



	}
}