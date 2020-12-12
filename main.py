import secrets
import string
from itertools import *
from math import pi, sin, cos, tan
from decimal import Decimal
from fractions import Fraction


def Fraction_to_dec_str(a, maxlen=4):
    signstr = ""
    if a.numerator < 0:
        signstr = "-"
    num = abs(a.numerator)
    den = a.denominator
    xint = num / den
    num = num % den
    zerosbase = 1
    zeroslen = 0
    while den % 2 == 0 or den % 5 == 0:
        if den % 2 == 0:
            den /= 2
        if den % 5 == 0:
            den /= 5
        zerosbase *= 10
        zeroslen += 1
    ninesbase = 0
    ninesbaselen = 0
    r = zerosbase

    while r % den and ninesbaselen < maxlen:
        ninesbase = ninesbase * 10 + 9
        ninesbaselen += 1
        r = ninesbase * zerosbase
    pstr = ""
    npstr = ""
    if ninesbase > 0:
        x = num * ninesbase * zerosbase / a.denominator
        xnp = x / ninesbase
        xp = x % ninesbase
        tail = ""
        if r % den:
            tail = ".."
        pstr = ("(%0" + str(ninesbaselen) + "d%s)") % (xp, tail)
    else:
        xnp = num * zerosbase / a.denominator
    if zeroslen > 0:
        npstr = ("%0" + str(zeroslen) + "d") % xnp

    s = signstr + "%d" % xint
    if ninesbase > 0 or zeroslen > 0:
        s += "." + npstr + pstr

    return s


one_to_nineteen = (u'ноль',
                   u'один', u'два', u'три', u'четыре', u'пять', u'шесть', u'семь', u'восемь', u'девять',
                   u'десять', u'одиннадцать', u'двенадцать', u'тринадцать', u'четырнадцать', u'пятнадцать',
                   u'шестнадцать', u'семнадцать', u'восемнадцать', u'девятнадцать')

decs = ('', u'десять', u'двадцать', u'тридцать', u'сорок',
        u'пятьдесят', u'шестьдесят', u'семьдесят', u'восемьдесят', u'девяносто')

hundreds = ('', u'сто', u'двести', u'триста', u'четыреста',
            u'пятьсот', u'шестьсот', u'семьсот', u'восемьсот', u'девятьсот')

thousands = ('', u'одна тысяча', u'две тысячи', u'три тысячи', u'четыре тысячи')


def _one_convert(integer):
    return one_to_nineteen[integer]


def _two_convert(integer, string):
    if integer in range(20):
        result = one_to_nineteen[integer]

    else:
        result = decs[int(string[0])]

        if string[1] != '0':
            result = u'%s %s' % (result, one_to_nineteen[int(string[1])])

    return result


def convert(string):
    length = len(string)
    integer = int(string)

    if length == 1:
        result = _one_convert(integer)

    elif length == 2:
        result = _two_convert(integer, string)

    elif length == 3:
        result = hundreds[int(string[0])]

        tail = string[-2:]

        if tail != '00':
            result = u'%s %s' % (result, convert(tail))

    elif length in range(4, 7):
        tail = convert(string[-3:])

        str_head = string[:-3]
        int_head = int(str_head)

        if int_head in range(1, 5):
            head = thousands[int_head]

        else:
            head = u'%s тысяч' % (convert(str_head))

        result = u'%s %s' % (head, tail)

    else:
        result = ''

    return result.strip()


