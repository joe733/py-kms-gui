"""
GUI
"""

# standard
import logging as logger

# external
import customtkinter as ctk

# internal
from def_service import FactoryService
from def_gui import generate_frame

SERVICE_NAME = 'PyKMS'
SERVICE_DESCRIPTION = 'Python KMS Server'

# Modes: 'System' (standard), 'Dark', 'Light'
ctk.set_appearance_mode('System')
# Themes: 'blue' (standard), 'green', 'dark-blue'
ctk.set_default_color_theme('blue')
# Factory Service Manager
fsm = FactoryService(SERVICE_NAME, SERVICE_DESCRIPTION)

# pylint: disable = logging-fstring-interpolation


class App(ctk.CTk):
    """
    Python KMS Service Manager
    """

    def __init__(self):
        super().__init__()
        self.title('Python KMS Service Manager')
        logger.debug('Generating window frame')
        generate_frame(self)

    def install_kms(self):
        """Install KMS"""
        logger.info('Installing service')
        fsm.install_service()

    def remove_kms(self):
        """Remove KMS"""
        logger.info('Removing service')
        fsm.remove_service()

    def start_kms(self):
        """Start KMS"""
        logger.info('Starting service')
        fsm.start_service()

    def stop_kms(self):
        """Stop KMS"""
        logger.info('Stopping service')
        fsm.stop_service()

    def change_appearance_mode(self, theme: str) -> None:
        """Change Appearance"""
        ctk.set_appearance_mode(theme)
        logger.debug(f'Changed theme to {theme}')

    def on_closing(self):
        """Close App"""
        self.destroy()
        logger.info('Exit application')


logger.basicConfig(
    datefmt='%Y-%m-%d %H:%M:%S',
    format='[%(asctime)s] ln. %(lineno)-3d %(levelname)-8s %(message)s',
    level=logger.DEBUG
)

if __name__ == '__main__':
    app = App()
    app.mainloop()
