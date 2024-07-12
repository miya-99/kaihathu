# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\29004\\Desktop\\python\\QRコード読込.py'],
    pathex=[],
    binaries=[(r'C:\Users\29004\AppData\Local\Programs\Python\Python312\Lib\site-packages\pyzbar\zbar_library.py', '.'),(r'C:\Users\29004\AppData\Local\Programs\Python\Python312\Lib\site-packages\pyzbar\libiconv.dll', '.'),(r'C:\Users\29004\AppData\Local\Programs\Python\Python312\Lib\site-packages\pyzbar\libzbar-64.dll', '.')],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='QRコード読込',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
