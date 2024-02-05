import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("string_arg", type=str)
    parser.add_argument("int_arg", type=int)
    parser.add_argument("float_arg", type=float)
    args = parser.parse_args()
    
    print("String argument:", args.string_arg)
    print("Integer argument:", args.int_arg)
    print("Float argument:", args.float_arg)

