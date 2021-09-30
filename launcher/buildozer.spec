[app]

title = Kivy Generic Launcher
package.name = launcher
package.domain = eu.antocuni

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 0.1
requirements =
    android,
    hostpython3==3.8.1,
    Kivy==58e70b1,
    libiconv,
    libzbar,
    Pillow==7.0.0,
    python3==3.8.1,
    pyzbar==0.1.8,
    xcamera==2019.928


orientation = portrait
fullscreen = 0

android.arch = armeabi-v7a
android.permissions = INTERNET,CAMERA

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

