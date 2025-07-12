from plyer import notification
import time

def send_notification(title, message, timeout=10):
    notification.notify(
        title=title,
        message=message,
        timeout=timeout  # seconds
    )

if __name__ == "__main__":
    while True:
        send_notification("💧 Hydration Reminder", "Time to drink water!", 5)
        time.sleep(60 * 60)  # Wait for 1 hour
