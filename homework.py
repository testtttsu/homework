import binascii
import os
import pyzipper

# 定义文件和目录名
txt_filename = 'lost_flag.txt'
zip_filename = 'secret.zip'
output_dir = 'lost_flag'
password = ''//yourpassword

# 读取文本文件中的十六进制数据
with open(txt_filename, 'r') as txt_file:
    hex_data = txt_file.read().strip()

# 将十六进制数据转换回二进制数据
binary_data = binascii.unhexlify(hex_data)

# 将二进制数据写入到ZIP文件中
with open(zip_filename, 'wb') as zip_file:
    zip_file.write(binary_data)

# 创建输出目录
os.makedirs(output_dir, exist_ok=True)

# 使用pyzipper解压缩ZIP文件
with pyzipper.AESZipFile(zip_filename, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as extracted_zip:
    extracted_zip.extractall(output_dir, pwd=str.encode(password))

print(f"文件已解压缩并保存到目录 {output_dir}")
