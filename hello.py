import platform
import getpass

print(f"Python version: {platform.python_implementation()} {platform.python_version()} ({', '.join(platform.python_build())}) [{platform.python_compiler()}])\n")

print("System detail:")
for uname,uvalue in platform.uname()._asdict().items():
  print(f"  {uname}={uvalue}")

print()

print(f"Hello {getpass.getuser()}! This is just for you.")
