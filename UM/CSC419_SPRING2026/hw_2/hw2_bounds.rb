# Create array of 10 integers (initialized to nil)
arr = Array.new(10, 0)

begin
  # Accessing an element out of range
  new_elem = arr[10]
  puts "Array element at index 10: #{new_elem}"
rescue IndexError => e
  puts "An error occurred: #{e.class}: #{e.message}"
end