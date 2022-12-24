from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


def IsPrime(x):
    if x <= 1:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def FactorizeInner(x):
    if x == 0:
        return "0"
    if x == 1:
        return "1"
    d = 2
    a = []
    while d * d <= x:
        if x % d == 0:
            a.append([d, 0])
            while x % d == 0:
                a[-1][-1] += 1
                x //= d
        d += 1
    if x != 1:
        a.append([x, 1])
    a = sorted(a)
    s = ""
    for i in range(len(a)):
        if i != 0:
            s += " * "
        s += str(a[i][0])
        if a[i][1] > 1:
            s += "^" + str(a[i][1])
    return s


def BinaryToDecimalInner(x):
    return str(int(x, 2))


def DecimalToBinaryInner(x):
    return bin(int(x))[2:]


def ReprAsPrimesSumInner(x):
    x = int(x)
    if x <= 1:
        return []
    if IsPrime(x):
        return [x]
    if x % 2 == 1:
        return [3] + ReprAsPrimesSumInner(x - 3)
    for i in range(1, x):
        j = x - i
        if IsPrime(i) and IsPrime(j):
            return [i, j]
    raise Exception()


def IsTriangularInner(x):
    n = 1
    i = 1
    while n <= x:
        if n == x:
            return True
        i += 1
        n += i
    return False

def CheckString(x):
    return x.isnumeric()


def Factorize(x):
    if not CheckString(x):
        return x + " is not a correct number"
    return FactorizeInner(int(x))


def BinaryToDecimal(x):
    if not CheckString(x):
        return x + " is not a correct number"
    return BinaryToDecimalInner(x)


def DecimalToBinary(x):
    if not CheckString(x):
        return x + " is not a correct number"
    return DecimalToBinaryInner(x)


def ReprAsPrimesSum(x):
    if not CheckString(x):
        return x + " is not a correct number"
    res = sorted(ReprAsPrimesSumInner(int(x)))
    if len(res) == 0:
        return x + " can't be represented as primes sum"
    ans = x + " = "
    for i in range(len(res)):
        if i != 0:
            ans += " + "
        ans += str(res[i])
    return ans

def IsTriangular(x):
    if not CheckString(x):
        return x + " is not a correct number"
    if IsTriangularInner(int(x)):
        return x + " is a triangular number"
    return x + " is not a triangular number"


token = '5973420336:AAGoNfAtPY3tqOtLDTnrUZgnNbzi_ctRdBY'

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет, этот бот позволяет бxrыстро узнать ответ на некоторые популярные вопросы о числах")
    await message.reply("Отправтье команду /help, чтобы узнать, что он умеет")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer(text=f"Отправьте команду /factorize X, чтобы узнать разложение числа X на простые множители"
                          "Отправьте команду /binary_to_decimal X, чтобы перевести число X из двоичной системы в десятичную"
                          "Отправьте команду /decimal_to_binary X, чтобы перевести число X из десятичной системы в двоичную"
                          "Отправьте команду /primes_sum_representation X, чтобы разложить  число X в сумму простых"
                          "Отправьте мне команду /istriangular X  , чтобы проверить число X на треугольность")

@dp.message_handler(commands=['factorize'])
async def process_factorize_command(msg: types.Message):
    await msg.answer(Factorize(msg.get_args()))


@dp.message_handler(commands=['binary_to_decimal'])
async def process_binary_to_decimal_command(msg: types.Message):
    await msg.answer(BinaryToDecimal(msg.get_args()))

@dp.message_handler(commands=['decimal_to_binary'])
async def process_binary_to_decimal_command(msg: types.Message):
    await msg.answer(DecimalToBinary(msg.get_args()))

@dp.message_handler(commands=['primes_sum_representation'])
async def process_binary_to_decimal_command(msg: types.Message):
    await msg.answer(ReprAsPrimesSum(msg.get_args()))

@dp.message_handler(commands=['istriangular'])
async def process_istriangular_command(msg: types.Message):
    await msg.answer(IsTriangular(msg.get_args()))


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    executor.start_polling(dp)
