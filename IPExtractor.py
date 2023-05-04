import re

# Open the input file (Replace with location of text file)
with open('C:/users/', 'r') as file:
    # Read the file content
    content = file.read()

    # Compile the regular expression pattern for IP addresses
    pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

    # Find all IP addresses in the file
    ip_addresses = re.findall(pattern, content)

    # Sort the IP addresses in ascending order
    ip_addresses.sort()
    # Print the sorted IP addresses
    for ip_address in ip_addresses:
        print(ip_address)
