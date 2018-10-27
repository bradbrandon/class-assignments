public class Animal{
	private int numberOflegs;
	private String animalName;
	private String familyName;

	public void  setNumflegs(int temp){
		this.numberOflegs=temp;
	}

public  void setAnimalname(String temp){
		this.animalName=temp;
	}

public void  setFamilyname(String temp){
		this.familyName=temp;
	}

public String getAnimalName(){
	return animalName;
}
public int getNumberofLegs(){
	return numberOflegs;
}
public String getFamilyname(){
	return familyName;
}
public void makeSound(){
	System.out.println("this animal makes animal sound");
}
public void reproduceBy(){
	System.out.println("this animal reproduces by ");
}

	}
