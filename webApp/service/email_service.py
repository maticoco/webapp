import os
import smtplib
import reflex as rx
from dotenv import load_dotenv
import time
# Cargar el archivo .env
load_dotenv(override=True)


# Obtener las credenciales desde el entorno
sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")
recipient_email = os.getenv("RECIPIENT_EMAIL")



class EmailServiceState(rx.State):
    notification: str = ""  # Almacena solo el mensaje de notificación
    form_data: dict = {}

    @rx.background
    async def send_email(self, form_data):
        """Función para enviar el correo con los datos del formulario."""
        
        first_name = form_data.get("first_name", "")
        last_name = form_data.get("last_name", "")
        cc_email = form_data.get("email", "")
        phone = form_data.get("phone", "")
        message = form_data.get("message", "")
        subject = f"VMH Constructora solicitud de contacto - {first_name.capitalize()} {last_name.capitalize()} quiere comunicarse"
        body = f"Nombre: {first_name}\nApellido: {last_name}\nEmail: {cc_email}\nTeléfono: {phone}\nMensaje: {message}"

        # Crear el mensaje con CC y BCC
        msg = f"Subject: {subject}\n"
        msg += f"From: {sender_email}\n"
        msg += f"To: {recipient_email}\n"        
        msg += f"Cc: {cc_email}\n"
        msg += f"\n{body}"  # Cuerpo del mensaje

     
        # Mostrar notificación de que se está enviando el correo
        async with self:
            self.notification = "Enviando..."
        
        # Conectar al servidor SMTP y enviar el correo
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, sender_password)
                # Enviar el correo a todos los destinatarios
                server.sendmail(sender_email, cc_email, msg.encode("utf-8"))
            
            # Actualizar el estado de la notificación con el mensaje de éxito
            async with self:
                self.notification = "Correo enviado con éxito"
            print("Correo enviado con éxito")
        except Exception as e:
            # Actualizar el estado de la notificación con el mensaje de error
            async with self:
                self.notification = f"Error al enviar el correo: {str(e)}"
            print(f"Error al enviar el correo: {str(e)}")
          

    @rx.background
    async def handle_submit(self, form_data: dict):
        """Manejar el envío del formulario."""
        async with self:
            self.form_data = form_data
            # Llamar a la tarea de fondo para enviar el correo
            return EmailServiceState.send_email(self.form_data)  # Devuelves la tarea


    @rx.background
    async def clear(self):
        """Manejar el envío del formulario."""
        async with self:
            self.notification = ""
