public class StudTest{
	public static void main(String[] args){
		Student stud= new Student();
		stud.setRegno(args[0]);
		stud.setName(args[1]);
		stud.setDob(args[2]);
		System.out.println(" the regristration no_ is " +stud.getRegno_());
		System.out.println(" the name of the student is " +stud.getName());
		System.out.println(" the date of brith of the student is " +stud.getDob());

	}
}