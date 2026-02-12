```python
import os
import requests

class MultiNotifier:
    def __init__(self):
        self.telegram_token = os.environ.get('TELEGRAM_BOT_TOKEN')
        self.telegram_chat_id = os.environ.get('TELEGRAM_CHAT_ID')
        self.discord_webhook = os.environ.get('DISCORD_WEBHOOK_URL')
        self.pushdeer_key = os.environ.get('PUSHDEER_KEY')

    def send_telegram(self, message):
        if not self.telegram_token or not self.telegram_chat_id:
            return False
        
        url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
        payload = {
            "chat_id": self.telegram_chat_id,
            "text": message
        }
        try:
            response = requests.post(url, json=payload)
            return response.status_code == 200
        except:
            return False

    def send_discord(self, message):
        if not self.discord_webhook:
            return False
        
        payload = {"content": message}
        try:
            response = requests.post(self.discord_webhook, json=payload)
            return response.status_code == 204
        except:
            return False

    def send_pushdeer(self, message):
        if not self.pushdeer_key:
            return False
        
        url = "https://api2.pushdeer.com/message/push"
        payload = {
            "pushkey": self.pushdeer_key,
            "type": "text",
            "text": message
        }
        try:
            response = requests.post(url, json=payload)
            return response.status_code == 200
        except:
            return False

    def notify(self, message):
        results = {
            "Telegram": self.send_telegram(message),
            "Discord": self.send_discord(message),
            "PushDeer": self.send_pushdeer(message)
        }
        
        success_channels = [channel for channel, status in results.items() if status]
        failed_channels = [channel for channel, status in results.items() if not status]
        
        print(f"通知发送成功: {success_channels}")
        print(f"通知发送失败: {failed_channels}")
```
