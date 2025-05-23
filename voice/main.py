import tkinter as tk
from gtts import gTTS
import pyaudio
import wave
import threading

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech App")

        self.text = ""
        self.text_entry = tk.Text(self.root, wrap=tk.WORD)
        self.text_entry.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.complete_button = tk.Button(self.root, text="Завершить ввод", command=self.complete_input)
        self.complete_button.pack(pady=10)

        self.generate_button = tk.Button(self.root, text="Создать аудио", command=self.generate_audio)
        self.generate_button.pack(pady=5)

        self.play_button = tk.Button(self.root, text="Воспроизвести аудио", command=self.play_audio)
        self.play_button.pack(pady=5)

    def complete_input(self):
        self.text = self.text_entry.get("1.0", "end-1c")

    def generate_audio(self):
        if self.text:
            tts = gTTS(self.text, lang='en', slow=False)
            tts.save("output.wav")

    def play_audio(self):
        if self.text:
            threading.Thread(target=self.play_audio_thread).start()

    def play_audio_thread(self):
        chunk = 1024
        wf = wave.open("output.wav", 'rb')
        p = pyaudio.PyAudio()

        stream = p.open(
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True
        )

        data = wf.readframes(chunk)

        while data:
            stream.write(data)
            data = wf.readframes(chunk)

        stream.close()
        p.terminate()

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
