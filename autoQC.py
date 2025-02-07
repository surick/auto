import os
import shutil
import argparse
from datetime import datetime, timedelta

def get_last_friday(current_date):
    # 计算上周五的日期
    days_since_friday = (current_date.weekday() - 4) % 7
    last_friday = current_date - timedelta(days=days_since_friday)
    return last_friday

def get_next_friday(current_date):
    # 计算下周五的日期
    days_until_friday = (4 - current_date.weekday()) % 7
    next_friday = current_date + timedelta(days=days_until_friday)
    return next_friday

def parse_date(date_str):
    """将MMDD格式的日期字符串转换为完整的日期对象"""
    if not date_str or len(date_str) != 4:
        raise ValueError("日期格式必须为MMDD，例如：0207")
    current_year = datetime.now().year
    return datetime.strptime(f"{current_year}{date_str}", "%Y%m%d")

def create_weekly_qc_folder(source_date=None, target_date=None):
    """
    创建QC文件夹并复制文件
    :param source_date: 源文件夹日期，格式MMDD，例如：0124
    :param target_date: 目标文件夹日期，格式MMDD，例如：0207
    """
    # 基础路径
    base_path = r"C:\Users\李晋国\Desktop\质量放行\irt\2025"
    
    if source_date is None or target_date is None:
        # 获取当前日期
        current_date = datetime.now()
        
        # 获取上周五和下周五的日期
        last_friday = get_last_friday(current_date)
        next_friday = get_next_friday(current_date)
        
        # 创建文件夹名称（MMDD格式）
        source_date = last_friday.strftime("%m%d")
        target_date = next_friday.strftime("%m%d")
    
    # 解析日期
    source_datetime = parse_date(source_date)
    target_datetime = parse_date(target_date)
    
    # 创建文件夹路径
    source_folder_path = os.path.join(base_path, source_date)
    target_folder_path = os.path.join(base_path, target_date)
    
    # 检查源文件夹是否存在
    if not os.path.exists(source_folder_path):
        print(f"源文件夹不存在: {source_folder_path}")
        return
    
    # 检查目标文件夹是否已存在
    if not os.path.exists(target_folder_path):
        os.makedirs(target_folder_path)
        print(f"成功创建文件夹: {target_folder_path}")
    else:
        print(f"文件夹已存在: {target_folder_path}")
    
    # 要复制的文件模板
    file_templates = [
        "TAPD需求追溯矩阵 TAPD Requirements Traceability Matrix.docx",
        "迭代发布质量放行报告 Iteration Release Quality Release Report.docx",
        "需求发布生产上线前检查清单 Requirement Release Production Pre-launch Checklist.xlsx"
    ]
    
    # 复制并重命名文件
    source_date_str = source_datetime.strftime("%Y%m%d")
    target_date_str = target_datetime.strftime("%Y%m%d")
    
    for template in file_templates:
        old_file = os.path.join(source_folder_path, f"{source_date_str} {template}")
        new_file = os.path.join(target_folder_path, f"{target_date_str} {template}")
        
        if os.path.exists(old_file):
            try:
                shutil.copy2(old_file, new_file)
                print(f"成功复制并重命名文件: {new_file}")
            except Exception as e:
                print(f"复制文件失败: {str(e)}")
        else:
            print(f"源文件不存在: {old_file}")

def main():
    parser = argparse.ArgumentParser(description='创建QC文件夹并复制文件')
    parser.add_argument('source_date', nargs='?', help='源文件夹日期 (MMDD格式，例如：0124)')
    parser.add_argument('target_date', nargs='?', help='目标文件夹日期 (MMDD格式，例如：0207)')
    
    args = parser.parse_args()
    create_weekly_qc_folder(args.source_date, args.target_date)

if __name__ == "__main__":
    main()