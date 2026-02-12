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
