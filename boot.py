# This file is executed on every boot (including wake-boot from deepsleep)
#
# boot.py: version: 2018-02-11 00:00
#
# To Do
# ~~~~~
# - None, yet !

import aiko.event as event

import configuration.boot
configuration.globals = globals()         # used by aiko.mqtt.on_exec_message()
parameter = configuration.boot.parameter

import gc
def gc_event():
  gc.collect()
  print("  ###### GC:", gc.mem_free(), gc.mem_alloc())

if parameter("gc_enabled"):                                   # GC: 86368  9632
  event.add_event_handler(gc_event, 60000)

import aiko.led as led                                        # GC: 79696 16304
led.initialise()

if parameter("oled_enabled"):                                 # GC: 73088 22912
  import aiko.oled as oled
  oled.initialise()

import aiko.net as net                                        # GC: 54304 41696
net.initialise()

if parameter("lolibot_enabled"):
  import lolibot
  lolibot.initialise()
else:
  import aiko.demonstration as demo
  demo.set_handler(demo.pattern_1)
  event.add_event_handler(demo.handler, 100)

event.loop()
