# Assetto Corsa Steering Bar
A steering visualization application for Assetto Corsa. Allows users to see their current steering input relative to the maximum left-to-right steering lock of their vehicle

![Gif demonstrating the steering bar](https://github.com/Jam-BD011/Assetto-Corsa-Steering-Bar/blob/main/media/demogif.gif)

## Features
- Real-time steering angle visualization, relative to maximum steering angle
- Adjustable hud size and opacity
- Multiple theme support
- Supports user-created themes

![Gif of different bar and dot themes](https://github.com/Jam-BD011/Assetto-Corsa-Steering-Bar/blob/main/media/ThemesGif.gif)

## Requirements
- Assetto Corsa
- [Assetto Corsa Content Manager](https://assettocorsa.club/content-manager.html)
- [Assetto Corsa Custom Shaders Patch](https://acstuff.club/patch/)

# Installation

1.) On the "Releases" page, download ``SteerBar.zip`` from the latest stable release

2.) Drag-and-drop ``SteerBar.zip`` onto an open instance of Content Manager. Using the Content Management Section, Install both `steerget` (Lua App) and `SteerBar` (Python App)

⚠️ _This app requires_  ***BOTH*** `steerget` _and_ `SteerBar` _to be installed in order to work correctly_!

_Alternatively..._\
_2.)_ Extract the content of SteerBar.zip anywhere. Move the `apps` folder to your Assetto Corsa Root folder. If you have the game through Steam, you can right-click on the game from you game list and select "_Manage_", then "_Browse Local Files_". This will take you to your Assetto Corsa root folder. Ensure that the `steerget` folder is within the `assettocorsa/apps/lua` folder, and that the `SteerBar` folder is within `assettocorsa/apps/python`

3.) Within Content Manager, navigate to "_Settings_", and under "_Python Apps_", be sure that the checkbox next to "_Steer Bar_" is enabled.

3.1) The settings under "_Python App Settings_" are **fallback values** that will ***only*** be used if the values found in `config.ini` cannot be found. 

4.) Launch the game, and under "_All Apps_", find "_Steer Bar_" and click to enable. To adjust the bar settings, enable the "_Steer Bar Settings_" app. The app also includes a debugging screen that accompanies the Lua app, `Steer Bar Debug` that may be useful if you encounter issues. Follow the [In-game Setup & Settings](#in-game-setup--settings) section for setup and adjustment help!

## Updating
It is not neccessary to remove older versions of the app before updating. You may still choose to do so if you wish! Otherwise...

1.) On the "Releases" page, download ``SteerBar.zip`` from the latest stable release

2.) Drag-and-drop ``SteerBar.zip`` onto an open instance of Content Manager. Using the Content Management Section, Install both apps. 

_Alternatively..._\
_2.)_ Extract the content of SteerBar.zip anywhere. Move the `apps` folder to your Assetto Corsa Root folder. Overwrite any files when prompted. You may also move the specific app folders to their paths within `assettocorsa/apps`. Place the `steerget` folder within the `assettocorsa/apps/lua` folder (overwrite files when prompted), and the `SteerBar` folder within `assettocorsa/apps/python` (overwrite files when prompted).


# In-game Setup & Settings
![Screenshot of in-game settings windows](https://github.com/Jam-BD011/Assetto-Corsa-Steering-Bar/blob/main/media/SettingsMenu.png)

The steering bar settings can be changed through the accompanied in-game app.

- **Max Angle**: The maximum rotational lock-to-lock angle of the vehicle you're using.
- **Theme**: Name of the current theme used. Use the the arrow to cycle between themes. If you add new themes while the game is running, you _may_ need to restart your game for them to appear.
- **HUD Scale**: Scale of app window. Adjust to fit your preference. Default is `1.0`.
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
The "bar" represents the maximum left and right steering value a car has. The "dot" represents where your current steering input is, relative to your left/right lock. The `steerget` Lua app utilizes the Custom Shaders Patch's Lua SDK to write the user's vehicle's steering lock to a text file. This file then gets read by the `Steer Bar` Python app, and utilizes the written value to determine the maximum steering lock for the vehicle, and how far the dot should travel along the bar in relation to the specified maximum.

Previously, this app worked by utilizing a user-defined maximum steering angle to define dot-travel behavior. This was a reasonable solution for the now older `ac` and `acsys` Python Libraries not supporting being able to return a vehicle's maximum steering lock. I was satisfied with this until I discovered [zibed1991's Steering Indicator](https://www.overtake.gg/downloads/xsteer_indicator.84656/). I noticed that their app provided another way to visualize steering input, but was much easier to setup and use than mine. No need to adjust max angles or movement scalars, it worked for every vehicle, every time. This led me to discover the Custom Shaders Patch Lua SDK: a modern and supremely robust Lua Library for creating Lua apps for Assetto Corsa. Using this new knowledge, I decided to incorporate a Lua "companion" app (the `steerget` app) that could finally solve my biggest issue with my Python app without needing to migrate the project entirely to Lua.

Again, huge thanks to [zibed1991's Steering Indicator](https://www.overtake.gg/downloads/xsteer_indicator.84656/) app from Overtake.gg for giving me the inspiration and helping me discover the Lua SDK. Please be sure to check out their app too!!

## Update Log
***8th July 2026***
- **NEW:** Added `steerget` Lua companion app for retrieving vehicle steering lock
- **NEW:** Added a new theme
- **FIX:** HUD scale now correctly switches between all available scale values.
    - Fixed a small issue where HUD scale could become stuck on values ending in `.05` due to the previously-set minimum
 
***28th June 2026***
- **FIX:** App window size now properly scales with bar & dot scale

***25th June 2026***
- **FIX:** Bar and Dot opacity are now properly saved on game exit

## Questions, Comments?
If there's anything you'd like to ask or discuss, please feel free to start a discussion here on GitHub, or contact me through my Discord. My username is `spartantracker`.
## License Info
This project is obtainable under the provided GNU GPLv3 License. See ["LICENSE.txt"](LICENSE.txt) for more info.
