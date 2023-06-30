import speech_recognition as sr
import pyautogui

def main():

    r = sr.Recognizer()

    with sr.Microphone() as source: 
        r.adjust_for_ambient_noise(source)  

        print("Please say something")

        audio = r.listen(source)

        print("Recognizing Now .... ")


        # recognize speech using google

        try:
            website = r.recognize_google(audio) #google speech api
            print("You have said: " + website)
            print("Audio Recorded Successfully \n ")

            # open the website in the default browser
            pyautogui.press("win")
            pyautogui.press("enter")
            pyautogui.write(website )
            pyautogui.press("enter")

        except Exception as e:
            print("Error :  " + str(e))


if __name__ == "__main__":
    main()