import gradio as gr
import nltk
from googletrans import Translator
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

def translate_eng_to_hindi(text):
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='hi')
    return translated_text.text

def translated_words(text):
    words = word_tokenize(text)
    pos_tags = pos_tag(words)
    translated_nouns = {}

    for word, tag in pos_tags:
        if tag == "NN" or tag == "NNS" or tag == "VB" or tag == "NNP":
            translated_noun = translate_eng_to_hindi(word)
            translated_nouns[translated_noun] = word
    return translated_nouns

def hinglish_translation(input_text):
    hindi = translate_eng_to_hindi(input_text)
    nouns = translated_words(input_text)

    strings = word_tokenize(hindi)

    modified_words = []

    for string in strings:
        if string in nouns:
            modified_words.append(nouns[string])
        else:
            modified_words.append(string)

    hinglish = " ".join(modified_words)
    return hinglish

iface = gr.Interface(
    fn=hinglish_translation,
    inputs=gr.Textbox(label="Enter text to translate to Hinglish:"),
    outputs=gr.Textbox(label="Hinglish translation:"),
    theme="default",
    title="HINGLISH TRANSLATOR",
    description="Translate English text to Hinglish.",
)

iface.launch()
