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

        names = people_names.split_name('Ms. Diane de Saint Victor', 'fml')
        self.assertEqual(names['first_name'], 'Diane')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'de Saint Victor')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Ms')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Matthew S. Ramsey, J.D.', 'fml')
        self.assertEqual(names['first_name'], 'Matthew')
        self.assertEqual(names['middle_name'], 'S')
        self.assertEqual(names['last_name'], 'Ramsey')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Samuel C. Scott, III.', 'fml')
        self.assertEqual(names['first_name'], 'Samuel')
        self.assertEqual(names['middle_name'], 'C')
        self.assertEqual(names['last_name'], 'Scott')
        self.assertEqual(names['suffix_name'], 'III')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Hon., Amb., Craig R. Stapleton', 'fml')
        self.assertEqual(names['first_name'], 'Craig')
        self.assertEqual(names['middle_name'], 'R')
        self.assertEqual(names['last_name'], 'Stapleton')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Hon')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Lt. Gen.(Retd). Richard V. Reynolds', 'fml')
        self.assertEqual(names['first_name'], 'Richard')
        self.assertEqual(names['middle_name'], 'V')
        self.assertEqual(names['last_name'], 'Reynolds')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Lt')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Keith E. St. Clair', 'fml')
        self.assertEqual(names['first_name'], 'Keith')
        self.assertEqual(names['middle_name'], 'E')
        self.assertEqual(names['last_name'], 'St Clair')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Carlos W. del Solar Simpson', 'fml')
        self.assertEqual(names['first_name'], 'Carlos')
        self.assertEqual(names['middle_name'], 'W')
        self.assertEqual(names['last_name'], 'del Solar Simpson')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Bernard de La Tour d\'Auvergne Lauraguais', 'fml')
        self.assertEqual(names['first_name'], 'Bernard')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'de La Tour d\'Auvergne Lauraguais')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Carlos Alberto da Veiga Sicupira', 'fml')
        self.assertEqual(names['first_name'], 'Carlos')
        self.assertEqual(names['middle_name'], 'Alberto')
        self.assertEqual(names['last_name'], 'da Veiga Sicupira')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Mauro di Carlo', 'fml')
        self.assertEqual(names['first_name'], 'Mauro')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'di Carlo')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Warren East, CBE', 'fml')
        self.assertEqual(names['first_name'], 'Warren')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'East')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Gov. Hon. Tommy G. Thompson, J.D.', 'fml')
        self.assertEqual(names['first_name'], 'Tommy')
        self.assertEqual(names['middle_name'], 'G')
        self.assertEqual(names['last_name'], 'Thompson')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Gov')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Fernando La Fuente Vila', 'fml')
        self.assertEqual(names['first_name'], 'Fernando')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'La Fuente Vila')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Eric G. Le Dain', 'fml')
        self.assertEqual(names['first_name'], 'Eric')
        self.assertEqual(names['middle_name'], 'G')
        self.assertEqual(names['last_name'], 'Le Dain')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Prof. Lars G. Josefsson', 'fml')
        self.assertEqual(names['first_name'], 'Lars')
        self.assertEqual(names['middle_name'], 'G')
        self.assertEqual(names['last_name'], 'Josefsson')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Prof')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mrs. Mary Callahan Erdoes', 'fml')
        self.assertEqual(names['first_name'], 'Mary')
        self.assertEqual(names['middle_name'], 'Callahan')
        self.assertEqual(names['last_name'], 'Erdoes')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mrs')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Lieutenant General (Retired) George R. Christmas', 'fml')
        self.assertEqual(names['first_name'], 'George')
        self.assertEqual(names['middle_name'], 'R')
        self.assertEqual(names['last_name'], 'Christmas')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Lt')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Timothy R. M. Main', 'fml')
        self.assertEqual(names['first_name'], 'Timothy')
        self.assertEqual(names['middle_name'], 'R M')
        self.assertEqual(names['last_name'], 'Main')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Governor Brian D. Schweitzer', 'fml')
        self.assertEqual(names['first_name'], 'Brian')
        self.assertEqual(names['middle_name'], 'D')
        self.assertEqual(names['last_name'], 'Schweitzer')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Gov')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Adm. (Retd.) Eric T. Olson', 'fml')
        self.assertEqual(names['first_name'], 'Eric')
        self.assertEqual(names['middle_name'], 'T')
        self.assertEqual(names['last_name'], 'Olson')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Adm')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Pedro Morazzani, CPA, C.V.A., C.F.E.', 'fml')
        self.assertEqual(names['first_name'], 'Pedro')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Morazzani')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Cesar A. Ortiz, CPA., J.D., Esq', 'fml')
        self.assertEqual(names['first_name'], 'Cesar')
        self.assertEqual(names['middle_name'], 'A')
        self.assertEqual(names['last_name'], 'Ortiz')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Philip S. "Scott" Moses', 'fml')
        self.assertEqual(names['first_name'], 'Philip')
        self.assertEqual(names['middle_name'], 'S')
        self.assertEqual(names['last_name'], 'Moses')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], 'Scott')

        names = people_names.split_name('Mr. Philip S. \'Scott\' Moses', 'fml')
        self.assertEqual(names['first_name'], 'Philip')
        self.assertEqual(names['middle_name'], 'S')
        self.assertEqual(names['last_name'], 'Moses')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], 'Scott')

        names = people_names.split_name('Mr. Christopher J. Reynolds, CGA', 'fml')
        self.assertEqual(names['first_name'], 'Christopher')
        self.assertEqual(names['middle_name'], 'J')
        self.assertEqual(names['last_name'], 'Reynolds')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Sen. William H. Frist M.D.', 'fml')
        self.assertEqual(names['first_name'], 'William')
        self.assertEqual(names['middle_name'], 'H')
        self.assertEqual(names['last_name'], 'Frist')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Sen')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. John I. Von Lehman', 'fml')
        self.assertEqual(names['first_name'], 'John')
        self.assertEqual(names['middle_name'], 'I')
        self.assertEqual(names['last_name'], 'Von Lehman')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Sergio Traversa Pharm.D. MBA.', 'fml')
        self.assertEqual(names['first_name'], 'Sergio')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Traversa')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Andrew ("Andy") Arno', 'fml')
        self.assertEqual(names['first_name'], 'Andrew')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Arno')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], 'Andy')

        names = people_names.split_name('Mr. LI Xinzhou (Paul Li)', 'fml')
        self.assertEqual(names['first_name'], 'LI')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Xinzhou')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], 'Paul Li')

        names = people_names.split_name('Mr. Stephen T. Wills, MST, CPA', 'fml')
        self.assertEqual(names['first_name'], 'Stephen')
        self.assertEqual(names['middle_name'], 'T')
        self.assertEqual(names['last_name'], 'Wills')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Robert A. Dickinson, B.Sc., M.Sc.', 'fml')
        self.assertEqual(names['first_name'], 'Robert')
        self.assertEqual(names['middle_name'], 'A')
        self.assertEqual(names['last_name'], 'Dickinson')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Gerald J. McConnell, QC', 'fml')
        self.assertEqual(names['first_name'], 'Gerald')
        self.assertEqual(names['middle_name'], 'J')
        self.assertEqual(names['last_name'], 'McConnell')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Gen. Janet Carol Wolfenbarger, USAF, Retired', 'fml')
        self.assertEqual(names['first_name'], 'Janet')
        self.assertEqual(names['middle_name'], 'Carol')
        self.assertEqual(names['last_name'], 'Wolfenbarger')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Gen')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Gen.(Retd.) Ronald R. Fogleman', 'fml')
        self.assertEqual(names['first_name'], 'Ronald')
        self.assertEqual(names['middle_name'], 'R')
        self.assertEqual(names['last_name'], 'Fogleman')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Gen')
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

        names = people_names.split_name('General Peter Pace, USMC (Retd.)', 'fml')
        self.assertEqual(names['first_name'], 'Peter')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Pace')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Gen')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Trevor Thomas, LLB.', 'fml')
        self.assertEqual(names['first_name'], 'Trevor')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Thomas')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. David E. De Witt, B.Com., LLB.', 'fml')
        self.assertEqual(names['first_name'], 'David')
        self.assertEqual(names['middle_name'], 'E')
        self.assertEqual(names['last_name'], 'De Witt')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Ronald W. Thiessen, FCPA, FCA.', 'fml')
        self.assertEqual(names['first_name'], 'Ronald')
        self.assertEqual(names['middle_name'], 'W')
        self.assertEqual(names['last_name'], 'Thiessen')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Gordon B. Keep, B.Sc., MBA, P.Geo.', 'fml')
        self.assertEqual(names['first_name'], 'Gordon')
        self.assertEqual(names['middle_name'], 'B')
        self.assertEqual(names['last_name'], 'Keep')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Christian Milau, CPA, CA, CPA (Illinois)', 'fml')
        self.assertEqual(names['first_name'], 'Christian')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Milau')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. David Laing, BSc Mining Engineering', 'fml')
        self.assertEqual(names['first_name'], 'David')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Laing')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Dr. Daniel S. J. Muffoletto, N.D.', 'fml')
        self.assertEqual(names['first_name'], 'Daniel')
        self.assertEqual(names['middle_name'], 'S J')
        self.assertEqual(names['last_name'], 'Muffoletto')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Dr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Comdr. Rigel D. Pirrone, USN', 'fml')
        self.assertEqual(names['first_name'], 'Rigel')
        self.assertEqual(names['middle_name'], 'D')
        self.assertEqual(names['last_name'], 'Pirrone')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Comdr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Donald W. Hedges , Esq.', 'fml')
        self.assertEqual(names['first_name'], 'Donald')
        self.assertEqual(names['middle_name'], 'W')
        self.assertEqual(names['last_name'], 'Hedges')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Ms. Susan Ludley, FCCA', 'fml')
        self.assertEqual(names['first_name'], 'Susan')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Ludley')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Ms')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Dr. William M. Harvey, B.A., Ph.D.', 'fml')
        self.assertEqual(names['first_name'], 'William')
        self.assertEqual(names['middle_name'], 'M')
        self.assertEqual(names['last_name'], 'Harvey')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Dr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Mr. Ulrich E. Rath, B.Sc.(Hons), M.Sc.(Geol.)', 'fml')
        self.assertEqual(names['first_name'], 'Ulrich')
        self.assertEqual(names['middle_name'], 'E')
        self.assertEqual(names['last_name'], 'Rath')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')

        names = people_names.split_name('Ms. Rosalind Morrow, B.A., B.Ed.,A.R.C.T,LL.B.', 'fml')
        self.assertEqual(names['first_name'], 'Rosalind')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Morrow')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Ms')
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
