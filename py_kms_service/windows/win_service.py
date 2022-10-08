"""
PyKMS Executor
"""

# standard
from subprocess import Popen
from sys import argv
import socket

# external
from py_kms_api import start_server, stop_server
import win32serviceutil
import servicemanager
import win32event
import win32service


def app_server_svc(s_name: str, d_name: str, operation: str):
    """App Service"""
    # pylint: disable = invalid-name c-extension-no-member
    arg_list = argv

    class AppServerSvc(win32serviceutil.ServiceFramework):
        """App Service Definition"""
        _svc_name_ = s_name
        _svc_display_name_ = d_name

        def __init__(self, args):
            super().__init__(args)
            self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
            socket.setdefaulttimeout(60)
            self.proc: Popen[bytes] | None = None

        def SvcStop(self):
            """Stop Service"""
            stop_server(self.proc)
            self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
            win32event.SetEvent(self.hWaitStop)

        def SvcDoRun(self):
            """Start Service"""
            servicemanager.LogMsg(
                servicemanager.EVENTLOG_INFORMATION_TYPE,
                servicemanager.PYS_SERVICE_STARTED,
                (self._svc_name_, '')
            )
            self.proc = start_server()

    # pylint: enable = invalid-name c-extension-no-member
    if operation:
        arg_list.append(operation)
    else:
        arg_list = None
    win32serviceutil.HandleCommandLine(AppServerSvc, argv=arg_list)
