# project_template
This is a template repository for Python data science projects

## Tour

- `sampleproject/` - the "source" directory, where we are storing all our useful python functions and classes
- `tests/` - where we are story code that tests the code in `sampleproject`
- `notebooks/` - where we keep notebooks that we use for explorations, trialling new ideas, tutorials, etc
- `data/` - where we will store any data that we are working on (it will not get uploaded to GitHub)
- `LICENSE.md` - a license file that lets other people know how they can use the code in the repository.
- `requirements.txt` - a list of python packages needed to run the code in the repository
- `pyproject.toml` - a file that helps to install and package the code in the repository

## Setup

### Using/downloading this template

- **Step 1**. Setup GitHub SSH keys if you haven't already, following [these instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh). This will allow you to use GitHub via the command line without constantly putting in a password.
- **Step 2**. Click the "use this template" button to create your own version of this template. 
  - (optional) **Step 2B** Rename your repository to something more descriptive. Go to Settings and you will see Repository name at the top.
- **Step 3**. Clone your copy of the repository. On your copy (i.e. at github.com/<your-user-name>/python-project_template) click the green "Code" button, make sure that the "SSH" tab is selected in the drop down that appears and then click the copy symbol. Then go to where you want to set up your project, open a terminal and type `git clone ` and then paste the URL and hit enter.


### Virtual environment

First set up a virtual environment, this makes sure that the packages that you install only affect this project. This is really useful because when we start using lots of different packages, they can need specific versions of other packages (dependencies) and it is common to need different versions of the same package for different projects. 

To create a new virtual environment open the terminal in the root of this repository and run:
`python3 -m venv venv/` 

Then to activate the environment, you can use:
`source venv/bin/activate` 
This command means: source (i.e. run) the `activate` script in the `venv/bin` directory.
Then from now on, all the packages that you install in this project, will be installed in the `venv` directory.

### Installing requirements

Install the required python packages:
`pip3 install -r requirements.txt`

### Install sample project code
The `-e` flag tells us that we want to install the package interactively, so that when we update the code in it, our installation is also updated.
`pip3 install -e .`

### Test our code
To run all our test code, we can use:
`python3 -m pytest .`

This should give us a message saying "1 passed in 0.02s" which lets us know the tests in our test directory passed!

## Using Git and GitHub

1. Make an issue for the problem you're planning on fixing if it doesn't already exist.
2. Make sure you are on the `main` branch. (`git checkout main`) and `git pull` all the latest changes.
2. Create a new `development` branch, where you will do your development and switch to it:
`git checkout -b development` (you can call it something more specific to the problem you're working on)
3. Create a work-in-progress Pull Request from your new branch to the `main` branch. This will be a place you can get an overview of the progress you're making.
3. Working locally, take regular snapshots of your progress using `git add` and `git commit -m` and update GitHub using `git push`.
3. When you are finished with a new feature, make sure your tests run `python3 -m pytest .`, this is a great time to ask for feedback if you'd have that option and would like to, then you can merge your changes into `main`. 


