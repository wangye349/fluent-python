import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:


    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    # this method can be replaced by __iter__()
    # def __getitem__(self, index):
    #     return self.words[index]

    # this iterator class can be replaced by generator
    # which is used by most python programmers
    # def __iter__(self):
    #     return SentenceIterator(self.words)

    def __iter__(self):
        for word in self.words:
            yield word
        return                  # this is not necessary,since yield
                                # wouldn't return StopIteration eventually

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

class SentenceIterator:

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

    def __iter__(self):
        return self

# simplest way
class Sentence_lazy:

    def __init__(self,text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        # for match in RE_WORD.finditer(self.text):
        #     yield match.group()
        # easy way to do the things
        return (match.group() for match in RE_WORD.finditer(self.text))

s = Sentence_lazy('"The time has come," the Walrus said,')
for word in s:
    print(word)
a = list(s)
b = iter(s)
pass


# different types of generator
import itertools

generator_one = itertools.takewhile(lambda x: x < 5, itertools.count(1, .5))
generator_one_list = list(generator_one)


# yield from
def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i

def chain_improvement(*iterables):
    for it in iterables:
        yield from it

pass
