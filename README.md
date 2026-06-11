# Assetto Corsa Steering Bar
A steering visualization application for Assetto Corsa. Allows users to see their current steering input relative to the maximum angle of their sim wheel or vehicle.

## Features
- Real-time steering angle visualization, relative to maximum steering angle (user defined)
- Adjustable maximum angle and steering sensitivity scalar
- Adjustable hud size and opacity
- Multiple theme support
- Supports user-created themes

## Requirements
- Assetto Corsa
- [Assetto Corsa Content Manager](https://assettocorsa.club/content-manager.html) (Highly Recommended)
- [Assetto Corsa Custom Shaders Patch](https://acstuff.club/patch/) (Highly Recommended)

# Installation
**⚠️Content Manager is _highly_ recommended!**

1.) On the "Releases" page, download ``SteerBar.zip``

2.) Drag-and-drop ``SteerBar.zip`` onto an open instance of Content Manager. Using the Content Management Section, Install ``SteerBar.zip``.

_Alternatively..._\
_2.)_ Extract the content of SteerBar.zip anywhere. Move these contents to your Assetto Corsa Root folder, under ``assettocorsa/apps/python``. If you have the game through Steam, you can right-click on the game from you game list and select "_Manage_", then "_Browse Local Files_". This will take you to your Assetto Corsa root folder.

3.) Within Content Manager, navigate to "_Settings_", and under "_Python Apps_", be sure that the checkbox next to "_Steer Bar_" is enabled.

4.) Under "_Python App Settings_", you can setup preliminary values for your "_User max angle_" (The angle of your sim wheel or vehicle), the _Bar Opacity_, and the _Dot Opacity_. These settings can also be changed in-game using the app's settings window.

# In-game Settings and Tweaks

***⚠️The app cannot automatically detect and update the max angle of the wheel or vehicle you're using. It will need to be changed manually if you want it to reflect the max angle of the car you're using!***

### Common fixes for common issues

## How's it work?
The app uses "User max angle" to define the maximum steering angle from lock-to-lock, either of the sim wheel you're physcially using, or the vehicle you're driving. A dot is placed where your steering input currently is, relative to the maximum angle. The closer you are to your wheel lock left/right, the closer the dot will be to the edge of the bar. 

***⚠️Once again, the app cannot automatically detect and update the max angle of the wheel or vehicle you're using. It will need to be changed manually.***

This is a small limitation with the ac and acsys Python Libraries, as well as the Assetto Corsa Shared Memory library. None of these have the ability to retrieve the maximum steering angle from the vehicle you're using. Had this been the case, updating the maximum angle could happen automatically.

## License Info
This project is obtainable under the provided GNU GPLv3 License. See ["LICENSE.txt"](LICENSE.txt) for more info.
