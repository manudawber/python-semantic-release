def print_hi(first_name: str, last_name: str = None) -> None:
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {first_name}{f" {last_name}" if last_name else None}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Manu', 'Dawber')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
