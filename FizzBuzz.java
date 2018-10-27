public class FizzBuzz{
	public  void fizbuz(int limit){
		for( int i=1; i<=limit;i+=1){
		if(i%3==0){
		System.out.println("Fuzz");

	}
	else if(i%5==0){
		System.out.println("Buzz");
	} 
	else if(i%3==0 && i%5==0){
		System.out.println("FizzBuzz");
	}
	else{
		System.out.println(i);
	}
} 


		}

	}