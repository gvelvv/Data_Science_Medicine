# def print_human_name(human):
#     print(human['name'])
# h1 = {'name': 'Anast'}
# h2 = {'name': 'Alena'}
# print_human_name(h1)
# print_human_name(h2)
# h3 = {'full_name': 'Karina'}
# print_human_name(h3)
class Phone:
    def __init__(self, model):
        # print(model, 'Object created')
        self.phone_model = model
        self._loading()
        self._id = 26256
    def call(self, tel):
        print('calling')
    def _loading(self):
        print(f'{self.phone_model} loading...')
    def get_id(self):
        return self._id

# my_phone = Phone('Nokia 1')
# my_phone.__loading() #obj._ClassName__foo()
# my_phone._Phone__loading()
# print(my_phone.get_id())
# print(my_phone.phone_model)
# my_phone1 = Phone()
# my_phone.call()
# my_phone1.call()
class SmartPhone(Phone):
    def sms(self):
        print('smsing')
# sphone = SmartPhone('nokia6600')
# sphone.call(563)
# sphone.sms()
class IPhone(SmartPhone):

    def __init__(self, model):
        # print(model, 'Object created')
        # self.phone_model = model
        # self._loading()
        # self._id = 26256
        super().__init__(model)
        print('show logo')

    def player(self):
        print('music')

    def sms(self):
        print('imassage')
        super().sms()


# iphone = IPhone('6')
# iphone.player()
# iphone.sms()
# print(iphone.get_id())
# class NextPhone(IPhone):
#     pass
class Player:
    def player_method(self):
        print('player_method')

    def qwe(self):
        print('player_won')

class Navigator:
    def navigator_method(self):
        print('navigator_method')

    def qwe(self):
        print('navigator_won')

class MPhone(Player, Navigator):
    def navigator_method(self):
        print('MPhone_method')

mphone = MPhone()
mphone.navigator_method()
mphone.player_method()
mphone.qwe()

# class Auto:
#     def auto_start(self, param1, param2=None):
#         if param2 is None:
#             print(param1)
#         else:
#             print(param1 + param2)
# a = Auto()
# a.auto_start(10)
# a.auto_start(10, 20)