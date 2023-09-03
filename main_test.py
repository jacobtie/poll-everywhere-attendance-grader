from main import get_absent_students, get_extra_credit_students


def test_get_absent_students():
    student_names = get_absent_students('01', '1', True)
    assert student_names == {'Matt Smith', 'Paul McGann'}


def test_get_extra_credit_students():
    student_names = get_extra_credit_students('01', '1')
    assert student_names == {'David Tenant',
                             'Tom Baker', 'Jodie Whittaker', 'Peter Capaldi'}
