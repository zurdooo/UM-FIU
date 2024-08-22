import java.util.Arrays;

public class testing {

    // -- main
    public static void main(String[] args) {
        // Initialize arrays
        int[] test_1 = new int[5];
        System.out.println("test_1: " + Arrays.toString(test_1));

        int[] test_2 = test_1.clone();
        test_2[1] = 5;
        System.out.println("test_2: " + Arrays.toString(test_2));
        System.out.println("test_1: " + Arrays.toString(test_1));
    }
}