units = {
    "ноль": 0,
    "нуля": 0,
    "ноля": 0,
    'одна': 1,
    "один": 1,
    "одного": 1,
    "два": 2,
    'две': 2,
    'двух': 2,
    'вторая': 2,
    'вторых': 2,
    "три": 3,
    "третьих": 3,
    "третья": 3,
    "трех": 3,
    "четыре": 4,
    "четырех": 4,
    "четвертая": 4,
    "четвертых": 4,
    "пять": 5,
    "пяти": 5,
    "пятых": 5,
    "пятая": 5,
    "шесть": 6,
    "шести": 6,
    "шестых": 6,
    "шестая": 6,
    "семь": 7,
    "семи": 7,
    "седьмых": 7,
    "седьмая": 7,
    "восемь": 8,
    "восеми": 8,
    "восьмая": 8,
    "восьмых": 8,
    "девять": 9,
    "девяти": 9,
    "девятая": 9,
    "девятых": 9,
    "десять": 10,
    "десяти": 10,
    "десятых": 10,
    "десятая": 10,
    "одиннадцать": 11,
    "одиннадцати": 11,
    "одиннадцатая": 11,
    "одиннадцатых": 11,
    "двенадцать": 12,
    "двенадцати": 12,
    "двенадцатых": 12,
    "двенадцатвая": 12,
    "тринадцать": 13,
    "тринадцати": 13,
    "тринадцатых": 13,
    "тринадцатая": 13,
    "четырнадцать": 14,
    "четырнадцати": 14,
    "четырнадцатых": 14,
    "четырнадцатая": 14,
    "пятнадцать": 15,
    "пятнадцати": 15,
    "пятнадцатых": 15,
    "пятнадцатая": 15,
    "шестнадцать": 16,
    "шестнадцати": 16,
    "шестнадцатых": 16,
    "шестнадцатая": 16,
    "семнадцать": 17,
    "семнадцати": 17,
    "семнадцатых": 17,
    "семнадцатая": 17,
    "восемнадцать": 18,
    "восемнадцати": 18,
    "восемнадцатых": 18,
    "восемнадцатая": 18,
    "девятнадцать": 19,
    "девятнадцати": 19,
    "девятнадцатых": 19,
    "девятнадцатая": 19,
    "двадцать": 20,
    "двадцати": 20,
    "двадцатых": 20,
    "двадцатая": 20,
    "тридцать": 30,
    "тридцати": 30,
    "тридцатых": 30,
    "тридцатая": 30,
    "сорок": 40,
    "сорока": 40,
    "сороковых": 40,
    "сороковая": 40,
    "пятьдесят": 50,
    "пятьдесяти": 50,
    "пятьдесятых": 50,
    "пятьдесятая": 50,
    "шестьдесят": 60,
    "шестьдесяти": 60,
    "шестьдесятых": 60,
    "шестьдесятая": 60,
    "семьдесят": 70,
    "семьдесяти": 70,
    "семьдесятых": 70,
    "семьдесятая": 70,
    "восемьдесят": 80,
    "восемьдесяти": 80,
    "восемьдесятых": 80,
    "восемьдесятая": 80,
    "девяносто": 90,
    "девяноста": 90,
    "девяностых": 90,
    "девяностая": 90,
    'сто': 100,
    'ста': 100,
    'двести': 200,
    'двухсот': 200,
    'двухсотых': 200,
    'двухсотая': 200,
    'триста': 300,
    'трехсот': 300,
    'трехсотых': 300,
    'трехсотая': 300,
    'четырехсот': 400,
    'четырехсотых': 400,
    'четырехсотая': 400,
    'четыреста': 400,
    'пятисот': 500,
    'пятисотых': 500,
    'пятисотая': 500,
    'пятьсот': 500,
    'шестисот': 600,
    'шестисотых': 600,
    'шестисотая': 600,
    'шестьсот': 600,
    'семисот': 700,
    'семисотых': 700,
    'семисотая': 700,
    'семьсот': 700,
    'восемисот': 800,
    'восемисотых': 800,
    'восемисотая': 800,
    'восемьсот': 800,
    'девятисот': 900,
    'девятисотых': 900,
    'девятисотая': 900,
    'девятьсот': 900,
}

fractions = (
    'десятых',
    'десятая',
    'сотых',
    'сотая',
    'десятитысячных',
    'десятитысячная',
    'статысячных',
    'статысячная',
    'тысячных',
    'тысячная',
    'миллионных',
    'миллионная'
)


def text2int(textnum):
    textnum = textnum.lower()

    for i in fractions:
        textnum = textnum.replace(i, "")

    num = [0, 0, 0, 0, 0, 0, 0]

    t = textnum.split(" миллион")
    if len(t) != 1:
        num[0] = units[t[0]]

    t = t[-1].split(" тысяч")
    if len(t) != 1:
        buff = t[0].split(" ")
        sot = 0
        for i in buff:
            if i != "":
                sot += units[i]
        step = 100
        index = 1
        while step != 0:
            num[index] = sot // step
            sot = sot % step
            step = int(step / 10)
            index += 1

    buff = t[-1].split(" ")
    sot = 0
    for i in buff:
        if i not in ("", " ", "и", "а"):
            try:
                sot += units[i]
            except:
                raise Exception("no correct number")
    step = 100
    index = 4
    while step != 0:
        num[index] = sot // step
        sot = sot % step
        step = int(step / 10)
        index += 1

    result = 0
    step = 1
    for i in num[::-1]:
        result += i * step
        step *= 10

    return result


