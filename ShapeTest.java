public class ShapeTest{
	public static void main(String[] args){
		int a=Integer.parseInt(args[0]);
		Shape myShape= new Shape();
		//System.out.println(myShape.length);
		//System.out.println(myShape.calcArea());
		//System.out.println(myShape.calcPerimeter());
		myShape.setLength(a);
		System.out.println(myShape.getLength());
		 
	}

}