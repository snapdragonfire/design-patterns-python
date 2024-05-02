from datetime import datetime


class Notification:
    def send(self, message):
        print(f"Sending notification: {message}")


class TimestampDecorator:
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        timestamped_message = f"{message} (Sent at {datetime.now()})"
        self.notification.send(timestamped_message)


class PriorityDecorator:
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        priority_message = f"Priority Notification: {message}"
        self.notification.send(priority_message)


# Usage
notification = Notification()
notification = TimestampDecorator(notification)
notification = PriorityDecorator(notification)

notification.send("Hello, World!")
