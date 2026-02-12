```python
import requests
import time
import json
from typing import List, Dict
from multi_notifier import MultiNotifier

def fetch_chain_fm_tokens() -> List[Dict]:
    """从chain.fm获取热门代币数据"""
    url = "https://api.chain.fm/trpc/token/hotList"
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Referer': 'https://chain.fm/'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json().get('result', [])
        return data
    except Exception as e:
        print(f"获取数据失败: {e}")
        return []

def filter_tokens(tokens: List[Dict]) -> List[Dict]:
    """
    筛选代币：
    1. 买入金额 ≥ $15,000
    2. 市值 ≥ $100,000 且上线时间 ≤ 1小时
    """
    return [
        token for token in tokens
        if (float(token.get('buyAmount', 0)) >= 15000) or 
           (float(token.get('marketCap', 0)) >= 100000 and 
            (time.time() - float(token.get('createdAt', 0)) / 1000) <= 3600)
    ]

def main():
    tokens = fetch_chain_fm_tokens()
    interesting_tokens = filter_tokens(tokens)
    
    if interesting_tokens:
        notifier = MultiNotifier()
        
        for token in interesting_tokens:
            message = f"""🚨 新代币预警:
名称: {token.get('name', '未知')}
合约地址: `{token.get('address', '未知')}`"""
            
            notifier.notify(message)

if __name__ == '__main__':
    main()
```

2. `multi_notifier.py`
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

3. `config.example.json`
```json
{
    "telegram": {
        "bot_token": "你的Telegram机器人Token",
        "chat_id": "接收消息的Chat ID"
    },
    "discord": {
        "webhook_url": "Discord Webhook地址"
    },
    "pushdeer": {
        "key": "PushDeer推送Key"
    }
}
```

4. `README.md`
```markdown
# Chain.fm 加密货币监控

## 功能
- 每15分钟监控 chain.fm 热门代币
- 多渠道通知（Telegram/Discord/PushDeer）
- 筛选条件：
  1. 买入金额 ≥ $15,000
  2. 市值 ≥ $100,000 且上线时间 ≤ 1小时

## 使用步骤
1. 安装依赖：`pip install requests`
2. 配置通知渠道
   - 复制 `config.example.json` 为 `config.json`
   - 填写 Telegram/Discord/PushDeer 配置

## 运行
```bash
python3 chain_fm_monitor.py
```
```

现在你可以在 GitHub 仓库逐个创建这些文件了。需要我具体指导你如何操作吗？
具体指导我
好的，具体指导你在 GitHub 上传文件：

1. 第一个文件 `chain_fm_monitor.py`：
- 点击 "Add file"
- 选 "Create new file"
- 文件名输入 `chain_fm_monitor.py`
- 代码框粘贴上面的 `chain_fm_monitor.py` 的全部代码
- 页面最下方 Commit 描述写 "Add main monitoring script"
- 点绿色 "Commit new file" 按钮

需要我详细说明每一步的具体点击位置吗？
你能帮我复制代码吗？
当然可以。我直接把 `chain_fm_monitor.py` 的代码复制给你：

```python
import requests
import time
import json
from typing import List, Dict
from multi_notifier import MultiNotifier

def fetch_chain_fm_tokens() -> List[Dict]:
    """从chain.fm获取热门代币数据"""
    url = "https://api.chain.fm/trpc/token/hotList"
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Referer': 'https://chain.fm/'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json().get('result', [])
        return data
    except Exception as e:
        print(f"获取数据失败: {e}")
        return []

def filter_tokens(tokens: List[Dict]) -> List[Dict]:
    """
    筛选代币：
    1. 买入金额 ≥ $15,000
    2. 市值 ≥ $100,000 且上线时间 ≤ 1小时
    """
    return [
        token for token in tokens
        if (float(token.get('buyAmount', 0)) >= 15000) or 
           (float(token.get('marketCap', 0)) >= 100000 and 
            (time.time() - float(token.get('createdAt', 0)) / 1000) <= 3600)
    ]

def main():
    tokens = fetch_chain_fm_tokens()
    interesting_tokens = filter_tokens(tokens)
    
    if interesting_tokens:
        notifier = MultiNotifier()
        
        for token in interesting_tokens:
            message = f"""🚨 新代币预警:
名称: {token.get('name', '未知')}
合约地址: `{token.get('address', '未知')}`"""
            
            notifier.notify(message)

if __name__ == '__main__':
    main()
```
