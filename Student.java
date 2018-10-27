import java.util.regex.Matcher; 
import java.util.regex.Pattern; 
public class Student{
	private String name;
	private String regno_;
	private String dob;
	private String dep;
	private String program;
  private Pattern  pattern;
  private Matcher  matcher;

	/*public  Student(String name,String regno_,String dob, String dep, String program){
		this.name=name;
		this.regno_=regno_;
		this.dob=regno_;
		this.dob=dob;
		this.dep= dep;
		this.program=program;
	}*/

  public void setRegno(String temp )throws RegException{
  String reg="^[H]+[0-9]{6}+[A-Z]{1}$";
  pattern= Pattern.compile(reg);
   matcher=pattern.matcher(temp);
  if (!(matcher.matches())){
  //  System.out.println("invalid regno" );
    throw new  RegException(reg);
    
      }
      else{
        this.regno_=temp;
      }



}

  public String getRegno_(){
    return regno_;

  }

  public void setName(String temp){
  	name=temp;

  }


public  String getName(){
  	return name;

  }

  public void setDob(String temp){

      String dpattern="^[0-9]{2}+[/]+[0-9]{2}+[/]+[0-9]{2}$";
  pattern= Pattern.compile(dpattern);
   matcher=pattern.matcher(temp);
  if (!(matcher.matches())){
    System.out.println("invalid date of birth" );
    
      }
      else{
        this.dob=temp;
      }


  }

  public String getDob(){
      	return dob;}

  
  public  void setProgram(String temp){
        program=temp;
  }
  public String getProgram(){
  	return program;

  }  
  public void setDep(String temp){
    dep=name;
  }

public String getDep(){
  	return dep;
  }}