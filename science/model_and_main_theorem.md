# Model and main theorem

## Closed cyclic work under a fixed permutation symmetry

Fix a local dimension $`d\ge2`$, a nondegenerate Hamiltonian

```math
H=\sum_{i=1}^{d}E_i|i\rangle\langle i|,
\qquad E_1\lt \cdots\lt E_d,
```

and a strictly passive full-rank state

```math
\rho=\sum_{i=1}^{d}p_i|i\rangle\langle i|,
\qquad p_1>\cdots>p_d>0,
\qquad \sum_i p_i=1.
```

All local parameters remain fixed as the number $`n`$ of copies grows. Define

```math
H_n=\sum_{a=1}^{n}H^{(a)},\qquad
\mathcal G_n=\{U\in\mathsf U((\mathbb C^d)^{\otimes n}):[U,P_\pi]=0
\text{ for every }\pi\in S_n\},
```

where $`P_\pi`$ permutes the tensor factors. The allowed control is an arbitrary element of $`\mathcal G_n`$, including arbitrary entangling transformations compatible with this exact symmetry. There is no restriction to product rotations $`u^{\otimes n}`$.

The extracted work is the mean decrease of the bare Hamiltonian in a cyclic unitary process:

```math
W_n^{\rm sym}(\rho,H)
=\max_{U\in\mathcal G_n}
\mathrm{Tr}\!\left[H_n
  \left(\rho^{\otimes n}-U\rho^{\otimes n}U^\dagger\right)\right].
```

The maximum exists because the allowed unitary group is compact. This is restricted ergotropy. The unitary in the definition acts on the ensemble alone. The operational system is the fixed $`n`$-particle ensemble; no bath, measurement/postselection, discarded ancillary entropy sink, or auxiliary system carrying particle-permutation charge is included.

## Fluctuation state

Let $`\mathcal R=\{(i,j):1\le i\lt j\le d\}`$, with $`R=|\mathcal R|=d(d-1)/2`$. For each pair define

```math
r_{ij}=\frac{p_j}{p_i}\in(0,1),\qquad
\omega_{ij}=E_j-E_i>0.
```

On $`\mathcal F=\ell^2(\mathbb N_0^{\mathcal R})`$, introduce

```math
Z_\infty=\prod_{i\lt j}\frac1{1-r_{ij}},\qquad
\tau_\infty=\frac1{Z_\infty}
\sum_{\boldsymbol m\in\mathbb N_0^{\mathcal R}}
\left(\prod_{i\lt j}r_{ij}^{m_{ij}}\right)
|\boldsymbol m\rangle\langle\boldsymbol m|,
```

```math
K_\infty=\sum_{i\lt j}\omega_{ij}N_{ij},\qquad
\mu_\infty=\mathrm{Tr}(\tau_\infty K_\infty)
=\sum_{i\lt j}\omega_{ij}\frac{r_{ij}}{1-r_{ij}}\lt \infty.
```

These mathematical oscillator modes describe within-sector fluctuations; they are not additional physical systems supplied to the protocol. The geometric root-mode state and associated tail estimates are established ingredients of quantum local asymptotic normality, particularly Kahn–Guţă's Lemma 6.3 and Section 7.6. Their exact tableau spectral formulas also underlie the proof below. See the [source locators](theorem_source_locators.md).

For a state $`\sigma`$ of finite energy and a nonnegative Hamiltonian $`K`$, write

```math
\mathcal W(\sigma,K)=\mathrm{Tr}(\sigma K)
-\inf_V\mathrm{Tr}(V\sigma V^\dagger K),
```

where $`V`$ ranges over unitaries; outputs of infinite energy cannot improve the infimum. For $`(\tau_\infty,K_\infty)`$, passive rearrangement attains the infimum and is approximable by finite permutations with an energy-tail certificate. [Passive rearrangement](passive_rearrangement.md) proves these statements.

## Theorem: finite collective activation work

Under the assumptions above,

```math
0\le W_n^{\rm sym}(\rho,H)\le C(p,E):=Z_\infty\mu_\infty
\qquad\text{for every }n\ge1,
```

and

```math
\boxed{\lim_{n\to\infty}W_n^{\rm sym}(\rho,H)
=W_\infty(p,E):=\mathcal W(\tau_\infty,K_\infty).}
```

Moreover,

```math
W_\infty(p,E)=0
\quad\Longleftrightarrow\quad
\rho=\frac{e^{-\beta H}}{\mathrm{Tr}e^{-\beta H}}
\text{ for some }\beta>0.
```

Thus a fixed strictly passive non-Gibbs source has a positive but finite asymptotic activation work under these controls. Its symmetric work density tends to zero.

The constant is deliberately non-sharp. The argument does not replace it by $`\mu_\infty`$: conditioning a geometric distribution on an arbitrary subset does not by itself justify that stronger bound.

## Scope of the conclusion

The symmetry is an operator constraint on every allowed unitary. Covariance of an averaged noisy channel is weaker and does not imply this theorem. The theorem concerns one fixed ensemble and one fixed permutation action. Selecting separate batches, changing control classes over time, or adding inhomogeneous addressability changes the allowed control algebra.

The result optimizes over an abstract unitary class. It does not assert efficient circuits, bounded interaction order, bounded drive strength, or robustness to symmetry-breaking perturbations. Strict population gaps and full rank are required; degenerate probabilities, vanishing probabilities, and gaps shrinking with $`n`$ are separate limits.

The [consequences](consequences.md) give the exact arbitrary-state identity, the bound for a fixed partition into control classes, and a concrete qutrit extraction operation.
