"""
GUI
"""

# standard
from subprocess import Popen
from pathlib import Path
from sys import platform
import logging as logger

# external
from py_kms_api import start_server, stop_server
import customtkinter as ctk

# internal
from def_gui import generate_frame

# Modes: 'System' (standard), 'Dark', 'Light'
ctk.set_appearance_mode('System')
# Themes: 'blue' (standard), 'green', 'dark-blue'
ctk.set_default_color_theme('blue')
# pylint: disable = logging-fstring-interpolation
pwd = Path(__file__).parent
logo = pwd / 'logo.ico' if platform == 'win32' else f'@/{pwd / "logo.xbm"}'


class App(ctk.CTk):
    """
    Python KMS Manager
    """

    def __init__(self) -> None:
        super().__init__()
        self.proc: Popen[bytes] | None = None
        self.iconbitmap(logo)
        self.title('Key Management Service Manager')
        generate_frame(self)
        logger.info('Start application')

    def update_status(self, message: str) -> None:
        """Update status"""
        self.service_status.configure(text=message)

    def start_kms(self) -> None:
        """Start KMS"""
        if isinstance(self.proc, Popen):
            self.update_status('Server already is running')
            logger.debug('KMS Server is already running at 0.0.0.0:1688')
            return
        self.proc = start_server()
        self.update_status('Server is running')
        logger.info('Started KMS server at 0.0.0.0:1688')

    def stop_kms(self) -> None:
        """Stop KMS"""
        if not self.proc:
            self.update_status('Please start the server')
            logger.debug('Please start KMS server')
            return

        if isinstance(self.proc, Popen):
            stop_server(self.proc)
            self.proc = None

        self.update_status('Server was stopped')
        logger.info('Stopped KMS server')

    def change_appearance_mode(self, theme: str) -> None:
        """Change Appearance"""
        ctk.set_appearance_mode(theme)
        logger.debug(f'Changed theme to {theme}')

    def on_closing(self):
        """Close App"""
        if self.proc:
            self.stop_kms()
        self.destroy()
        logger.info('Exit application')


logger.basicConfig(
    datefmt='%Y-%m-%d %H:%M:%S',
    format='[%(asctime)s] ln. %(lineno)-3d %(levelname)-8s %(message)s',
    level=logger.DEBUG
)
# pylint: enable = logging-fstring-interpolation

if __name__ == '__main__':
    print()
    app = App()
    app.mainloop()
    print()
