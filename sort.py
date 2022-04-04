import os
import shutil

def main():
  path = input('Input your path to sort: ')

  list_ = os.listdir(path)

  for file_ in list_:
    name, ext = os.path.splitext(file_)
    ext = ext[1:]
    
    if ext == '':
      continue
    
    if os.path.exists(f'{path}/{ext}'):
      shutil.move(f'{path}/{file_}', f'{path}/{ext}/{file_}')
    else:
      os.makedirs(f'{path}/{ext}')
      shutil.move(f'{path}/{file_}', f'{path}/{ext}/{file_}')
      
if __name__ == '__main__':
  main()
