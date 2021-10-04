[app]

title = Gestione Container 2
package.name = mcont2
package.domain = eu.antocuni

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

presplash.filename = %(source.dir)s/data/icon.png
icon.filename = %(source.dir)s/data/icon.png


version = 0.1
requirements = python3,
               kivy==2.0.0,
               libiconv,
               libzbar,
               pillow==7.0.0

orientation = portrait
fullscreen = 0

#android.arch = armeabi-v7a
# .archs is needed with the aab buildozer version
android.archs = armeabi-v7a,arm64-v8a

android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
#android.api = 27
android.api = 30

# (int) Minimum API your APK will support.
android.minapi = 21

#android.sdk = 20
#android.ndk = 19b
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True


# for aab
p4a.branch = develop
android.release_artifact = aab 

[buildozer]
log_level = 2

