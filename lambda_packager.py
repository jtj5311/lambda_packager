#!/usr/bin/python3
import os
import fire


def build_tool(t, *package_list):
    command = f"uv pip install {' '.join(package_list)} --target {t}"
    os.system(command)
    os.system(f"zip -rq {t}.zip {t}")
    os.system(f"rm -rf {t}")
    os.system(f"du -h {t}.zip")


if __name__ == "__main__":
    fire.Fire(build_tool)
