#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:33:11 2018

@author: denise
"""

class Patients():
    
    def get_all_data(self):
        return [
            {'id': 0, 'gender': 'male', 'age': 30},
            {'id': 1, 'gender': 'male', 'age': 22},
            {'id': 2, 'gender': 'male', 'age': 23},
            {'id': 3, 'gender': 'female', 'age': 7},
            {'id': 4, 'gender': 'male', 'age': 18},
            {'id': 5, 'gender': 'male', 'age': 11},
            {'id': 6, 'gender': 'male', 'age': 30},
            {'id': 7, 'gender': 'female', 'age': 2},
            {'id': 8, 'gender': 'female', 'age': 15},
            {'id': 9, 'gender': 'female', 'age': 7}
        ]
    
    def get_by_criteria(self, criteria):
        patients_having_criteria = []
        patients = self.get_all_data()
        for patient in patients:
            [patients_having_criteria.append(patient) for key, value in 
             criteria.items() if patient[key] == value]            
        return patients_having_criteria
            