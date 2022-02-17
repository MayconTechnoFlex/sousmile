import PyInstaller.__main__

PyInstaller.__main__.run([
    './pyqt/main.py',
    '--name=HMI Sousmile',
    '--noconsole',
    '--noconfirm',
    '--specpath=dist',
    "--add-data=../pyqt/assets/images/RN_Logo.png;assets/images",
    "--add-data=../pyqt/assets/images/RN_Logo.ico;.",
])
