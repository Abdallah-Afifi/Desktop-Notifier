from plyer import notification
import time

def desktop_notifier(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Desktop Notifier',
        timeout=10  # Notification will be visible for 10 seconds
    )

def main():
    interval_minutes = 60  # Set the interval in minutes
    title = "Reminder"
    message = "Don't forget to take a break and stretch!"

    while True:
        desktop_notifier(title, message)
        time.sleep(interval_minutes * 60)  # Convert minutes to seconds

if __name__ == "__main__":
    main()
