# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 19:56:26 2018

@author: nguarinz
"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["axes.spines.right"] = False
plt.rcParams["axes.spines.top"] = False
plt.rcParams["mathtext.fontset"] = "cm"

plt.figure(figsize=(3, 2))
t = np.arange(0, 26, 5)
K = [2, 2, 4, 0, -6, 0]

plt.plot(t, K, marker="o")
plt.xticks(t)
plt.yticks(np.arange(-6, 5, 2))
plt.grid()
plt.xlabel(r"$t$ (s)")
plt.ylabel(r"$K(t)$ (kgf/cm²)")
plt.savefig("esfuerzo_dependiente_tiempo.pdf", bbox_inches="tight",
            transparent=True)