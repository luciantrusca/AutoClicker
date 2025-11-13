import dearpygui.dearpygui as dpg
import dearpygui.demo as demo
from autoclicker import Autoclicker
import threading

dpg.create_context()
print('rewre')
def callback(sender,data):
    print(sender, "returned:", data)

with dpg.window(label='jlrewj', no_title_bar=True, no_move=True, width=600, height=600):
    # double click delay slider
    dpg.add_button(label='flsdf')
    slider = dpg.add_slider_float(min_value=0.03, max_value=1, callback=callback)

    # regular click delay slider
    dpg.add_button(label='flsdf')
    dpg.add_slider_float(min_value=0.03, max_value=1)

# dpg.destroy_context()

if __name__ == '__main__':
    # ac = Autoclicker()
    # ac.start()
    print('debug',threading.active_count())
    ac = Autoclicker()
    ac_thread = threading.Thread(target=ac.start)
    ac_thread.start()


    dpg.create_viewport(title='Custom Title', width=600, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()

    # clean up the dearpygui context
    # dpg.destroy_context()


