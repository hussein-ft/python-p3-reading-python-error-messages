#!/usr/bin/env python3

import runpy

class TestNameError:
    '''
    a_name_error.py
    '''

    def test_name_error(self):
        '''
        contains defined name "hello_world"
        '''

        runpy.run_path('lib/a_name_error.py')

class TestSyntaxError:
    '''
    a_syntax_error.py
    '''

    def test_syntax_error(self):
        '''
        multiplies two numbers
        '''
        
        runpy.run_path('lib/a_syntax_error.py')

class TestTypeError:
    '''
    a_type_error.py
    '''

    def test_type_error(self):
        #!/usr/bin/env python3


        class TestNameError:
            '''
            a_name_error.py
            '''

            def test_name_error(self):
                '''
                contains defined name "hello_world"
                '''
                runpy.run_path('lib/a_name_error.py')

        class TestSyntaxError:
            '''
            a_syntax_error.py
            '''

            def test_syntax_error(self):
                '''
                multiplies two numbers
                '''
                runpy.run_path('lib/a_syntax_error.py')

        class TestTypeError:
            '''
            a_type_error.py
            '''

            def test_type_error(self):
                '''
                adds two numbers
                '''
                runpy.run_path('lib/a_type_error.py')

        class TestAssertionError:
            '''
            an_assertion_error.py
            '''

            def test_assertion_error(self):
                '''
                evaluates two equal values
                '''
                runpy.run_path('lib/an_assertion_error.py')

        class TestIndexError:
            '''
            an_index_error.py
            '''

            def test_index_error(self):
                '''
                accesses an out-of-range list index
                '''
                runpy.run_path('lib/an_index_error.py')

        class TestKeyError:
            '''
            a_key_error.py
            '''

            def test_key_error(self):
                '''
                accesses a non-existent dictionary key
                '''
                runpy.run_path('lib/a_key_error.py')

        class TestValueError:
            '''
            a_value_error.py
            '''

            def test_value_error(self):
                '''
                converts an invalid string to an integer
                '''
                runpy.run_path('lib/a_value_error.py')

        class TestZeroDivisionError:
            '''
            a_zero_division_error.py
            '''

            def test_zero_division_error(self):
                '''
                divides a number by zero
                '''
                runpy.run_path('lib/a_zero_division_error.py')

        # We recommend installing an extension to run python tests.