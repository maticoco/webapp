import reflex as rx
from pathlib import Path
from typing import List
from ..scripts.seedkey_95320 import find_fazit, find_keys, find_pin, find_vin, find_dash_model, find_mac, find_eeprom_key, forzar_seed
from ..scripts.pincode_bcm_celta import find_pin_v2,find_vin_v2
from ..scripts.read_write_exctract_files import read_file
from ..scripts.airbags import compare_bin_files, apply_diff_to_bin
from ..scripts.cstowords import show_words
from ..modules.process_list import PROCESS1,PROCESS2,PROCESS3


class UploadState(rx.State):
    """The app state."""
    show_download_button = False
    show_checkbox = False
    process: str = ""
    uploaded_file: Path = None
    decoded_data: str = ""
    modified_file: Path = None  # Para almacenar el archivo modificado
    modified_filename: str =""
    module: str = ""
    img: str = ""

    async def handle_upload(self, files: List[rx.UploadFile]):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() /file.filename
            self.modified_filename=f"/{file.filename}_cleared.bin"
            
            
            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)
                

            # Update the uploaded file and process it
            self.uploaded_file = outfile            
            if self.process == PROCESS2:
                self.process_file_mm95320()
    
            elif self.process == PROCESS1:
                self.process_uploaded_airbags()

            elif self.process == PROCESS3:
                self.process_file_bcm_celta()

    def process_file_bcm_celta(self):
        if self.uploaded_file:
            data = read_file(self.uploaded_file)
            
            # Procesar el archivo con las funciones de Seedkey
            pin = find_pin_v2(data)
            vin = find_vin_v2(data)
        
            # Crear el resultado final
            self.decoded_data = (
                f"\n{pin}\n{vin}\n"
            )
    
    def process_file_mm95320(self):
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
            if seed_result is not None:
                words=show_words(seed_result[0:24])
                # Crear el resultado final
                self.decoded_data = (
                    f"{fazit}\n{keys}\n{pin}\n{vin}\n{dash_model}\n{mac}\nEEPROM Key: {eeprom_key}\nCS: {seed_result.upper()}\nSeed Key: {seed_key.upper()}\n\n WORDS:\n {words.upper()}"
                )
            else:
                # Crear el resultado final
                self.decoded_data = (
                    f"{fazit}\n{keys}\n{pin}\n{vin}\n{dash_model}\n{mac}\nEEPROM Key: {eeprom_key}\nCS: {seed_result}\nSeed Key: {seed_key}\n\n"
                )

    
    def process_uploaded_airbags(self):
        if self.uploaded_file:
            # Asume que tienes el archivo de comparación predefinido
            
            #solo para nuevos airbags
            #file2_path = 'webApp/cronos_airbag/test_final.bin'
            #diff_file_path = 'webApp/cronos_airbag/diff_list.txt'


            diff_file_path = f'webApp/modules/{self.module}'
            output_file_path = f"{self.uploaded_file}_cleared.bin"
            
            try:
                apply_diff_to_bin(self.uploaded_file, diff_file_path, output_file_path)
                
                self.modified_file = output_file_path  # Guardar el archivo modificado
                self.decoded_data = "El archivo ha sido modificado exitosamente."
                self.show_download_button = True
            except ValueError as e:
                self.decoded_data = str(e)
    
    def set_config(self, process: str , module: str, img: str):
        self.process = process
        self.module = module
        self.img = img

   
    