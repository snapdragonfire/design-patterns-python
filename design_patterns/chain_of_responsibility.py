class NotificationHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_notification(self, notification):
        if self.successor:
            self.successor.handle_notification(notification)


class EmailHandler(NotificationHandler):
    def handle_notification(self, notification):
        if notification["channel"] == "email":
            print(f"Sending email notification: {notification['message']}")
        else:
            super().handle_notification(notification)


class SMSHandler(NotificationHandler):
    def handle_notification(self, notification):
        if notification["channel"] == "sms":
            print(f"Sending SMS notification: {notification['message']}")
        else:
            super().handle_notification(notification)


class PushNotificationHandler(NotificationHandler):
    def handle_notification(self, notification):
        if notification["channel"] == "push":
            print(f"Sending push notification: {notification['message']}")
        else:
            super().handle_notification(notification)


# Usage
email_handler = EmailHandler()
sms_handler = SMSHandler()
push_handler = PushNotificationHandler()

email_handler.successor = sms_handler
sms_handler.successor = push_handler

notification = {"channel": "push", "message": "Hello, World!"}
email_handler.handle_notification(notification)
