# Assetto Corsa Steering Bar
A steering visualization application for Assetto Corsa. Allows users to see their current steering input relative to the maximum angle of their sim wheel or vehicle.

![Gif demonstrating the steering bar](https://github.com/Jam-BD011/Assetto-Corsa-Steering-Bar/blob/main/media/demogif.gif)

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

1.) On the "Releases" page, download ``SteerBar.zip`` from the latest stable release

2.) Drag-and-drop ``SteerBar.zip`` onto an open instance of Content Manager. Using the Content Management Section, Install ``SteerBar.zip``.

_Alternatively..._\
_2.)_ Extract the content of SteerBar.zip anywhere. Move these contents to your Assetto Corsa Root folder, under ``assettocorsa/apps/python``. If you have the game through Steam, you can right-click on the game from you game list and select "_Manage_", then "_Browse Local Files_". This will take you to your Assetto Corsa root folder.

3.) Within Content Manager, navigate to "_Settings_", and under "_Python Apps_", be sure that the checkbox next to "_Steer Bar_" is enabled.

3.1) The settings under "_Python App Settings_" are **fallback values** that will ***only*** be used if the values found in `config.ini` cannot be found. 

4.) Launch the game, and under "_All Apps_", find "_Steer Bar_" and click to enable. To adjust the bar settings, enable the "_Steer Bar Settings_" app. Follow the next section for setup help and tips!

# In-game Setup, Settings, Tweaks
![Screenshot of in-game settings windows](https://github.com/Jam-BD011/Assetto-Corsa-Steering-Bar/blob/main/media/SettingsMenu.png)

***⚠️The app cannot automatically detect and update the max angle of the wheel or vehicle you're using. It will need to be changed manually if you want it to reflect the max angle of the car you're using! (with some exceptions)***

The steering bar settings can be changed through the accomponied in-game app.

- **Max Angle**: The maximum angle of the wheel you're using, or the maximum steering lock of the vehicle you're driving.
    - If you're using a controller, I recommend a max angle of 1080 regardless of your vehicle.
      - If you're using a keyboard; why?
    - ***Can I use my sim wheel's max lock?*** Yes, however on vehicles that have _a lot more_ or _less_ max steering angle than the wheel you're using, it may not represent lock-to-lock representation correctly. Generally, for vehicles that have _roughly_ the same max rotation as your physical wheel, the difference isn't too jarring.
    - ***What if I don't know the vehicle's max lock?*** No worries! It's easy to quickly find out:
      - Turn your wheel left/right towards lock, and watch the dot move as you do so:
        - If the dot _doesn't_ reach the far left/right of the bar but your wheel or car is at it's max lock, you can ***decrease*** the **Max Angle** until the dot moves slightly. Increase by a small value (+10) from there. Alternatively, you can also ***increase*** the **Steer Scale** value.
        - If the dot reaches the far left/right of the bar _before_ your wheel or the car hits max lock, you can ***increase*** the **Max Angle** until the dot moves slightly. Decrease by a small value (-10) from there. Alternatively, you can also ***decrease*** the **Steer Scale** value.
- **Steer Scale**: Scalar for dot movement. An alternate option to adjusting the **Max Angle**. Slightly less precise, but more convenient. Default is `2.0`.
- **HUD Scale**: Scale of both the bar and the dot. Adjust to fit your preference. Default is `1.0`.
- **Theme**: Name of the current theme used. the the arrow to cycle between themes. If you add new themes while the game is running, you may need to restart your game for them to appear.
- **Bar Opacity**: Option to change the opacity of the bar. Default is `1.0`.
- **Dot Opacity**: Option to change the opacity of the dot. Default is `1.0`.

# Custom Bar and Dot Creation
It is possible to make your own bar and dot for this mod! The process is easy.

### Before you begin...
- ***Regardless of what you choose to make, you'll need image/photo editing software.*** This can be as simple as MS Paint! Personally, I quite like using [GIMP](https://www.gimp.org/) and [ibisPaint](https://ibispaint.com/?lang=en-US).
  
1.) Go back to your Assetto Corsa root folder. Navigate to `apps/python/SteerBar/Themes`. Create a new folder within `Themes`. The name of the folder will be the name of your custom theme, so name it however you'd like.\
2.) You will need to create both a `bar.png` and a `dot.png` for the app to display them correctly. Instructions for those are right below here.

### Creating a Bar
1.) The canvas for the bar should follow an image ratio of `40:1`. It should be very thin. Some common canvas sizes I've used are `800x20`, `1600x40`, `2400x60`, and `3200x80`. You can use higher resolutions if you'd like too!\
2.) Design the bar however you'd like! Keep it simple or go nuts.\
3.) Export your bar as `bar.png` directly to your new folder in `Themes`, or move it there manually.

### Creating a Dot
1.) The canvas for the dot should be `1:1`. Some canvas sizes for dots I've made have ranged from `40x40` to `200x200`, so experiment with what you like the best.\
2.) Design the dot however you'd like! It doesn't explicitly have to be "dot" shaped either. You can make it any shape!\
3.) Export your dot as `dot.png` directly to your new folder in `Themes`, or move it there manually.

If done correctly, your new folder should only contain `bar.png` and `dot.png`. Head in-game and open the `Steer Bar Settings` app and find your new theme! 

## How's it Work?
The app uses "User max angle" to define the maximum steering angle from lock-to-lock, either of the sim wheel you're physcially using, or the vehicle you're driving. A dot is placed where your steering input currently is, relative to the maximum angle. The closer you are to your wheel lock left/right, the closer the dot will be to the edge of the bar. 

***⚠️Once again, the app cannot automatically detect and update the max angle of the wheel or vehicle you're using. It will need to be changed manually for each car to most accurately reflect the lock-to-lock value.***

This is a small limitation with the ac and acsys Python Libraries, as well as the Assetto Corsa Shared Memory library. None of these have the ability to retrieve the maximum steering angle from the vehicle you're using.\
**However...**\
Custom Shader's Patch's Lua SDK _does_ come with a way to retrieve steering lock. Stay tuned for an important update for this app later!

## Update Log
***28th June 2026***
- **FIX:** App window size now properly scales with bar & dot scale

***25th June 2026***
- **FIX:** Bar and Dot opacity are now properly saved on game exit

## Questions, Comments?
If there's anything you'd like to ask or discuss, please feel free to start a discussion here on GitHub, or contact me through my Discord. My username is `spartantracker`.
## License Info
This project is obtainable under the provided GNU GPLv3 License. See ["LICENSE.txt"](LICENSE.txt) for more info.
