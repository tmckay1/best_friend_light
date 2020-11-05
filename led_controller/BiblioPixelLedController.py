from bibliopixel.layout.strip import Strip

# control the ambient leds around the personality
class BiblioPixelLedController(object):

  # bibliopixel animation for the leds
  _led = None

  def __init__(self, driver):
    super(object, self).__init__()
    self._led = Strip(driver)

  def turn_off(self):
    self._led.all_off()
    self._led.push_to_driver()
    self._led.start()

  def turn_on_color(self, color):
    self._led.fill(color)
    self._led.push_to_driver()
    self._led.start()