# ITU KSADMAL1KU-NLP - Advanced Machine Learning for NLP in KCS 2024

### Goal/Learning Outcome:
- Define and describe basic machine learning terms and methods,
- Develop and implement machine learning methods on your own in an appropriate programming language,
- Characterize, relate, and analyze central machine learning concepts and algorithms,
- Combine and modify machine learning methods to analyze practical datasets and reflect on the results.

### Procedure/Framework:
- **All info and static material: https://learnit.itu.dk/course/view.php?id=3024579**
- 14 blocks of theory/concept lectures and group discussions
- 10 blocks exercises hands-on + 4 weeks for exam/mini-project: everyone can practise on prepared material
- Everyone decides for themselves which blocks to participate in
- No mandatory hand-ins, participation according to your own organisation, but all lectures and exercises are relevant for the exam
- Mandatory participation in course exam/mini project, which will be part of the exam
- Location: 2F13, Tue 10-12 (Lectures) & 12-14 (Exercises)
- We discuss or wrap up hands-on questions or experiences in plenum
- There is a Student Forum for questions outside the plenum/exercises (the TAs will help)
- Dynamic material: https://github.itu.dk/AML4KCS/AML4KCS2024-NLP

### Local Installation Instructions
The following instructions are prepared to install a basic environment to experience Machine Learning and the necessary package on your computer. Later, during the course, we will look into online as well as collaborative environments and make use of them. Nevertheless, a basic environment should always be under control.

Don't worry about any difficulties and let the TA or the teachers know. We will help with this in the exercises of Week-1.

##### Highly suggested environment:
- Best/Standard OS for machine learning is Ubuntu (20.04 or higher) 
    - Windows/MacOS sufficient for first steps and development
- Pycharm professional (recent version, https://www.jetbrains.com/pycharm/download/ need to register using university email) - this already includes Jupyter notebook

##### Alternative minimal environments:
- Pycharm community (https://www.jetbrains.com/pycharm/download/) OR Spyder(download from Anaconda, https://www.spyder-ide.org/)
- Jupyter notebook (https://jupyter.org/install)

##### Preparations
- Dependencies between python packages can always be tricky. Be resilient with installing individual packages until everything works just fine.
- **Ubuntu:**
    - Open a terminal, navigate to a directory where you want to install class materials, then run the command 
  `git clone https://github.itu.dk/AML4KCS/AML4KCS2024-NLP.git`
    - Install everything via `source install-ubuntu.sh`    
- **Windows:**
    - Install Tortoise Git 
      and clone https://github.itu.dk/AML4KCS/AML4KCS2024-NLP.git
    - Open the gitfolder AML4DS2024 as a project in PyCharm 
    - Add a new Project Interpreter (Settings -> Project -> Project Interpreter -> click gear-wheel -> Add... -> New environment)
        > We suggest to choose `<gitfolder>/venvWin/` as location and chose Python 3.10 or higher as Base interpreter.
    - In Pycharm open `W00-preparations/E00_test_setup.py` 
        - Pycharm will ask to "Package requirement *** not satisfied" -> click "Install requirement".
            > Pycharm will install all packages that we defined in the `requirements.txt`. 
        - If this fails, install all these packages manually
            - in the "Terminal" tab run `pip3 install -r requirements.txt`
            - or via cmd run `python3 get-pip.py` ([download get-pip.py](https://bootstrap.pypa.io/get-pip.py)) and run `pip3 install -r requirements.txt`
            - or click-install the packages one by one from Settings -> Project -> Project Interpreter
    - Install torch and tensorflow via `install-windows.sh` from your IDE terminal
        - if this 'install-windows.sh' does not work, then install manually from the terminal as follows (Windows will ask you how to open this -> just choose nothing or "Command Promt"):
            - pip3 install -r requirements.txt
            - pip3 install torch==2.3.0 -f https://download.pytorch.org/whl/torch_stable.html
            - pip3 install tensorflow==2.15.0
- **Mac:**
  - analogous
  - for Mac M1 users: 
    - The Apple silicon version of PyCharm has some issues with opening jupyter notebooks. So it is advised to install the intel version to ensure that there are no software related issues with running the exercises.
    - Matplotlib might give some errors when installing. In this case try to use another version as suggested in *requirements.txt* file: `pip install matplotlib`.
- For all: if your PC/Laptop does NOT have a GPU that you can use for computations and CUDA installed, then you might install tensorflow-cpu instead of tensorflow

##### Test packages via test_setup.py
- Run the test_setup.py in debug mode (Run -> Debug..). If no errors/exceptions pop up, then you are good. Otherwise check which package is missing or was installed in an incorrect version and try again.
- Test jupyter notebook test_jupyter.ipynb:
    - In Pycharm open `W00-preparations/E00_test_jupyter.ipynb`
    - Press the **Run All** button within the test_jupyter.ipynb
        > A Jupyter server should start and run. On the right side of the GUI you should see the executed code and result. If no error pops up, you are fine. Otherwise check the Jupyter documentation.
	
##### Update materials
Open a terminal on Linux or Mac (or Tortoise Git on Windows), navigate (using cd command) to the folder of this git repository on your computer. Type `git pull`. It should ask you to log in with your GitHub account. After that, files will automatically get downloaded. If any conflict arises, you can either follow the suggestion printed in the terminal or create a new folder and redo git clone as above.
