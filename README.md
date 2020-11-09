### Overview
This repo is a project that contains code that acts as a "Best Friend" light. A "Best Friend" light has another light that it synchronizes the color with.

### Design
You will need to run this program on each light that you have and you'll need the web server running here: https://github.com/tmckay1/raspberrypi_gateway. The program works by checking for user input, and if the user changes the color of the light it tells the web server to set the current color to that color. It also continually checks the raspberry pi gateway web server for the current color in case another lamp changed it, and if it did change, the lamp will synchronize with that color.

### Running the Program
To run the program you'll need to first change the url within the color repository: https://github.com/tmckay1/best_friend_light/blob/main/repositories/ColorRepository.py to match the url of the web server you have setup. Make sure to also have BiblioPixel installed https://github.com/ManiacalLabs/BiblioPixel since this is a necessary dependency for the project. Then you'll need to modify the parameters of the main program to make sure the pins you used in your circuit match the ones defined there. You can then run the program issuing the following comand:
```
sudo python3 ./main.py
```
