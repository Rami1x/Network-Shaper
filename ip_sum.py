import pandas as pd


def is_valid_ip(ip:str) -> bool:
    """
        checks if ip is valid
    """

    segmented_ip = []
    segmented_ip = ip.split(".")

    if len(segmented_ip) != 4:
        print("4 segments needed in an IP address")
        return False


    try:
        for segment in segmented_ip:
            if int(segment) > 255:
                print("IP out of scope")
                return False
            
    except TypeError:
        print("Invalid IP")

    print(f"IP {ip}, is valid")
    return True


def ip_to_bits(ip:str) -> list:
    """
        This function returns an 8bit version of the IP and returns a list of 4 8bit segments
    """
    split_ip = ip.split(".")
    ip_bits = []
    segment_bits = ""
    
    n = 7
    digit = 2 ** n
    

    for seg in split_ip:

        current_difference = int(seg)
        
        while n >= 0:

            if current_difference >= digit:
                segment_bits = segment_bits + "1"
                current_difference = current_difference - digit
            else:
                segment_bits = segment_bits + "0"

            n -= 1
            digit = 2 ** n

        ip_bits.append(segment_bits)

        segment_bits = ""
        n = 7
        digit = 2 ** n
          

    return ip_bits


def get_summarized_subnet(ip_one:list, ip_two:list) -> str:
    """
        gets the subnet
    """
    
    ip_one_str = "".join(ip_one)
    ip_two_str = "".join(ip_two)
    count = 0

    while ip_one_str[count] == ip_two_str[count]:
        count += 1


    print(f"subnet: /{count}")
    return count

def usable_bits(subnet_mask:int) -> int:

    subnet_bit = ""
    count = 0

    while count < 32:
        if len(subnet_bit) < subnet_mask:
            subnet_bit += "1"
        else:
            subnet_bit += "0"

        count += 1

    return subnet_bit

def get_avaialble_addresses(subnet_mask:int) -> int:
    """ 
    minuses 0 and 255 away from the ip addresses
    """

    host_bits = 32 - subnet_mask
    total_addresses = 2 ** host_bits
    usable_addresses = total_addresses - 2

    return usable_addresses



def bits_to_ip(ip_bits:list) -> str:

    ip = []

    for segment in ip_bits:
        decimal = 0
        power = 7

        for bit in segment:
            if bit == "1":
                decimal += 2 ** power

            power -= 1

        ip.append(str(decimal))

    return ".".join(ip)


def get_valid_ip(ip:str, subnet_mask:int) -> list:

    ip_bits = "".join(ip_to_bits(ip))

    host_bits = 32 - subnet_mask
    total_addresses = 2 ** host_bits

    network_bits = ip_bits[:subnet_mask]

    valid_ips = []

    for i in range(1, total_addresses - 1):

        host_binary = ""

        for power in range(host_bits - 1, -1, -1):

            if i >= 2 ** power:
                host_binary += "1"
                i -= 2 ** power
            else:
                host_binary += "0"

        full_ip = network_bits + host_binary

        segmented_bits = []

        for j in range(0, 32, 8):
            segmented_bits.append(full_ip[j:j + 8])

        valid_ips.append(bits_to_ip(segmented_bits))

    return valid_ips



#def list_of_valid_ip(ip_one:str, ip_two:str) -> list:
    """
        returns list for pandas dataframe
    """




print(ip_to_bits("192.168.10.1"))


get_summarized_subnet(ip_to_bits("192.168.10.1"), ip_to_bits("192.168.10.100"))

addresses = get_valid_ip("192.168.10.1", 24)
print(addresses)
print("Total:", len(addresses))