"""
GUI
"""

# standard
from subprocess import Popen
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

class App(ctk.CTk):
    """
    Python KMS Manager
    """

    def __init__(self) -> None:
        super().__init__()
        self.proc: Popen[bytes] | None = None
        self.title('Key Management Service Manager')
        generate_frame(self)

    def update_status(self, message) -> None:
        """Update status"""
        self.service_status.configure(
            text=f'KMS Status:\n\n{message}'
        )

    def start_kms(self) -> None:
        """Start KMS"""
        if isinstance(self.proc, Popen):
            self.update_status('Server already is running at 0.0.0.0:1688')
            logger.debug('KMS Server is already running')
            return
        self.proc = start_server()
        self.update_status('Server started at 0.0.0.0:1688')
        logger.info('Started KMS server')

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
        self.stop_kms()
        self.destroy()
        logger.info('Exit application')


logger.basicConfig(
    datefmt='%Y-%m-%d %H:%M:%S',
    format='[%(asctime)s] ln. %(lineno)-3d %(levelname)-8s %(message)s',
    level=logger.DEBUG
)

if __name__ == '__main__':
    print()
    app = App()
    app.mainloop()
    print()
