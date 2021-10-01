[app]

title = Kivy py2 Generic Launcher
package.name = launcher27
package.domain = eu.antocuni

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 0.2
requirements = python3,kivy==2.0.0,libiconv,libzbar

orientation = portrait
fullscreen = 0

android.arch = armeabi-v7a
android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
#android.api = 27

# (int) Minimum API your APK will support.
android.minapi = 21

#android.sdk = 20
#android.ndk = 19b
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True


[buildozer]
log_level = 2

