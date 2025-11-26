#!/usr/bin/env python3
"""
Faster Whisper GUI 启动脚本
"""

import os
import sys
from pathlib import Path

def check_dependencies():
    """检查必要的依赖"""
    required_packages = [
        'faster_whisper',
        'torch',
        'tkinter'  # GUI库
    ]

    missing_packages = []

    for package in required_packages:
        try:
            if package == 'tkinter':
                import tkinter
            else:
                __import__(package.replace('-', '_'))
            print(f"✓ {package} 已安装")
        except ImportError:
            missing_packages.append(package)
            print(f"✗ {package} 未安装")

    if missing_packages:
        print("\n缺少以下依赖包:")
        for pkg in missing_packages:
            print(f"  - {pkg}")

        if 'tkinter' in missing_packages:
            print("\n注意: tkinter 通常随 Python 一起安装，")
            print("如果没有，请安装 python3-tk (Ubuntu/Debian) 或重新安装 Python")

        print("\n安装方法:")
        print("pip install -r gui_requirements.txt")
        return False

    print("✅ 所有依赖检查通过")
    return True

def check_models():
    """检查模型文件"""
    models_dir = Path("models")
    available_models = []

    if (models_dir / "whisper-base-ct2").exists():
        available_models.append("base")

    if (models_dir / "whisper-large-v3-ct2").exists():
        available_models.append("large-v3")

    if available_models:
        print(f"✅ 找到模型: {', '.join(available_models)}")
        return True
    else:
        print("❌ 未找到模型文件")
        print("请确保在 models/ 目录中有以下文件夹之一:")
        print("  - whisper-base-ct2/")
        print("  - whisper-large-v3-ct2/")
        return False

def main():
    """主函数"""
    print("🎤 Faster Whisper GUI 启动检查")
    print("=" * 40)

    # 检查依赖
    if not check_dependencies():
        input("\n按回车键退出...")
        return

    print()

    # 检查模型
    if not check_models():
        print("\n即使没有模型文件，程序也能启动，")
        print("但需要在线下载模型。")
        input("\n按回车键继续启动...")

    print("\n🚀 启动 GUI 界面...")

    try:
        # 导入并启动GUI
        from gui_transcriber import WhisperGUI

        app = WhisperGUI()
        app.run()

    except ImportError as e:
        print(f"❌ 导入错误: {e}")
        print("请确保 gui_transcriber.py 文件存在")
        input("\n按回车键退出...")

    except Exception as e:
        print(f"❌ 启动失败: {e}")
        input("\n按回车键退出...")

if __name__ == "__main__":
    main()