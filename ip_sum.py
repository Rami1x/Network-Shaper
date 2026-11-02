

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

def get_summarized_subnet(ip_one:list, ip_two:list) -> int:
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

print(ip_to_bits("192.168.10.1"))

get_summarized_subnet(ip_to_bits("192.168.10.1"), ip_to_bits("192.168.10.100"))