#!/usr/bin/env python
"""Django 用于管理任务的命令行工具。"""
import os
import sys


def main():
    """运行管理任务。"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstdata.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "无法导入 Django。你确定它已安装，并且在你的 PYTHONPATH "
            "环境变量中可用吗？你是否忘记激活虚拟环境了？"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()