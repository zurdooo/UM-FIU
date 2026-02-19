def main():
    try:
        # Create array of size 10
        arr = [0] * 10
        # Access out of bounds element
        out_of_bounds = arr[10]
    except Exception as e:
        # This is how we grab the excepts "name"
        print(f"An error occurred, Error Type : {e.__class__.__name__} - {e}")


if __name__ == "__main__":
    main()
