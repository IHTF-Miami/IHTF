import subprocess
import os

workspace = r"c:\Users\alvar\OneDrive\Documentos\GitHub\IHTF-Miami\IHTF"
scratch_dir = os.path.join(workspace, "scratch")
rar_path = r"C:\Users\alvar\Downloads\teatro.rar"
unrar_exe = r"C:\Program Files\WinRAR\UnRAR.exe"

cmd = [unrar_exe, "x", "-y", rar_path, r"teatro\2016 _ teatroavante_files\*", r"teatro\2017 _ teatroavante_files\*", scratch_dir + "\\"]
res = subprocess.run(cmd, capture_output=True, text=True)
print("Exit code:", res.returncode)
print(res.stdout[:500])
