

def read_file(path):
    # Leyendo un archivo binario
    with open(path, 'rb') as file:
        data = file.read()
        return data
    
def write_file(data):
    # Escribiendo a un archivo binario
    namefile = "./"+str(input("ingrese el nombre del archivo a guardar: "))
    with open(namefile, 'wb') as file:
        file.write(data)

def modify_byte(data, position, new_value):
    return data[:position] + bytes([new_value]) + data[position+1:]

def extract_bytes_from_address(data, address, bytes_per_line=16):
    start = int(address, 16)  # Convertir la dirección hexadecimal a un entero
    return data[start:start+bytes_per_line]

def visualize(data, bytes_per_line=16):
    for i in range(0, len(data), bytes_per_line):
        line = data[i:i+bytes_per_line]
        hex_view = ' '.join(f'{byte:02x}' for byte in line)
        ascii_view = ''.join(chr(byte) if 32 <= byte < 127 else '.' for byte in line)

        print(f"{i:04x}: {hex_view.ljust(bytes_per_line*3)} {ascii_view}")        

