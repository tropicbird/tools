import os
import sys

from pathlib import Path
print(sys.version)
#print(sys.version_info)
print(os.getcwd())

#import glob
#print(glob.glob('/mnt/d/picture/nikon40to69_P900_D5300/nikon43 D5300', recursive=True))
def delete_files(path,ext):
    p = Path(path)
    #p = Path("/mnt/d/picture/nikon40to69_P900_D5300/")
    #for file in p.glob("**/*.NEF"):#**/とすることで、再帰的にファイルを探索する。
    for file in p.glob(f"**/*.{ext}"):  # **/とすることで、再帰的にファイルを探索する。
        print(file)
        if file.is_file():#ファイルかディレクトリか確認する。
            file.unlink() #ファイルを削除する。

'''
pathlibモジュールの使い方で参考にしたサイト↓
https://note.nkmk.me/python-pathlib-iterdir-glob/
https://www.javadrive.jp/python/file/index10.html
'''


#p = Path("/mnt/c/temp/")
#print(list(p.glob("**/*.NEF")))

# for file in p.glob("**/*"):
#     print(file)
#     if file.is_file():
#         file.unlink()

#print(glob.glob('/mnt/d/picture/nikon40to69_P900_D5300/*/*.NEF',recursive=True))

# for root, dirs, file in glob.glob('/mnt/d/picture/nikon40to69_P900_D5300/nikon43 D5300', recursive=True):
#     print(file)
#     base, ext = os.path.splitext(file)
#     #print(base, ext)
#     if ext == '.NEF':
#         print('file:{},ext:{}'.format(file,ext))

