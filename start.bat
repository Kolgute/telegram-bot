@echo off

call %~dp0pybot\Scripts\activate

set ID_GROUP=

set TOKEN=

cd %~dp0
python bot_telegram.py
pause