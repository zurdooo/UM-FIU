package lab01;

public class CoinFlipExperiment {
    static public int coinFlipExperiment() {
        int winnings = 0;
        for (int i = 0; i <= 99; i++) {
            double flip = Math.random();
            if (flip < 0.505) {
                System.out.println("Heads");
                winnings++;
            } else {
                System.out.println("Tails");
                winnings--;
            }
        }
        return winnings;
    }

    public static void main(String[] args) {
        // System.out.println("Hello, World!");
        int amount = coinFlipExperiment();
        System.err.println("Win/loss amount: " + amount);

        // Declare an int variable to keep track of winnings.
        // Set winnings to 0.
        // Loop 100 times.
        // Flip the coin – reuse the code you wrote in the lab
        // If heads, add $1 to winnings.
        // If tails, subtract $1 from winnings.
        // Print out winnings.

        // int winnings = 0;

    }
}
