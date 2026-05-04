from file_utils import add_numbers, count_words, format_greeting


def main():
    name = input("Enter your name: ")
    print(format_greeting(name))

    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    total = add_numbers(first_number, second_number)
    print(f"The sum is: {total}")

    input_path = "input.txt"
    output_path = "output.txt"

    try:
        with open(input_path, "r", encoding="utf-8") as input_file:
            text = input_file.read()
    except FileNotFoundError:
        print(f"File not found: {input_path}")
        return

    word_count = count_words(text)

    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(f"Word count: {word_count}\n")

    print(f"Processed '{input_path}' and wrote '{output_path}'.")


if __name__ == "__main__":
    main()
