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
