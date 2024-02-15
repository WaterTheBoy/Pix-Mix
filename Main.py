# Pix Mix
# Copyright (c) 2024 Water Corulla and Water& Incorporated
#
# This software is licensed under the terms of the Pix Mix License Agreement.
# For more details, see the LICENSE.txt file.
#
# The art used in this software was provided by OrangeGulp (https://www.instagram.com/orangegulp/)
# The art is protected under copyright laws and thus may not be used without the artists express permission.
#
# This file includes code from the pixelate library (https://pypi.org/project/pixelate/)
# Licensed under the BSD License by Georgy Bazhukov

from tkinter import *
from tkinter import colorchooser, ttk, filedialog as fd
from PIL import Image, ImageTk, ImageFile, ImageFilter
from multiprocessing import Barrier, Pool, cpu_count
from threading import Thread  
from pixelate import pixelate
import os
import sys
import json
import shutil
import imageio
import cv2 
import math
import numpy as np  
import multiprocessing
import threading 
import concurrent.futures 
import time 
import glob
import gc
ImageFile.LOAD_TRUNCATED_IMAGES = True
os.system('cls')
gc.collect()

def create_canvas():
    my_canvas = Canvas(root, width=301, height=151, bg="#9fd27f", borderwidth=0, highlightthickness=0)
    my_canvas.place(x=math.ceil(screen_width*.1), y=math.ceil(screen_height*.45))
    #Show default colors. Sets area and then color from default list.
    tim = 0
    if switch == 1:
        while tim <= 15:
            tam = [[0,0,50,50],[50,0,100,50],[100,0,150,50],[150,0,200,50],[200,0,250,50],[0,50,50,100],[50,50,100,100],[100,50,150,100],[150,50,200,100],[200,50,250,100],[0,100,50,150],[50,100,100,150],[100,100,150,150],[150,100,200,150],[200,100,250,150],[250,100,300,150]]
            tom = [["#8c8fae"],["#584563"],["#3e2137"],["#9a6348"],["#d79b7d"],["#f5edba"],["#c0c741"],["#647d34"],["#e4943a"],["#9d303b"],["#d26471"],["#70377f"],["#7ec4c1"],["#34859d"],["#17434b"],["#1f0e1c"]]
            my_canvas.create_rectangle(tam[tim], fill=tom[tim])
            tim += 1
    # variable to store hexadecimal code of color
    if switch == 0:
        def choose_color(value):
            color_code = colorchooser.askcolor(title ="Choose color")
            my_canvas.create_rectangle(value[0:4], fill=color_code[1])
            if len(chosencolorpalette) > value[4]:
                chosencolorpalette[value[4]] = color_code[0]
            else:
                chosencolorpalette.append(color_code[0])
        button1 = Button(root, text = "1", command=lambda:choose_color((0,0,50,50, 0)))
        button1.configure(width = 3, activebackground = "#33B5E5", relief = FLAT)
        button1_window = my_canvas.create_window(10, 10, anchor=NW, window=button1)
        button2 = Button(root, text = "2", command=lambda:choose_color((50,0,100,50, 1)))
        button2.configure(width = 3, activebackground = "#33B5E5", relief = FLAT)
        button2_window = my_canvas.create_window(60, 10, anchor=NW, window=button2)
        button3 = Button(root, text = "3", command=lambda:choose_color((100,0,150,50, 2)))
        button3.configure(width = 3, activebackground = "#33B5E5", relief = FLAT)
        button3_window = my_canvas.create_window(110, 10, anchor=NW, window=button3)
        button4 = Button(root, text = "4", command=lambda:choose_color((150,0,200,50, 3)))
        button4.configure(width = 3, activebackground = "#33B5E5", relief = FLAT)
        button4_window = my_canvas.create_window(160, 10, anchor=NW, window=button4)
        button5 = Button(root, text = "5", command=lambda:choose_color((200,0,250,50, 4)))
        button5.configure(width = 3, activebackground = "#33B5E5", relief = FLAT)
        button5_window = my_canvas.create_window(210, 10, anchor=NW, window=button5)
        button6 = Button(root, text = "6", command=lambda:choose_color((0,50,50,100, 5)))
        button6.configure(width = 3, activebackground = "#33B5E5", relief = FLAT)
        button6_window = my_canvas.create_window(10, 60, anchor=NW, window=button6)
        button7 = Button(root, text = "7", command=lambda:choose_color((50,50,100,100, 6)))
        button7.configure(width = 3, activebackground = "#33B5E5", relief = FLAT)
        button7_window = my_canvas.create_window(60, 60, anchor=NW, window=button7)
        button8 = Button(root, text = "8", command=lambda:choose_color((100,50,150,100, 7)))
        button8.configure(width = 3, activebackground = "#33B5E5", relief = FLAT)
        button8_window = my_canvas.create_window(110, 60, anchor=NW, window=button8)
        button9 = Button(root, text = "9", command=lambda:choose_color((150,50,200,100, 8)))
        button9.configure(width = 3, activebackground = "#33B5E5", relief = FLAT)
        button9_window = my_canvas.create_window(160, 60, anchor=NW, window=button9)
        button10 = Button(root, text = "10", command=lambda:choose_color((200,50,250,100, 9)))
        button10.configure(width = 3, activebackground = "#33B5E5", relief = FLAT)
        button10_window = my_canvas.create_window(210, 60, anchor=NW, window=button10)
        button11 = Button(root, text = "11", command=lambda:choose_color((0,100,50,150, 10)))
        button11.configure(width = 3, activebackground = "#33B5E5", relief = FLAT)
        button11_window = my_canvas.create_window(10, 110, anchor=NW, window=button11)
        button12 = Button(root, text = "12", command=lambda:choose_color((50,100,100,150, 11)))
        button12.configure(width = 3, activebackground = "#33B5E5", relief = FLAT)
        button12_window = my_canvas.create_window(60, 110, anchor=NW, window=button12)
        button13 = Button(root, text = "13", command=lambda:choose_color((100,100,150,150, 12)))
        button13.configure(width = 3, activebackground = "#33B5E5", relief = FLAT)
        button13_window = my_canvas.create_window(110, 110, anchor=NW, window=button13)
        button14 = Button(root, text = "14", command=lambda:choose_color((150,100,200,150, 13)))
        button14.configure(width = 3, activebackground = "#33B5E5", relief = FLAT)
        button14_window = my_canvas.create_window(160, 110, anchor=NW, window=button14)
        button15 = Button(root, text = "15", command=lambda:choose_color((200,100,250,150, 14)))
        button15.configure(width = 3, activebackground = "#33B5E5", relief = FLAT)
        button15_window = my_canvas.create_window(210, 110, anchor=NW, window=button15)
        button16 = Button(root, text = "16", command=lambda:choose_color((250,100,300,150, 15)))
        button16.configure(width = 3, activebackground = "#33B5E5", relief = FLAT)
        button16_window = my_canvas.create_window(260, 110, anchor=NW, window=button16)
    switchPalette()

