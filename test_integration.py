#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 13:46:31 2018

@author: denise


Simple script using TDD to integrate Hail into Glowing Bear having i2b2.
"""

import unittest
from patients import Patients

class Testing(unittest.TestCase):
    """ Goal: select patients based on cliniclal and genomics data.
    """
        
    def test_number_of_patients(self):
        patients = Patients().get_all_data()
        self.assertEqual(len(patients), 10)

    def test_patient_ids(self):
        patients = Patients().get_all_data()
        ids = [patient['id'] for patient in patients]
        self.assertEqual(list(range(10)), ids)
        
    def test_patient_female_number(self):
        females = Patients().get_by_criteria({'gender': 'female'})
        self.assertEqual(4, len(females))
        
    def test_patient_male_number(self):
        males = Patients().get_by_criteria({'gender': 'male'})
        self.assertEqual(6, len(males))
        
    def test_patient_age_number(self):
        patient_30_years = Patients().get_by_criteria({'age': 30})
        print(patient_30_years)
        self.assertEqual(2, len(patient_30_years))
        



if __name__ == '__main__':
    unittest.main()