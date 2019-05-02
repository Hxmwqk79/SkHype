from gi.repository import Gtk
import gi
import threading
import socket

win = Gtk.Window()
win.set_title("PyTalk")
win.set_default_size(500, 500)

box = Gtk.VBox()
vb = Gtk.VBox()
hb = Gtk.HBox()
label = Gtk.Label("")
label.set_alignment(0, 0)
entry = Gtk.Entry()

button = Gtk.Button("Send", stock=None, use_underline=True)

vb.pack_start(label, expand=False, fill=False, padding=0)
hb.pack_start(entry, expand=True, fill=True, padding=0)

hb.pack_end(button, expand=False, fill=False, padding=0)

vb.pack_end(hb, expand=False, fill=False, padding=0)
box.add(vb)

win.add(box)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8000))
s.listen(1)
(c, addr) = s.accept()
label.set_text("Connected.")


def send(widget, event):
    label.set_text(label.get_text() + "\n" + entry.get_text())
    c.send((entry.get_text()).encode('ascii'))
    entry.set_text("")


button.connect("button_press_event", send)

win.connect("destroy", Gtk.main_quit)
win.show_all()


class listenThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            message = c.recv(2048).decode('ascii')
            label.set_text(label.get_text() + message)


# Create new threads
listen = listenThread()

# Start new Threads
listen.start()

Gtk.main()
