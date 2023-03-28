### PyInstaller for Windows

````
sudo apt install wine
wget https://www.python.org/ftp/python/3.7.6/python-3.7.6-amd64.exe
wine msiexec /i python-3.7.6-amd64.exe /qb

wine /home/$USER/.wine/drive_c/users/$USER/Local\ Settings/Application\ Data/Programs/Python/Python37/Scripts/pip install checkmaster pyinstaller
wine /home/$USER/.wine/drive_c/users/$USER/Local\ Settings/Application\ Data/Programs/Python/Python37/Scripts/pyinstaller \
 -F --clean \
 --hidden-import checkmaster.filesystems \
 --hidden-import checkmaster.distribution \
 --hidden-import checkmaster.hardware \
 --hidden-import checkmaster.sockets \
 --hidden-import checkmaster.commands \
 --paths /home/$USER/.wine/drive_c/users/$USER/Local\ Settings/Application\ Data/Programs/Python/Python37/site-packages /home/$USER/.wine/drive_c/users/$USER/Local\ Settings/Application\ Data/Programs/Python/Python37/Scripts/checkmaster
````

Expect number of false positives with VirtusTotal with the above compilation process, so to bypass that proceed as follow:

````
pip uninstall pyinstaller
````
Then download and install [VS Cpp Community Edition](http://visualstudio.microsoft.com/vs/features/cplusplus/).
Download [pyInstaller package](http://github.com/pyinstaller/pyinstaller/releases) and unzip it in `C:\Pyinstaller`

then
````
cd C:\Pyinstaller\bootloader
python ./waf all --target-arch=64bit

set PYPATH="c:\users\utente\appdata\local\packages\pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0\localcache\roaming\python\python39"

pyinstaller -F --hidden-import checkmaster.filesystems --hidden-import checkmaster.distribution --hidden-import checkmaster.hardware --hidden-import checkmaster.sockets --hidden-import checkmaster.commands --paths $PYPATH\site-packages $PYPATH\\Scripts\checkmaster
````

If you are still having false positive from virus total consider sending your checkmaster.exe to antivirus vendors!
