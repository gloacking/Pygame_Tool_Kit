import os
import shutil
import subprocess

if (__name__ == '__main__'):
    for folder in ['dist', 'build', '*.egg-info']:
        if (os.path.exists (folder)):
            shutil.rmtree (folder, ignore_errors = True)

    subprocess.check_call ([os.sys.executable, 'setup.py', 'sdist', 'bdist_wheel'])
    subprocess.check_call (['twine', 'check', 'dist/*'])
    subprocess.check_call (['twine', 'upload', 'dist/*'])
