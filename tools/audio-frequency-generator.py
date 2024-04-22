import numpy as np
import sounddevice as sd
import threading

def generate_sinusoidal_signal(frequency, duration, sampling_rate):
    t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
    signal = np.sin(2 * np.pi * frequency * t)
    return signal

def play_sound(signal, sampling_rate):
    sd.play(signal, samplerate=sampling_rate)
    sd.wait()

def convert_to_seconds(hours, minutes):
    return hours * 3600 + minutes * 60

def main():
    frequency = float(input("Enter the frequency you want to play (in Hz): "))
    hours = int(input("Enter the duration (hours): "))
    minutes = int(input("Enter the duration (minutes): "))
    duration = convert_to_seconds(hours, minutes)
    sampling_rate = 44100  # Standard audio sampling rate

    signal = generate_sinusoidal_signal(frequency, duration, sampling_rate)
    
    # Creating a thread to play the sound
    play_thread = threading.Thread(target=play_sound, args=(signal, sampling_rate))
    play_thread.start()

if __name__ == "__main__":
    main()
