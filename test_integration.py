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
        females = Patients().get_by_criterion(criterion={'gender': 'female'})
        self.assertEqual(4, len(females))
        
    def test_patient_male_number(self):
        males = Patients().get_by_criterion(criterion={'gender': 'male'})
        self.assertEqual(6, len(males))
        
    def test_patient_age_number(self):
        patient_30_years = Patients().get_by_criterion(criterion={'age': 30})
        self.assertEqual(3, len(patient_30_years))
            
    def test_two_criteria_or(self):
        patients_two_criteria = Patients().get_by_multiple_criteria(
                                criteria=[{'gender': 'male'}, {'age': 30}],
                                syntax='OR')
        self.assertEqual(7, len(patients_two_criteria))
    
    def test_two_criteria_and(self):
        patients_two_criteria = Patients().get_by_multiple_criteria(
                                criteria=[{'gender': 'male'}, {'age': 30}],
                                syntax='AND')
        self.assertEqual(2, len(patients_two_criteria))
        
    def test_three_criteria_or(self):
        patients_three_criteria = Patients().get_by_multiple_criteria(
                                  criteria=[{'gender': 'male'}, {'age': 30},
                                  {'variant_type': 'SNV'}], syntax='OR')
        self.assertEqual(9, len(patients_three_criteria))
    
    def test_three_criteria_and(self):
        patients_three_criteria = Patients().get_by_multiple_criteria(
                                  criteria=[{'gender': 'male'}, {'age': 30},
                                  {'variant_type': 'SNV'}], syntax='AND')
        self.assertEqual(1, len(patients_three_criteria))

    def test_all_unique_genes(self):
        possible_values = Patients().get_values_of_criterion(criterion=
                          {'gene': ''})
        self.assertEqual(8, len(possible_values)) # ['CTNNB1', 'REST', 'PAX6', 
                                # 'BAP1', 'BRCA1', 'SMARCE1', 'EPHA2', 'NPHP4']

    def test_all_unique_significance(self):
        possible_values = Patients().get_values_of_criterion(criterion=
                          {'significance': ''})
        self.assertEqual(5, len(possible_values)) # ['pathogenic', 
                 # 'likely pathogenic', 'likely benign', 'benign', 'uncertain']

    def test_unique_significance_multiple_criteria(self):
        possible_values = Patients().get_values_of_multiple_criteria(criteria=
                          [{'gene': 'CTNNB1'}, {'significance': ''}])
        self.assertEqual(2, len(possible_values)) # ['pathogenic', 
                                                  # 'likely pathogenic']
        
    def test_unique_significance_multiple_criteria_2(self):
        possible_values = Patients().get_values_of_multiple_criteria(criteria=
                          [{'gene': 'BRCA1'}, {'significance': ''}])
        self.assertEqual(1, len(possible_values)) # ['pathogenic']
        
    def test_unique_genes_of_wilms(self):
        possible_values = Patients().get_values_of_multiple_criteria(criteria=
                          [{'cancer_type': 'Wilms tumor'}, {'gene': ''}])
        self.assertEqual(3, len(possible_values)) # ['CTNNB1', 'REST', 'PAX6']

if __name__ == '__main__':
    unittest.main()