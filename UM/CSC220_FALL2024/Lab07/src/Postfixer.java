// package lab07;

import java.util.*;

public class Postfixer {

    /**
     * Converts an operator to its precedence priority
     *
     * We expect you to be able to handle +, -, *, /, ^, and ( (why don't you
     * need ")" as well? see algorithm in part 4)
     *
     * The order of these is as follows: ^, * and /, + and -, (
     *
     * @param op a string representing an operator, e.g. "+" or "-"
     * @return an integer value reflecting its precedence
     */
    private static int opToPrcd(String op) {
        //DONE: Lab Part 2.1
        int pre = switch (op) {
            case "^" ->
                4;
            case "*", "/" ->
                3;
            case "+", "-" ->
                2;
            case "(" ->
                1;
            // Invalid
            default ->
                0;
        };
        return pre;
    }

    /**
     * Determines if the first operator has same or greater precedence than the
     * second
     *
     * @param op1 the first operator
     * @param op2 the second operator
     * @return the boolean result
     */
    private static boolean hasPrecedence(String op1, String op2) {
        //DONE: Lab Part 2.2
        // Get precedence for both then compare
        return opToPrcd(op1) >= opToPrcd(op2);
    }

    /**
     * determines if the input token is an operator
     *
     * @param token the string token to check
     * @return a boolean reflecting the result
     */
    private static boolean isOperator(String token) {
        //DONE: Lab Part 2.3
        return switch (token) {
            case "+", "-", "*", "/", "^" ->
                true;
            // All other cases
            default ->
                false;
        };

    }

    /**
     * Evaluates an expression
     *
     * NOTE Beware the order of pop and evaluation when receiving operand1 and
     * operand2 as input.
     *
     * @param operand1 the first operand
     * @param operator the operator to apply
     * @param operand2 the second operand
     * @return a double expressing the result
     * @throws IllegalArgumentException if operator passed is not one of "+",
     * "-", "*", "/", or "^"
     *
     */
    private static double evaluate(double operand1, String operator, double operand2) {
        //Done: Lab Part 2.4
        // Check if operator is valid
        if (!isOperator(operator)) {
            throw new IllegalArgumentException("Invalid operator");
        }
        // Perform operation
        return switch (operator) {
            case "+" ->
                operand1 + operand2;
            case "-" ->
                operand1 - operand2;
            case "*" ->
                operand1 * operand2;
            case "/" ->
                operand1 / operand2;
            case "^" ->
                Math.pow(operand1, operand2);
            // Never accessed
            default ->
                0.0;
        };
    }

    /**
     * give a description of the purpose of this method
     *
     *
     * @param line fill in
     * @return fill in
     */
    public static double infixEvaluator(String line) {
        //DONE: Lab Part 3
        //HINT: You must use the algorithm described in Lab Part 4
        StringSplitter data = new StringSplitter(line);
        Stack<String> operators = new Stack<String>();
        Stack<Double> operands = new Stack<Double>();

        while (data.hasNext()) {
            String token = data.next();
            // Check if token is an operator
            if (isOperator(token)) {
                while (!operators.empty() && hasPrecedence(operators.peek(), token)) {
                    // Get operator
                    String operator = operators.pop();
                    // Get operands
                    double operand2 = operands.pop();
                    double operand1 = operands.pop();
                    // Push the evaluated result
                    operands.push(evaluate(operand1, operator, operand2));
                }
                // Push the operator
                operators.push(token);
                // Right parenthesis
            } else if (token.equals(")")) {
                // Thing on top isn't left parenthesis
                while (!operators.peek().equals("(")) {
                    // Get operator
                    String operator = operators.pop();
                    // Get operands
                    double operand2 = operands.pop();
                    double operand1 = operands.pop();
                    // Push the evaluated result
                    operands.push(evaluate(operand1, operator, operand2));
                }
                // Discard left parenthesis
                operators.pop();
                // Left parenthesis
            } else if (token.equals("(")) {
                // Push the left parenthesis
                operators.push(token);
                // Number
            } else {
                operands.push(Double.parseDouble(token));
            }
        }
        while (!operators.empty()) {
            // Get operator
            String operator = operators.pop();
            // Get operands
            double operand2 = operands.pop();
            double operand1 = operands.pop();
            // Push the evaluated result
            operands.push(evaluate(operand1, operator, operand2));
        }
        // return last value in operands
        return operands.pop();
    }

    /**
     * give a description of the purpose of this method
     *
     * @param line fill in
     * @return fill in
     */
    public static String toPostfix(String line) {
        //DONE: Lab Part 4
        // Declare operator stack and postfix 
        Stack<String> operators = new Stack<String>();
        String postfix = "";
        // Iterate over line
        for (int i = 0; i < line.length(); i++) {
            // Get character
            char c = line.charAt(i);
            // Check if character is operand
            if (Character.isDigit(c)) {
                // Add to postfix
                postfix += c;
                // Character is an operator
            } else if (isOperator(String.valueOf(c))) {
                String currentOperator = String.valueOf(c);
                while (!operators.peek().equals("(") && hasPrecedence(operators.peek(), currentOperator)) {
                    postfix += operators.pop();
                }
                // Push operator to stack
                operators.push(currentOperator);
                // Left Parenthesis
            } else if (c == '(') {
                // Push to stack
                operators.push(String.valueOf(c));
            } else if (c == ')') {
                // Pop until left parenthesis
                while (!operators.peek().equals("(")) {
                    postfix += operators.pop();
                }
                // Discard left parenthesis
                operators.pop();
            }
        }
        return postfix;
    }

    public static void main(String[] args) {

        //Add Tests for Lab part 2
        //opToPrcd(String op) Tests
        //hasPrecedence(String op1, String op2) Tests
        //isOperator(String token) Tests
        //evaluate(double operand1, String operator, double operand2) Tests
        //Uncomment when you are ready to test Lab Part 3
        if (infixEvaluator("10 + 2") != 12) {
            System.err.println("test1 failed --> your answer should have been 12");
        }
        if (infixEvaluator("10 - 2 * 2 + 1") != 7) {
            System.err.println("test1 failed --> your answer should have been 7");
        }
        if (infixEvaluator("100 * 2 + 12") != 212) {
            System.err.println("test2 failed --> your answer should have been 212");
        }
        if (infixEvaluator("100 * ( 2 + 12 )") != 1400) {
            System.err.println("test3 failed --> your answer should have been 1400");
        }
        if (infixEvaluator("100 * ( 2 + 12 ) / 14") != 100) {
            System.err.println("test4 failed --> your answer should have been 100");
        }
        System.out.println("Lab Testing Done!!!");

        /* uncomment the below lines for assignment */
        if (!toPostfix(new String("(4+5)")).equals("45+")) {
            System.err.println("test1 failed --> should have been 45+");
        }
        if (!toPostfix(new String("((4+5)*6)")).equals("45+6*")) {
            System.err.println("test2 failed --> should have been 45+6*");
        }
        if (!toPostfix(new String("((4+((5*6)/7))-8)")).equals("456*7/+8-")) {
            System.err.println("test3 failed --> should have been 456*7/+8-");
        }
        if (!toPostfix(new String("((4+5*(6-7))/8)")).equals("4567-*+8/")) {
            System.err.println("test4 failed --> should have been 4567-*+8/");
        }
        if (!toPostfix(new String("(9+(8*7-(6/5^4)*3)*2)")).equals("987*654^/3*-2*+")) {
            System.err.println("test5 failed --> should have been 987*654^/3*-2*+");
        }
        System.out.println("Assignment Testing Done!!!");
    }

}
