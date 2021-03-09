from pydub import AudioSegment
import numpy as np
from scipy.io import wavfile
from tempfile import mktemp
import matplotlib.pyplot as plt
plt.rcParams['agg.path.chunksize'] = 10000
np.seterr(divide='ignore')


def audio_viz(video_file):
    # Load a video file in mp4 format and extract audio segment
    vid_aud = AudioSegment.from_file(video_file, format="mp4")
    # Setting channel = 1
    # Converting stereo to mono type audio
    vid_aud = vid_aud.set_channels(1)
    # creating a temporary file in wav format
    wav_clip = mktemp('.wav')
    # exporting audio segment in to wav format file
    vid_aud.export(wav_clip, format="wav")
    # Reading .wav audio file
    fs, wav_data = wavfile.read(wav_clip)
    # Parameters of audio file
    print("Array of amplitude length", len(wav_data))
    print("Maximum amplitude", max(wav_data))
    print("Minimum Amplitude", min(wav_data))
    print("Duration of audio in seconds", wav_data.size/fs)
    # Plot of audio file
    time = np.linspace(0, wav_data.shape[0] / fs, wav_data.shape[0])
    plt.title("Audio extracted")
    plt.plot(time, wav_data, label="Amplitude Variations")
    plt.xlabel("Time in seconds")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.show()


audio_viz("sample_com.mp4")
