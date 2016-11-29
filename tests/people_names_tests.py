import unittest
from people_names import people_names

class UtilsTests(unittest.TestCase):
    def test_add_name_parts_to_dict(self):
        obj = {'job': 'auror'}
        name_parts = {
            'first_name': 'harry',
            'middle_name': 'james',
            'last_name': 'potter',
            'suffix_name': '',
            'nominal_name': 'Sir',
            'nickname': 'the choosen one'
        }
        people_names.add_name_parts_to_dict(obj, name_parts)
        self.assertEqual(obj['first_name'], 'harry')
        self.assertEqual(obj['middle_name'], 'james')
        self.assertEqual(obj['last_name'], 'potter')
        self.assertEqual(obj['suffix_name'], '')
        self.assertEqual(obj['nominal_name'], 'Sir')
        self.assertEqual(obj['nickname'], 'the choosen one')

    def test_split_name_fml(self):
        names = people_names.split_name('', 'fml')
        self.assertEqual(names['first_name'], '')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], '')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Gen.(Retd.) Peter Pace', 'fml')
        self.assertEqual(names['first_name'], 'Peter')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Pace')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Gen')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Gen. (Retd.) Peter Pace', 'fml')
        self.assertEqual(names['first_name'], 'Peter')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Pace')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Gen')
        self.assertEqual(names['nickname'], '')


        names = people_names.split_name('Ms. Jacqueline Williams-Roll', 'fml')
        self.assertEqual(names['first_name'], 'Jacqueline')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Williams-Roll')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Ms')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Archbold van Beuren', 'fml')
        self.assertEqual(names['first_name'], 'Archbold')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'van Beuren')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Jan van der Velden', 'fml')
        self.assertEqual(names['first_name'], 'Jan')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'van der Velden')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Dr. Harry F. Hixson Jr.', 'fml')
        self.assertEqual(names['first_name'], 'Harry')
        self.assertEqual(names['middle_name'], 'F')
        self.assertEqual(names['last_name'], 'Hixson')
        self.assertEqual(names['suffix_name'], 'Jr')
        self.assertEqual(names['nominal_name'], 'Dr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Marshall S. McCrea, III', 'fml')
        self.assertEqual(names['first_name'], 'Marshall')
        self.assertEqual(names['middle_name'], 'S')
        self.assertEqual(names['last_name'], 'McCrea')
        self.assertEqual(names['suffix_name'], 'III')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('James R. (Rick) Perry', 'fml')
        self.assertEqual(names['first_name'], 'James')
        self.assertEqual(names['middle_name'], 'R')
        self.assertEqual(names['last_name'], 'Perry')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], 'Rick')


        names = people_names.split_name('Gen.(Retd.) Ronald R. Fogleman', 'fml')
        self.assertEqual(names['first_name'], 'Ronald')
        self.assertEqual(names['middle_name'], 'R')
        self.assertEqual(names['last_name'], 'Fogleman')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Gen')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Gen. (Retd.) Peter Pace', 'fml')
        self.assertEqual(names['first_name'], 'Peter')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Pace')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Gen')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Robert D. Cochran Esq.', 'fml')
        self.assertEqual(names['first_name'], 'Robert')
        self.assertEqual(names['middle_name'], 'D')
        self.assertEqual(names['last_name'], 'Cochran')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Esq')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Dr. Michael Severino, M.D.', 'fml')
        self.assertEqual(names['first_name'], 'Michael')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Severino')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Dr')
        self.assertEqual(names['nickname'], '')

    def test_split_name_lmf(self):
        names = people_names.split_name('', 'lfm')
        self.assertEqual(names['first_name'], '')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], '')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Davis, Alicia Boler', 'lmf')
        self.assertEqual(names['first_name'], 'Alicia')
        self.assertEqual(names['middle_name'], 'Boler')
        self.assertEqual(names['last_name'], 'Davis')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('ABDULHAMID, AMMAR', 'lmf')
        self.assertEqual(names['first_name'], 'Ammar')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Abdulhamid')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('ABBOTT, GIFFORD WHEELER JR', 'lmf')
        self.assertEqual(names['first_name'], 'Gifford')
        self.assertEqual(names['middle_name'], 'Wheeler')
        self.assertEqual(names['last_name'], 'Abbott')
        self.assertEqual(names['suffix_name'], 'Jr')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('ABRAMS, MARCIA KAREN DR PHD', 'lmf')
        self.assertEqual(names['first_name'], 'Marcia')
        self.assertEqual(names['middle_name'], 'Karen')
        self.assertEqual(names['last_name'], 'Abrams')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Dr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('ABRAHAM, RALPH LEE DR. JR', 'lmf')
        self.assertEqual(names['first_name'], 'Ralph')
        self.assertEqual(names['middle_name'], 'Lee')
        self.assertEqual(names['last_name'], 'Abraham')
        self.assertEqual(names['suffix_name'], 'Jr')
        self.assertEqual(names['nominal_name'], 'Dr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('ALARCON, RICHARD ANTHONY MR.', 'lmf')
        self.assertEqual(names['first_name'], 'Richard')
        self.assertEqual(names['middle_name'], 'Anthony')
        self.assertEqual(names['last_name'], 'Alarcon')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('ANNA, SANTA MR. THE III', 'lmf')
        self.assertEqual(names['first_name'], 'Santa')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Anna')
        self.assertEqual(names['suffix_name'], 'III')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('ANTLEY, RAY MILLS JR MD', 'lmf')
        self.assertEqual(names['first_name'], 'Ray')
        self.assertEqual(names['middle_name'], 'Mills')
        self.assertEqual(names['last_name'], 'Antley')
        self.assertEqual(names['suffix_name'], 'Jr')
        self.assertEqual(names['nominal_name'], 'MD')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('smith, JANE cpa', 'lmf')
        self.assertEqual(names['first_name'], 'Jane')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Smith')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'CPA')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('BONIFICIA, ANTHONY A JR', 'lmf')
        self.assertEqual(names['first_name'], 'Anthony')
        self.assertEqual(names['middle_name'], 'A')
        self.assertEqual(names['last_name'], 'Bonificia')
        self.assertEqual(names['suffix_name'], 'Jr')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('VON ADAMS III, PHILIP MONROE', 'lmf')
        self.assertEqual(names['first_name'], 'Philip')
        self.assertEqual(names['middle_name'], 'Monroe')
        self.assertEqual(names['last_name'], 'Von Adams')
        self.assertEqual(names['suffix_name'], 'III')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')


        names = people_names.split_name('BRASS JR, HERMAN (GEORGE)', 'lmf')
        self.assertEqual(names['first_name'], 'Herman')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Brass')
        self.assertEqual(names['suffix_name'], 'Jr')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], 'George')

        names = people_names.split_name('PERRY, JAMES R (RICK)', 'lmf')
        self.assertEqual(names['first_name'], 'James')
        self.assertEqual(names['middle_name'], 'R')
        self.assertEqual(names['last_name'], 'Perry')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], 'Rick')



# python -m unittest discover -s tests -p "*_tests.py"
