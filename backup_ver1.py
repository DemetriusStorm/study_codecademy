# Имя файла backup_ver1.py
# Резервные копии важных файлов

import os
import time

source = ['D:\\Temp\\SRC1', 'D:\\Temp\\SRC2']
target_dir = 'D:\\Temp\\Backup'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.7z'
zip_command = "7z a -tzip {} {}".format(target, ' '.join(source))

#отладка
#print(zip_command)

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии не удалось..')