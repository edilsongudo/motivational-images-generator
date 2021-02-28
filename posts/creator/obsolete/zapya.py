import shutil
import os

os.chdir('C:/Users/Kevin 2/Documents/Zapya/Photo')
try:
    for item in os.listdir('c:/Users/Kevin 2/Documents/Zapya/Photo/'):
        try:
            if item.endswith('.dm'):
                print(item)
                shutil.copy(
                    item, f"c:/Users/Kevin 2/Documents/Zapya/Photo/{item.replace('.dm', '')}")
                shutil.move(item, item.replace('.dm', ''))
        except Exception as e:
            print(e)
except Exception as e:
    print(e)

# with open('output.txt', 'w') as f:
#   f.write('')

# n = 0
# for folder, folders, file in os.walk('c:/Users/Kevin/', topdown=True):
#   try:
#       for f in file:
#           if f.endswith('.doc') or f.endswith('.docx'):
#               print(os.path.join(folder, f))
#               print('')
#               with open('output.txt', 'a') as ficheiro:
#                   ficheiro.write(os.path.join(folder, f))
#                   ficheiro.write('\n')
#   except Exception as e:
#       print(e)
#   n +=1
#   if n % 10000 == 0:
#       print(f'{n} Done.')
