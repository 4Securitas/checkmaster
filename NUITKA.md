### NUITKA

## System dependencies
````
sudo apt install patchelf
````
## Compile
````
python3 -m nuitka checkmaster/bin/checkmaster --standalone --follow-imports --include-plugin-directory=checkmaster
````

## Compilation log

````
Nuitka-Options:INFO: Used command line options: checkmaster/bin/checkmaster --standalone
Nuitka:INFO: Starting Python compilation with Nuitka '1.5.4' on Python '3.10' commercial grade 'not installed'.
Nuitka:INFO: Completed Python level compilation and optimization.                                    
Nuitka:INFO: Generating source code for C backend compiler.
Nuitka:INFO: Running data composer tool for optimal constant value handling.                                     
Nuitka:INFO: Running C compilation via Scons.
Nuitka-Scons:INFO: Backend C compiler: gcc (gcc).
Nuitka-Scons:INFO: Backend linking program with 183 files (no progress information available).
Nuitka-Scons:WARNING: You are not using ccache.
Nuitka-Plugins:INFO: data-files: Included data file 'certifi/cacert.pem' due to package data for 'certifi'.
Nuitka:INFO: Keeping build directory 'checkmaster.build'.                                            
Nuitka:INFO: Successfully created 'checkmaster.dist/checkmaster.bin'.

````
