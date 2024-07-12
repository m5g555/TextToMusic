import music


notes = [
    130.813, # C3
    146.832, # D3
    164.814, # E3
    174.614, # F3
    195.998, # G3
    220.000, # A3
    246.942, # B3
    261.626, # C4
    293.665, # D4
    329.628, # E4
    349.228, # F4
    391.995, # G4
    440.000, # A4
    493.883, # B4
    523.251, # C5
    587.330, # D5
]


def __main__():
    soundVector = []
    print("What would you like to convert to music?")
    text = input()
    hexValue = text.encode("utf-8").hex()
    for x in hexValue:
        note = notes[int(x, 16)]
        sound = music.core.synths.note(note, 0.5)
        soundVector.append(sound)
        
    stackedMusic = music.utils.horizontal_stack(*soundVector)
    music.core.io.write_wav_stereo(stackedMusic, text+".wav", 44100)
        
    
    
__main__()