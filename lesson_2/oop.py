

class Phone:

    mobile_type = 'Common Phone'

    def __init__(self, model, imei):
        self._model = model
        self._imei = imei

    def call(self, to):
        self._connect_to_another_device(to)
        print(f'Okey, i am calling {to} from {self._model}')

    def _connect_to_another_device(self, to):
        print('Some connection magic')

    def get_model(self):
        return self._model

    def set_model(self, value):
        self._model = value

    def get_imei(self):
        return self._imei

    def set_imei(self, value):
        self._imei = value


class MobilePhone(Phone):

    def send_message(self, message_text, to):
        print(f' sending message {message_text} to {to}')

class Application:

    def __init__(self, name, marketplace):
        self._name = name
        self._marketplace = marketplace
        self._downloaded = False

    def start(self):
        if self._downloaded:
            print(f'Starting the {self._name} application ')

    def download(self):
        print(f'Downloading {self._name} from {self._marketplace}')
        self._downloaded = True

#Aggregation
class SmartPhone(MobilePhone):
    """
    Ассоциация - вытекающая из насследования особенность которая
    гласит, что аттрибутами объекта могут быть объекты других классов
    Композиция - объект создается внутри класса, и далее обрабатывается средставми класса
    Аггрегация - объект создается ВНЕ класса, передается Объекту класса, и далее обрабатывается средставми класса
    """
    def play_audio(self):
        print("Playing audio")

    def play_video(self):
        print("Playing video")

    # def download_application(self, app_name, market_place):
    #     app = Application(app_name, market_place)
    #     app.download()
    #     self._app = app


    #Waiting for object type Application
    def start_application(self, application_object):
        application_object.start()

#Composition
class SmartPhone1(MobilePhone):

    def play_audio(self):
        print("Playing audio")

    def play_video(self):
        print("Playing video")

    def download_application(self, app_name, market_place):
        app = Application(app_name, market_place)
        app.download()
        self._app = app

    # starting app object that already created
    def start_application(self):
        self._app.start()


class SatelitePhone(Phone):

    def call(self, satelite_coordinates, to):
        print(f'Caliing {to} from {self.get_model()} satelite: {satelite_coordinates}')

smartphone = SmartPhone('Apple', '77777777')
app = Application('Player', 'PlayMarket')
app.download()
smartphone.start_application(app)

# smartphone.download_application('Player', 'PlayMarket')
# smartphone.start_application()
# mobile_phone = MobilePhone('model', 'PPPZZZCCC')
# mobile_phone.send_message('Good evening!','+38094212312')
# print(mobile_phone.get_model())
#
# satelite_phone = SatelitePhone('saturn', '+380942132312')
# satelite_phone.call('60.5/23.5', '+380942132312')

# phone = Phone('Nokia', '12312312')
# print(phone._imei)
# phone.call()

# print(Phone.mobile_type)
# Phone.mobile_type = "Tablet"
# phone = Phone('Nokia', 'EZ12345678')
# phone.call("+38095791234")
# phone.imei = "QWE"
#
# phone.phone_number = "+38094782134"
#
# print(phone.phone_number)
# print(phone.imei)
#
#
# phone2 = Phone('Siemens', 'EZXC12345')
# phone2.call('+38094512312312')
# print(phone2.imei)
#
# phone.mobile_type = "SMARTPHONE"
#
# print(Phone.mobile_type)
# print(phone.mobile_type)


class Cat:

    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def __add__(self, other):
        return Cat(self._name + other._name,
                   self._weight + other._weight)



print(Cat.__bases__)
cat1 = Cat('kitty', 3)
cat2 = Cat('cat', 4)

cat3 = cat1 + cat2 + cat2

a = 0

print(cat3._name, cat3._weight)