class Student {
    private String firstName;
    private String lastName;
    private String pantherId;
    private double gpa;

    public Student(String firstName, String lastName, String pantherId, double gpa) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.pantherId = pantherId;
        this.gpa = gpa;
    }

    // Getters
    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public String getPantherId() {
        return pantherId;
    }

    public double getGpa() {
        return gpa;
    }

    // Setters
    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public void setPantherId(String pantherId) {
        this.pantherId = pantherId;
    }

    public void setGpa(double gpa) {
        this.gpa = gpa;
    }

    // Override toString method so that we can print the object
    @Override
    public String toString() {
        return "Student{" +
                "firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", pantherId='" + pantherId + '\'' +
                ", gpa=" + gpa +
                '}';
    }
}