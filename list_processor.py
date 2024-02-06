def process_list(input_list):
    if len(input_list) % 10 != 0:
        raise ValueError("Input list length must be a multiple of 10")

    output_list = [x for i, x in enumerate(input_list) if (i + 1) % 2 != 0 and (i + 1) % 3 != 0]
    return output_list

if __name__ == "__main__":
    # Example usage
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    try:
        processed_list = process_list(input_list)
        print("Processed List:", processed_list)
    except ValueError as e:
        print("Error:", e)
