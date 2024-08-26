import schedule
import time
import shutil
from datetime import datetime
from service.utils.upload_helper import upload_to_server  # You need to create this function

def backup_and_upload():
    # Backup the database
    backup_filename = f"activity_monitor_backup_{datetime.now().strftime('%Y%m%d')}.db"
    shutil.copy('activity_monitor.db', backup_filename)

    # Upload to server
    upload_to_server(backup_filename)

# Schedule the task to run every day at 2 AM
schedule.every().day.at("02:00").do(backup_and_upload)

def start_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)
