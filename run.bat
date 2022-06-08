call activate finlab
python auto_update.py
python bband_detect.py --ls long --date 2022-05-12
@REM python bband_detect.py --long_short a --date 2022-05-24
python bband_result.py
call conda deactivate
pause