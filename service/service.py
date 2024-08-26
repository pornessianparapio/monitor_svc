import os
import logging
import sys
import win32serviceutil
import win32service
import win32event
import servicemanager
from service.monitoring.activity_monitor import ActivityMonitor
from service.utils.scheduler import start_scheduler  # Import the scheduler
from service.init_db import db, initialize_db



def get_username():
    username = os.getlogin()
    print(username)

    return username

class MonitorService(win32serviceutil.ServiceFramework):
    _svc_name_ = "ActivityMonitorService"
    _svc_display_name_ = "Activity Monitor Service"
    _svc_description_ = "Monitors user activity on the system."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.running = True

    def SvcStop(self):
        self.running = False
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        initialize_db()
        username = get_username()
        print(f"entered username: {username}")
        activity_monitor = ActivityMonitor(username)

        # Start the scheduler in a new thread
        import threading
        scheduler_thread = threading.Thread(target=start_scheduler)
        scheduler_thread.start()

        activity_monitor.start_monitoring(self.running)

if __name__ == '__main__':
    try:
        if __name__ == '__main__':
            if len(sys.argv) == 1:
                servicemanager.Initialize()
                servicemanager.PrepareToHostSingle(MonitorService)
                servicemanager.StartServiceCtrlDispatcher()
            else:
                win32serviceutil.HandleCommandLine(MonitorService)
    except Exception as e:
        logging.basicConfig(filename='service.log', level=logging.ERROR, format='%(asctime)s %(levelname)s:%(message)s')
        print(e)
