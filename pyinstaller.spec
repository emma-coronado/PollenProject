# pyinstaller.spec
from PyInstaller.utils.hooks import collect_all

datas, binaries, hiddenimports = collect_all("cv2")

a = Analysis(
    ["src/main.py"],
    pathex=["."],
    datas=datas + [("models", "models")],
    binaries=binaries,
    hiddenimports=hiddenimports,
)

exe = EXE(
    a.pure,
    a.scripts,
    name="SegmentationApp",
    windowed=True,
)
