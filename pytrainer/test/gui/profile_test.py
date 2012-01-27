# -*- coding: utf-8 -*-
from unittest import  TestCase
from pytrainer.gui.windowprofile import FieldValidator
import gettext


#Copyright (C) Nathan Jones ncjones@users.sourceforge.net

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

class FieldValidatorTest (TestCase):

    def setUp (self):
        """ These tests are meant to be executed for the source main directory.
            Need to initialize the locale to deal with FieldValidator
            translated error messages. """
        gettext_path =  "./locale"

        gettext.install("pytrainer", gettext_path, unicode=1)


    def tearDown (self):
        pass

    def test_all_good (self):
        field_dict = {
            FieldValidator.FV_HEIGHT: '191',
            FieldValidator.FV_WEIGHT: '80',
            FieldValidator.FV_BIRTH_DATE: '1972-12-30',
            FieldValidator.FV_MAX_HRATE: '181',
            FieldValidator.FV_MIN_HRATE: '45',
        }

        F = FieldValidator ()
        retVal, msg = F.validateFields (field_dict)
        self.assertTrue (retVal)
        self.assertEquals (msg, '')

        # Empty fields are accepted
        field_dict = {
            FieldValidator.FV_HEIGHT: '',
            FieldValidator.FV_WEIGHT: '',
            FieldValidator.FV_BIRTH_DATE: '',
            FieldValidator.FV_MAX_HRATE: '',
            FieldValidator.FV_MIN_HRATE: '',
        }
        retVal, msg = F.validateFields (field_dict)
        self.assertTrue (retVal)
        self.assertEquals (msg, '')

    def test_invalid_height (self):
        wrongHeights = [ '191a', 'a191', '0', '-1', '-191']
        field_dict = {
            FieldValidator.FV_HEIGHT: '191a',
            FieldValidator.FV_WEIGHT: '80',
            FieldValidator.FV_BIRTH_DATE: '1972-12-30',
            FieldValidator.FV_MAX_HRATE: '181',
            FieldValidator.FV_MIN_HRATE: '45',
        }

        F = FieldValidator ()
        for h in wrongHeights:
            field_dict[FieldValidator.FV_HEIGHT] = h
            retVal, msg = F.validateFields (field_dict)
            self.assertTrue (not retVal)
            self.assertEquals (msg, F.FVEM_HEIGHT)
        

    def test_invalid_weight (self):
        wrongWeight = [ '80a', 'a80', '0', '-1', '-80']
        field_dict = {
            FieldValidator.FV_HEIGHT: '191',
            FieldValidator.FV_WEIGHT: '80a',
            FieldValidator.FV_BIRTH_DATE: '1972-12-30',
            FieldValidator.FV_MAX_HRATE: '181',
            FieldValidator.FV_MIN_HRATE: '45',
        }

        F = FieldValidator ()
        for w in wrongWeight:
            field_dict [FieldValidator.FV_WEIGHT] = w

            retVal, msg = F.validateFields (field_dict)
            self.assertTrue (not retVal)
            self.assertEquals (msg, F.FVEM_WEIGHT)

    def test_invalid_date_of_birth (self):
        wrongDates = [
            # Wrong format
            'aaaaaaa',
            # Wrong day 
            '1972-12-32',
            '1972-11-31',
            '1972-02-30',
            '1972-02-31',
            '1972-02-00',
            '1972-02-s0',
            # Wrong month
            '1972-00-28',
            '1972-13-28',
            '1972-1a-28',
            # Wrong year
            '1972a-10-28',
            '197-10-28',
            '19-10-28',
            '1-10-28',
            '10000-10-28',
            # Not split year
            '1973-02-29',
            ]

        field_dict = {
            FieldValidator.FV_HEIGHT: '191',
            FieldValidator.FV_WEIGHT: '80',
            FieldValidator.FV_BIRTH_DATE: 'aaaaa',
            FieldValidator.FV_MAX_HRATE: '181',
            FieldValidator.FV_MIN_HRATE: '45',
        }
        
        F = FieldValidator ()
        for d in wrongDates:
            field_dict [FieldValidator.FV_BIRTH_DATE] = d

            retVal, msg = F.validateFields (field_dict)
            self.assertTrue (not retVal)
            self.assertEquals (msg, F.FVEM_BIRTH_DATE)

    def test_date_of_birth_split_year (self):
        field_dict = {
            FieldValidator.FV_HEIGHT: '191',
            FieldValidator.FV_WEIGHT: '80',
            FieldValidator.FV_BIRTH_DATE: '1972-02-29',
            FieldValidator.FV_MAX_HRATE: '181',
            FieldValidator.FV_MIN_HRATE: '45',
        }

        F = FieldValidator ()
        retVal, msg = F.validateFields (field_dict)
        self.assertTrue (retVal)
        self.assertEquals (msg, '')


    def test_invalid_max_heart_rate (self):
        wrongHeartRate = [ '181a', 'a181', '0', '-1', '-181']
        field_dict = {
            FieldValidator.FV_HEIGHT: '191',
            FieldValidator.FV_WEIGHT: '80',
            FieldValidator.FV_BIRTH_DATE: '1972-12-30',
            FieldValidator.FV_MAX_HRATE: '181',
            FieldValidator.FV_MIN_HRATE: '45',
        }

        F = FieldValidator ()
        for h in wrongHeartRate:
            field_dict[FieldValidator.FV_MAX_HRATE] = h
            retVal, msg = F.validateFields (field_dict)
            self.assertTrue (not retVal)
            self.assertEquals (msg, F.FVEM_MAX_HRATE)
        
    def test_invalid_min_heart_rate (self):
        wrongHeartRate = [ '45a', 'a45', '0', '-1', '-45']
        field_dict = {
            FieldValidator.FV_HEIGHT: '191',
            FieldValidator.FV_WEIGHT: '80',
            FieldValidator.FV_BIRTH_DATE: '1972-12-30',
            FieldValidator.FV_MAX_HRATE: '181',
            FieldValidator.FV_MIN_HRATE: '45',
        }

        F = FieldValidator ()
        for h in wrongHeartRate:
            field_dict[FieldValidator.FV_MIN_HRATE] = h
            retVal, msg = F.validateFields (field_dict)
            self.assertTrue (not retVal)
            self.assertEquals (msg, F.FVEM_MIN_HRATE)
        
    def test_validate_field (self):
        wrongIntegerField = [ '45a', 'a45', '0', '-1', '-45']
        goodFields = ['1', '22']
        integerFields = [
            FieldValidator.FV_HEIGHT, 
            FieldValidator.FV_WEIGHT, 
            FieldValidator.FV_MAX_HRATE, 
            FieldValidator.FV_MIN_HRATE, 
            FieldValidator.FV_LIFE_EXPECT,
            FieldValidator.FV_MET,
            FieldValidator.FV_MAX_PACE,
        ]

        # How do I check the logs are created?
        F = FieldValidator ()
        for fieldId in integerFields:
            for fieldStr in wrongIntegerField:
                self.assertFalse (F.validateSingleFieldAndLog (fieldId,
                            fieldStr))
            for fieldStr in goodFields:
                self.assertTrue (F.validateSingleFieldAndLog (fieldId,
                            fieldStr))

        wrongDates = [
            # Wrong format
            'aaaaaaa',
            # Wrong day 
            '1972-12-32',
            '1972-11-31',
            '1972-02-30',
            '1972-02-31',
            '1972-02-00',
            '1972-02-s0',
            # Wrong month
            '1972-00-28',
            '1972-13-28',
            '1972-1a-28',
            # Wrong year
            '1972a-10-28',
            '197-10-28',
            '19-10-28',
            '1-10-28',
            '10000-10-28',
            # Not split year
            '1973-02-29',
            ]

        goodDates = [
            '1972-12-30']

        for fieldStr in wrongDates:
            self.assertFalse (F.validateSingleFieldAndLog (
                        FieldValidator.FV_BIRTH_DATE, fieldStr))
        for fieldStr in goodDates:
            self.assertTrue (F.validateSingleFieldAndLog (
                        FieldValidator.FV_BIRTH_DATE, fieldStr))

        wrongIntegerField = [ '45a', 'a45', '-1', '-45']
        goodIntergerField = [ '0', '1', '27']
        integerFields = [
            FieldValidator.FV_PRIOR_USE, 
        ]

        for fieldId in integerFields:
            for fieldStr in wrongIntegerField:
                self.assertFalse(F.validateSingleFieldAndLog (fieldId,
                            fieldStr))
            for fieldStr in goodIntergerField:
                self.assertTrue(F.validateSingleFieldAndLog (fieldId,
                            fieldStr))
                

    def test_all_equipment_good (self):
        field_dict = {
            FieldValidator.FV_LIFE_EXPECT: '5',
            FieldValidator.FV_PRIOR_USE: '2',
        }

        F = FieldValidator ()
        retVal, msg = F.validateEquipmentFields (field_dict)
        self.assertTrue (retVal)
        self.assertEquals (msg, '')

        # Empty fields are accepted
        field_dict = {
            FieldValidator.FV_LIFE_EXPECT: '',
            FieldValidator.FV_PRIOR_USE: '',
        }
        retVal, msg = F.validateEquipmentFields (field_dict)
        self.assertTrue (retVal)
        self.assertEquals (msg, '')

        field_dict = {
            FieldValidator.FV_LIFE_EXPECT: '1',
            FieldValidator.FV_PRIOR_USE: '0',
        }
        retVal, msg = F.validateEquipmentFields (field_dict)
        self.assertTrue (retVal)
        self.assertEquals (msg, '')


    def test_invalid_life_expect (self):
        wrongLifeExpect = [ '5a', 'a5', '0', '-1', '-5', '5.35']
        field_dict = {
            FieldValidator.FV_LIFE_EXPECT: '1',
            FieldValidator.FV_PRIOR_USE: '0',
        }

        F = FieldValidator ()
        for h in wrongLifeExpect:
            field_dict[FieldValidator.FV_LIFE_EXPECT] = h
            retVal, msg = F.validateEquipmentFields (field_dict)
            self.assertTrue (not retVal)
            self.assertEquals (msg, F.FVEM_LIFE_EXPECT)

    def test_invalid_prior_usage (self):
        wrongPriorUsage = [ '5a', 'a5', '-1', '-5', '5.35']
        field_dict = {
            FieldValidator.FV_LIFE_EXPECT: '1',
            FieldValidator.FV_PRIOR_USE: '0',
        }

        F = FieldValidator ()
        for h in wrongPriorUsage:
            field_dict[FieldValidator.FV_PRIOR_USE] = h
            retVal, msg = F.validateEquipmentFields (field_dict)
            self.assertTrue (not retVal)
            self.assertEquals (msg, F.FVEM_PRIOR_USE)

    def test_all_sport_good (self):
        field_dict = {
            FieldValidator.FV_MET: '5',
            FieldValidator.FV_EXTRA_WEIGHT: '2.3',
            FieldValidator.FV_MAX_PACE: '2',
        }

        F = FieldValidator ()
        retVal, msg = F.validateSportFields (field_dict)
        self.assertTrue (retVal)
        self.assertEquals (msg, '')

        # Empty fields are accepted
        field_dict = {
            FieldValidator.FV_MET: '',
            FieldValidator.FV_EXTRA_WEIGHT: '',
            FieldValidator.FV_MAX_PACE: '',
        }
        retVal, msg = F.validateSportFields (field_dict)
        self.assertTrue (retVal)
        self.assertEquals (msg, '')

        field_dict = {
            FieldValidator.FV_MET: '5',
            FieldValidator.FV_EXTRA_WEIGHT: '0.0',
            FieldValidator.FV_MAX_PACE: '2',
        }
        retVal, msg = F.validateSportFields (field_dict)
        self.assertTrue (retVal)
        self.assertEquals (msg, '')


    def test_invalid_met (self):
        wrongMET = [ '5a', 'a5', '-1', '-5', '5.35', '0']
        field_dict = {
            FieldValidator.FV_MET: '',
            FieldValidator.FV_EXTRA_WEIGHT: '1.1',
            FieldValidator.FV_MAX_PACE: '3',
        }

        F = FieldValidator ()
        for h in wrongMET:
            field_dict[FieldValidator.FV_MET] = h
            retVal, msg = F.validateSportFields (field_dict)
            self.assertTrue (not retVal)
            self.assertEquals (msg, F.FVEM_MET)

    def test_invalid_extra_weight (self):
        wrongExtraWeight = [ '5.2a', 'a5.2', '-1.2', '-5.2' ]
        field_dict = {
            FieldValidator.FV_MET: '5',
            FieldValidator.FV_EXTRA_WEIGHT: '1.1',
            FieldValidator.FV_MAX_PACE: '3',
        }

        F = FieldValidator ()
        for h in wrongExtraWeight:
            field_dict[FieldValidator.FV_EXTRA_WEIGHT] = h
            retVal, msg = F.validateSportFields (field_dict)
            self.assertTrue (not retVal)
            self.assertEquals (msg, F.FVEM_EXTRA_WEIGHT)

    def test_invalid_extra_weight (self):
        wrongExtraWeight = [ '5.2a', 'a5.2', '-1.2', '-5.2' ]
        field_dict = {
            FieldValidator.FV_MET: '5',
            FieldValidator.FV_EXTRA_WEIGHT: '1.1',
            FieldValidator.FV_MAX_PACE: '3',
        }

        F = FieldValidator ()
        for h in wrongExtraWeight:
            field_dict[FieldValidator.FV_EXTRA_WEIGHT] = h
            retVal, msg = F.validateSportFields (field_dict)
            self.assertTrue (not retVal)
            self.assertEquals (msg, F.FVEM_EXTRA_WEIGHT)

    def test_invalid_maximum_pace (self):
        wrongMaximumPace = [ '5a', 'a5', '-1', '-5', '5.5', '0' ]
        field_dict = {
            FieldValidator.FV_MET: '5',
            FieldValidator.FV_EXTRA_WEIGHT: '1.1',
            FieldValidator.FV_MAX_PACE: '3',
        }

        F = FieldValidator ()
        for h in wrongMaximumPace:
            field_dict[FieldValidator.FV_MAX_PACE] = h
            retVal, msg = F.validateSportFields (field_dict)
            self.assertTrue (not retVal)
            self.assertEquals (msg, F.FVEM_MAX_PACE)

