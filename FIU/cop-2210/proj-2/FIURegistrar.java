import javax.swing.JOptionPane;

public class FIURegistrar {
    // This is the main method,
    public static void main(String[] args) {
        Student[] students = createArrayOfStudents();
        processArrayOfStudents(students);
    }

    public static Student[] createArrayOfStudents() {
        // Ask the user how many students they want to create
        String numStudentsString = JOptionPane.showInputDialog("How many students do you wish to process,");
        // Convert the string to an integer
        int numStudents = Integer.parseInt(numStudentsString);
        // Create an array of students
        Student[] students = new Student[numStudents];
        // Loop through the array and ask the user for the student's details
        for (int i = 0; i < numStudents; i++) {
            // Ask the user for the student's details
            String firstName = JOptionPane.showInputDialog("Enter first name for student " + (i + 1) + ":");
            String lastName = JOptionPane.showInputDialog("Enter last name for student " + (i + 1) + ":");
            String pantherId = JOptionPane.showInputDialog("Enter Panther ID for student " + (i + 1) + ":");

            // Validate the GPA input
            String gpaString = JOptionPane.showInputDialog("Enter GPA for student " + (i + 1) + ":");
            double gpa = Double.parseDouble(gpaString);

            while (gpa < 0 || gpa > 4.0) {
                JOptionPane.showMessageDialog(null, "Invalid GPA. Please enter a value between 0 and 4.0.");
                gpaString = JOptionPane.showInputDialog("Enter GPA for student " + (i + 1) + ":");
                gpa = Double.parseDouble(gpaString);
            }

            // Create a new student object and add it to the array
            students[i] = new Student(firstName, lastName, pantherId, gpa);
        }
        return students;
    }

    public static void processArrayOfStudents(Student[] students) {
        double highestGpa = students[0].getGpa();
        double lowestGpa = students[0].getGpa();
        Student highestGpaStudent = students[0];
        Student lowestGpaStudent = students[0];

        double totalGpa = 0;

        for (Student student : students) {
            // Print the student, null for default "frame" for the dialog
            JOptionPane.showMessageDialog(null, student.toString());

            // Get the GPA of the student and accumulate it
            double gpa = student.getGpa();
            totalGpa += gpa;

            // Check if the GPA is higher than the highest GPA
            if (gpa > highestGpa) {
                highestGpa = gpa;
                highestGpaStudent = student;
            }
            // Check if the GPA is lower than the lowest GPA
            if (gpa < lowestGpa) {
                lowestGpa = gpa;
                lowestGpaStudent = student;
            }
        }

        double averageGpa = totalGpa / students.length;
        // Print the average GPA, Null means default "frame" for the dialog
        JOptionPane.showMessageDialog(null, "The average GPA is: " + averageGpa);
        // Print the student with the highest GPA
        JOptionPane.showMessageDialog(null, "The student with the highest GPA is: " + highestGpaStudent);
        // Print the student with the lowest GPA
        JOptionPane.showMessageDialog(null, "The student with the lowest GPA is: " + lowestGpaStudent);

        // Print the students with GPA above average
        JOptionPane.showMessageDialog(null, "Students with GPA above average:");
        for (Student student : students) {
            if (student.getGpa() > averageGpa) {
                JOptionPane.showMessageDialog(null, student.toString());
            }
        }
    }
}