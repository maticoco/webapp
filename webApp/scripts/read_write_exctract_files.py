

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

# def visualize_to_dataframe(data, bytes_per_line=16):
#     addresses = []
#     hex_views = []
#     ascii_views = []

#     for i in range(0, len(data), bytes_per_line):
#         line = data[i:i+bytes_per_line]
#         hex_view = ' '.join(f'{byte:02x}' for byte in line)
#         ascii_view = ''.join(chr(byte) if 32 <= byte < 127 else '.' for byte in line)
        
#         addresses.append(f"{i:04x}")
#         hex_views.append(hex_view)
#         ascii_views.append(ascii_view)

#     df = pd.DataFrame({
#         'Address': addresses,
#         'Hex View': hex_views,
#         'ASCII View': ascii_views
#     })

#     return df

# Por ejemplo, para leer un entero de 4 bytes desde los datos binarios:
#data=App.get_running

# Usar la función y mostrar el DataFrame
#df = visualize_to_dataframe(data)
#print(df)

#visualize(data)
#bytes_at_5c0 = extract_bytes_from_address(data, '5c0')
#print(bytes_at_5c0)

#data = modify_byte(data, 10, 0xFF)  # Modifica el byte en la posición 10 con el valor 0xFF