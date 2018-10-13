# -*- mode: python -*-

block_cipher = None


a = Analysis(['qzy_to_json.py'],
             pathex=['C:\\Users\\ovewa\\Desktop\\git-storage\\python\\诗琳通\\指纹库采集处理_全站仪定位版'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='qzy_to_json',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
