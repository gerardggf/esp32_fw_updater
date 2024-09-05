from PyInstaller.utils.hooks import collect_submodules

# Recolecta submódulos ocultos de esptool
hiddenimports = collect_submodules('esptool')

a = Analysis(['flash_fw.py'],
             pathex=[C:\Users\ggutierrez\Documents\proyectos python\esp32_fw_updater],
             binaries=[],
             datas=[],
             hiddenimports=hiddenimports,
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             cipher=None,
             noarchive=False)
