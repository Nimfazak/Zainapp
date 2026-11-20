
[app]

# Application identity
title = Zain AI
package.name = zainai
package.domain = org.farouk
version = 1.1.0

# Source files
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,otf

# Python and Kivy
requirements = python3,kivy==2.3.1

# Display
orientation = portrait
fullscreen = 0

# Android configuration
android.permissions = INTERNET
android.api = 34
android.minapi = 23
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

# Android application settings
android.private_storage = True
android.allow_backup = False

# Build configuration
p4a.bootstrap = sdl2

# Logging
log_level = 2

[buildozer]

# Buildozer settings
warn_on_root = 1
