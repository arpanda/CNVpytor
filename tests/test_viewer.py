import cnvpytor
from pathlib import Path


def test_module():
    app = cnvpytor.Viewer(["HepG2_WGS.pytor"], bin_size=100000)
    print(app.ls())


if __name__ == "__main__":
    print("Welcome to python version test")
    test_module()

