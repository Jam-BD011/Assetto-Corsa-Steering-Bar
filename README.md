# Assetto Corsa Steering Bar
A steering visualization application for Assetto Corsa. Allows users to see their current steering input relative to the maximum angle of their sim wheel or vehicle.

## Features
- Real-time steering angle visualization, relative to maximum steering angle (user defined)
- Adjustable maximum angle and steering sensitivity scalar
- Adjustable hud size and opacity
- Multiple theme support
- Supports user-created themes

![Gif of different bar and dot themes](https://github.com/Jam-BD011/Assetto-Corsa-Steering-Bar/blob/main/media/ThemesGif.gif)

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

3.1) The settings under "_Python App Settings_" are **fallback values** that will ***only*** be used if the values found in `config.ini` cannot be found. 

4.) Launch the game, and under "_All Apps_", find "_Steer Bar_" and click to enable. To adjust the bar settings, enable the "_Steer Bar Settings_" app. Follow the next section for setup help and tips!

# In-game Setup, Settings, Tweaks
![Screenshot of in-game settings windows](https://github.com/Jam-BD011/Assetto-Corsa-Steering-Bar/blob/main/media/SettingsMenu.png)

***⚠️The app cannot automatically detect and update the max angle of the wheel or vehicle you're using. It will need to be changed manually if you want it to reflect the max angle of the car you're using!***

The steering bar settings can be changed through the accomponied in-game app.

- **Max Angle**: The maximum angle of the wheel you're using, or the maximum steering lock of the vehicle you're driving.
    - If you're using a controller, I recommend a max angle of 1080 regardless of your vehicle.
      - If you're using a keyboard; why?
    - ***What if I don't know the vehicle's max lock?*** No worries! It's easy to quickly find out:
      - Turn your wheel left/right towards lock, and watch the dot move as you do so:
        - If the dot doesn't reach the far left/right of the bar but your wheel or car is at it's max lock, you can ***decrease*** the **Max Angle** until the dot moves slightly. Increase by a small value from there. Alternatively, you can also ***increase*** the **Steer Scale** value.
        - If the dot reaches the far left/right of the bar before you wheel or the car hits max lock, you can ***increase*** the **Max Angle** until the dot moves slightly. Decrease by a small value from there. Alternatively, you can also ***decrease*** the **Steer Scale** value.
- **Steer Scale**: Scalar for dot movement. An alternate option to adjusting the **Max Angle**. Slightly less precise, but more convenient.
- **HUD Scale**: Scale of both the bar and the dot. Adjust to fit your preference.
- **Theme**: Name of the current theme used. the the arrow to cycle between themes. If you add new themes while the game is running, you may need to restart your game for them to appear.
- **Bar Opacity**: Option to change the opacity of the bar.
- **Dot Opacity**: Option to change the opacity of the dot.

## How's it Work?
The app uses "User max angle" to define the maximum steering angle from lock-to-lock, either of the sim wheel you're physcially using, or the vehicle you're driving. A dot is placed where your steering input currently is, relative to the maximum angle. The closer you are to your wheel lock left/right, the closer the dot will be to the edge of the bar. 

***⚠️Once again, the app cannot automatically detect and update the max angle of the wheel or vehicle you're using. It will need to be changed manually.***

This is a small limitation with the ac and acsys Python Libraries, as well as the Assetto Corsa Shared Memory library. None of these have the ability to retrieve the maximum steering angle from the vehicle you're using. Had this been the case, updating the maximum angle could happen automatically.

# Custom Bar and Dot Creation

## License Info
This project is obtainable under the provided GNU GPLv3 License. See ["LICENSE.txt"](LICENSE.txt) for more info.
