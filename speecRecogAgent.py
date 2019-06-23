'''
Copyright 2019 Agnese Salutari.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License
'''

import speech_recognition as sr


def listenToMicrophone(language='en-US', listeningTime=5, readyMsg="Ok", confirmMsg="Received",
                       showTextMsg="Text: ", errorMsg="Error"):
    # language is the language used in the speech, language="it-IT" for Italian.
    # listeningTime is the time used for listening, in seconds.
    # readyMsg is the string printed when the system is ready for listening.
    # confirmMsg is the string printed when speech has been recorded.
    # showTextMsg is the string printed when speech text is shown.
    # errorMsg is the string printed when an error occurs.
    assert isinstance(readyMsg, str)
    assert isinstance(confirmMsg, str)
    assert isinstance(showTextMsg, str)
    assert isinstance(errorMsg, str)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print(readyMsg)
        audio = r.listen(source, phrase_time_limit=listeningTime)
        print(confirmMsg)
        try:
            text = r.recognize_google(audio, language=language)  # Internet connection needed
            # text = r.recognize_sphinx(audio)  # Offline recognizer
            print(showTextMsg + text)
            return text
        except Exception as e:
            print(errorMsg)
            return e


def findInText(pieceOfText, text, answer=""):
    # pieceOfText is the string to find.
    # text is the string to analyze.
    # answer is the string printed if pieceOfText has been found inside text.
    if not isinstance(pieceOfText, str):
        pieceOfText = str(pieceOfText)
    if not isinstance(text, str):
        text = str(text)
    if not isinstance(answer, str):
        answer = str(answer)
    if pieceOfText.lower() in text.lower():
        print(answer)
        return True
    return False


def main():
    phraseTime = 3  # Listening time (seconds)
    readyMsg = "I'm listening, you can speak :)"
    confirmMsg = "Message received. I'm processing..."
    showTextMsg = "You told: "
    errorMsg = "Sorry, I didn't understand :("
    while True:
        recordedText = listenToMicrophone( language='en-US', listeningTime=phraseTime,
                                           readyMsg=readyMsg, confirmMsg=confirmMsg,
                                           showTextMsg=showTextMsg, errorMsg=errorMsg)
        findInText(pieceOfText="hello", text=recordedText, answer="Hi there! :)")


if __name__ == '__main__':
    main()
    
