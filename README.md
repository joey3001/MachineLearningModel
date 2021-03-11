# Fannie Mae Loan Predictor Machine Learning Model 

## By Joseph Nero 

### Description
This is an end to end machine learning model that will predict whether or not loans acquired by Fannie Mae will go into foreclosure using a variety of borrower data. 

#### By Joseph Nero 

## 🔧 Setup/Installation Requirements
#### If you have difficulty following any of the steps/instructions listed below, please contact me at josephnero111@gmail.com 

1. cmd prompt & Git.  
    - To clone the repository from Github using git commands in the terminal, you need a terminal program & Git. For the conda environment to work, you need to use the cmd prompt on Windows. 

2. VSCode (or another code editor)
    - To view/edit this code, you need a code editor. I recommend VSCode. 

3. For Detailed instructions on how to install Git Bash & VSCode, visit the Setup/Installation Requirements section of the README for [this repo.](https://github.com/joey3001/first-friday-project)

4. Python and the Anaconda Package Manager 

    You can download Anaconda [here.](https://www.anaconda.com/products/individual) Anaconda is a Python package manager that comes preloaded with the various packages we will need to run the model. 

#### Intention of this project 

This project will take in a variety of loan data to predict if loans will be foreclosed on or not. 

To do this we take data about the loan and whether or not it was foreclosed on and formated it in a way that
can be used to train a machine learning model. 
This includes the following steps: 

1. Applying headers to data tables for ease of reading and organization. 

2. Determining the data neccesary for your machine learning model to function. In our case, 
   we don't need any performance data apart from whether or not the loan was forelosed on. As such, 
   we will have to go into our performance data set and extract only this relevant piece. On the other hand, 
   we want all of the acquisition data possible as to strengthen the accuracy of our model. 

3. converting all possible variable types to numbers, as machine learning models can only work with 
   numerical data. 

4. It also includes splitting your data set into a "training" set and a "testing" set. 
   You use the training set to train the model, and you use the testing set to evalute the model's accuracy. 
   Without this step, your model will test well artificially, as it's not 
   actually attempting to predict new values. 

#### Interpreting the output 

The following output is delivered by the project: 

            Accuracy Score: .5 
            False Negatives: .4 
            False Postives: .4

The Accuracy score is the percentage of times the model is able to predict the loan's future foreclosure status accurately. 
The False Negatives Score is the percentage of times a model predicts that the loan will not be foreclosed on, but it is. 
The False Positives Score is the percentage of times a model predicts that the loan will be foreclosed on, but it is not. 

For our purposes, a false negative score is more important than a false positive score, as we do not want to 
acquire loans that will eventually be foreclosed upon. 

#### To clone this project using git commands in the terminal : 

1. Use the following command in your terminal program to clone the repo :

            git clone https://github.com/joey3001/MachineLearningModel

#### To set up the machine learning model and run the project using terminal commands, follow the instructions below : 

1. Enter the loan-prediction directory using cd commands. Conda requires commands to be entered in a cmd prompt terminal. Git bash will not work.  

2. The base conda environment contains the required packages. Activate the environment with the following command:

            conda activate base 

3. Run the scripts in this order: assemble.py => annotate.py => predict.py by entering the following commands: 

            python assemble.py 
            python annotate.py
            python predict.py 

4. The output will be presented to the terminal. 

#### To view the code in the VSCode editor using commands in the terminal :  

1. Navigate to the project's root directory with the cd command. 

2. Once you are within the project's root directory, enter the following command into your terminal program to view all of the project's code in VSCode : 

            code . 

#### To download a file containing the contents of this repository to a location of your choice :  

1. Use a web browser to go to the repository webpage at [this link.](https://github.com/joey3001/AnimalShelterAPI.Solution)
2. Click on the green button labeled "code" towards the right side of the page's center. In the drop-down menu that opens, click on the button labeled "Download Zip."
3. Once your download is complete, open the zipped file. Click on the button labeled "Extract All" at the top of your file explorer. 
4. Choose the location in which you want to extract the files, and navigate to that location once this process is complete. 

## 🐛 Known Bugs

No known bugs are present at this time. 

## 📫 Support and contact details

If you have an issue, reach out to me at josephnero111@gmail.com

## 🛠️ Technologies Used

* Anaconda - Python Package Manager 
* pandas
* matplotlib
* scikit-learn
* numpy 
* ipython
* scipy

### 📘 License

[MIT License](https://choosealicense.com/licenses/mit/)

Copyright (c) 2020 Joseph Nero 
