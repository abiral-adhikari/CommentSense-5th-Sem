import re
from langdetect import detect
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

# function to completely remove the emojis from the comments using re
def removeemoji(text):
    # Define a regular expression pattern to match emojis
    emoji_pattern = re.compile("["
                               "\U0001F600-\U0001F64F"  # Emoticons
                               "\U0001F300-\U0001F5FF"  # Symbols & Pictographs
                               "\U0001F680-\U0001F6FF"  # Transport & Map Symbols
                               "\U0001F700-\U0001F77F"  # Alphabetic Presentation Forms
                               "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                               "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                               "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                               "\U0001FA00-\U0001FA6F"  # Chess Symbols
                               "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                               "\U0001FB00-\U0001FBFF"  # Symbols for Legacy Computing
                               "\U0001FC00-\U0001FCFF"  # Symbols for Legacy Computing
                               "\U0001FD00-\U0001FDFF"  # Symbols for Legacy Computing
                               "\U0001F700-\U0001F77F"  # Alphabetic Presentation Forms
                               "\U0001FE00-\U0001FEFF"  # Variation Selectors
                               "\U0001FF00-\U0001FFFF"  # Variation Selectors
                               "\U0001F200-\U0001F251"
                               "❤"
                               "❤️"
                               "]+", flags=re.UNICODE)

    # Use the sub method to remove emojis
    text_no_emojis = emoji_pattern.sub(r'', text)
    return text_no_emojis


def filter_english_comments(text):
  # we ue re module for multi seperator split
    sentences=re.split(r'[.:]',text)
    englishcomments=[]
    for sentence in sentences:
        try:
            # print(sentence)
            # print(detect(sentence))
            if(detect(sentence)=="en"):
                englishcomments.append(sentence)
        except:
            pass
    filteredcomment='.'.join(englishcomments)
    return filteredcomment

def remove_tags(text):
    TAG_RE = re.compile(r'<[^>]+>')
    '''Removes HTML tags: replaces anything between opening and closing <> with empty space'''
    return TAG_RE.sub('', text)

def preprocessing(text):
    text=str(text)
    # Convert to lowercase
    text=text.lower()

    # Remove html tags
    text= remove_tags(text)

    # Substitute 'n't' with 'not'
    text = re.sub(r"n't", "not",text)
    
    # Remove punctuations and numbers
    text = re.sub('[^a-zA-Z]', ' ',text)

    # Single character removal
    text = re.sub(r"\s+[a-zA-Z]\s+", ' ', text)  # When we remove apostrophe from the word "Mark's", the apostrophe is replaced by an empty space. Hence, we are left with single character "s" that we are removing here.

    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)  # Next, we remove all the single characters and replace it by a space which creates multiple spaces in our text. Finally, we remove the multiple spaces from our text as well.

    # Remove Stopwords
    pattern = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
    text = pattern.sub('', text)

    return text

def clean(text):
    sent=removeemoji(text)
    sent=filter_english_comments(sent)
    sent=preprocessing(text)
    print(sent)
    return sent
    
