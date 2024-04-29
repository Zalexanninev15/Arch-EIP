from gi.repository import Gtk, Adw, Gio, GObject
import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_default_size(600, 250)
        self.set_title("Fedeip")

        # Main layout containers
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.set_child(self.box1)  # Horizontal box to window
        self.box1.append(self.box2)  # Put vert box in that box
        self.box1.append(self.box3)  # And another one, empty for now

        self.grid1 = Gtk.GridView()
        self.box3.append(self.grid1)

        factory = Gtk.SignalListItemFactory()

        def f_setup(fact, item):
            label = Gtk.Label(halign=Gtk.Align.START)
            label.set_selectable(False)
            item.set_child(label)

        factory.connect("setup", f_setup)

        def f_bind(fact, item):
            item.get_child().set_label(item.get_item().name)

        factory.connect("bind", f_bind)

        self.grid1.set_factory(factory)

        def on_selected_items_changed(selection, position, n_items):
            selected_item = selection.get_selected_item()
            if selected_item is not None:
                print(f"Selected item changed to: {selected_item.name}")

        # Add a button
        self.button = Gtk.Button(label="Hello")
        self.button.connect('clicked', self.hello)
        # But button in the first of the two vertical boxes
        self.box2.append(self.button)

        # Add a check button
        self.check = Gtk.CheckButton(label="And goodbye?")
        self.box2.append(self.check)

        # Add a box containing a switch and label
        self.switch_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.switch_box.set_spacing(5)

        self.switch = Gtk.Switch()
        self.switch.set_active(True)
        self.switch.connect("state-set", self.switch_switched)

        self.label = Gtk.Label(label="PIP")

        self.switch_box.append(self.switch)
        self.switch_box.append(self.label)
        self.box2.append(self.switch_box)

    def switch_switched(self, switch, state):
        print(f"The switch has been switched {'on' if state else 'off'}")

    def hello(self, button):
        print("Hello world")
        if self.check.get_active():
            print("Goodbye world!")
            self.close()


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


app = MyApp(application_id="com.Fedeip.Zalexanninev15")
app.run(sys.argv)
