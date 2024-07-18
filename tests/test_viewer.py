import cnvpytor
from pathlib import Path


def test_module():
    pytor_path = "HepG2_WGS.pytor"
    if Path(pytor_path).exists():
        app = cnvpytor.Viewer([pytor_path], params={"bin_size":100000})
        print(app.ls())
    else:
        print(f"Incorrect Path: {pytor_path}")


if __name__ == "__main__":
    print("Welcome to python version test")
    test_module()

