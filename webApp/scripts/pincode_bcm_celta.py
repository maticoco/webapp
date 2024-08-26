from binascii import unhexlify, hexlify
import struct
from .read_write_exctract_files import extract_bytes_from_address


def find_pin_v2(data):
    pin = extract_bytes_from_address(data, "686",bytes_per_line=4)
    pin=f"PIN: {reverse_string(pin[0:7].decode('utf-8'))}"
    return pin


def find_vin_v2(data):
    
    dash= extract_bytes_from_address(data, "77c",bytes_per_line=17)
    vin=f"VIN: {reverse_string(dash[0:33].decode('utf-8'))}"
    return vin

def find_pin_v1(data):
    pin = extract_bytes_from_address(data, "686",bytes_per_line=4)
    pin=f"PIN: {pin[0:7].decode('utf-8')}"
    return pin


def find_vin_v1(data):
    
    dash= extract_bytes_from_address(data, "77c",bytes_per_line=17)
    vin=f"VIN: {dash[0:33].decode('utf-8')}"
    return vin

def reverse_string(input_string):
    # Invertir el string utilizando slicing
    return input_string[::-1]