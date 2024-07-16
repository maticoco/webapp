
#For new airbags module compare & creat a diff_list.txt to analize

import os

def compare_bin_files(file1_path, file2_path, save_diff=False, diff_file_path='diff_list.txt'):
    with open(file1_path, 'rb') as file1, open(file2_path, 'rb') as file2:
        data1 = file1.read()
        data2 = file2.read()

    if len(data1) != len(data2):
        raise ValueError(f"Los archivos {file1_path} y {file2_path} tienen diferentes tamaños y no se pueden comparar.")

    diff_list = []
    length = len(data1)
    i = 0

    while i < length:
        if data1[i] != data2[i]:
            start_address = i
            content = []
            while i < length and data1[i] != data2[i]:
                content.append(data2[i])
                i += 1
            diff_list.append({
                'address': hex(start_address),
                'length': hex(len(content)),
                'content': ' '.join(format(byte, '02X') for byte in content)
            })
        else:
            i += 1

    if save_diff:
        with open(diff_file_path, 'w') as diff_file:
            for diff in diff_list:
                diff_file.write(f"{diff['address']} {diff['length']} {diff['content']}\n")

    return diff_list

def parse_diff_file(diff_file_path):
    diff_list = []
    with open(diff_file_path, 'r') as diff_file:
        for line in diff_file:
            parts = line.strip().split()
            address = parts[0]
            length = parts[1]
            content = ' '.join(parts[2:])
            diff_list.append({
                'address': address,
                'length': length,
                'content': content
            })
    return diff_list

def apply_diff_to_bin(file_path, diff_file_path, output_file_path=None):
    with open(file_path, 'rb') as file:
        data = bytearray(file.read())
    
    diff_list = parse_diff_file(diff_file_path)

    for diff in diff_list:
        address = int(diff['address'], 16)
        length = int(diff['length'], 16)
        content = bytes(int(byte, 16) for byte in diff['content'].split())

        for i in range(length):
            if address + i < len(data):
                data[address + i] = content[i]
            else:
                data.extend([0] * (address + i + 1 - len(data)))
                data[address + i] = content[i]

    if output_file_path:
        with open(output_file_path, 'wb') as output_file:
            output_file.write(data)
    #else:
        # with open(file_path, 'wb') as file:
        #     file.write(data)
