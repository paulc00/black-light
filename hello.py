import platform

print(f"Python version: {platform.python_version()}\n")

print("System detail:")
for uname,uvalue in platform.uname()._asdict().items():
  print(f"  {uname}={uvalue}")
