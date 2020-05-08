from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from math import ceil, sqrt

Window.system_size = [500,600]
Window.clearcolor = (.83,.5,.5, .5)
LabelBase.register(name='Got',
                   fn_regular='BenguiatGothicC_Bold.ttf')


class Lab4App(App):
    def build(self):
        def is_square(x):
            return (int(x ** 0.5)) ** 2 == x

        def is_prime(n):
            if n == 1:
                return True
            a = 2
            while n % a != 0:
                a += 1
            return a == n

        def check_n(n):
            if n < 0:
                txt_prime.text = 'Введене число від\'ємне.'
                return True
            if is_prime(n):
                txt_prime.text = 'Введене число є простим.'
                return True
            if n % 2 == 0:
                txt_prime.text = 'Число має бути непарне.'
                return True

        def ferma_factorize(n):
            if is_square(n):
                return int(n ** 0.5), int(n ** 0.5)
            a = int(n ** 0.5) + 1
            c = 0
            while not is_square(a * a - n):
                a += 1
                c += 1
            b = int((a * a - n) ** 0.5)
            p, q = a - b, a + b
            return p, q

        def get_factors(n, prime_factors):
            p, q = ferma_factorize(n)
            if is_prime(p):
                prime_factors.append(p)
            else:
                if not check_n(p):
                    get_factors(p, prime_factors)
            if is_prime(q):
                prime_factors.append(q)
            else:
                if not check_n(q):
                    get_factors(q, prime_factors)
            return prime_factors

        txt_field = TextInput(text='', input_filter='int', multiline=False)

        def calculate(instance):
            result.text = ''
            try:
                n = int(txt_field.text)
                if check_n(n):
                    return
                txt_prime.text = 'Прості множники:'
                prime_factors = []
                prime_factors = get_factors(n, prime_factors)
                for i in range(len(prime_factors)):
                    prime_factors[i] = str(prime_factors[i])
                result.text = ', '.join(prime_factors)
            except:
                txt_prime.text = 'Неправильний ввід.'
            
        bl = BoxLayout(orientation='vertical', padding = 20)
        bl.add_widget(Label(text='Павлюк Олексій',
                            font_size=15, size_hint_y = .4,
                            font_name='Got',
                            bold='True', outline_width=2, outline_color=[0,0,0]))
        bl.add_widget(Label(text='ІO-72',
                            font_size=15, size_hint_y = .4,
                            bold='True', outline_width=2, outline_color=[0,0,0]))
        grd = GridLayout(cols = 1, size_hint = [.5,.6], spacing = 15)
        grd.add_widget(txt_field)
        al = AnchorLayout(anchor_x = 'center')
        grd.add_widget(Button(text='Факторизувати', font_name='Got',
                             background_color=[.4,.12, .12, .65],
                             background_normal='',
                             on_press=calculate))
        al.add_widget(grd)
        bl.add_widget(al)
        txt_prime = Label(text='',
                        font_size=15, size_hint_y = .4,
                        bold='True', outline_width=2, outline_color=[0,0,0])
        result = Label(text='',
                        font_size=15, size_hint_y = .4,
                        bold='True', outline_width=2, outline_color=[0,0,0])                
        bl.add_widget(txt_prime)
        bl.add_widget(result)

        return bl

if __name__ == "__main__":
    Lab4App().run()