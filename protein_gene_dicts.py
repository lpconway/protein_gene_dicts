# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 09:36:21 2021

@author: Louis
"""
import os
import pickle

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(__location__+'\\protein_gene_dicts.pkl', 'rb') as f:
    acc2gene = pickle.load(f)
gene2acc = {x:y for y, x in acc2gene.items() if '-' not in y}