import os, glob, re

def death_finder():
  os.chdir("data/brooklyn/")

  for file in glob.glob("*.xlsx"):
      death = re.search('death', file, re.IGNORECASE)
      if death:
        os.rename(f"{file}", f"deaths/{file}")

death_finder()
