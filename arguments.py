import argparse

def demo() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("string_arg", help = "Enter a string", type = str)
    parser.add_argument("int_arg", help = "Enter a integer", type = int)
    parser.add_argument("float_arg", help = "Enter a float". type = float)

    args = parser.parse_args()

    print("String argument: ", args.string_arg)
    print("Integer argument: ", args.int_arg)
    print("Float argument: ", args.float_arg)

    