from bs4 import BeautifulSoup
import urllib
import nltk
import re
from pprint import pprint
import csv
from collections import OrderedDict
import pandas as pd
import numpy as np
import unicodedata

# given a soup, this function pulls out text from the following sections:
# Background, Season [1-5]
def return_character_dictionary(soup, char, char_dict):
    p=re.compile("Background$")

    # extracts the paragraphs for background, season 1, ...

    # get background separately "Background"
    for section in soup.findAll('span', text=re.compile("Background$")):
        # fix up the section text name
        nextNode = section
        text_tmp = ''
        foundTextFlag = False
        while True:
            if nextNode is None:
                break # ??

            nextNode = nextNode.next
            if foundTextFlag == True and \
            (nextNode is None or nextNode.name == 'h3' or nextNode.name == 'h2'):
                # check if this is a new section
                # if it is, we are done, and we should break
                #print('Done! Here is the text for {}:').format(section.text)
                #print(text_tmp)
                #print('*** end text ***')

                # process the text, removing any references
                # p is a compiled regex
                # s is a string
                # s = p.sub(process_match, s)

                p = re.compile('\[\d+\]')
                text_tmp = p.sub('', text_tmp) # removes references
                p = re.compile(u'\n')
                text_tmp = p.sub(' ', text_tmp) # removes newlines
                char_dict['Background'][char] = text_tmp.replace(u'\xa0', u' ')
                break

            if nextNode is not None and nextNode.name == 'p':
                # found the text, now loop through until we find the next section
                text_tmp += ' ' + nextNode.text
                foundTextFlag = True
            else:
                continue

    p=re.compile("Season [1-5]$")

    for section in soup.findAll('span', text=p):
        section_text = p.findall(section.text)
        if len(section_text) == 1:
            section_text = section_text[0]
        else:
            section_text = section.text

        nextNode = section
        text_tmp = ''
        foundTextFlag = False
        while True:
            nextNode = nextNode.next
            if nextNode is None:
                break # ??

            if foundTextFlag == True and \
            (nextNode.name == 'h3' or nextNode.name == 'h2'):
                # check if this is a new section
                # if it is, we are done, and we should break
                #print('Done! Here is the text for {}:').format(section.text)
                #print(text_tmp)
                #print('*** end text ***')

                # process the text, removing any references
                p = re.compile('\[\d+\]')
                text_tmp = p.sub('', text_tmp)
                if section.text in char_dict.keys():
                    char_dict[section_text][char] = text_tmp.replace('\n', '').replace(u'\xa0', u' ')

                break

            if nextNode is not None and nextNode.name == 'p':
                # found the text, now loop through until we find the next section
                text_tmp += ' ' + nextNode.text
                foundTextFlag = True
            else:
                continue

    return char_dict
