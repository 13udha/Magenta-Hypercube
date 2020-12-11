# Installation of the SDK for Development Usage

## Requirements for developing

The Python micro-service the SDK creates is designed to run in an UNIX-compatible environment. This includes Linux, macOS but excludes all versions of Windows. 
To run the micro-service under Windows-compatible OS, please use `--dev` run parameter, that essentially deactivates UNIX-only Gunicorn and uses integrated WSGIRefServer.

Before you start your development, install the following components:

- [Python 3](https://docs.python.org/3/using/index.html)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Recent version of the [SDK](https://github.com/telekom/voice-skill-sdk/)
- [Pip](https://pip.pypa.io/en/stable/installing/) (at least version 9.01)
- Solution for [Python virtual environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

>To run Docker services, you need a recent version of [Docker](https://www.docker.com/community-edition#/download).

>To compile the `.po` files [GNU gettext](https://www.gnu.org/software/gettext/) is required. 
[How to install gettext on MacOS X](https://stackoverflow.com/questions/14940383/how-to-install-gettext-on-macos-x/).

**Further information**

To create a virtual environment, set it up for Python 3 (`-p` argument).

## Installation of the SDK

To install SDK for development usage:

1. Activate the virtual environment that you want to install the SDK in.
2. Switch to the SDK folder (for example, `cd voice-skill-sdk`).
3. Run the setup via `python setup.py develop`.

For production, use `python setup.py install`.

Older versions of `pip` might compile the dependencies during install. Update to a newer version to speed up the process.

## Alternative installation with Pipenv

If you are creating a virtual environment for an existing project, proceed as follows:
1. Navigate to your project directory.
2. Optionally set `PIPENV_VENV_IN_PROJECT=1` variable. For further information, click [here](https://pipenv.readthedocs.io/en/latest/advanced/#pipenv.environments.PIPENV_VENV_IN_PROJECT).
3. Issue <code>pipenv install -e <b><em>path_to_sdk_folder</em></b></code>.
 
If you already have a virtual environment and just want to install SDK, proceed as follows:
- Activate your virtual environment.
- Issue <code>pipenv install -e <b><em>path_to_sdk_folder</em></b></code>.

The `-e` parameter installs SDK in 
[development mode](https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode). In this case, you can trace or modify it easier.

For further information about Pipenv, click [here](https://pipenv.readthedocs.io/en/latest/).
