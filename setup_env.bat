call conda env remove -n finlab
call conda create -n finlab python=3.7 --yes

REM =============== PACKAGES ==============

call conda activate finlab

call conda install -c conda-forge implicit
call conda install -c anaconda py-xgboost
call conda install bottleneck

call python -m pip install pandas==1.1.4 requests==2.22.0 tqdm==4.31.1 seaborn tensorflow==1.14.0 ipykernel keras==2.2.4 lightgbm==2.2. ipywidgets==7.4.2 lxml
call python -m pip install eli5==0.10.1 Skater==1.0.4 shap==0.37.0 mlxtend==0.18.0
call python -m pip install scikit-learn==0.21.3
call python -m pip install pyfolio==0.9.2

REM ================= TALIB ===============

call python -m pip install gdown

call python -c "import gdown;gdown.download('https://drive.google.com/uc?export=download&id=1U60ZIn_GcY3GTzg-O4etKBALHGEkHUcg', 'TA_Lib-0.4.19-cp37-cp37m-win_amd64.whl')"
REM powershell -Command "(New-Object Net.WebClient).DownloadFile('https://drive.google.com/uc?export=download&id=1U60ZIn_GcY3GTzg-O4etKBALHGEkHUcg', 'TA_Lib-0.4.19-cp37-cp37m-win_amd64.whl')"
call python -m pip install TA_Lib-0.4.19-cp37-cp37m-win_amd64.whl

REM ======== JUPYTER LAB IPYWIDGETS ======

call conda deactivate

call python -m pip install jupyterlab==3.0.0
call python -m pip install widgetsnbextension==3.5.1
call python -m pip install jupyterlab-widgets==1.0.0


call conda activate finlab

REM ============= KERNEL SETUP ============

call jupyter kernelspec uninstall finlab
call python -m ipykernel install --user --name finlab

REM ================ CHECK ===============

call python -m pip uninstall -y numpy
call python -m pip uninstall -y pandas
call python -m pip uninstall -y scipy
call python -m pip install numpy==1.19.3 pandas==1.1.4 scipy
call python -m pip install h5py==2.10a
call python -m pip install git+https://github.com/quantopian/pyfolio
call python -m pip install gdown

call python -c "import gdown;gdown.download('https://drive.google.com/uc?export=download&id=1GQzRpMN_RR1v9kXWOXn5BXMHKfyk0ET4', 'check.py')"
REM powershell -Command "(New-Object Net.WebClient).DownloadFile('https://drive.google.com/uc?export=download&id=1GQzRpMN_RR1v9kXWOXn5BXMHKfyk0ET4', 'check.py')"
call python check.py


call python -c "import gdown;gdown.download('https://drive.google.com/uc?export=download&id=1zgu4UuMtvWNwVsgzi1Yo-bNHW_ZGJAzd', 'download_material.py')"
REM powershell -Command "(New-Object Net.WebClient).DownloadFile('https://drive.google.com/uc?export=download&id=1zgu4UuMtvWNwVsgzi1Yo-bNHW_ZGJAzd', 'download_material.py')"
call python download_material.py
cd finlab_ml_course
call python auto_update.py
