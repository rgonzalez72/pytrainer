# -*- coding: utf-8 -*-
from unittest import  TestCase
from pytrainer.gui.windowprofile import HeightFieldValidator
from pytrainer.gui.windowprofile import WeightFieldValidator
from pytrainer.gui.windowprofile import DateOfBirthFieldValidator
from pytrainer.gui.windowprofile import MaxHeartRateFieldValidator
from pytrainer.gui.windowprofile import RestHeartRateFieldValidator
from pytrainer.gui.windowprofile import METFieldValidator
from pytrainer.gui.windowprofile import ExtraWeightFieldValidator
from pytrainer.gui.windowprofile import MaximumPaceFieldValidator
from pytrainer.gui.windowprofile import LifeExpentancyFieldValidator
from pytrainer.gui.windowprofile import PriorUsageFieldValidator
import gettext


#Copyright (C) Rodolfo Gonzalez rgonzalez72@yahoo.com

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

class FieldValidatorTest2 (TestCase):

    def setUp (self):
        """ These tests are meant to be executed for the source main directory.
            Need to initialize the locale to deal with FieldValidator
            translated error messages. """
        gettext_path =  "./locale"

        gettext.install("pytrainer", gettext_path, unicode=1)


    def tearDown (self):
        pass

    def execute_single_field_validator (self, validator, good_fields,
            wrong_fields):
        for field in good_fields:
            self.assertTrue (validator.validate_field(field))
        for field in wrong_fields:
            self.assertFalse (validator.validate_field (field))

        # Make sure the function is available
        # How do I check the message is right?
        msgErr = validator.get_error_message ()
        msgLog = validator.get_log_message ()


    def test_height_field_validator (self):
        good_height = ['191', '']
        wrong_height = [ '191a', 'a191', '0', '-1', '-191']

        V = HeightFieldValidator ()
        self.execute_single_field_validator (V, good_height, wrong_height)


    def test_wight_field_validator (self):
        good_weight = ['50', '']
        wrong_weight = [ '50a', 'a80', '0', '-1', '-80']

        V = WeightFieldValidator ()
        self.execute_single_field_validator (V, good_weight, wrong_weight)

    def test_date_of_birth_field_validator (self):
        good_date = ['1972-12-30','']
        wrong_date = [ 'aaaaaa']

        V =  DateOfBirthFieldValidator ()
        self.execute_single_field_validator (V, good_date, wrong_date)
        
    def test_max_heart_rate_field_validator (self):
        good_rate = ['191', '']
        wrong_rate = [ '191a', 'a191', '0', '-1', '-191']

        V = MaxHeartRateFieldValidator ()
        self.execute_single_field_validator (V, good_rate, wrong_rate)

    def test_rest_heart_rate_field_validator (self):
        good_rate = ['45', '']
        wrong_rate = [ '45a', 'a45', '0', '-1', '-45']

        V = RestHeartRateFieldValidator ()
        self.execute_single_field_validator (V, good_rate, wrong_rate)

    def test_MET_field_validator (self):
        good_MET = ['45', '44.4', '0.0', '']
        wrong_MET = [ '45.4a', 'a45.4', '-0.0001', '-1.0', '-45.0']

        V = METFieldValidator ()
        self.execute_single_field_validator (V, good_MET, wrong_MET)
    
    def test_extra_weight_field_validator (self):
        good_weigth = ['45', '44.4', '0.0', '']
        wrong_weigth = [ '45.4a', 'a45.4', '-0.0001', '-1.0', '-45.0']

        V = ExtraWeightFieldValidator ()
        self.execute_single_field_validator (V, good_weigth, wrong_weigth)

    def test_maximum_pace_field_validator (self):
        good_pace = ['45', '44.4', '0.0', '']
        wrong_pace = [ '45.4a', 'a45.4', '-0.0001', '-1.0', '-45.0']

        V = MaximumPaceFieldValidator ()
        self.execute_single_field_validator (V, good_pace, wrong_pace)

    def test_life_expentancy_field_validator (self):
        good_life = ['45', '']
        wrong_life = [ '45a', 'a45', '0', '-1', '-45']

        V = LifeExpentancyFieldValidator ()
        self.execute_single_field_validator (V, good_life, wrong_life)

    def test_prior_usage_field_validator (self):
        good_usage = ['45', '', '0']
        wrong_usage = [ '45a', 'a45', '-1', '-45']

        V = PriorUsageFieldValidator ()
        self.execute_single_field_validator (V, good_usage, wrong_usage)

