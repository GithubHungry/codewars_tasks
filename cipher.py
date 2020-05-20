"""Vigenère Cipher"""
"""The Vigenère cipher is a method of encrypting 
alphabetic text by using a series of different 
Caesar ciphers based on the letters of a keyword. 
It is a simple form of polyalphabetic substitution."""


class VigenereCipher:
    _alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, key: str, alphabet=_alphabet):
        self.key = key
        self.alphabet = alphabet
        self.alphabet_dict = {}
        self.alphabet_dict_reversed = {}
        self.len_key_counter = len(key)

    def alphabet_dict_gen(self):
        for index, value in enumerate(self.alphabet):
            self.alphabet_dict[index] = value
            self.alphabet_dict_reversed[value] = index

    def key_gen(self, text: str):
        print(text)
        print(self.key)
        if len(self.key) != self.len_key_counter:
            self.key = self.key[:self.len_key_counter]

        if len(self.key) == len(text):
            self.key = self.key
        else:
            for index in range(len(text) - len(self.key)):
                print('index:', index)
                self.key += self.key[index % len(self.key)]

    def transform(self, text: str):
        self.key_gen(text)
        self.alphabet_dict_gen()
        final_list = []
        new_text = []
        for letter in text:
            if letter in self.alphabet_dict_reversed.keys():
                new_text.append(self.alphabet_dict_reversed.get(letter))
            else:
                new_text.append(letter)
        new_key = [self.alphabet_dict_reversed[letter] for letter in self.key if
                   letter in self.alphabet_dict_reversed.keys()]
        for i in range(len(new_text)):
            if type(new_text[i]) != str:
                new_text[i] += new_key[i]
                if new_text[i] >= len(self.alphabet_dict_reversed):
                    new_text[i] -= len(self.alphabet_dict_reversed)
                    final_list.append(new_text[i])
                else:
                    final_list.append(new_text[i])
            else:
                final_list.append(new_text[i])
        return final_list

    def encode(self, text: str):
        encrypted_list = []
        for elem in self.transform(text):
            if type(elem) == str:
                encrypted_list.append(elem)
            else:
                encrypted_list.append(self.alphabet_dict[elem])
        return ''.join(encrypted_list)

    def decode(self, text: str):
        self.alphabet_dict_gen()
        self.key_gen(text)
        digit_text = []
        for letter in text:
            if letter in self.alphabet_dict_reversed.keys():
                digit_text.append(self.alphabet_dict_reversed.get(letter))
            else:
                digit_text.append(letter)
        new_key = [self.alphabet_dict_reversed[letter] for letter in self.key if
                   letter in self.alphabet_dict_reversed.keys()]
        for i in range(len(digit_text)):
            if type(digit_text[i]) != str:
                if new_key[i] > digit_text[i]:
                    digit_text[i] = len(self.alphabet_dict_reversed) + (digit_text[i] - new_key[i])
                else:
                    digit_text[i] -= new_key[i]
            else:
                continue
        print(digit_text)
        for ind in range(len(digit_text)):
            if type(digit_text[ind]) != str:
                digit_text[ind] = self.alphabet_dict.get(digit_text[ind])
            else:
                continue
        return ''.join(digit_text)
