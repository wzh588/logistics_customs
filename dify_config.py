import os

# Dify环境配置文件
# 在Dify平台上，这些路径可能需要根据实际环境进行调整

# 基础目录设置
BASE_DIR = os.getcwd()  # 在Dify中获取当前工作目录

# 文件夹配置
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "outputs")
TEMPLATES_FOLDER = os.path.join(BASE_DIR, "templates")
IMAGES_FOLDER = os.path.join(BASE_DIR, "images")

# 模板文件路径
EXAMPLE_FILE = os.path.join(TEMPLATES_FOLDER, "001.xlsx")

# 确保必要的目录存在
def ensure_directories():
    """确保所有必要的目录都存在"""
    directories = [
        UPLOAD_FOLDER,
        OUTPUT_FOLDER,
        TEMPLATES_FOLDER,
        IMAGES_FOLDER
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

# Dify平台特定配置
DIFY_CONFIG = {
    "max_file_size": 10 * 1024 * 1024,  # 10MB最大文件大小
    "supported_formats": [".xlsx"],
    "temp_storage_days": 7,  # 临时文件存储天数
}
