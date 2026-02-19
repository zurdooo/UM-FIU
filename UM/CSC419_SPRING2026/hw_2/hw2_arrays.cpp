#include <vector>
#include <chrono>
#include <print>

const int ARRAY_SIZE = 1000;
const int LOOP_ITERATIONS = 1000000;

/// @brief Creates a static array of integers, static has a lifetime of the entire program, is only initialized once
void createStaticArray()
{
    static int arr[ARRAY_SIZE];
}

/// @brief Creates a stack array of integers, stack arrays have a lifetime of the function call, initialized each time the function is called on stack
void createStackArray()
{
    int arr[ARRAY_SIZE];
}

/// @brief Creates a heap array of integers using std::vector which does the heap allocation for us, vectors have a lifetime of the function call
void createHeapVector()
{
    std::vector<int> arr(ARRAY_SIZE);
}

int main()
{

    // Static array
    auto start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < LOOP_ITERATIONS; ++i)
    {
        createStaticArray();
    }
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;
    std::println("Static array duration: {} seconds", duration.count());

    // Stack array
    start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < LOOP_ITERATIONS; ++i)
    {
        createStackArray();
    }
    end = std::chrono::high_resolution_clock::now();
    duration = end - start;
    std::println("Stack array duration: {} seconds", duration.count());

    // Heap array (vector)
    start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < LOOP_ITERATIONS; ++i)
    {
        createHeapVector();
    }
    end = std::chrono::high_resolution_clock::now();
    duration = end - start;
    std::println("Heap array duration: {} seconds", duration.count());

    return 0;
}