[app]

title = Kivy Generic Launcher
package.name = launcher
package.domain = eu.antocuni

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 0.1
requirements = python2,kivy

orientation = portrait
fullscreen = 0

android.arch = armeabi-v7a
android.permissions = INTERNET,CAMERA

# (int) Target Android API, should be as high as possible.
#android.api = 27

# (int) Minimum API your APK will support.
android.minapi = 19

#android.sdk = 20
#android.ndk = 19b
#android.ndk_api = 19

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = False


[buildozer]
log_level = 2

