import ac
import acsys
import math
import os

#Author: Jam-BD011
"""
 Assetto Corsa Steering Bar; a steering visualization app for Assetto Corsa
    Copyright (C) 2026 Jam-BD011

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

# =========================================================
# APPS
# =========================================================

barApp = 0
settingsApp = 0

# =========================================================
# TEXTURES
# =========================================================

barTexture = 0
dotTexture = 0
barOpacityLabel = 0
dotOpacityLabel = 0

# =========================================================
# CONFIG
# =========================================================

CONFIG_PATH = "apps/python/SteerBar/config.ini"
THEME_ROOT = "apps/python/SteerBar/themes/"

# =========================================================
# SETTINGS
# =========================================================

USER_MAX_ANGLE = 900.0
STEER_SCALE = 2.0
WINDOW_SCALE = 1.0
BAR_OPACITY = 1.0
DOT_OPACITY = 1.0
CURRENT_THEME = "Base"

# =========================================================
# HUD
# =========================================================

BAR_X = 0
BAR_Y = 50

BASE_BAR_WIDTH = 800
BASE_BAR_HEIGHT = 20
BASE_DOT_SIZE = 20

BAR_WIDTH = BASE_BAR_WIDTH
BAR_HEIGHT = BASE_BAR_HEIGHT
DOT_SIZE = BASE_DOT_SIZE

# =========================================================
# STEERING
# =========================================================

steerSmooth = 0

# =========================================================
# THEME SYSTEM
# =========================================================

THEMES = []
themeIndex = 0

# =========================================================
# LABELS
# =========================================================

angleLabel = 0
scaleLabel = 0
sizeLabel = 0
themeLabel = 0
restartLabel = 0

# =========================================================
# CONFIG
# =========================================================

#try to save current config settings
def save_config():
    try:
        with open(CONFIG_PATH, "w") as f:
            f.write("USER_MAX_ANGLE=" + str(USER_MAX_ANGLE) + "\n")
            f.write("STEER_SCALE=" + str(STEER_SCALE) + "\n")
            f.write("WINDOW_SCALE=" + str(WINDOW_SCALE) + "\n")
            f.write("BAR_OPACITY=" + str(BAR_OPACITY) + "\n")
            f.write("DOT_OPACITY=" + str(DOT_OPACITY) + "\n")
            f.write("THEME=" + CURRENT_THEME + "\n")

    except:
        ac.log("Failed to save config")


#attempt to load current config settings
def load_config():
    global USER_MAX_ANGLE
    global STEER_SCALE
    global WINDOW_SCALE
    global CURRENT_THEME
    global BAR_OPACITY
    global DOT_OPACITY

    #try and load config settings from cofig path
    try:
        with open(CONFIG_PATH, "r") as f:

            for line in f:

                #only look for assigned values
                if "=" not in line:
                    continue

                #k=attribute, v=value for attribute
                k, v = line.split("=")

                k = k.strip()
                v = v.strip()

                if k == "USER_MAX_ANGLE":
                    USER_MAX_ANGLE = float(v)

                elif k == "STEER_SCALE":
                    STEER_SCALE = float(v)

                elif k == "WINDOW_SCALE":
                    WINDOW_SCALE = float(v)

                elif k == "BAR_OPACITY":
                    BAR_OPACITY = float(v)

                elif k == "DOT_OPACITY":
                    DOT_OPACITY = float(v)

                elif k == "THEME":
                    CURRENT_THEME = v

    #fallback settings
    except:
        USER_MAX_ANGLE = 900.0
        STEER_SCALE = 2.0
        WINDOW_SCALE = 1.0
        BAR_OPACITY = 1.0
        DOT_OPACITY = 1.0
        CURRENT_THEME = "Base"

# =========================================================
# THEME SCANNING
# =========================================================

#look for themes
def scan_themes():
    global THEMES

    THEMES = []

    #try and get themes from theme root path
    try:
        for folder in os.listdir(THEME_ROOT):

            full = os.path.join(THEME_ROOT, folder)

            if os.path.isdir(full):
                THEMES.append(folder)

    except:
        THEMES = ["Base"]

# =========================================================
# LOAD THEME
# =========================================================

#load theme
def load_theme():
    global barTexture
    global dotTexture

    themePath = THEME_ROOT + CURRENT_THEME + "/"

    #every themes uses bar.png and dot.png
    barTexture = ac.newTexture(themePath + "bar.png")
    dotTexture = ac.newTexture(themePath + "dot.png")

# =========================================================
# HUD SCALE
# =========================================================

#change the hud scale
def update_hud_scale():
    global BAR_WIDTH
    global BAR_HEIGHT
    global DOT_SIZE

    BAR_WIDTH = BASE_BAR_WIDTH * WINDOW_SCALE
    BAR_HEIGHT = BASE_BAR_HEIGHT * WINDOW_SCALE
    DOT_SIZE = BASE_DOT_SIZE * WINDOW_SCALE

# =========================================================
# LABELS
# =========================================================

#update labelss to reflect user changes
def update_labels():

    ac.setText(
        angleLabel,
        "Max Angle: " + str(int(USER_MAX_ANGLE))
    )

    ac.setText(
        scaleLabel,
        "Steer Scale: " + str(round(STEER_SCALE, 2))
    )

    ac.setText(
        sizeLabel,
        "HUD Scale: " + str(round(WINDOW_SCALE, 2))
    )

    ac.setText(
        barOpacityLabel, 
        "Bar Opacity: " + str(round(BAR_OPACITY, 2))
        )

    ac.setText(
        dotOpacityLabel, 
        "Dot Opacity: " + str(round(DOT_OPACITY, 2)))

    ac.setText(
        themeLabel,
        "Theme: " + CURRENT_THEME
    )

# =========================================================
# SETTINGS BUTTONS
# =========================================================

#clamp for bar and dot opacity
def clamp(x):
    return max(0.0, min(1.0, x))

#reduce max angle
def angle_minus(*args):
    global USER_MAX_ANGLE

    USER_MAX_ANGLE = max(180, USER_MAX_ANGLE - 10)

    update_labels()
    save_config()

#increase max angle
def angle_plus(*args):
    global USER_MAX_ANGLE

    USER_MAX_ANGLE = min(1440, USER_MAX_ANGLE + 10)

    update_labels()
    save_config()

#reduce steering scalar
def scale_minus(*args):
    global STEER_SCALE

    STEER_SCALE = max(0.1, STEER_SCALE - 0.1)

    update_labels()
    save_config()


#increase setting scalar
def scale_plus(*args):
    global STEER_SCALE

    STEER_SCALE += 0.1

    update_labels()
    save_config()


#reduce window size
def size_minus(*args):
    global WINDOW_SCALE

    WINDOW_SCALE = max(0.25, WINDOW_SCALE - 0.1)

    update_hud_scale()

    update_labels()
    save_config()

#increase window size
def size_plus(*args):
    global WINDOW_SCALE

    WINDOW_SCALE += 0.1

    update_hud_scale()

    update_labels()
    save_config()

#reduce bar opacity
def bar_opacity_minus(*args):
    global BAR_OPACITY
    BAR_OPACITY = clamp(BAR_OPACITY - 0.1)
    update_labels()
    save_config()
    
#increase bar opacity
def bar_opacity_plus(*args):
    global BAR_OPACITY
    BAR_OPACITY = clamp(BAR_OPACITY + 0.1)
    update_labels()
    save_config()

#decrease dot opacity
def dot_opacity_minus(*args):
    global DOT_OPACITY
    DOT_OPACITY = clamp(DOT_OPACITY - 0.1)
    update_labels()
    save_config()

#increase dot opacity
def dot_opacity_plus(*args):
    global DOT_OPACITY
    DOT_OPACITY = clamp(DOT_OPACITY + 0.1)
    update_labels()
    save_config()

# =========================================================
# THEME SWITCHING
# =========================================================

#go to next themne
def next_theme(*args):
    global themeIndex
    global CURRENT_THEME

    themeIndex += 1

    if themeIndex >= len(THEMES):
        themeIndex = 0

    CURRENT_THEME = THEMES[themeIndex]

    load_theme()

    update_labels()

    save_config()

#previous theme switching not currently working. indexing issue i think? removed for now
#not a big deal but somewhat annoying

#create the setup settings menu
def setup_settings_ui():
    global angleLabel
    global scaleLabel
    global sizeLabel
    global themeLabel
    global barOpacityLabel
    global dotOpacityLabel
    global restartLabel

    # -------------------------
    # LABELS
    # -------------------------

    angleLabel = ac.addLabel(settingsApp, "")
    ac.setPosition(angleLabel, 20, 20)

    scaleLabel = ac.addLabel(settingsApp, "")
    ac.setPosition(scaleLabel, 20, 80)

    sizeLabel = ac.addLabel(settingsApp, "")
    ac.setPosition(sizeLabel, 20, 140)

    themeLabel = ac.addLabel(settingsApp, "")
    ac.setPosition(themeLabel, 20, 200)

    barOpacityLabel = ac.addLabel(settingsApp, "")
    ac.setPosition(barOpacityLabel, 20, 260)

    dotOpacityLabel = ac.addLabel(settingsApp, "")
    ac.setPosition(dotOpacityLabel, 20, 320)
    
    #just in case theme switching doesnt work, you'd need to back out and go back in
    restartLabel = ac.addLabel(
        settingsApp,
        "Theme changes may require restart"
    )
    ac.setPosition(restartLabel, 20, 225)

    # -------------------------
    # MAX ANGLE
    # -------------------------

    btn = ac.addButton(settingsApp, "-")
    ac.setPosition(btn, 220, 20)
    ac.setSize(btn, 30, 30)
    ac.addOnClickedListener(btn, angle_minus)

    btn = ac.addButton(settingsApp, "+")
    ac.setPosition(btn, 260, 20)
    ac.setSize(btn, 30, 30)
    ac.addOnClickedListener(btn, angle_plus)

    # -------------------------
    # STEER SCALE
    # -------------------------

    btn = ac.addButton(settingsApp, "-")
    ac.setPosition(btn, 220, 80)
    ac.setSize(btn, 30, 30)
    ac.addOnClickedListener(btn, scale_minus)

    btn = ac.addButton(settingsApp, "+")
    ac.setPosition(btn, 260, 80)
    ac.setSize(btn, 30, 30)
    ac.addOnClickedListener(btn, scale_plus)

    # -------------------------
    # WINDOW SCALE
    # -------------------------

    btn = ac.addButton(settingsApp, "-")
    ac.setPosition(btn, 220, 140)
    ac.setSize(btn, 30, 30)
    ac.addOnClickedListener(btn, size_minus)

    btn = ac.addButton(settingsApp, "+")
    ac.setPosition(btn, 260, 140)
    ac.setSize(btn, 30, 30)
    ac.addOnClickedListener(btn, size_plus)

    # -------------------------
    # BAR OPACITY
    # -------------------------
    barOpacityLabel = ac.addLabel(settingsApp, "")
    ac.setPosition(barOpacityLabel, 20, 260)

    btn = ac.addButton(settingsApp, "-")
    ac.setPosition(btn, 220, 260)
    ac.setSize(btn, 30, 30)
    ac.addOnClickedListener(btn, bar_opacity_minus)

    btn = ac.addButton(settingsApp, "+")
    ac.setPosition(btn, 260, 260)
    ac.setSize(btn, 30, 30)
    ac.addOnClickedListener(btn, bar_opacity_plus)

    # -------------------------
    # DOT OPACITY
    # -------------------------
    dotOpacityLabel = ac.addLabel(settingsApp, "")
    ac.setPosition(dotOpacityLabel, 20, 320)

    btn = ac.addButton(settingsApp, "-")
    ac.setPosition(btn, 220, 320)
    ac.setSize(btn, 30, 30)
    ac.addOnClickedListener(btn, dot_opacity_minus)

    btn = ac.addButton(settingsApp, "+")
    ac.setPosition(btn, 260, 320)
    ac.setSize(btn, 30, 30)
    ac.addOnClickedListener(btn, dot_opacity_plus)

    # -------------------------
    # THEME
    # -------------------------
    
    btn = ac.addButton(settingsApp, ">")
    ac.setPosition(btn, 260, 200)
    ac.setSize(btn, 30, 30)
    ac.addOnClickedListener(btn, next_theme)

    update_labels()

# =========================================================
# MAIN
# =========================================================


def acMain(ac_version):
    global barApp
    global settingsApp
    global themeIndex

    #get config settings
    load_config()

    #scan for themes
    scan_themes()

    if CURRENT_THEME in THEMES:
        themeIndex = THEMES.index(CURRENT_THEME)

    update_hud_scale()

    # =====================================================
    # BAR APP
    # =====================================================

    #bar app window
    barApp = ac.newApp("Steer Bar")

    ac.setSize(barApp, 800, 100)

    ac.setTitle(barApp, "")

    ac.drawBorder(barApp, 0)
    ac.setIconPosition(barApp, 10000, 10000)

    ac.setBackgroundOpacity(barApp, 0)

    # =====================================================
    # SETTINGS APP
    # =====================================================

    #settings app window
    settingsApp = ac.newApp("Steer Bar Settings")

    ac.setSize(settingsApp, 320, 400)

    setup_settings_ui()

    # =====================================================
    # LOAD THEME
    # =====================================================

    load_theme()

    # =====================================================
    # RENDER CALLBACK
    # =====================================================

    ac.addRenderCallback(barApp, onFormRender)

    return "Steer Bar"

def acUpdate(deltaT):
    global steerSmooth

    #keep UI transparent
    ac.setBackgroundOpacity(barApp, 0)
    ac.drawBorder(barApp, 0)

    #read steering input
    raw = ac.getCarState(0, acsys.CS.Steer)

    #normalize using user-defined wheel rotation range
    steer = raw / USER_MAX_ANGLE

    #smooth input
    steerSmooth += (steer - steerSmooth) * 0.2

def onFormRender(deltaT):

    #find bar center
    centerX = BAR_X + BAR_WIDTH / 2

    #apply smoothing, then mulitply by the desired scalar
    #make sure the dot cant move beyond the bar using max
    steer = steerSmooth * STEER_SCALE
    steer = max(-1.0, min(1.0, steer))

    #find max distance the dot can travel across the bar
    #subtract dot size to make sure dot stays within bar length
    travel = (BAR_WIDTH - DOT_SIZE) / 2

    #convert normalized steering value into relevant screen position
    #position = center + offset
    #offset = steer * travel
    dotX = centerX + steer * travel

    #set bar opacity
    ac.glColor4f(1, 1, 1, BAR_OPACITY)
    
    #draw bar
    ac.glQuadTextured(
        BAR_X,
        BAR_Y,
        BAR_WIDTH,
        BAR_HEIGHT,
        barTexture
    )

    #set dot opacity
    ac.glColor4f(1, 1, 1, DOT_OPACITY)

    #draw dot
    ac.glQuadTextured(
        dotX - DOT_SIZE / 2,
        BAR_Y,
        DOT_SIZE,
        DOT_SIZE,
        dotTexture
    )

    #save settings on shutdown
def acShutdown():

    save_config()
    ac.log("Settings saved")