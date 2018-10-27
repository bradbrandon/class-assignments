public class RegException extends Exception {
	private  String Regno;

public  RegException( String Regno){
	this.Regno=Regno;


}
public void expceptionMessage(){
	 System.out.println("invalid regno :"+  Regno );

}
}