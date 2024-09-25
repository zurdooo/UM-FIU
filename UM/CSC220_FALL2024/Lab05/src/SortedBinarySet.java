// package lab05;

/**
 * Represents a sorted set of doubles backed by a simple array.
 * The set remains sorted at all times and does not allow duplicates.
 */
public class SortedBinarySet {

    /**
     * The array that holds the list of values
     */
    public double[] theData;
    /**
     * The capacity of the storage array
     */
    private int capacity;
    /**
     * The current number of elements in the list
     */
    private int size;

    /**
     * Constant for the initial storage array capacity
     */
    private static final int INITIAL_STORAGE_CAPACITY = 11;

    /**
     * A flag to toggle between binary search and sequential search.
     */
    public boolean usesBinarySearch = true; // Keep as false for the Lab. You will need this in the assignment.

    /**
     * Default constructor that initializes the set with the default capacity.
     */
    public SortedBinarySet() {
        theData = new double[INITIAL_STORAGE_CAPACITY];
        capacity = INITIAL_STORAGE_CAPACITY;
        size = 0;

    }

    /**
     * Constructor that initializes the set with an input array. This is for the
     * assignment, not for the lab.
     *
     * @param input The array to initialize the set with.
     */
    public SortedBinarySet(double[] input) {
        // Initialize the set with the default capacity
        theData = new double[INITIAL_STORAGE_CAPACITY];
        capacity = INITIAL_STORAGE_CAPACITY;
        size = 0;

        // Loop through the input array
        for (int i = 0; i < input.length - 1; i++) {
            // Check if element is already in the set
            if (contains(input[i])) {
                continue;
            }
            // Call the insert method to add the elements
            insert(input[i]);
        }
    }

    /**
     * Checks if the set is empty.
     *
     * @return true if the set is empty, false otherwise.
     */
    public boolean empty() {
        if (size == 0) {
            return true;
        }
        return false;

    }

    /**
     * Returns the number of elements in the set.
     *
     * @return The number of elements in the set.
     */
    public int size() {
        // Getter for the size
        return size;
    }

    /**
     * Grows the storage array by doubling its capacity.
     */
    public void grow() {
        // Create a new array with double the capacity
        int new_capacity = capacity * 2;
        double[] new_theData = new double[new_capacity];
        // copy the elements
        for (int i = 0; i < size; i++) {
            new_theData[i] = theData[i];
        }
        // Update theData to point to the new array
        theData = new_theData;
        // Update capacity
        capacity = new_capacity;

    }

    /**
     * Converts the set to a string that includes its elements, capacity, and
     * size. This is primarily used for testing purposes.
     *
     * @return A string representing the set.
     */
    public String toString() {
        String string_to_print = "";
        for (int i = 0; i < size; i++) {
            string_to_print += theData[i];
            string_to_print += " ";
        }
        string_to_print += "\nCapacity: " + capacity;
        string_to_print += "\nSize: " + size;
        return string_to_print;
    }

    /**
     * Clears all elements from the set. After this method is called, the set
     * should be empty.
     */
    public void clear() {
        // Set the size to 0
        size = 0;

        // Reset theData
        theData = new double[capacity];
    }

    /**
     * Inserts a new value into the set in the correct position. The value is
     * inserted only if it's not already in the set.
     *
     * @param newVal The value to insert.
     * @return true if the value was successfully inserted, false if it already
     * exists.
     */
    public boolean insert(double newVal) {
        // Check if the array is full
        if (size == capacity) {
            grow();
        }

        // Find the index to insert the new value
        int index = findIndex(newVal);

        // If the value is already in the set
        if (index >= 0) {
            return false;
        }

        // Edge Cases, first and last
        if (size == 0) {
            theData[0] = newVal;
            size += 1;
            return true;
        } else if (index == -size - 1) {
            theData[size] = newVal;
            size += 1;
            return true;
        }
        // Shift the elements to the right
        for (int i = size - 1; i >= -index - 1; i--) {
            theData[i + 1] = theData[i];
        }

        // Insert the new value
        theData[-index - 1] = newVal;
        size += 1;

        return true;
    }

    /**
     * Sequentially searches for a target in the set.
     *
     * @param target The target value to search for.
     * @return The index where the target is found, or -index - 1 if not found.
     */
    private int sequentialFind(double target) {
        for (int i = 0; i < size; i++) {
            // Target found
            if (theData[i] == target) {
                return i;
                // Target is greater than the current element
            } else if (theData[i] > target) {
                return -i - 1;
            }
        }
        // Not found so return index where it should be inserted
        return -size - 1;
    }

    // *********************************************************************
    // * you will implement the rest of the methods for your assignment *
    // * don't touch them before finishing the lab portion *
    // *********************************************************************
    /**
     * Removes a specified element from the set.
     *
     * @param element The element to remove.
     * @return true if the element was removed, false if it did not exist.
     */
    public boolean remove(double element) {
        // Element not found
        if (findIndex(element) < 0) {
            return false;
        }
        // Remove the element
        for (int i = findIndex(element); i < size - 1; i++) {
            theData[i] = theData[i + 1];
        }
        // Update the size
        size -= 1;
        return true;
    }

    /**
     * Uses binary search to find the target in the set (only if enabled).
     *
     * @param target The target value to search for.
     * @return The index where the target is found, or -index - 1 if not found.
     */
    private int binaryFind(double target) {
        int low = 0;
        int high = size - 1;

        while (low <= high) {
            int mid = (low + high) / 2;
            // Target found
            if (theData[mid] == target) {
                return mid;
                // Target is larger
            } else if (theData[mid] < target) {
                low = mid + 1;
                // Target is smaller
            } else {
                high = mid - 1;
            }
        }
        // Not found so return index where it should be inserted
        return sequentialFind(target);
    }

    /**
     * Checks if the set contains a specific element.
     *
     * @param element The element to check.
     * @return true if the element is found, false otherwise.
     */
    public boolean contains(double element) {
        // Look for the element
        if (findIndex(element) >= 0) {
            return true;
        }
        return false;
    }

    /**
     * Checks if the set contains all the elements of an input array.
     *
     * @param elements The array of elements to check.
     * @return true if all elements are found in the set, false otherwise.
     */
    public boolean containsAll(double[] elements) {
        // Check if all elements are in the set
        for (int i = 0; i < elements.length; i++) {
            // If one element isn't found return false
            if (!contains(elements[i])) {
                return false;
            }
        }
        // All elements are found
        return true;
    }

    /**
     * Finds the index of a target value using either sequential or binary
     * search.
     *
     * @param target The target value to search for.
     * @return The index where the target is found, or -index - 1 if not found.
     */
    public int findIndex(double target) {
        if (usesBinarySearch) {
            return binaryFind(target);
        } else {
            return sequentialFind(target);
        }
    }

}
