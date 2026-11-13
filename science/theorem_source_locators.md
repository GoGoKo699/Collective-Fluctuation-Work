# Theorem source locators

These are the primary sources needed to audit the mathematical dependency chain. Equation and page locators below refer to the explicitly linked arXiv versions. The broader thermodynamic novelty comparison belongs in the separate literature account.

## Exact representation-theory ingredients

**Jonas Kahn and Mădălin Guţă, “Local asymptotic normality for finite dimensional quantum systems,” Communications in Mathematical Physics 289, 597–652 (2009).** [DOI](https://doi.org/10.1007/s00220-009-0787-3); [arXiv:0804.3876v1](https://arxiv.org/abs/0804.3876v1); [primary PDF](https://arxiv.org/pdf/0804.3876v1).

| Locator in the preprint | Ingredient used here |
|---|---|
| Theorem 5.2, p. 27 | Semistandard tableaux index a generally nonorthogonal basis of the irrep. |
| Paragraph following Theorem 5.2, p. 27 | Coordinates $`m_{ij}`$ count entries $`j`$ in row $`i`$. |
| Eq. (5.9), p. 28 | Exact diagonal-state eigenvalues are a highest-weight factor times $`\prod_{i\lt j}(p_j/p_i)^{m_{ij}}`$. |
| Lemma 6.3, p. 34 | Uniform convergence of typical block states to the oscillator thermal state. |
| Section 7.6, pp. 57–59; Eqs. (7.37)–(7.44) | Product geometric root modes, normalization estimates, finite-occupation inclusion, geometric tails, and the nonorthogonality issue. |

The present proof uses weight-space orthogonalization only for the joint spectrum of fixed diagonal state and energy operators. It does not identify this exact spectral isometry with the paper's approximate channel for rotated statistical models.

## Schur probabilities and concentration

**Michael Keyl and Reinhard F. Werner, “Estimating the spectrum of a density operator,” Physical Review A 64, 052311 (2001).** [DOI](https://doi.org/10.1103/PhysRevA.64.052311); [arXiv:quant-ph/0102027v1](https://arxiv.org/abs/quant-ph/0102027v1); [primary PDF](https://arxiv.org/pdf/quant-ph/0102027v1).

| Locator in the preprint | Ingredient used here |
|---|---|
| Section II, Eqs. (2)–(4), p. 2 | Schur–Weyl decomposition and the two commuting representation actions. |
| Eq. (10), p. 2 | The distribution of normalized Young shapes converges to the point mass at the state spectrum. |
| Eq. (17), p. 3 | Sector probability equals the representation character times the permutation-irrep dimension. |

Only convergence in probability is needed; the stronger large-deviation result in that paper is not required for the theorem as stated.

## The elementary mode-swap witness

**Eric G. Brown, Nicolai Friis, and Marcus Huber, “Passivity and practical work extraction using Gaussian operations,” New Journal of Physics 18, 113028 (2016).** [DOI](https://doi.org/10.1088/1367-2630/18/11/113028); [arXiv:1608.04977v2](https://arxiv.org/abs/1608.04977v2); [primary PDF](https://arxiv.org/pdf/1608.04977v2).

Theorem 1, p. 3, orders thermal mode populations against frequencies in the Gaussian-passivity criterion. Proof step (P4), p. 5, especially Eqs. (25)–(27), describes the relevant beam-splitter sorting. The qutrit witness in this project is a direct occupation-coordinate swap; its work is calculated explicitly and is not claimed to equal the full ergotropy.

## Attribution boundary

Schur–Weyl duality, tableau spectra, root-mode limits, geometric tail control, passive spectral sorting, and oscillator mode sorting are inherited ingredients. The task-specific theorem concerns the complete cyclic-unitary work optimization under a fixed global permutation commutant: a uniform bound, an exact finite fluctuation-work limit, its Gibbs criterion, and the resulting consequences for fixed control classes. The supplied proofs of passive rearrangement and finite-cutoff certification make the energetic limit self-contained; they are not claims that spectral rearrangement itself is new.
