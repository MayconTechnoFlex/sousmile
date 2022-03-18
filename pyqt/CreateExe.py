import PyInstaller.__main__

PyInstaller.__main__.run([
    './main.py',
    '--name=HMI Sousmile',
    # '--noconsole',
    '--noconfirm',
    '--specpath=dist',
    "--add-data=../assets/images/RN_Logo.png;assets/images",
    "--add-data=../assets/images/RN_Logo.ico;.",
])
