import os

import pandas as pd
from collections import Counter
from itertools import combinations
from tqdm import tqdm

import spacy
nlp = spacy.load("en_core_web_sm")

import networkx as nx
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20,20)

def main():
    