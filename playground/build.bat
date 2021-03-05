@echo off
g++ -shared -m32 test.cpp -o test_x86.dll
g++ -shared -m64 test.cpp -o test_x86_64.dll