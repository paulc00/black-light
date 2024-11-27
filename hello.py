import platform

print(f"Python version: {platform.python_implementation()} {platform.python_version()} ({', '.join(platform.python_build())}) [{platform.python_compiler()}])\n")

print("System detail:")
for uname,uvalue in platform.uname()._asdict().items():
  print(f"  {uname}={uvalue}")