def onPrint():
    #Add detailed UI! Give 'em a show.
    root.state('zoomed')
    BackgroundImage_Label = Label(image=BackgroundImage, borderwidth=0, highlightthickness=0)
    BackgroundImage_Label.place(x=0, y=0)
    BackgroundImage_Label.lower()
    #Button changes
    TextEntry.config(image=TextField, borderwidth=0, highlightthickness=0)
    TextEntry.place(x=math.ceil(screen_width/2-(TextField.width()/2)), y=math.ceil((screen_height*.2)))
    imageFileName_button.place(x=math.ceil(screen_width*.37), y=math.ceil(screen_height*.215))
    Fetch_button.config(image=EntryButton, borderwidth=0, highlightthickness=0)
    Fetch_button.place(x=math.ceil(screen_width*.7), y=math.ceil(screen_height*.2))
    button_showimage = Button(root, image=PaletteButton, command=create_canvas , borderwidth=0, highlightthickness=0)
    button_showimage.place(x=math.ceil(screen_width/2-(PaletteButton.width()/2)), y=math.ceil((screen_height/2)*.6))
    #UI details
    startLabel.config(text=(imageFileName[:60]), bg='#9fd27f')
    startLabel.place(x=math.ceil(screen_width*.43), y=math.ceil(screen_height*.21))
    startLabel.lift()
    TutorialLabel.config(text="")
    #Sliders for Pixel Size!
    pixelslider_title = Label(text="Pixel Size", bg='#9fd27f')
    pixelslider_title.place(x=math.ceil(screen_width*.045), y=math.ceil((screen_height)*.46))
    global pixelsize
    pixelsize = Scale(root, from_=1, to=42, bg='#9fd27f') #, tickinterval=8)
    pixelsize.set(5)
    pixelsize.place(x=math.ceil(screen_width*.05), y=math.ceil((screen_height)*.5))
    #If filename is supported, continue the process.
    image_extensions = ('.png', '.tiff', '.bmp', '.gif', '.jpg', '.jpeg', '.webp')
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv')
    global MakeOutput 
    global imageSize
    global frames
    global resized
    global imageLabel
    MakeOutput = (imageFileName)
    if imageFileName.lower().endswith(image_extensions):
        # Handle image file
        imageObject = Image.open(MakeOutput)
        #Do some checks
        #print("Format:", imageObject.format)
        #print("Mode:", imageObject.mode)
        #Get the size and display it
        imageSize.config(text="The Size: " + str(imageObject.size), bg='#9fd27f')
        imageSize.place(x=math.ceil(screen_width*.82), y=math.ceil(screen_height*.82))
        #Get frames (and frame duration) of GIF
        frames = len(MakeOutput)
        #Scale the preview image
        newsize = imageObject.size
        while newsize > (math.ceil(screen_width*.3), math.ceil(screen_height*.2)):
            newsize = (math.ceil(int(newsize[0]/2)),math.ceil(int(newsize[1]/2)))
        resized = imageObject.resize(newsize, Image.Resampling.LANCZOS)
        if MakeOutput != ".gif" or None:
            #Show preview
            my_img = ImageTk.PhotoImage(resized)
            imageLabel.config(image=my_img)
            imageLabel.image_ref = my_img
            imageLabel.place(x=math.ceil(screen_width*.8-(my_img.width()/2)), y=math.ceil(screen_height*.55-(my_img.height()/2)))
        else:
            my_img = ErrorPNG
            imageLabel.config(image=my_img)
            imageLabel.image_ref = my_img
            imageLabel.place(x=math.ceil(screen_width*.8-(my_img.width()/2)), y=math.ceil(screen_height*.55-(my_img.height()/2)))
        imageSize.lift()
        #Show the image submit button, which will look the same as the video version for the sake of confusing people on purpose.
        button_Submit = Button(root, image=SubmitButton, command=lambda: view_gif(button_Submit), borderwidth=0, highlightthickness=0)
        button_Submit.place(x=math.ceil(screen_width/2-(SubmitButton.width()/2)), y=math.ceil((screen_height*.4)))
    elif imageFileName.lower().endswith(video_extensions):
        # Handle video file
        my_img = VideoPNG
        imageLabel.config(image=my_img)
        imageLabel.image_ref = my_img
        imageLabel.place(x=math.ceil(screen_width*.8-(my_img.width()/2)), y=math.ceil(screen_height*.55-(my_img.height()/2)))
        imageLabel.config(bg="#9fd27f")
        button_Submit = Button(root, image=SubmitButton, command=lambda: view_video(button_Submit), borderwidth=0, highlightthickness=0)
        button_Submit.place(x=math.ceil(screen_width/2-(SubmitButton.width()/2)), y=math.ceil((screen_height*.4)))
    else:
        imageSize.config(text="Unsupported file type, dork.", bg='#9fd27f')
        imageSize.lift()
        return
    return True

