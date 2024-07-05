import reflex as rx
from pathlib import Path
from typing import List
from ..scripts.seedkey_95320 import find_fazit, find_keys, find_pin, find_vin, find_dash_model, find_mac, find_eeprom_key, forzar_seed
from ..scripts.read_write_exctract_files import read_file

class UploadState(rx.State):
    """The app state."""

    # Definir los tipos de los atributos
    uploaded_file: Path = None
    decoded_data: str = ""
    img: List[str] = []

    async def handle_upload(self, files: List[rx.UploadFile]):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename

            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            # Update the uploaded file and process it
            self.uploaded_file = outfile
            self.process_file()

    def process_file(self):
        if self.uploaded_file:
            data = read_file(self.uploaded_file)
            # Procesar el archivo con las funciones de Seedkey
            fazit = find_fazit(data)
            keys = find_keys(data)
            pin = find_pin(data)
            vin = find_vin(data)
            dash_model = find_dash_model(data)
            mac = find_mac(data)
            eeprom_key = find_eeprom_key(data)
            seed_result, seed_key = forzar_seed(data)

            # Crear el resultado final
            self.decoded_data = (
                f"{fazit}\n{keys}\n{pin}\n{vin}\n{dash_model}\n{mac}\nEEPROM Key: {eeprom_key}\nCS: {seed_result.upper()}\nSeed Key: {seed_key.upper()}"
                
            )
            self.img.append(str(self.uploaded_file))
