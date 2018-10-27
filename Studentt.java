import java.util.regex.Matcher; 
import java.util.regex.Pattern; 
public class Student(){
	private String name;
	private String regno_;
	private String dob;
	private String dep;
	private String program;
  private Pattern  pattern;
  private Matcher  matcher;

	public  Student(String name,String regno_,String dob, String dep, String program){
		this.name=name;
		this.regno_=regno_;
		this.dob=regno_;
		this.dob=dob
		this.dep= dep;
		this.program=program;
	}

  public String setRegno_(String temp){
  String reg="^[H]+[170]+[0-9]{6}+[A-Z]{1}$";
  pattern= Pattern.compile(reg);
  if !(matcher.matches(temp)){
    System.out.println("invalid regno" );
      }
      else{
        this.regno_=temp;
      }



}

  public void getRegno_(){
    return regno_;

  }

  public String setName(String temp){
  	name=temp;

  }


public void getName(){
  	return name;

  }

  public String setDob(String temp){
    dob=temp;

  }

  public String getDob(){}
  	return dob;

  }
  public  String setProgram(String temp){
        program=temp;
  }
  public void getProgram(){
  	return program;

  }  
  public String setDep(String temp){
    dep=name;
  }

}public void getDep(){
  	return dep;
  }