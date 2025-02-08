bits = ""
version_sum = 0


def read_data(input_data):
    global bits
    bits = [int(char) if char.isdigit() else ord(char) - ord("A") + 10 for char in input_data]
    bits = [bin(bit)[2:].zfill(4) for bit in bits]
    bits = "".join(bits)


def run(input_data):
    read_data(input_data)
    version, type_id, index = packet_header(0)
    # print(" "*index  + bits[index:])
    if type_id == 4:
        index, result = type_4(index)
        print(int(result, base=2))
    else:
        len_type_id = int(bits[index])
        index += 1
        if len_type_id == 0:
            sub_packets_len = int(bits[index:index + 15], base=2)
            index += 15
            parse_sub_packets_by_len(index, index + sub_packets_len)
        elif len_type_id == 1:
            sub_packets_count = int(bits[index:index + 11], base=2)
            index += 11
            parse_sub_packets_by_count(index, sub_packets_count)
    return version_sum


def parse_sub_packets_by_len(index, sub_packet_end):
    print("parse_sub_packets_by_len")
    while index < sub_packet_end:
        version, type_id, index = packet_header(index)
        index, result = type_4(index, bits)
        print(int(result, base=2))


def parse_sub_packets_by_count(index, sub_packet_count):
    print(f"parse_sub_packets_by_count: {index=}, {sub_packet_count=}, {bits=}")
    for i in range(sub_packet_count):
        version, type_id, index = packet_header(index)
        index, result = type_4(index)
        print(int(result, base=2))


def packet_header(index):
    global version_sum
    version = int(bits[index:index + 3], base=2)
    type_id = int(bits[index + 3:index + 6], base=2)
    version_sum += version
    print(" " * index + "VVVTTT" + bits[index + 6:])
    print(" " * index + f" {version}  {type_id} " + bits[index + 6:])
    return version, type_id, index + 6


def type_4(index):
    result = ""
    while True:
        result += bits[index + 1:index + 5]
        if bits[index] == "0":
            return index + 5, result
        index += 5


if __name__ == "__main__":
    print(run("8A004A801A8002F478"))
    # print(run(open("src/2021/data/days/16/data", "r").read()))
