public class Shape{
	private int no_OfSides;
	private int no_OfAngles;
	private String name;
 	private int length;
 	 private int width;

 	/*public Shape (int length){
 		this.length=length;
 	}
	public Shape(int length, int width){
		this.length=length;
		this.width= width;
	} */
	public int getLength(){
		return length;
	}
	public void setLength(int x){
		if (x>0){
			length=x;
		}
		else {
			System.out.println("Invalid length value");
		}
	}
	public void setWidth(int x){
		if (x>0){
			width=x;
		}
	}

	public double calcArea(int lengths ){
		double area= lengths* lengths;
		return area;

	}
	public double calcPerimeter(int lengths){
		double perimeter= lengths*4;
		return perimeter;


	}
	public double calcPerimeter(){
		double perimeter= (length+width) *2;
		return perimeter;


	}
	public double calcArea(){
		return length*length;
	}

	

	}
