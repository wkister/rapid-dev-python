#!/usr/bin/env python3
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hello GNOME")
        self.button = Gtk.Button(label="Clique aqui")
        self.add(self.button)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()