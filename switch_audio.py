import numpy as np
import simpleaudio as sa

# calculate note frequencies
A_freq = 440
Csh_freq = A_freq * 2 ** (4 / 12)
E_freq = A_freq * 2 ** (7 / 12)

# get timesteps for each sample, T is note duration in seconds
sample_rate = 44100

T = 5
t = np.linspace(0, T, T * sample_rate, False)

# generate sine wave notes
A_note = np.sin(A_freq * t * 2 * np.pi)
Csh_note = np.sin(Csh_freq * t * 2 * np.pi)
E_note = np.sin(E_freq * t * 2 * np.pi)

# concatenate notes
audio = np.hstack((A_note, Csh_note, E_note))
# normalize to 16-bit range
audio *= 32767 / np.max(np.abs(audio))
# convert to 16-bit data
audio = audio.astype(np.int16)

# start playback
#play_obj = sa.play_buffer(audio, 1, 2, sample_rate)

# wait for playback to finish before exiting
#play_obj.wait_done()
#play_obj.stop()

from pynput.keyboard import Key, Listener

keydown = False
#wo = sa.WaveObject(audio,1,2,sample_rate)
wo = sa.WaveObject.from_wave_file("audio_tracks/Boat_Amie.wav")

def on_press(key):
    global keydown, play_obj
    if keydown == False:
        play_obj = wo.play()
        keydown = True
    print('{0} pressed'.format(key))

def on_release(key):
    global keydown,play_obj
    print('{0} release'.format(key))
    play_obj.stop()
    if key == Key.esc:
        # Stop listener
        return False
    keydown = False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
