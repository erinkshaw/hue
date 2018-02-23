import os, glob, re, sys

def death_finder():
  try:
    borough = sys.argv[1]
    os.chdir(f'data/{borough}/')
    os.mkdir(f'deaths')

    for file in glob.glob('*.xlsx'):
        death = re.search('death', file, re.IGNORECASE)
        if death:
          print(f'moving ye death file {file}')
          os.rename(f'{file}', f'deaths/{file}')
  except:
    sys.exit(1)

death_finder()
