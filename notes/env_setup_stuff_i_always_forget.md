# Those things I always forget how to do because I've only done them maybe 3 times

## Setting up virtualenv-wrapper on Windows Subsystem Linux

After installing mkvirtualenv, after a restart there are often path issues. Resolve by running this.

```bash
source /home/name-of-user-on-wsl/.local/bin/virtualenvwrapper.sh
```

To make a python 3.8 virtual env

```bash
mkvirtualenv -p python3.8 name-of-new-virtualenv
```
