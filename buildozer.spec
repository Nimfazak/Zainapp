[app]

# (str) Title of your application
title = Zain

# (str) Package name
package.name = zain

# (str) Package domain (needed for android packaging)
package.domain = org.nimfazak

# (str) Source files where the main file resides
source.dir = .

# (list) Source files to include (let it include python scripts and json memory)
source.include_exts = py,json,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,requests

# (str) Version of the application
version = 1.0

# (list) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (bool) Automatically accept Android SDK licenses to fix build-tools error
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
