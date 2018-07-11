#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:33:11 2018

@author: denise
"""

class Patients():
    
    def get_all_data(self):
        # Note: The genomic location is based on GRCh38.
        return [
            {'id': 0, 'gender': 'female', 'age': 30, 'variant_type': 'deletion', 'gene': 'CTNNB1', 'significance': 'pathogenic', 'cancer_type': 'Wilms tumor', 'chromosome': 3, 'start_location': 41224645, 'end_location': 41224647},
            {'id': 1, 'gender': 'male', 'age': 22, 'variant_type': 'SNV', 'gene': 'CTNNB1', 'significance': 'likely pathogenic', 'cancer_type': 'Wilms tumor', 'chromosome': 3, 'start_location': 41224646, 'end_location': 41224646},
            {'id': 2, 'gender': 'male', 'age': 23, 'variant_type': 'SNV', 'gene': 'REST', 'significance': 'likely pathogenic', 'cancer_type': 'Wilms tumor', 'chromosome': 4, 'start_location': 56919853, 'end_location': 56919853},
            {'id': 3, 'gender': 'female', 'age': 7, 'variant_type': 'SNV', 'gene': 'PAX6', 'significance': 'likely benign', 'cancer_type': 'Wilms tumor', 'chromosome': 11, 'start_location': 31786049, 'end_location': 31786049},
            {'id': 4, 'gender': 'male', 'age': 30, 'variant_type': 'SNV', 'gene': 'BAP1', 'significance': 'pathogenic', 'cancer_type': 'Meningioma', 'chromosome': 3, 'start_location': 52405897, 'end_location': 52405897},
            {'id': 5, 'gender': 'male', 'age': 11, 'variant_type': 'indel', 'gene': 'BRCA1', 'significance': 'pathogenic', 'cancer_type': 'breast-ovarian cancer', 'chromosome': 17, 'start_location': 43094141, 'end_location': 43094144},
            {'id': 6, 'gender': 'male', 'age': 30, 'variant_type': 'duplication', 'gene': 'BRCA1', 'significance': 'pathogenic', 'cancer_type': 'breast cancer', 'chromosome': 17, 'start_location': 43057065, 'end_location': 43057065},
            {'id': 7, 'gender': 'male', 'age': 22, 'variant_type': 'deletion', 'gene': 'SMARCE1', 'significance': 'pathogenic', 'cancer_type': 'Meningioma', 'chromosome': 17, 'start_location': 40632282, 'end_location': 40632285},
            {'id': 8, 'gender': 'female', 'age': 15, 'variant_type': 'SNV', 'gene': 'EPHA2', 'significance': 'benign', 'cancer_type': 'lung carcinoma', 'chromosome': 1, 'start_location': 16137994, 'end_location': 16137994},
            {'id': 9, 'gender': 'female', 'age': 7, 'variant_type': 'insertion', 'gene': 'NPHP4', 'significance': 'uncertain', 'cancer_type': 'carcinoma of colon', 'chromosome': 1, 'start_location': 5877257, 'end_location': 5877263}
        ]
    
    def get_by_criterion(self, criterion):
        patients_having_criterion = []
        patients = self.get_all_data()
        for key, value in criterion.items(): 
            for patient in patients:
                if value == '':
                    patients_having_criterion.append(patient)
                elif value == patient[key]:
                    patients_having_criterion.append(patient)
        return patients_having_criterion

    def get_by_multiple_criteria(self, criteria, syntax):
        patients_having_criteria = []
        temp_patients_having_criteria = []
        for criterion in criteria:
            patients_having_criterion = self.get_by_criterion(criterion)
            # When the syntax 'and' is defined a patient should at least meet 
            # one of the criteria. Duplicates of patients will be prevented.
            if syntax.lower() == 'or':   
                [patients_having_criteria.append(patient) for patient in 
                 patients_having_criterion if patient not in 
                 patients_having_criteria]
            elif syntax.lower() == 'and':
                temp_patients_having_criteria.extend(patients_having_criterion)
        # When the syntax 'and' is defined a patient should meet all the 
        # criteria. So the patient is found as many time as the defined number 
        # of criteria. 
        if syntax.lower() == 'and':
            patients_having_criteria = self.get_patients_having_both_criteria(
               temp_patients=temp_patients_having_criteria, criteria=criteria)
        return patients_having_criteria

    def get_patients_having_both_criteria(self, temp_patients, criteria):
        patients_having_both_criteria = []
        criteria_number = len(criteria)
        [[patients_having_both_criteria.append(patient), temp_patients.remove(
          patient)] for patient in temp_patients if temp_patients.count(
          patient) == criteria_number]
        return patients_having_both_criteria

    def get_values_of_criterion(self, criterion):
        patients_having_criterion_value = self.get_by_criterion(criterion=
                                                                criterion)
        unique_values = []
        for key in criterion.keys():
            [unique_values.append(patient[key]) for patient in 
             patients_having_criterion_value if patient[key] not in 
             unique_values]
        return unique_values
        
    def get_values_of_multiple_criteria(self, criteria):
        patients_having_a_criterion = []
        unique_values = []
        for criterion in criteria:
            patients_having_a_criterion.extend(self.get_by_criterion(
                                               criterion=criterion))
        patients_having_both_criteria = self.get_patients_having_both_criteria(
                  temp_patients=patients_having_a_criterion, criteria=criteria)
        for key in criteria[-1].keys():
            [unique_values.append(patient[key]) for patient in 
            patients_having_both_criteria if patient[key] not in unique_values]
        return unique_values
