# -*- coding: utf-8 -*-
"""
Esta wia va a graficar funcione
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi,np.pi,100)

cos = np.cos(x)
sen = np.sin(x)

plt.plot(x,cos, label = "cos(x)")
plt.plot(x,sen, label = "sen(x)")
plt.legend()
plt.xlabel("x [rad]")
plt.title("Dos funciones muy conocidas.\n(Ninguna es la Todd Function)")
plt.savefig("sencos.png")
plt.show()