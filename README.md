# ECGDatabase

Database with search functionalities for the [Epic Card Game](http://www.epiccardgame.com/)


## Build

This project is built using [PyBuilder](http://pybuilder.github.io/). To setup your build
environment simply do the following:

```bash
virtualenv -p python2.7 venv
source venv/bin/activate
pip install --upgrade pip
pip install pybuilder
pyb install_dependencies
```

To perform a build, i.e. execute unit tests and package the deployment artifact:

```bash
pyb -X publish
```


## Run Locally

To build, deploy, and run locally you can run the following script from within the **project
root directory**:

```bash
source build/build_and_run_locally.sh
```

Afterwards you can test the application from within your web browser:

* [http://localhost:5000/all_decks](http://localhost:5000/all_decks)
