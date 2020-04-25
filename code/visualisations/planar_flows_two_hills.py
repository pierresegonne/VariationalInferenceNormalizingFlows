import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import sys

sys.path.append("..")

from target_distributions import two_hills_y, two_hills_sigma2

def visualise(q, shape):
    z0, zk, ldj, mu, log_var = q(tf.zeros(shape))

    npdf = lambda x, m, v: np.exp(-(x-m)**2/(2*v))/np.sqrt(2*np.pi*v)
    prior = lambda x: npdf(x, 0, 1)
    lik = lambda x: npdf(two_hills_y, x**2, two_hills_sigma2)
    post_scaled = lambda x: prior(x)*lik(x)

    plt.figure()
    count, bins, ignored = plt.hist(z0.numpy(), 100, density=True, color='slategray', alpha=0.6)
    plt.plot(bins, post_scaled(bins), linewidth=2, color='r')
    plt.legend(['True Posterior', 'q0'])

    plt.figure()
    count, bins, ignored = plt.hist(zk.numpy(), 100, density=True, color='darkslategrey', alpha=0.6)
    plt.plot(bins, post_scaled(bins), linewidth=2, color='r')
    plt.legend(['True Posterior', 'qk'])

    plt.show()