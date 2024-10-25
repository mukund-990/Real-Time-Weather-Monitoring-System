from config.config import Config

class AlertSystem:
    def __init__(self):
        self.consecutive_alerts = 0

    def check_temperature_threshold(self, temperature):
        if temperature > Config.MAX_TEMPERATURE_THRESHOLD:
            self.consecutive_alerts += 1
            if self.consecutive_alerts >= Config.CONSECUTIVE_ALERTS:
                self.trigger_alert(f"High temperature alert: {temperature}°C")
        else:
            self.consecutive_alerts = 0

    def trigger_alert(self, message):
        # In a real-world scenario, you might want to send an email or push notification
        print(f"ALERT: {message}")
