# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['scampy.py'],
             pathex=['/home/danny/Development/Development/Python/SCAMPY'],
             binaries=[],
             datas=[],
             hiddenimports=['img2pdf', 'yagmail'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='scampy',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='app.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='scampy')
