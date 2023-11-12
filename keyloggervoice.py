import speech_recognition as sr
import discord


def voice_logger():
	recognizer = sr.Recognizer()


	with sr.Microphone() as source:
		print("aguardado")
		recognizer.adjust_for_ambient_noise(source, duration=1)
		while True:
			audio = recognizer.listen(source, timeout=35)
			try:
				text = recognizer.recognize_google(audio, language="pt-BR")
				print(text)
			
			except sr.UnknownValueError:
				print("n foi possivel te ouvir")
			except sr.RequesrError as e:
				print("gay")


if __name__ == "__main__":
	voice_logger()
