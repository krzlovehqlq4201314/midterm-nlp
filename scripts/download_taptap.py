"""Download TapTap reviews dataset from Kaggle."""
import subprocess, pathlib

dest = pathlib.Path('data/raw')
dest.mkdir(parents=True, exist_ok=True)

cmd = [
    'kaggle', 'datasets', 'download',
    '-d', 'griffith000/taptap-reviews',
    '-p', str(dest),
    '--unzip'
]
print('Running:', ' '.join(cmd))
subprocess.run(cmd, check=True)
print('✅  Download complete')
