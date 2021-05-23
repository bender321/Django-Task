from urllib import error, request
import xml.etree.ElementTree as ET
import re


class IcoValidator(object):
    '''
    Takes care about validation of ICO number format and if it is legit.
    ICO number can be specified during creation of object or you can use provided method set_data() for later usage.
    For the validation itself use provided method validate_ico().
    '''

    def __init__(self, ico=None):
        self.ico = ico
        self.url = 'https://wwwinfo.mfcr.cz/cgi-bin/ares/darv_std.cgi?ico='

    def set_data(self, ico):
        '''
        Method for setting up ico parameter.

        :param ico: Ico number
        :return: None
        '''
        self.ico = ico

    def validate_ico(self):
        '''
        Takes care of validation of given ICO and returns code as result of validation process.

        :return: Code: 0->OK, 1->non exist, 2->wrong format, 3->url error
        '''

        if self.ico.isdecimal() and len(str(self.ico)) == 8:
            self.url = self.url + str(self.ico)

            try:
                self.response = request.urlopen(self.url).read()
            except error.URLError:
                return 3
            else:
                self.tree = ET.fromstring(self.response)

            if self.tree[0][0].text != "0":
                return 0
            else:
                return 1
        else:
            return 2

class MailValidator(object):
    '''
    Takes care of validation of email adress format.
    Email adress can be specified during creation of object or you can use provided method set_data() for later usage.
    For the validation itself use provided method validate_mail().
    '''

    def __init__(self, email):
        self.__regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        self.email = email

    def set_data(self, email):
        '''
        Method for setting up ico parameter.

        :param email: email adress
        :return: None
        '''
        self.email = email

    def validate_mail(self):
        '''
        Takes care of validation of given email adress and returns code as result of validation process.

        :return: Code: 0->OK, 1->wrong format
        '''

        if re.search(self.__regex, self.email):
            return 0
        else:
            return 1

#test =IcoValidator()
#test.set_data('28650301')
#print(test.validate_ico())

