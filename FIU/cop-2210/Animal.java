public class Animal {
    private String type;
    private String color;
    private int age;
    
    public Animal() { // Default constructor
       type = "Undefined";
       color = "Unspecified";
       age = 0;
    }
    
    public Animal(String animalType) {
       type = animalType;
       color = "Unspecified";
       age = 0;
    }
    
    public Animal(String animalType, String animalColor, int animalAge) {
       type = animalType;
       color = animalColor;
       age = animalAge;
    }
    
    public void print() {
       System.out.println("Animal: " + type + ", " + color + ", " + age);
    }
 }