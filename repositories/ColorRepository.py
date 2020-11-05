import requests

class ColorRepository(object):

  _base_url = "http://10.0.0.151:3000/best_friend_lights"

  def get_current_color(self, current_color_index):
    try:
      response = requests.get(self._base_url + "/get_color_index/").json()
      print("got color " + str(response["color_index"]))
      return int(response["color_index"])
    except ConnectionError:
      print("Error getting current color")
      return current_color_index

  def set_current_color(self, color_index):
    try:
      requests.post(self._base_url + "/set_color_index/?color_index=" + str(color_index))
    except ConnectionError:
      print("Error setting current color")