[app]

# Zain AI
title = Zain AI
package.name = zain
package.domain = org.nimfazak

# Location of main.py
source.dir = .

# Files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt

# Python and Kivy (Cython and hostpython3 added)
requirements = python3,hostpython3,kivy==2.3.1,cython

# App version
version = 1.0

# Android settings
android.python_version = 3.10
android.api = 33
android.minapi = 23
android.archs = arm64-v8a, armeabi-v7a

# Screen
orientation = portrait
fullscreen = 0

# Internet access
android.permissions = INTERNET

# Accept Android SDK license
android.accept_sdk_license = True

# Let Buildozer manage NDK automatically to avoid path/version mismatch in CI
# android.ndk = 25b

[buildozer]

# Buildozer logging (set to detailed debug mode)
log_level = 2

# Do not stop because Buildozer is running as root
warn_on_root = 1
0
