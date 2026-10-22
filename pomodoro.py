#!/usr/bin/env python3
"""极简番茄钟命令行工具，零第三方依赖。"""

import argparse
import sys
import time


def countdown(minutes: int, label: str) -> None:
    seconds = minutes * 60
    print(f"\n[{label}] 开始专注 {minutes} 分钟，按 Ctrl+C 提前结束。")
    try:
        while seconds > 0:
            m, s = divmod(seconds, 60)
            print(f"\r剩余时间: {m:02d}:{s:02d}", end="", flush=True)
            time.sleep(1)
            seconds -= 1
        print("\n✅ 计时结束！")
    except KeyboardInterrupt:
        print("\n⏹️ 已手动结束本轮。")
        sys.exit(0)


def main() -> None:
    parser = argparse.ArgumentParser(description="一个极简的命令行番茄钟")
    parser.add_argument("-w", "--work", type=int, default=25, help="专注时长（分钟），默认 25")
    parser.add_argument("-b", "--break", type=int, default=5, help="休息时长（分钟），默认 5")
    parser.add_argument("-n", "--rounds", type=int, default=1, help="番茄轮数，默认 1")
    args = parser.parse_args()

    for i in range(1, args.rounds + 1):
        print(f"===== 第 {i}/{args.rounds} 轮 =====")
        countdown(args.work, "工作")
        if i < args.rounds:
            countdown(args.break_, "休息")


if __name__ == "__main__":
    main()
