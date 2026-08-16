[app]

# (str) Title of your application
title = Zain AI Assistant

# (str) Package name
package.name = zainapp

# (str) Package domain (needed for android packaging)
package.domain = org.zain

# (list) Source files to include (let it include all python files and assets)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Add dependencies like requests or urllib3 if needed
requirements = python3,kivy,requests,urllib3,certifi

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (bool) Automatically accept SDK licenses
android.accept_sdk_license = True

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Supported architectures
android.archs = arm64-v8a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2
