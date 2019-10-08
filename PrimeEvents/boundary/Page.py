class Page:
    """
    This class help to build user interface.
    An object of this class can be printed as a user friendly page

    title: the title of the page
    content: a list of any object
    options: the options for user to choose which is a dict: (str : str) pairs.
    wide: the number of characters of the page
    """
    def __init__(self, title='Unknown', contents=[], options=dict()):
        self.pageTitle = title
        self.contents = contents
        self.options = options
        self.wide = 50

    def __str__(self):
        return self.generateTitleLine() + self.generateBodyLine() + self.generateBottonLine()

    def generateTitleLine(self):
        titleLength = len(self.pageTitle)
        if ((self.wide - 2) - titleLength) % 2 == 0:
            return '+' + '-' * (((self.wide - 2) - titleLength) // 2) \
                   + self.pageTitle + '-' * (((self.wide - 2) - titleLength) // 2) + '+\n'
        else:
            return '+' + '-' * (((self.wide - 2) - titleLength) // 2) \
                   + self.pageTitle + '-' * (((self.wide - 2) - titleLength) // 2 + 1) + '+\n'

    def generateBodyLine(self):
        result = ''
        for content in self.contents:
            lines = content.__str__().split('\n')
            for line in lines:
                lineLength = len(line)
                result = result + '|' + line + ' ' * (self.wide - 2 - lineLength) + '|\n'
            result += '|' + '-' * (self.wide - 2) + '|\n'
        result += '|' + ' ' * (self.wide - 2) + '|\n'
        for option in self.options:
            toPrint = 'Press ' + option + ' to ' + self.options[option]
            optionLength = len(toPrint)
            result = result + '|' + toPrint + ' ' * (self.wide - 2 - optionLength) + '|\n'
        return result

    def generateBottonLine(self):
        return '+' + '-'*48 + '+'

    def setTitle(self, title):
        self.pageTitle = title

    def setContents(self, alist):
        self.contents = list(alist)

    def setOptions(self, adict):
        self.options = dict(adict)

    def getTitle(self):
        return self.pageTitle

    def getContents(self):
        return self.contents

    def getOptions(self):
        return self.options

