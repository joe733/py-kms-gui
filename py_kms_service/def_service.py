"""
Service definitions
"""

# standard
from sys import platform

# internal
from windows.win_service import app_server_svc


class WindowService:
    """Windows Service Manager"""

    def __init__(self, s_name, d_name) -> None:
        self.s_name = s_name
        self.d_name = d_name

    def install_service(self) -> None:
        """Install windows service"""
        app_server_svc(self.s_name, self.d_name, 'install')

    def remove_service(self) -> None:
        """Install windows service"""
        app_server_svc(self.s_name, self.d_name, 'remove')

    def start_service(self) -> None:
        """Start windows service"""
        app_server_svc(self.s_name, self.d_name, 'debug')

    def stop_service(self) -> None:
        """Stop windows service"""
        app_server_svc(self.s_name, self.d_name, 'stop')


class LinuxService:
    """Linux Service Manager"""

    def __init__(self) -> None:
        pass

    def install_service(self) -> None:
        """Install linux service"""

    def remove_service(self) -> None:
        """Install linux service"""

    def start_service(self) -> None:
        """Start linux service"""

    def stop_service(self) -> None:
        """Stop linux service"""


class FactoryService:
    """Factory Service"""

    def __init__(self, s_name, d_name) -> None:
        self.s_name = s_name
        self.d_name = d_name

        if platform == 'linux':
            self.service = LinuxService()
        elif platform == 'win32':
            self.service = WindowService(s_name, d_name)

    def install_service(self) -> None:
        """Install Service"""
        self.service.install_service()

    def remove_service(self) -> None:
        """Install Service"""
        self.service.remove_service()

    def start_service(self) -> None:
        """Install Service"""
        self.service.start_service()

    def stop_service(self) -> None:
        """Install Service"""
        self.service.stop_service()
