
import os
import runpy
import sys

os.chdir("/home/container")
sys.path.insert(0, "/home/container")

sys.argv = ["heroku", "--no-git"]
runpy.run_module("heroku", run_name="__main__", alter_sys=True)
