"""Program: Configuración de las credenciales
    Propósito: Obtener los datos de las variables de entorno
    Autor(es): Miguel Ángel García Flores
    Fecha Creación: 23 Diciembre 2022
    (c) 2022 - Miguel Ángel García Flores
    Todos los derechos reservados
"""
from pydantic import BaseSettings

class BaseSettingsApp(BaseSettings):
    """
    Obtención de las variables de entorno

    Atrributes:
        app_name (str): Nombre de la aplicación
        app_version (str): Versión de la aplicación
    """
    app_name: str
    app_version: str

    class Config:
        """
        Configuración de un archivo env

        Attributes:
            env_file (str): Tipo de archivo
            env_file_encoding (str): Codificación del archivo
        """
        env_file = '.env'
        env_file_encoding = 'utf-8'
