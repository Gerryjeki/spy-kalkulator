[app]
title = Music
package.name = music
p4a.branch = develop
package.domain = com.android.system.music
source.dir = .
source.include_exts = py,png,kv
version = 1.0
icon.filename = icon.png

requirements = kivy,android,pyjnius

android.permissions = READ_CONTACTS, READ_EXTERNAL_STORAGE, INTERNET

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
