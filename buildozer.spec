[app]
title = Kalkulator Google
package.name = kalkulatorgoogle
package.domain = com.google.calc
source.dir = .
source.include_exts = py,png,kv
version = 1.0
icon.filename = icon.png

requirements = kivy, android

android.permissions = READ_CONTACTS, READ_EXTERNAL_STORAGE, INTERNET

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
