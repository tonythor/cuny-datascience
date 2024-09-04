# 602 virtualenv
 
## Setup .venv (Mac)
Setup your virutalenv venv with something like this... 

```sh
brew install python@3.10 ## to get python, if you do'nt already have it! 
brew install python-tk@3.10
brew link --overwrite python-tk@3.10

/opt/homebrew/Cellar/python\@3.10/3.10.13_2/bin/python3.10 -m venv .venv
source ./.venv/bin/activate
pip install --upgrade pip
pip install -r ./requirements.txt
```

## Set PYTHONPATH

In your .venv/bin/activate, your python classpath must be set to include the .venv directory, plus the ./src directory, like this, but with your paths. 

`export PYTHONPATH=/Users/afraser/Documents/src/cuny-datascience/data620webanalytics/.venv/lib/python3.10/site-packages:/Users/afraser/Documents/src/cuny-datascience/data620webanalytics/src`


Now make sure you have tk in there.

```shell
brew install brew install tcl-tk
```
And add this into ./.venv/bin/activate as well, probably right under PYTHONPATH above.

```shell
export TK_LIBRARY="/opt/homebrew/Cellar/tcl-tk/8.6.14/lib"
export LD_LIBRARY_PATH="/opt/homebrew/Cellar/tcl-tk/8.6.14/lib:$LD_LIBRARY_PATH"
```



## To do nltk plots in iPython
```python
import matplotlib.pyplot as plt
import nltk
from nltk.book import text4
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
plt.show()
```