def to_num(text: str):
    t = text.split(' и ')
    zn = "-" if text.find("минус") != -1 else "+"

    buff = []
    for i in t:
        buff.append(text2int(i))

    t = text.split(" ")

    if t[-1] == 'десятых' or t[-1] == 'десятая':
        if zn == "-":
            return -(buff[0] + buff[-1] / 10)
        else:
            return buff[0] + buff[-1] / 10
    elif t[-1] == 'сотых' or t[-1] == 'сотая':
        if zn == "-":
            return -(buff[0] + buff[-1] / 100)
        else:
            return buff[0] + buff[-1] / 100
    elif t[-1] == 'тысячных' or t[-1] == 'тысячная':
        if zn == "-":
            return -(buff[0] + buff[-1] / 1000)
        else:
            return buff[0] + buff[-1] / 1000
    elif t[-1] == 'десятитысячных' or t[-1] == 'десятитысячная':
        if zn == "-":
            return -(buff[0] + buff[-1] / 10000)
        else:
            return buff[0] + buff[-1] / 10000
    elif t[-1] == 'статысячных' or t[-1] == 'статысячная':
        if zn == "-":
            return -(buff[0] + buff[-1] / 100000)
        else:
            return buff[0] + buff[-1] / 100000
    elif t[-1] == 'миллионных' or t[-1] == 'миллионная':
        if zn == "-":
            return -(buff[0] + buff[-1] / 1000000)
        else:
            return buff[0] + buff[-1] / 1000000
    else:
        if zn == "-":
            return -(buff[0])
        else:
            return buff[0]


znak = {
    " умножить на ": " * ",
    " умножить на": " * ",
    "умножить на ": " * ",
    "умножить на": " * ",
    " разделить на ": " / ",
    " разделить на": " / ",
    "разделить на ": " / ",
    "разделить на": " / ",
    " плюс ": " + ",
    " плюс": " + ",
    "плюс ": " + ",
    "плюс": " + ",
    " минус ": " - ",
    " минус": " - ",
    "минус ": " - ",
    "минус": " - ",
    " в степени ": " ** ",
    " в степени": " ** ",
    "в степени ": " ** ",
    "в степени": " ** ",
    " скобка открывается ": " ( ",
    "скобка открывается ": " ( ",
    "скобка открывается": " ( ",
    " скобка открывается": " ( ",
    " скобка закрывается ": " ) ",
    " скобка закрывается": " ) ",
    "скобка закрывается": " ) ",
    "скобка закрывается ": " ) ",
    " косинус от ": " cos ",
    " косинус от": " cos ",
    "косинус от ": " cos ",
    "косинус от": " cos ",
    "синус от": " sin ",
    "синус от ": " sin ",
    " синус от": " sin ",
    " синус от ": " sin ",
    "тангенс от": " tan ",
    "тангенс от ": " tan ",
    " тангенс от": " tan ",
    " тангенс от ": " tan ",
    "пи": "pi",
    "пи ": "pi",
    " пи": "pi",
    " пи ": "pi",
}

convert_units = {
    "два": "две",
    "один": "одна"
}

convert_ = {
    "один": "первая",
    "два": "вторых",
    "три": "третьих",
    "четыре": "четвертых",
    "пять": "пятых",
    "шесть": "шестых",
    "семь": "седьмых",
    "восемь": "восьмых",
    "девять": "девятых",
    "десять": "десятых",
    "одиннадцать": "одиннадцатых",
    "двенадцать": "двенадцатых",
    "тринадцать": "тринадцатых",
    "четырнадцать": "четырнадцатых",
    "пятьнадцать": "пятьнадцатых",
    "шестнадцать": "шестнадцатых",
    "семнадцать": "семнадцатых",
    "восемнадцать": "восемнадцатых",
    "девятнадцать": "девятнадцатых",
    "двадцать": "двадцатых",
    "тридцать": "тридцатых",
    "сорок": "сороковых",
    "пятьдесят": "пятидесятых",
    "шестьдесят": "шестидесятых",
    "семьдесят": "семидесятых",
    "восемьдесят": "восемидесятых",
    "девяносто": "девяностых",
}


def num2text(textnum):
    if textnum < 0:
        znak = "минус "
        textnum = str(textnum)[1:]
    else:
        znak = ""

    buff = []
    for i in str(textnum).split("."):
        buff.append(convert(str(i)))

    if len(buff) == 1:
        return znak + buff[0]

    bf = buff[1].split(" ")
    try:
        bf[-1] = convert_units[buff[1].split(" ")[-1]]
    except:
        pass
    text = " и ".join([buff[0], " ".join(bf)])

    if len(str(textnum).split(".")[-1]) == 1:
        if str(textnum)[-1] == "1":
            text += " десятая"
        else:
            text += " десятых"
    elif len(str(textnum).split(".")[-1]) == 2:
        if str(textnum)[-1] == "1":
            text += " сотая"
        else:
            text += " сотых"
    elif len(str(textnum).split(".")[-1]) == 3:
        if str(textnum)[-1] == "1":
            text += " тысячная"
        else:
            text += " тысячных"
    elif len(str(textnum).split(".")[-1]) == 4:
        if str(textnum)[-1] == "1":
            text += " десятитысячная"
        else:
            text += " десятисячных"
    elif len(str(textnum).split(".")[-1]) == 5:
        if str(textnum)[-1] == "1":
            text += " статысячная"
        else:
            text += " статысячных"
    elif len(str(textnum).split(".")[-1]) == 6:
        if str(textnum)[-1] == "1":
            text += " миллионная"
        else:
            text += " миллионных"

    return znak + text.replace(" ноль тысяч ", " ")


