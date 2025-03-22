import speech_recognition as sr

r = sr.Recognizer()
def speech():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        return("creo que dijiste" + r.recognize_google(audio, language = "es-ES"))
    except sr.UnknownValueError:
        return("¿que dijiste? no entendi")
    except sr.RequestError as e:
        return("repite en otra vez no escuche; {0}".format(e))

    