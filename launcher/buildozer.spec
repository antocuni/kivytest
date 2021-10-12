[app]

title = Gestione Container 2
package.name = mcont2
package.domain = eu.antocuni

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

presplash.filename = %(source.dir)s/data/icon.png
icon.filename = %(source.dir)s/data/icon.png


version = 0.4

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
android.api = 30

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

# https://github.com/kivy/python-for-android/pull/1922
# https://github.com/kivy/buildozer/pull/1369
p4a.fork = antocuni
p4a.branch = fileprovider-rebased
p4a.extra_args = --fileprovider-paths=/github/workspace/launcher/file_paths.xml

#android.arch = armeabi-v7a
# .archs is needed with the aab buildozer version
android.archs = armeabi-v7a

android.extra_manifest_application_arguments = application_arguments.xml.in

# profile to build a release aab ready for the play store
[app@aab]

android.archs = armeabi-v7a,arm64-v8a
android.release_artifact = aab 


[buildozer]
log_level = 2

