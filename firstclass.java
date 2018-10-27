
public class FirstClass {
	public static void main(String [] args){
		String myName= args[0];
		String temp= args[1];
		int age= Integer.parseInt(temp);

		age +=5;
		System.out.println(" My name is  "+ myName + " My age is " + age);

	}
}