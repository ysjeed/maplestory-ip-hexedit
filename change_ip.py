import argparse

def convert_ip_to_ascii_bytes(ip_address):
    if len(ip_address) > 15:
        raise ValueError("IP address must be at most 15 characters (including dots)")
    
    ascii_bytes = ip_address.encode('ascii')
    padding_length = 15 - len(ascii_bytes)
    padded_bytes = ascii_bytes + b'\x00' * padding_length
    
    return padded_bytes

def replace_ip_in_binary(file_path, ip_address, output_path=None):
    replacement_ip = convert_ip_to_ascii_bytes(ip_address)
    
    with open(file_path, 'rb') as f:
        binary_data = f.read()

    target_pattern = b'\x31\x32\x37\x2E\x30\x2E\x30\x2E\x31' + b'\x00' * 6  # "127.0.0.1" with padding
    occurrences = binary_data.count(target_pattern)

    if occurrences != 3:
        raise ValueError(f"Expected exactly 3 instances of '127.0.0.1', but found {occurrences}.")
    
    modified_data = binary_data.replace(target_pattern, replacement_ip)
    output_file = output_path if output_path else file_path

    with open(output_file, 'wb') as f:
        f.write(modified_data)

    print(f"Replaced IP address and saved the modified EXE as {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Replace an IP address in an EXE file.")
    parser.add_argument('exe_file_path', metavar='exe_file', type=str, 
                        help="Path to the EXE file to modify.")
    parser.add_argument('new_ip_address', metavar='ip', type=str, 
                        help="New IP address to replace the old one (in standard IP format).")
    parser.add_argument('--output', metavar='output_file', type=str, 
                        help="Optional: Path to save the modified EXE (if not provided, the original EXE will be overwritten).")
    
    args = parser.parse_args()

    try:
        replace_ip_in_binary(args.exe_file_path, args.new_ip_address, args.output)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
