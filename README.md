# pomodoro-cli

一个零依赖的 Python 番茄钟命令行小工具，适合用来专注学习或工作。

## 运行环境

- Python 3.7+

## 使用方法

```bash
# 默认：专注 25 分钟
python pomodoro.py

# 专注 50 分钟，休息 10 分钟，共 4 轮
python pomodoro.py -w 50 -b 10 -n 4
```

## 参数说明

| 参数 | 说明 | 默认值 |
| --- | --- | --- |
| `-w, --work` | 专注时长（分钟） | 25 |
| `-b, --break` | 休息时长（分钟） | 5 |
| `-n, --rounds` | 番茄轮数 | 1 |

运行中按 `Ctrl+C` 可提前结束当前轮次。

## License

MIT
