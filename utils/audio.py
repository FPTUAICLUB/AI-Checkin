from gtts import gTTS
import playsound
import os.path as osp

def play(out_dir, name):
    output = gTTS(name, lang="vi", slow=False)
    out_audio = osp.join(out_dir, f'{name}.mp3')
    output.save(out_audio)
    playsound.playsound(out_audio, True)