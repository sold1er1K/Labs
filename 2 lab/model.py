import xml.sax
from xml.dom import minidom


class PetsHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.name = ""
        self.date = ""
        self.last_visit = ""
        self.vet = ""
        self.diagnosis = ""
        self.list = []
        self.dictionary = {}
        self.index = -1
        self.next_element = "name"

    def startElement(self, tag, attributes):
        self.CurrentData = tag

    def endElement(self, tag):
        if self.CurrentData == "name" and self.next_element == "name":
            self.list.append(self.name)
            self.next_element = "date"
        elif self.CurrentData == "date" and self.next_element == "date":
            self.list.append(self.date)
            self.next_element = "last_visit"
        elif self.CurrentData == "last_visit" and self.next_element == "last_visit":
            self.list.append(self.last_visit)
            self.next_element = "veterinarian"
        elif self.CurrentData == "veterinarian" and self.next_element == "veterinarian":
            self.list.append(self.vet)
            self.next_element = "diagnosis"
        elif self.CurrentData == "diagnosis" and self.next_element == "diagnosis":
            self.list.append(self.diagnosis)
            self.next_element = "name"
        if len(self.list) == 5:
            self.index += 1
            self.dictionary[self.index] = self.list
            self.list = []
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "name":
            self.name = content
        elif self.CurrentData == "date":
            self.date = content
        elif self.CurrentData == "last_visit":
            self.last_visit = content
        elif self.CurrentData == "veterinarian":
            self.vet = content
        elif self.CurrentData == "diagnosis":
            self.diagnosis = content


def Load(fname):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = PetsHandler()
    parser.setContentHandler(Handler)
    parser.parse(fname)
    return Handler.dictionary


class DomWriter:
    def create_xml_file(self, dct, file_name: str):
        domtree = minidom.Document()
        table = domtree.createElement("vet")
        for ind in dct:
            element = domtree.createElement("pet")
            for it in range(5):
                temp_tag = ""
                if it == 0:
                    temp_tag = "name"
                elif it == 1:
                    temp_tag = "date"
                elif it == 2:
                    temp_tag = "last_visit"
                elif it == 3:
                    temp_tag = "veterinarian"
                elif it == 4:
                    temp_tag = "diagnosis"
                tag = domtree.createElement(temp_tag)
                value = domtree.createTextNode(dct[ind][it])
                tag.appendChild(value)
                element.appendChild(tag)
            table.appendChild(element)
        domtree.appendChild(table)
        domtree.writexml(open(file_name + '.xml', 'w'), indent="  ", addindent="  ", newl='\n', encoding="WINDOWS-1251")
        domtree.unlink()


table = []
dctnry = {}


class Model:
    def __init__( self ):
        self.dctnry = {}
        self.filename = ''
        self.buffer = None

    def get_data(self):
        return self.dctnry

    def set_filename(self, name):
        self.filename = name

    def save_to_file(self, file_name):
        writer = DomWriter()
        writer.create_xml_file(self.dctnry, file_name)

    def add(self, input_name, input_date_of_birth, input_date_of_visit, input_veterinarian, input_diagnosis):
        i = len(self.dctnry)
        self.dctnry[i] = [input_name, input_date_of_birth, input_date_of_visit, input_veterinarian,
                          input_diagnosis]

    def load_to_dctnry(self):
        self.dctnry = Load(self.filename)
        table.append(self.dctnry)

    def t_dell(self, textinput):
        text = textinput.text
        k = 0
        for i in range(len(self.dctnry)):
            if self.dctnry[i][4].lower().find(text) != -1:
                del self.dctnry[i]
                k += 1
        new_dctnry = {}
        i = 0
        for key in self.dctnry:
            new_dctnry[i] = [self.dctnry[key][0], self.dctnry[key][1], self.dctnry[key][2], self.dctnry[key][3],
                             self.dctnry[key][4]]
            i += 1
        self.dctnry = new_dctnry.copy()
        return k

    def s_dell(self, textinput, date):
        text = textinput.text
        k = 0
        for i in range(len(self.dctnry)):
            if self.dctnry[i][3].find(text) != -1 and self.dctnry[i][2] == date.text:
                del self.dctnry[i]
                k += 1
        new_dctnry = {}
        i = 0
        for key in self.dctnry:
            new_dctnry[i] = [self.dctnry[key][0], self.dctnry[key][1], self.dctnry[key][2], self.dctnry[key][3],
                             self.dctnry[key][4]]
            i += 1
        self.dctnry = new_dctnry.copy()
        return k

    def f_dell(self, textinput, date):
        text = textinput.text
        k = 0
        for i in range(len(self.dctnry)):
            if self.dctnry[i][0].find(text) != -1 and self.dctnry[i][1] == date.text:
                del self.dctnry[i]
                k += 1
        new_dctnry = {}
        i = 0
        for key in self.dctnry:
            new_dctnry[i] = [self.dctnry[key][0], self.dctnry[key][1], self.dctnry[key][2], self.dctnry[key][3],
                             self.dctnry[key][4]]
            i += 1
        self.dctnry = new_dctnry.copy()
        return k

    def f_search(self, textinput, date):
        text = textinput.text
        new_dctnry = {}
        k = 0
        for i in range(len(self.dctnry)):
            if self.dctnry[i][0].find(text) != -1 and self.dctnry[i][1] == date.text:
                new_dctnry[k] = [self.dctnry[i][0], self.dctnry[i][1], self.dctnry[i][2], self.dctnry[i][3],
                                 self.dctnry[i][4]]
                k += 1
        return new_dctnry, k

    def s_search(self, textinput, date):
        text = textinput.text
        new_dctnry = {}
        k = 0
        for i in range(len(self.dctnry)):
            if self.dctnry[i][3].find(text) != -1 and self.dctnry[i][2] == date.text:
                new_dctnry[k] = [self.dctnry[i][0], self.dctnry[i][1], self.dctnry[i][2], self.dctnry[i][3],
                                 self.dctnry[i][4]]
                k += 1
        return new_dctnry, k

    def t_search(self, textinput):
        text = textinput.text
        new_dctnry = {}
        k = 0
        for i in range(len(self.dctnry)):
            if self.dctnry[i][4].lower().find(text) != -1:
                new_dctnry[k] = [self.dctnry[i][0], self.dctnry[i][1], self.dctnry[i][2], self.dctnry[i][3], self.dctnry[i][4]]
                k += 1
        return new_dctnry, k

    def spinner_names(self, num):
        lol = []
        for i in range(len(self.dctnry)):
            if self.dctnry[i][num] not in lol:
                lol.append(self.dctnry[i][num])
        return lol
