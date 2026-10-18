# Renders the solver's graphs for 25B-B Q1 and 20B-C Q1 (matplotlib). Run from the repo root.
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def base(ax, xl, yl):
    ax.set_xlim(*xl); ax.set_ylim(*yl)
    ax.axhline(0, color="black", lw=0.8); ax.axvline(0, color="black", lw=0.8)
    ax.grid(True, color="#dddddd", lw=0.6)
    ax.set_xlabel("x"); ax.set_ylabel("y")


# 25B-B Q1: f(x) = x e^(1/(x-2))
fig, ax = plt.subplots(figsize=(6.4, 4.8), dpi=120)
base(ax, (-6, 9), (-6, 14))
for lo, hi in ((-6, 1.999), (2.0005, 9)):
    xs = np.linspace(lo, hi, 4000)
    ys = xs*np.exp(1/(xs - 2))
    ys[ys > 14.5] = np.nan
    ax.plot(xs, ys, color="#c0392b", lw=2)
xs = np.linspace(-6, 9, 10)
ax.plot(xs, xs + 1, "--", color="#2c6fbb", lw=1.2, label="y = x + 1")
ax.axvline(2, ls="--", color="#2c6fbb", lw=1.2)
ax.plot([2], [0], "o", mfc="white", mec="#c0392b", ms=6)
ax.plot([1, 4, 1.6], [np.exp(-1), 4*np.exp(0.5), 1.6*np.exp(-2.5)], "o", color="black", ms=4)
ax.annotate("max (1, 1/e)", (1, np.exp(-1)), xytext=(-5.5, 3.2), arrowprops=dict(arrowstyle="->", lw=0.8))
ax.annotate("min (4, 4√e)", (4, 4*np.exp(0.5)), xytext=(4.6, 3.2), arrowprops=dict(arrowstyle="->", lw=0.8))
ax.annotate("inflection x=8/5", (1.6, 1.6*np.exp(-2.5)), xytext=(-1.2, -3.5), arrowprops=dict(arrowstyle="->", lw=0.8))
ax.text(2.15, 12.8, "x = 2", color="#2c6fbb")
ax.legend(loc="upper left")
fig.tight_layout(); fig.savefig("images/exams/25B-B-Q1-graph.png"); plt.close(fig)

# 20B-C Q1: f(x) = x^3 / (2 (x+1)^2)
fig, ax = plt.subplots(figsize=(6.4, 4.8), dpi=120)
base(ax, (-8, 5), (-14, 4))
for lo, hi in ((-8, -1.001), (-0.999, 5)):
    xs = np.linspace(lo, hi, 4000)
    ys = xs**3/(2*(xs + 1)**2)
    ys[ys < -14.5] = np.nan
    ax.plot(xs, ys, color="#c0392b", lw=2)
xs = np.linspace(-8, 5, 10)
ax.plot(xs, xs/2 - 1, "--", color="#2c6fbb", lw=1.2, label="y = x/2 - 1")
ax.axvline(-1, ls="--", color="#2c6fbb", lw=1.2)
ax.plot([-3, 0], [-27/8, 0], "o", color="black", ms=4)
ax.annotate("max (-3, -27/8)", (-3, -27/8), xytext=(-7.6, 1.5), arrowprops=dict(arrowstyle="->", lw=0.8))
ax.annotate("inflection (0, 0)", (0, 0), xytext=(0.8, -4), arrowprops=dict(arrowstyle="->", lw=0.8))
ax.text(0.15, -12.5, "x = -1", color="#2c6fbb")
ax.legend(loc="lower right")
fig.tight_layout(); fig.savefig("images/exams/20B-C-Q1-graph.png"); plt.close(fig)
print("wrote images/exams/25B-B-Q1-graph.png, images/exams/20B-C-Q1-graph.png")
