from pathlib import Path

path = Path.cwd()
for p in path.glob('*/**/*.*'):
    print(p)