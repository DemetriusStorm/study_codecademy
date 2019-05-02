# Имя файла backup_ver2.py
# Резервные копии важных файлов

import os
import time

source = ['D:\\Temp\\SRC1', 'D:\\Temp\\SRC2']
target_dir = 'D:\\Temp\\Backup'

year = target_dir + os.sep + time.strftime('%Y')
if not os.path.exists(year):
    os.mkdir(year)
    
month = year + os.sep + time.strftime('%m')
if not os.path.exists(month):
    os.mkdir(month)
    
day = month + os.sep + time.strftime('%d')
if not os.path.exists(day):
    os.mkdir(day)
    
now = time.strftime('%H%M%S')

target = day + os.sep + now + '.7z'
zip_command = "7z a -tzip {} {}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии не удалось..')