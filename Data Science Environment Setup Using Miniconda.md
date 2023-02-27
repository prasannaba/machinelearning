# Data Science Environment Setup Using Miniconda
Tuesday, October 27, 2020
10:23 PM

Author: Prasanna Badami

## Download Miniconda for Windows 10 64-bit
	https://docs.conda.io/en/latest/miniconda.html

	Select
	Python 3.8	Miniconda3 Windows 64-bit

## Python Modules for Data Science
	Note: First try conda install, usually conda will try for repodata, if not try conda install -c conda-forge, where -c is for channel.
	You can install multiple modules in a single command without y/n? prompt by using:
		conda install module1 module2 module3=2.2.2 module4 -y

	1. conda update conda
	2. conda install anaconda-navigator
	3. conda install spyder (check if Anaconda Navigator has latest, if not executed below)
		a. conda install spyder=4.1.5
	4. conda install matplotlib -y
		a. conda install numpy
	5. conda install scipy
	6. conda install pandas
	7. conda install statsmodels
	8. conda install -c bokeh bokeh or install holoviews
	9. conda install -c pyviz holoviz (this may installs older version of matplotlib, in such case install individual modules below):
		a. conda install -c pyviz holoviews bokeh
			i. conda install -c pyviz panel
			ii. conda install -c pyviz param
			iii. conda install notebook
		b. conda install -c pyviz hvplot
			i. conda install colorcet
		c. conda install datashader
	10. conda install plotly
	11. conda install scikit-learn
	12. conda install seaborn
	13. conda install voila
	14. conda install notebook
	15. conda install ipyparallel
	16. conda install nodejs
	17. conde install yarn
	18. conda install ipywidgets
	19. conda install -c bokeh ipywidgets_bokeh
	20. conda install -c bokeh jupyter_bokeh
	21. conda install jupyterlab=2.2.6
	22. conda install xlrd

	To list the module installed use the command: conda list

## JupyterLab Shortcut
	Create desktop shortcut with below path
	
		C:\ProgramData\Miniconda3\python.exe C:\ProgramData\Miniconda3\cwp.py C:\ProgramData\Miniconda3 C:\ProgramData\Miniconda3\python.exe C:\ProgramData\Miniconda3\Scripts\jupyter-lab-script.py %USERPROFILE%

	Right-click on created shortcut & set the 'start in' path to %USERPROFILE% & change the icon to JupyterLab
	Rename desktop shortcut to JupyterLab

## Configuring Browser (change default browser) for JupyterLab
	Generate jupyter_notebook_config.py
		Run below command at miniconda prompt
			jupyter lab --generate-config
	
		Add one of the below line for specific browser in jupyter_notebook_config.py stored at path %USERPROFILE%/.jupyter 
	
		Firefox (-P is for browser profile to use)
			c.NotebookApp.browser = 'C:/Program Files/Mozilla Firefox/firefox.exe -P "Juypter" %s'
	
		Microsoft Edge (--profile-directory is for browser profile to use)
			c.NotebookApp.browser = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s --profile-directory="Profile 2"'
	
		Google Chrome
			c.NotebookApp.browser = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe --app=%s"

## JupyterLab Extension Installation
	General
		○ jupyter labextension install @jupyter-widgets/jupyterlab-manager
	Bokeh
		○ jupyter labextension install @bokeh/jupyter_bokeh
	Matplotlib
		○ conda install ipympl
		○ jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-matplotlib@0.7.4
		check the labextension version that should corresponds to ipympl version
		use %matplotlib widget in notebook cell for interactive matplotlib plots
	Plotly
		○ # JupyterLab renderer support (verify the version number with module installed)
		jupyter labextension install jupyterlab-plotly@4.12.0
		
		○ # OPTIONAL: Jupyter widgets extension
		jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget@4.12.0
	Holoviz/hvplot/Pyviz
		○ jupyter labextension install @pyviz/jupyterlab_pyviz

## Final Important
    Run this command at prompt after completing all the steps (The progress bar in bokeh, holoviews, panel save() function started working after this running this command
	conda update -n base -c defaults conda

## Atom IDE
	Install hydrogen extension
	Refer: https://nteract.io/kernels
	Run following commands or just second command (b)
		a. python -m pip install ipykernel (don't have to run this command if ipykernel is already installed)
		b. python -m ipykernel install --user
	Add followings to system variables path in Windows 10
		a. C:\ProgramData\Miniconda3
		b. C:\ProgramData\Miniconda3\Scripts
		c. C:\ProgramData\Miniconda3\Library\bin

