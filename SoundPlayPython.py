from tkinter import *
import pygame , os
from tkinter import filedialog


window = Tk()
window.title("MusicPlayer")
window.geometry("1000x400+400+200")

# Initialze Pygame Mixer
pygame.mixer.init()

#Create Playlist Box
song_box = Listbox(window, bg="pink", fg="black", width=60, selectbackground="orange", selectforeground="black")
song_box.pack(pady=20)

#ADD song function
def add_song():
    song = filedialog.askopenfilename(initialdir='/home/user/Downloads/Amapiano/', title="Choose A Song",filetypes=(("mp3 Files", "*.wav"), ))

    #strip out the directory info and .mp3 extension from the song name
    song = song.replace("/home/user/Downloads/Amapiano/", "")
    song = song.replace(".mp3", "")

    #Add song to listbox
    song_box.insert(END, song)

#Add Many Songs to playlist
def add_many_songs():
    song = filedialog.askopenfilename(initialdir='Amapiano/', title="Choose A Song",filetypes=(("mp3 Files", "*.wav"), ))

#Loop in the song list and replace directory info and mp3
    for song in song:
        song = song.replace("/home/user/Downloads/Amapiano/", "")
        song = song.replace(".mp3", "")
        #Insert into playlist
        song_box.insert(END, song)


#Play Function
def play():
    song = song_box.get(ACTIVE)
    song = f'/home/user/Downloads/Amapiano/{song}'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

#Stop Function
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)


#Create  Global Pause Variable

global paused
paused = False

#Pause Function
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        # Unpause
        pygame.mixer.music.unpause()
        paused = False

    else:
        #pause
       pygame.mixer.music.pause()
       paused = True

#Fast forward Function
def next_song():

    next_one = song_box.curselection()
    next_one = next_one[0]+1
    song = song_box.get(next_one)

    song = f'/home/user/Downloads/Amapiano/{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0, END)

    song_box.activate(next_one)

#Previous song Function
def previous_song():
    back_one = song_box.curselection()
    back_one = back_one[0] - 1
    song = song_box.get(back_one)

    song = f'/home/user/Downloads/Amapiano/{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0, END)

    song_box.activate(back_one)






#Create Player Control Buttons
back_button_icon = PhotoImage(file='/home/user/Downloads/Player Music/rewind.png')
forward_button_icon = PhotoImage(file='/home/user/Downloads/Player Music/fast-forward.png')
play_button_icon = PhotoImage(file='/home/user/Downloads/Player Music/play 1.png')
stop_button_icon = PhotoImage(file='/home/user/Downloads/Player Music/stop .png')
pause_button_icon = PhotoImage(file='/home/user/Downloads/Player Music/pause1 .png')

#Create Player Control Frame
controls_frame = Frame(window)
controls_frame.pack()

#Create Player Control Buttons

back_button = Button(controls_frame, image=back_button_icon, borderwidth=2,command=previous_song)
forward_button = Button(controls_frame, image=forward_button_icon, borderwidth=2,command=next_song)
play_button = Button(controls_frame, image=play_button_icon, borderwidth=2, command=play)
stop_button = Button(controls_frame, image=stop_button_icon, borderwidth=2, command=stop)
pause_button = Button(controls_frame,image=pause_button_icon,borderwidth=2, command=lambda: pause(paused))

back_button.grid(row=0, column=0, padx=10)
pause_button.grid(row=0, column=1, padx=10)
forward_button.grid(row=0, column=2, padx=10)
play_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

#Create Menu
my_menu = Menu(window)
window.config(menu=my_menu)

#Add Add Song Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)

#Add Many Songs to playlist
add_song_menu.add_command(label="Add Many Song To Playlist", command=add_song)

window.mainloop()