def switchPalette():
    global switch
    global chosencolorpalette
    PaletteLabel.place(x=math.ceil(screen_width*.141-(PaletteButton.width()/2)), y=math.ceil((screen_height/2)*.53))
    if switch == 0:
        switch = 1
        chosencolorpalette = [(0,0,0)]
        PaletteLabel.config(image=CustomPalette)
    else:
        switch = 0
        PaletteLabel.config(image=DefaultPalette)

#Filters
def color_palette(image, switch, px, ccp):
    if ccp is None or any(color is None for color in ccp):
        ccp = [(0, 0, 0)]
    pixelate(image, image, px)
    img = Image.open(image)
    img = img.convert("RGBA")
    d = img.getdata()
    new_image = []
    if switch == 0:
        colorpalette = [
        [140, 143, 174],
        [88, 69, 99],
        [62, 33, 55],
        [154, 99, 72],
        [215, 155, 125],
        [245, 237, 186],
        [192, 199, 65],
        [100, 125, 52],
        [228, 148, 58],
        [157, 48, 59],
        [210, 100, 113],
        [112, 55, 127],
        [126, 196, 193],
        [52, 133, 157],
        [23, 67, 75],
        [31, 14, 28]
        #Pink [255, 192, 203]
        #80s simple
        #[70,30,82],
        #[221,81,126],
        #[230,142,53],
        #[85,108,201],
        #[122,152,238]
        ]
    else:
        colorpalette = ccp
    for item in d:
        winningcolor = [255,255,255]
        comparefactor = 1
        for i in colorpalette:
            r = i[0]
            g = i[1]
            b = i[2]
            itemr = item[0]
            itemg = item[1]
            itemb = item[2]
            distance = math.sqrt((itemr-r)**2+(itemg-g)**2+(itemb-b)**2)
            percent = distance/math.sqrt((255)**2+(255)**2+(255)**2)
            if percent <= comparefactor:
                comparefactor = percent
                winningcolor = i
        new_image.append(tuple(winningcolor))
    ################################ ADD SWITCH FOR ALPHA, even though I don't think it's possible for GIFs ##########
    #alpha = img.split()[-1]
    img.putdata(new_image)
    #img.putalpha(alpha)
    img.save(image)
    return

