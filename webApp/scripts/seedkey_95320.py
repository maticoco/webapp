from Crypto.Cipher import AES
from binascii import unhexlify, hexlify
import struct


def extract_bytes_from_address(data, address, bytes_per_line=16):
    start = int(address, 16)  # Convertir la dirección hexadecimal a un entero
    return data[start:start+bytes_per_line]


def find_fazit(data):
    fazit1 = extract_bytes_from_address(data, "b0")
    fazit2 = extract_bytes_from_address(data, "c0")
    fazit3 = extract_bytes_from_address(data, "5c0")
    print ('FAZIT: ',fazit3[0:9].decode('utf-8'),fazit1.decode('utf-8')+fazit2[0:6].decode('utf-8'),fazit2[8:16].decode('utf-8'))
    fazit='FAZIT: '+ fazit3[0:9].decode('utf-8')+fazit1.decode('utf-8')+fazit2[0:6].decode('utf-8')+fazit2[8:16].decode('utf-8')
    return fazit

def find_keys(data):
    keys1 = extract_bytes_from_address(data, "490").hex()
    keys2 = extract_bytes_from_address(data, "4A0").hex()
    keys3 = extract_bytes_from_address(data, "4A0").hex()
    
    keys=f'KEY 1: {keys1[8:16].upper()}\nKEY 2: {keys1[16:24].upper()}\nKEY 3: {keys1[24:32].upper()}\n'
    keys+=f'KEY 4: {keys2[0:8].upper()}\nKEY 5: {keys2[8:16].upper()}\nKEY 6: {keys2[16:24].upper()}\nKEY 7: {keys2[24:32].upper()}\n'
    keys+=f'KEY 8: {keys3[0:8].upper()}'
    return keys

def find_pin(data):
    pin = extract_bytes_from_address(data, "420")
    pin= struct.unpack('<h', pin[8:10])
    pin=f'PIN CODE: {(pin[0])}'
    return pin

def find_vin(data):
    dash = extract_bytes_from_address(data, "70")
    dash+= extract_bytes_from_address(data, "80")
    vin=f"VIN: {dash[12:29].decode('utf-8')}"
    return vin

def find_dash_model(data):
    dash = extract_bytes_from_address(data, "20")
    dash+= extract_bytes_from_address(data, "30")
    dash=f"DASH MODEL: {dash[8:18].decode('utf-8')}"
    return dash

def find_mac(data):                             #extrae linea y busca la mac del tablero y la ecu
    mac = extract_bytes_from_address(data, "460").hex()
    mac_dash=(mac[14:16]+mac[12:14]).upper()
    mac_ecu=(mac[30:32]+mac[28:30]).upper()
    
    mac=f"MAC DASH: {mac_dash} \nMAC ECU: {mac_ecu}"
    return mac

def find_eeprom_key(data):
    #print(linea5c0[6:18])
    #print(linea5c0[0:16])
    #print(invert_bits_hex(reverse_bytes_hex(linea5c0[0:16])))
    linea5c0 = extract_bytes_from_address(data, "5c0").hex()
    eeprom_key=linea5c0[6:18]+invert_bits_hex(reverse_bytes_hex(linea5c0[0:16]))
    print (invert_bits_hex(linea5c0[0:16]))
    return eeprom_key

def invert_bits_hex(hex_value: str) -> str:
    """
    Invierte los bits de un valor hexadecimal.

    Args:
    - hex_value (str): Valor en formato hexadecimal al que se le invertirán los bits.

    Returns:
    - str: Valor hexadecimal con los bits invertidos.
    """
    
    # Convertir el valor hexadecimal a un entero
    value = int(hex_value, 16)

    # Invertir los bits
    bit_length = len(hex_value) * 4  # 4 bits por cada carácter hexadecimal
    inverted = value ^ ((1 << bit_length) - 1)

    # Devolver el valor en formato hexadecimal
    return format(inverted, f'0{len(hex_value)}x')

def reverse_bytes_hex(hex_value: str) -> str:
    """
    Invierte el orden de los bytes de un valor hexadecimal.

    Args:
    - hex_value (str): Valor en formato hexadecimal al que se le intercambiarán los bytes.

    Returns:
    - str: Valor hexadecimal con los bytes en orden inverso.
    """

    # Asegurarse de que el valor hexadecimal tiene una longitud par
    if len(hex_value) % 2 != 0:
        hex_value = '0' + hex_value  # Si el valor es impar, añadir un '0' al principio
    
    # Separar en bytes y luego invertirlos
    bytes_list = [hex_value[i:i+2] for i in range(0, len(hex_value), 2)]
    reversed_bytes = ''.join(reversed(bytes_list))

    return reversed_bytes

def desencriptar_aes_ecb(ciphertext_hex: str, seed_key_hex: str) -> str:
    """
    Desencripta un texto cifrado (en formato hexadecimal) usando AES en modo ECB con una seed key (también en formato hexadecimal).

    Args:
    - ciphertext_hex (str): El texto cifrado en formato hexadecimal.
    - seed_key_hex (str): La seed key en formato hexadecimal.

    Returns:
    - str: El texto desencriptado en formato hexadecimal.
    """
    
    # Convertir el texto cifrado y la seed key de hexadecimal a bytes
    ciphertext = unhexlify(ciphertext_hex)
    seed_key = unhexlify(seed_key_hex)

    # Asegurarse de que la llave tenga el tamaño adecuado para AES (16 bytes para AES-128, 24 para AES-192, 32 para AES-256)
    if len(seed_key) not in [16, 24, 32]:
        raise ValueError("Longitud de la seed key no es válida para AES.")

    # Desencriptar usando AES en modo ECB
    cipher = AES.new(seed_key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)

    # Convertir el texto plano a formato hexadecimal y retornarlo
    return hexlify(plaintext).decode()

def forzar_seed(data):
    
    ciphertext_hex = extract_bytes_from_address(data, "440").hex()
    eeprom_key= find_eeprom_key(data)
    for i in range(1,65536):
    
        hex_value = format(i, '04X')
        seed_key_hex = hex_value + eeprom_key
        resultado = desencriptar_aes_ecb(ciphertext_hex, seed_key_hex)
        if "00000000" in resultado[24:32]:
            
            return resultado,seed_key_hex




# Ejemplo de uso:





# print(find_vin())
# print(find_dash_model())
# print(find_fazit())
# print(f"CS:{forzar_seed()[0].upper()}\nSeed key:{forzar_seed()[1].upper()}")
# print(find_mac())
# print(find_pin())
# print(find_keys())
