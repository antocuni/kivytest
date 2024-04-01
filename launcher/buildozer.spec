# The lastest succesful build is with this details:
# 2024-04-01
# Buildozer 1.5.0
# android-ndk-r25b
# my branch of p4a: release-2024.01.21+fileprovider
#
# ls .buildozer/android/platform/build-arm64-v8a_armeabi-v7a/dists/mcont2/_python_bundle__armeabi-v7a/_python_bundle/site-packages/
#    android/
#    android-1.0-py3.11.egg-info
#    bin/
#    certifi/
#    certifi-2024.2.2.dist-info/
#    chardet/
#    chardet-5.2.0.dist-info/
#    _distutils_hack/
#    distutils-precedence.pth
#    idna/
#    idna-3.6.dist-info/
#    jnius/
#    kivy/
#    Kivy-2.0.0-py3.11.egg-info/
#    PIL/
#    Pillow-8.4.0-py3.11.egg-info/
#    pkg_resources/
#    pyjnius-1.6.1-py3.11.egg-info/
#    requests/
#    requests-2.31.0.dist-info/
#    setuptools/
#    setuptools-51.3.3-py3.11.egg-info/
#    six-1.15.0-py3.11.egg-info
#    urllib3/
#    urllib3-2.2.1.dist-info/
#    usr/
#

[app]

title = Gestione Container 2
package.name = mcont2
package.domain = eu.antocuni

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

presplash.filename = %(source.dir)s/data/icon.png
icon.filename = %(source.dir)s/data/icon.png

version = 0.5

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as app version and should only be edited if you know
# what you're doing
# android.numeric_version = 1

requirements = python3,
               kivy==2.0.0,
               libiconv,
               libzbar,
               pillow==7.0.0

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

#android.sdk = 20
#android.ndk = 19b
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
# for storage.py
android.add_src = java_src


# for fileprovider: useful links:
# https://github.com/kivy/python-for-android/pull/1922
# https://github.com/kivy/buildozer/pull/1369
# https://github.com/kivy/python-for-android/pull/2200
# https://github.com/kivy/python-for-android/issues/1964
# https://github.com/Android-for-Python/Android-for-Python-Users?tab=readme-ov-file#android-storage
# https://github.com/t0theRANCH/addFileProvider/tree/master

# here I'm using this commit: 13fd3dea
p4a.fork = antocuni
p4a.branch = release-2024.01.21+fileprovider
#p4a.extra_args = --fileprovider-paths=/home/kiwi/test3/kivy_android_builder/launcher/file_paths.xml
p4a.extra_args = --fileprovider-paths=/home/antocuni/pypy/misc/kivy_android_builder/launcher/file_paths.xml

[buildozer]
log_level = 2
