import java.util.Scanner;

/*
 This class calculates and displays the calories consumed and burned for each day of the week,
 as well as the total and average calories consumed and burned, and the net weekly pounds gained or lost.
*/
public class Calories_Consumed_Burned {
    // Global variables to store daily calorie consumption and burn
    static int day1CalConsumed, day1CalBurned;
    static int day2CalConsumed, day2CalBurned;
    static int day3CalConsumed, day3CalBurned;
    static int day4CalConsumed, day4CalBurned;
    static int day5CalConsumed, day5CalBurned;
    static int day6CalConsumed, day6CalBurned;
    static int day7CalConsumed, day7CalBurned;

    // Global variables to store total and average calories
    static int totalCaloriesConsumed, totalCaloriesBurned;
    
    // Double globals
    static double averageCaloriesConsumed, averageCaloriesBurned;
    static double netWeeklyPounds;

    // Method to get user input for 7 days
    public static void getUserInput() {
        Scanner scnr = new Scanner(System.in);

        // Get input for each day
        for (int i = 1; i <= 7; i++) {
            System.out.print("Enter calories consumed for day #" + i + ": ");
            int caloriesConsumed = scnr.nextInt();
            System.out.print("Enter calories burned for day #" + i + ": ");
            int caloriesBurned = scnr.nextInt();
            System.out.println();

            // Assign values to the correct day
            if (i == 1) {
                day1CalConsumed = caloriesConsumed;
                day1CalBurned = caloriesBurned;
            } else if (i == 2) {
                day2CalConsumed = caloriesConsumed;
                day2CalBurned = caloriesBurned;
            } else if (i == 3) {
                day3CalConsumed = caloriesConsumed;
                day3CalBurned = caloriesBurned;
            } else if (i == 4) {
                day4CalConsumed = caloriesConsumed;
                day4CalBurned = caloriesBurned;
            } else if (i == 5) {
                day5CalConsumed = caloriesConsumed;
                day5CalBurned = caloriesBurned;
            } else if (i == 6) {
                day6CalConsumed = caloriesConsumed;
                day6CalBurned = caloriesBurned;
            } else if (i == 7) {
                day7CalConsumed = caloriesConsumed;
                day7CalBurned = caloriesBurned;
            }
        }
    }

    // Method to calculate total and average calories
    public static void calculateCalories() {
        // Calculate total calories consumed and burned
        totalCaloriesConsumed = day1CalConsumed + day2CalConsumed + day3CalConsumed + day4CalConsumed + day5CalConsumed + day6CalConsumed + day7CalConsumed;
        totalCaloriesBurned = day1CalBurned + day2CalBurned + day3CalBurned + day4CalBurned + day5CalBurned + day6CalBurned + day7CalBurned;

        // Calculate average calories consumed and burned
        averageCaloriesConsumed = (double) totalCaloriesConsumed / 7;
        averageCaloriesBurned = (double) totalCaloriesBurned / 7;

        // Calculate net weekly pounds
        netWeeklyPounds = (double) (totalCaloriesConsumed - totalCaloriesBurned) / 3000.0;
    }

    // Method to display all information to the user
    public static void displayCalories() {

        System.out.println();
        System.out.printf("You consumed a total of %,d calories this week.\n", totalCaloriesConsumed);
        System.out.printf("You burned a total of %,d calories this week.\n", totalCaloriesBurned);
        System.out.println();

        System.out.printf("You consumed an average of %,.2f calories a day.\n", averageCaloriesConsumed);
        System.out.printf("You burned an average of %,.2f calories a day.\n", averageCaloriesBurned);
        System.out.println();

        System.out.printf("Your net weekly gain/loss was %.3f pounds.\n", netWeeklyPounds);
    }

    // Main method
    public static void main(String[] args) {
        getUserInput();

        calculateCalories();

        displayCalories();
    }
}