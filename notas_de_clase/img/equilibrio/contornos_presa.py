# -*- coding: utf-8 -*-
"""
Grafica los contornos de esfuerzo para una presa triangular
con un angulo interno de pi/4

@author: Nicolas Guarin-Zapata
@date: Marzo 22, 2018
"""
from __future__ import division, print_function
import meshio
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["axes.spines.right"] = False
plt.rcParams["axes.spines.top"] = False
plt.rcParams["mathtext.fontset"] = "cm"

#%% Malla
points, cells, _, _, _ = meshio.read("presa_triangular.msh")
x = points[:, 0]
y = points[:, 1]
tri =  cells["triangle"]

#%% Campos
gamma = 1.0
sigma_xx = gamma*x - 2*gamma*y
sigma_yy = -gamma*x
sigma_xy = -gamma*y
tau_max = np.sqrt(0.25*(sigma_xx - sigma_yy)**2 + sigma_xy**2)
campos = [sigma_xx, sigma_yy, sigma_xy, tau_max]

#%% Visualizacion
plot_args = {"cmap": "RdYlBu_r", "shading": "gouraud",
             "vmin": -1, "vmax": 1}
titulos = [r"$\sigma_{xx}$", r"$\sigma_{yy}$",
           r"$\tau_{xy}$", r"$\tau_{\max}$"]
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(4, 4))
for cont, ax in enumerate(axes.flat):
    ax.invert_yaxis()
    im = ax.tripcolor(y, x, tri, campos[cont], **plot_args)
    ax.tricontour(y, x, tri, campos[cont], colors="black")
    ax.set_title(titulos[cont], fontsize=14)
    ax.xaxis.set_ticks([0, 0.5, 1])
    ax.yaxis.set_ticks([0, 0.5, 1])
    ax.axis("image")
    if cont < 2:
        ax.xaxis.set_ticks([])
        ax.spines["bottom"].set_color("none")
    if cont%2 == 1:
        ax.yaxis.set_ticks([])
        ax.spines["left"].set_color("none")

fig.colorbar(im, ax=axes.ravel().tolist(), shrink=0.75)
plt.savefig("presa_esfuerzos.pdf", bbox_inches="tight", transparent=True)