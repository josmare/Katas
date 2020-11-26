import unittest


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    assert name.__len__() == 10
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def array_diff(a, b):
    if a.__len__() == 0:
        return a
    if b.__len__() == 0:
        return a
    x = list()
    for aa in a:
        for bb in b:
            if aa is not bb:
                x.append(aa)
    return x


def wave(str):
    return return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]


def dict_replacer(string, dictionary):
    if dictionary is None:
        return ''
    for k, v in dictionary.items():
        string = string.replace('$' + k + '$', v)
    return string


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        pass

    def test_wave1(self):
        result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
        self.assertEqual(wave("hello"), result)

    def test_wave2(self):
        result = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
        self.assertEqual(wave("codewars"), result)

    def test_wave3(self):
        result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs",
                  "two wordS"]
        self.assertEqual(wave("two words"), result)

    def test_wave4(self):
        result = [" Gap ", " gAp ", " gaP "]
        self.assertEqual(wave(" gap "), result)

    def test_array_diff1(self):
        self.assertEqual(array_diff([1, 2], [1]), [2])

    def test_array_diff2(self):
        self.assertEqual(array_diff([1, 2, 2], [1]), [2, 2])

    def test_array_diff3(self):
        self.assertEqual(array_diff([1, 2, 2], []), [1, 2, 2])

    def test_array_diff4(self):
        self.assertEqual(array_diff([], [1,2]), [])

    def test_dict_replacer1(self):
        self.assertEqual(dict_replacer('', None), '')

    def test_dict_replacer2(self):
        self.assertEqual(dict_replacer('$temp$', {'temp': 'temporary'}), 'temporary')

    def test_dict_replacer3(self):
        self.assertEqual(dict_replacer('$temp$ here comes the name $name$', {'temp': 'temporary', 'name': 'John Doe'}),\
           'temporary here comes the name John Doe')


if __name__ == '__main__':
    unittest.main()
