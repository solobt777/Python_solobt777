python -m venv myevn
source myevn/bin/activate
deactivate
### to check globally what is available pip list
pip3 list | grep pandas

### use pip freeze to list all the python libraries install in the current Virtual Env
pip freeze

# if you using conda
conda create --name <name of the project as your wish e.g 'regressingProject'>
conda activate regressingProject
conda deactivate

conda install jupyter notebook
## to open
jupyter notebook
## if you want to install specific python version
conda install python=3.7.6


### pyenv commands
pyenv versions
pyenv install --list
pyenv uninstall <version>
pyenv install <version> e.g. pyenv install 3.13.5
pyenv shell <version>
pyenv local <version>
pyenv global <version>