def update_progress_bar(current, total):
    progress = 100 * (current / total)
    progress_bar['value'] = progress
    root.update_idletasks()  # Refresh GUI to reflect progress update

#Video Section
def process_frame(args):
    frame_index, video_filename, output_dir, switch, px, ccp = args
    cap = cv2.VideoCapture(video_filename)
    if cap.isOpened():
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = cap.read()
        if ret:
            frame_path = os.path.join(output_dir, f'keyframe{frame_index}.png')
            if not os.path.exists(frame_path):
                cv2.imwrite(frame_path, frame)
                # Call color_palette for each frame
                color_palette(frame_path, switch, px, ccp)
    cap.release()
def clear_output_dir(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')
def run_create_video_in_thread(switch, PixEffect, button_Submit):
    # Disable the buttons, so that people don't overwhelm their system.
    PixEffect.config(state="disabled")
    button_Submit.config(state="disabled")
    def create_video_and_update_ui():
        CreateVideo(switch)
        # Schedule the UI update to re-enable the button on the main thread
        root.after(0, lambda: PixEffect.config(state="normal"))
        root.after(0, lambda: button_Submit.config(state="normal"))
    # Start the video creation process in a new thread
    thread = threading.Thread(target=create_video_and_update_ui)
    thread.start()
def CreateVideo(switch):
    px = pixelsize.get()
    ccp = chosencolorpalette
    video_filename = MakeOutput 
    Readiness.lower()
    #Progress Bar
    progress_bar['maximum'] = 100  # Set progress bar to 100% maximum
    progress_bar['value'] = 0  # Reset to 0% at start
    progress_bar.place(x=math.ceil(screen_width/2-(TextField.width()/2)), y=math.ceil((screen_height*.162)))
    progress_bar.lift()
    #Check if configuration is the same. If so, retain the frames. This is in case of crashes.
    current_config = load_project_config('project_config.json')
    existing_config = load_project_config('old_project_config.json')
    if current_config != existing_config:
        # Configuration has changed, clear output directory before processing
        #print("Configuration changed, clearing existing frames.")
        clear_output_dir('VideoFramedata')
    #Process
    cap= cv2.VideoCapture(video_filename)
    if not cap.isOpened():
        #print("Error, Cap not open.")
        return
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()
    output_dir = 'VideoFramedata'
    os.makedirs(output_dir, exist_ok=True)
    # Prepare arguments for each frame to be processed
    frame_args = [(i, video_filename, output_dir, switch, px, ccp) for i in range(total_frames)]
    # Use multiprocessing to process frames
    with Pool(cpu_count()) as pool:
        for i, _ in enumerate(pool.imap_unordered(process_frame, frame_args), 1):
            update_progress_bar(i, total_frames)
    # Compile processed frames back into a video
    compile_frames_to_video(output_dir, 'VideoFramedata/All_PixMixed.avi', fps)
    # Save new config
    save_project_config('old_project_config.json', current_config)
    # Clear progress bar from screen and show where the file is.
    root.after(0, progress_bar.place_forget)
    Readiness.lift()
    Readiness.config(text="Find Filtered Video in VideoFramedata folder.")
    Readiness.place(x=math.ceil((screen_width*.48)-(SubmitButton.width()/2)), y=math.ceil((screen_height*.16)))
def compile_frames_to_video(output_dir, output_video_path, fps):
    filelist = glob.glob(os.path.join(output_dir, 'keyframe*.png'))
    filelist.sort(key=lambda f: int(''.join(filter(str.isdigit, os.path.basename(f))))) 
    if not filelist:
        #print("No frames found for compilation.")
        return
    first_frame = cv2.imread(filelist[0])
    height, width, _ = first_frame.shape
    size = (width, height)
    out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for filename in filelist:
        img = cv2.imread(filename)
        out.write(img)
    out.release()
# Save changes to reduce redundancy.
def save_project_config(file_path, config):
    with open(file_path, 'w') as f:
        json.dump(config, f, indent=4)
def load_project_config(config_path):
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        #print("JSON file is empty or corrupted. Returning default configuration.")
        return {}
def compare_and_save_config(new_config):
    existing_config = load_project_config('project_config.json')
    if new_config != existing_config:
        save_project_config('project_config.json', new_config)
def view_video(button_Submit):
    current_config = {
        'video_filename': MakeOutput,  # The path to the current video
        'pixel_size': pixelsize.get(),  # The value from a Tkinter Scale/Entry widget
        'color_palette': chosencolorpalette,  # The selected color palette
        'switch': switch
    }
    # Compare the current configuration with the existing one and save if there are changes
    compare_and_save_config(current_config)
    # Ensure the output directory exists
    if not os.path.exists('./VideoFramedata/'):
        os.makedirs('./VideoFramedata/')
    # Setup the button to initiate video processing
    PixEffect = Button(root, image=PixelizeButton, command=lambda: run_create_video_in_thread(switch, PixEffect, button_Submit), borderwidth=0, highlightthickness=0)
    PixEffect.place(x=math.ceil(screen_width/2-(PixelizeButton.width()/2)), y=math.ceil((screen_height*.5)))

#Get GIF, turn into PNGs and then become GIF again!
def process_frame_images(frame_data):
    frame_index, gif_path, output_dir, switch, px, ccp = frame_data
    im = Image.open(gif_path)
    im.seek(frame_index)
    frame_path = f"{output_dir}/frames{frame_index}.PNG"
    im.save(frame_path)
    color_palette(frame_path, switch, px, ccp)  
def PNG_list():
    px = pixelsize.get()
    ccp = chosencolorpalette
    Readiness.lower()
    output_dir = "Framedata"
    os.makedirs(output_dir, exist_ok=True)
    gif_path = MakeOutput
    im = Image.open(gif_path)
    frames = im.n_frames if hasattr(im, 'is_animated') and im.is_animated else 1
    metadata = [im.info.get('duration', 0) for i in range(frames)]  # Preserving metadata for each frame
    # Prepare data for multiprocessing
    frame_data = [(i, gif_path, output_dir, switch, px, ccp) for i in range(frames)]
    # Progress Bar
    progress_bar['value'] = 0
    progress_bar['maximum'] = 100
    progress_bar.place(x=math.ceil(screen_width/2-(TextField.width()/2)), y=math.ceil((screen_height*.162)))
    # Use multiprocessing to process frames
    with Pool(cpu_count()) as pool:
        for i, _ in enumerate(pool.imap_unordered(process_frame_images, frame_data), 1):
            update_progress_bar(i, frames)
    # Reassemble the processed frames into a GIF
    PNGs = [Image.open(f"{output_dir}/frames{i}.PNG") for i in range(frames)]
    PNGs[0].save(f'{output_dir}/All_PixMixed.gif', format="GIF", append_images=PNGs[1:], save_all=True, duration=metadata, loop=0)
    # Update the Tkinter GUI to notify the user
    root.after(0, progress_bar.place_forget)
    Readiness.lift()
    Readiness.config(text="Find Filtered Gif in Framedata folder.")
    Readiness.place(x=math.ceil((screen_width*.5)-(SubmitButton.width()/2)), y=math.ceil((screen_height*.16)))
def run_PNG_list_in_thread(PixEffect, button_Submit):
    # Disable the buttons, so users don't overwhelm their system.
    button_Submit.config(state='disabled')
    PixEffect.config(state="disabled")
    def create_gif_and_update_ui():
        PNG_list()
        # Schedule the UI update to re-enable the buttons on the main thread
        root.after(0, lambda: PixEffect.config(state="normal"))
        root.after(0, lambda: button_Submit.config(state="normal"))
    # Start the video creation process in a new thread
    thread = threading.Thread(target=create_gif_and_update_ui)
    thread.start()
# Admittedly, this button is just here because the art was already done.
def view_gif(button_Submit):
    PixEffect = Button(root, image=PixelizeButton, command=lambda: run_PNG_list_in_thread(PixEffect, button_Submit), borderwidth=0, highlightthickness=0)
    PixEffect.place(x=math.ceil(screen_width/2-(PixelizeButton.width()/2)), y=math.ceil((screen_height*.5)))

#######To Do List########
#Allow Alpha in images/videos that support it.
#Increase Custom Palette size from 16 to 21
#########################

if __name__ == "__main__":
    multiprocessing.freeze_support()
    root = Tk()
    root.title('Pix Mix')
    root.geometry("380x200")
    root.configure(background='#95b97f')
    def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory. ' +  directory)
    createFolder('./Framedata/')

    def resource_path(relative_path):
        #Get absolute path to resource, works for dev and for PyInstaller
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    #open images
    icon = (ImageTk.PhotoImage(Image.open(resource_path("icon.ico"))))
    root.wm_iconphoto(False, icon)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    ui_TopButton = Image.open(resource_path("UI_topButton.png"))
    TopButton = ui_TopButton.resize((math.ceil(219*(screen_width/1920)),math.ceil(86*(screen_height/1080))), Image.Resampling.LANCZOS)
    PaletteButton = ImageTk.PhotoImage(TopButton)
    ui_MiddleButton = Image.open(resource_path("UI_middleButton.png"))
    MiddleButton = ui_MiddleButton.resize((math.ceil(220*(screen_width/1920)),math.ceil(85*(screen_height/1080))), Image.Resampling.LANCZOS)
    SubmitButton = ImageTk.PhotoImage(MiddleButton)
    ui_BottomButton = Image.open(resource_path("UI_bottomButton.png"))
    BottomButton = ui_BottomButton.resize((math.ceil(230*(screen_width/1920)),math.ceil(82*(screen_height/1080))), Image.Resampling.LANCZOS)
    PixelizeButton = ImageTk.PhotoImage(BottomButton)
    ui_temp_adjacentButton = ImageTk.PhotoImage(Image.open(resource_path("UI_entryButton_starter.png")))
    ui_AdjacentButton = Image.open(resource_path("UI_entryButton.png"))
    AdjacentButton = ui_AdjacentButton.resize((math.ceil(216*(screen_width/1920)),math.ceil(60*(screen_height/1080))), Image.Resampling.LANCZOS)
    EntryButton = ImageTk.PhotoImage(AdjacentButton)
    ui_temp_enterText = ImageTk.PhotoImage(Image.open(resource_path("UI_enterText_starter.png")))
    ui_TextEntry = Image.open(resource_path("UI_enterText.png"))
    TextEntry = ui_TextEntry.resize((math.ceil(594*(screen_width/1920)),math.ceil(60*(screen_height/1080))), Image.Resampling.LANCZOS)
    TextField = ImageTk.PhotoImage(TextEntry)
    ui_Background = Image.open(resource_path("UI_background.png"))
    resized_Background = ui_Background.resize(((screen_width), math.ceil(screen_height - (screen_height*.1))), Image.Resampling.LANCZOS)
    BackgroundImage = ImageTk.PhotoImage(resized_Background)
    ui_defaultPalette = Image.open(resource_path("UI_paletteTitle_default.png"))
    ui_customPalette = Image.open(resource_path("UI_paletteTitle_custom.png"))
    ui_defaultPalette = ui_defaultPalette.resize((math.ceil(417*(screen_width/1920)),math.ceil(87*(screen_height/1080))), Image.Resampling.LANCZOS)
    ui_customPalette = ui_customPalette.resize((math.ceil(417*(screen_width/1920)),math.ceil(87*(screen_height/1080))), Image.Resampling.LANCZOS)
    DefaultPalette = ImageTk.PhotoImage(ui_defaultPalette)
    CustomPalette = ImageTk.PhotoImage(ui_customPalette)
    ui_ErrorPNG = Image.open(resource_path("Error.png"))
    ui_ErrorPNG = ui_ErrorPNG.resize((math.ceil(screen_width*.25), math.ceil(screen_height*.4)), Image.Resampling.LANCZOS)
    ErrorPNG = ImageTk.PhotoImage(ui_ErrorPNG)
    ui_VideoPNG = Image.open(resource_path("Video.png"))
    ui_VideoPNG = ui_VideoPNG.resize((math.ceil(screen_width*.25), math.ceil(screen_height*.4)), Image.Resampling.LANCZOS)
    VideoPNG = ImageTk.PhotoImage(ui_VideoPNG)

    #Open Program and Get that darn GIF!
    startLabel = Label(root, text="Open the File, and hit Fetch to begin.", bg='#95b97f', wraplength=300, justify="center")
    startLabel.pack(pady=1)
    TextEntry = Label(image=ui_temp_enterText, borderwidth=0, highlightthickness=0)
    TextEntry.place(x=10, y=45)
    imageLabel = Label(root, text="")
    imageSize = Label(root, text="")
    TutorialLabel = Label(root, text='Once you are in, press Submit.\nYou can later press Palette to switch to your colors,\nbut you must hit Submit again to save changes.', bg='#95b97f')
    TutorialLabel.place(x=50, y=150)
    PaletteLabel = Label(image=DefaultPalette, borderwidth=0, highlightthickness=0)
    chosencolorpalette = [(0,0,0)]
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=TextField.width(), mode="determinate")
    Readiness = Label(root, text="", bg='#9fd27f', borderwidth=2, highlightthickness=2)
    switch = 0
    imageFileName = ""

    def GetImageFile():
        global imageFileName
        #While this program supports plenty of file types, I'm going to lead people into using a few, just in case there are unpredictable conflicts.
        root.imageFileNameish = fd.askopenfilename(initialdir="/gui/", title="Select A File", filetypes=(('All Files', '*.*'), ("Gif Files", "*.gif"), ("PNG Files", "*.png"), ("MP4 Files", "*.mp4")))
        startLabel.config(text=root.imageFileNameish[:100])
        imageFileName = root.imageFileNameish

    #Main Button
    Fetch_button = Button(root, image=ui_temp_adjacentButton, command=onPrint, borderwidth=0, highlightthickness=0)
    Fetch_button.place(x=120, y=110)
    imageFileName_button = Button(root, text='Open Visual', bg='#9fd27f', command=GetImageFile)
    imageFileName_button.place(x=150, y=63)

    root.mainloop()