def generate_string(count):
    alphabet = string.ascii_letters + string.digits + '-_'
    password = ''.join(secrets.choice(alphabet) for i in range(count))
    return password


def reduction(drob):
    numerator, denominator = drob
    if numerator >= denominator:
        rg = denominator
    else:
        rg = numerator

    for i in range(1, rg + 1)[::-1]:
        if numerator % i == 0 and denominator % i == 0:
            return (numerator // i, denominator // i)


OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}


def parse(formula_string):
    for s in formula_string:
        yield s


def shunting_yard(parsed_formula):
    stack = []  # в качестве стэка используем список
    for token in parsed_formula:
        # если элемент - оператор, то отправляем дальше все операторы из стека,
        # чей приоритет больше или равен пришедшему,
        # до открывающей скобки или опустошения стека.
        # здесь мы пользуемся тем, что все операторы право-ассоциативны
        if token in OPERATORS:
            while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                yield stack.pop()
            stack.append(token)
        elif token == ")":
            # если элемент - закрывающая скобка, выдаём все элементы из стека, до открывающей скобки,
            # а открывающую скобку выкидываем из стека.
            while stack:
                x = stack.pop()
                if x == "(":
                    break
                yield x
        elif token == "(":
            # если элемент - открывающая скобка, просто положим её в стек
            stack.append(token)
        else:
            # если элемент - число, отправим его сразу на выход
            yield token
    while stack:
        yield stack.pop()


def polish(polish):
    stack = []
    for token in polish:
        if token in OPERATORS:  # если приходящий элемент - оператор,
            y, x = stack.pop(), stack.pop()  # забираем 2 числа из стека
            stack.append(OPERATORS[token][1](x, y))  # вычисляем оператор, возвращаем в стек
        else:
            stack.append(token)
    return stack[0]  # результат вычисления - единственный элемент в стеке


def calc(text):
    text = text.lower()

    t = text.split(" ")

    if t[0] == "перестановки" or t[0] == 'размещений' or t[0] == "сочетаний":
        nums = []
        for i in text.split(" "):
            try:
                nums.append(to_num(i))
            except:
                continue

        buff = []
        if t[0] == 'перестановки':
            for i in permutations(generate_string(nums[0])):
                buff.append(i)
        elif t[0] == 'размещений':
            for i in permutations(generate_string(nums[0]), nums[1]):
                buff.append(i)
        else:
            for i in combinations(generate_string(nums[0]), nums[1]):
                buff.append(i)
        return num2text(len(buff))
    else:
        is_drob = False
        fracts = []
        for i in text.split(" умножить на "):
            for j in i.split(" разделить на "):
                for k in j.split(" плюс "):
                    for t in k.split(" минус "):
                        for f in t.split(" в степени "):
                            for r in f.split("скобка открывается"):
                                for y in r.split("скобка закрывается"):
                                    for x in y.split("косинус от "):
                                        for v in x.split("синус от "):
                                            for c in v.split("тангенс от "):
                                                if c == " " or c == "" or c.find("пи") != -1:
                                                    continue
                                                tt = c.replace(" целых ", " и ")
                                                if tt.find(" и ") != -1:
                                                    if tt.split(" ")[-1] in fractions:
                                                        num = to_num(tt)
                                                    else:
                                                        if tt.find("минус") != -1:
                                                            znk = "-"
                                                            tt = tt.replace("минус", "")
                                                        else:
                                                            znk = ""
                                                        buff = [to_num(tt.split(" и ")[0]), tt.split(" и ")[-1]]

                                                        bf = []

                                                        for ii in buff[-1].split(" "):
                                                            bf.append(to_num(ii))

                                                        drob = [0, 0]

                                                        index = 0
                                                        for ii in bf:
                                                            drob[index] += ii

                                                            if ii < 20:
                                                                drob[index] = str(drob[index])
                                                                index += 1
                                                        if drob[-1] not in (0, "0", "0,0") and drob[0] not in (
                                                                0, "0", "0,0"):
                                                            fracts.append(
                                                                Fraction((int(drob[0]) + int(buff[0]) * int(drob[-1])),
                                                                         int(drob[-1])))
                                                            num = "{}"  # "(" + " * ".join([str(buff[0]), "/".join(drob)]) + ")"
                                                            is_drob = True
                                                        else:
                                                            num = znk + str(drob[0]) if drob[-1] in (
                                                                0, "0") else znk + str(drob[-1])
                                                else:
                                                    if tt.split(" ")[-1] in fractions:
                                                        num = to_num(tt)
                                                    else:
                                                        if tt.find("минус") != -1:
                                                            znk = "-"
                                                            tt = tt.replace("минус", "")
                                                        else:
                                                            znk = ""

                                                        bf = []

                                                        flag = True
                                                        for ii in tt.split(" "):
                                                            try:
                                                                bf.append(to_num(ii))
                                                            except:
                                                                flag = False

                                                        if flag:
                                                            drob = [0, 0]

                                                            index = 0
                                                            for ii in bf:
                                                                drob[index] += ii

                                                                if ii < 20:
                                                                    drob[index] = str(drob[index])
                                                                    index += 1

                                                            if drob[-1] not in (0, "0") and drob[0] not in (0, "0"):
                                                                num = '{}'  # f"({znk}" + "/".join(drob) + ")"
                                                                fracts.append(Fraction(int(drob[0]), int(drob[-1])))
                                                                is_drob = True
                                                            else:
                                                                num = znk + str(drob[0]) if drob[-1] in (
                                                                    0, "0") else znk + str(drob[-1])
                                                        else:
                                                            num = to_num(tt)

                                                text = text.replace(c, str(num), 1)

        for key, value in znak.items():
            text = text.replace(key, str(value))

        t = text.split(" ")

        for i in range(len(t)):
            if t[i] in ("sin", "cos", "tan", "**"):
                if t[i + 1] != "":
                    if t[i + 1] != "(":
                        t.insert(i + 1, "(")
                        t.insert(i + 3, ")")
                else:
                    if t[i + 2] != "(":
                        t.insert(i + 2, "(")
                        t.insert(i + 4, ")")
        text = "".join(t)

        if not is_drob:
            result = round(eval(text), 6)

            if result % 1 == 0:
                result = int(result)

            return num2text(result)

        else:
            for i in range(len(t)):
                if t[i] == "{}":
                    t[i] = fracts.pop(0)
                elif t[i] not in ("*", "+", "-", "/"):
                    t[i] = Fraction(t[i])

            result = polish(shunting_yard(parse(t)))

            if result.numerator == result.denominator:
                return num2text(int(result))
            elif result.numerator == 0:
                return num2text(0)

            if result.numerator < 0:
                zn = "минус "
                result = Fraction(result.numerator * -1, result.denominator)
            else:
                zn = ""

            whole_part = result.numerator // result.denominator

            text = zn + num2text(whole_part) + " и "

            numerator_text = num2text(result.numerator % result.denominator).split(" ")

            try:
                numerator_text[-1] = convert_units[numerator_text[-1]]
            except:
                pass

            text += ' '.join(numerator_text)

            denominator_text = num2text(result.denominator).split(" ")

            denominator_text[-1] = convert_[denominator_text[-1]]

            if numerator_text[-1] == "одна":
                denominator_text[-1] = denominator_text[-1].replace('ых', 'ая')
                denominator_text[-1] = denominator_text[-1].replace('их', 'я')

            return text + " " + " ".join(denominator_text)


if __name__ == '__main__':
    import datetime

    start = datetime.datetime.now()


    print(calc("двадцать пять плюс тринадцать"))
    print(calc("одна третья минус одна третья"))
    print(calc("одна третья плюс две третьих"))
    print(calc("одна третья минус две третьих"))
    print(calc("сорок один и тридцать одна сотая разделить на семнадцать"))
    print(calc("пять плюс два умножить на три минус один"))
    print(calc("скобка открывается пять плюс два скобка закрывается умножить на три минус один"))
    print(calc("пять минус минус один"))
    print(calc("одна шестая умножить на две третьих"))
    print(calc("один и четыре пятых плюс шесть седьмых"))
    print(calc("два в степени четыре"))
    print(calc("синус от скобка открывается пи разделить на четыре скобка закрывается"))
    print(calc("размещений из трех по два"))
    print(calc("две тысячи сто двадцать пять плюс одна тысяча двести двадцать пять"))

    print(datetime.datetime.now() - start)
