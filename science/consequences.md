# Positivity and control consequences

This section proves the remaining assertions of the [main theorem](model_and_main_theorem.md). All limiting statements retain the strict population gaps, full rank, fixed local dimension, and nondegenerate Hamiltonian stated there.

## Zero fluctuation work exactly for Gibbs populations

If $`p_i=Z_H^{-1}e^{-\beta E_i}`$ for some $`\beta>0`$, then

```math
r_{ij}=e^{-\beta\omega_{ij}},
\qquad
\tau_\infty
=\frac{e^{-\beta K_\infty}}
       {\mathrm{Tr}e^{-\beta K_\infty}}.
```

Its populations decrease with energy, so it is already passive and $`W_\infty=0`$. In this case the original product state is Gibbs for $`H_n`$, and its work is zero for every $`n`$, even without the symmetry restriction.

For the converse, define the inverse temperatures of the adjacent root modes,

```math
\beta_i
=\frac{\log(p_i/p_{i+1})}{E_{i+1}-E_i}>0,
\qquad 1\le i\lt d.
```

If all these numbers equal $`\beta`$, telescoping gives $`p_i\propto e^{-\beta E_i}`$. Thus a non-Gibbs population vector has two adjacent root modes, denoted $`a`$ and $`b`$, with $`\beta_a\lt \beta_b`$. Write their gaps as $`\omega_a,\omega_b`$.

There exist positive integers $`m,\ell`$ satisfying

```math
\frac{\omega_b}{\omega_a}
\lt \frac{m}{\ell}
\lt \frac{\beta_b\omega_b}{\beta_a\omega_a},
```

because this interval is nonempty and the rationals are dense. Compare two fluctuation basis states: $`A`$ has $`m`$ excitations in mode $`a`$ and all other modes empty; $`B`$ has $`\ell`$ excitations in mode $`b`$ and all other modes empty. Then

```math
K_A=m\omega_a>\ell\omega_b=K_B,
```

but

```math
(\tau_\infty)_A
=Z_\infty^{-1}e^{-m\beta_a\omega_a}
>Z_\infty^{-1}e^{-\ell\beta_b\omega_b}
=(\tau_\infty)_B.
```

Swapping these two basis vectors extracts

```math
\bigl[(\tau_\infty)_A-(\tau_\infty)_B\bigr](K_A-K_B)>0.
```

This is a finite permutation, so it is included in the fluctuation ergotropy and eventually fits in every sufficiently deep Schur sector. Hence $`W_\infty>0`$ for every strictly passive non-Gibbs source. For $`d=2`$, every strictly passive full-rank state is Gibbs for the fixed Hamiltonian, consistently giving zero.

## Exact identity for an arbitrary input state

This identity does not require a strict spectrum. Let $`\sigma`$ be any state on the same finite-dimensional system, and let $`\sigma_{\rm pass}`$ be its passive rearrangement relative to $`H`$. Choose a unitary $`V`$ such that

```math
V\sigma V^\dagger=\sigma_{\rm pass}.
```

Because $`V^{\otimes n}\in\mathcal G_n`$, right multiplication by $`V^{\otimes n}`$ is a bijection of the allowed unitary group. The minimum attainable final energy is therefore the same for $`\sigma^{\otimes n}`$ and $`\sigma_{\rm pass}^{\otimes n}`$. Subtracting their different initial energies gives the exact identity

```math
\boxed{
W_n^{\rm sym}(\sigma,H)
=n\,\mathcal W(\sigma,H)
+W_n^{\rm sym}(\sigma_{\rm pass},H).
}
```

If $`\sigma`$ has a strictly ordered full-rank spectrum, the main theorem applies to its passive rearrangement and gives

```math
W_n^{\rm sym}(\sigma,H)
=n\,\mathcal W(\sigma,H)
+W_\infty(\sigma_{\rm pass},H)+o(1).
```

Thus the extensive term is exactly the single-copy ergotropy. The limiting theorem is not being extended here to degenerate or rank-deficient spectra; only the preceding algebraic identity holds without that qualification.

## A fixed partition into control classes

Partition the $`n`$ copies into $`b`$ nonempty classes of sizes $`n_1,\ldots,n_b`$. The partition remains fixed throughout the protocol. Allow every global unitary commuting with independent permutations inside each class:

```math
[U,P_{\pi_1}\otimes\cdots\otimes P_{\pi_b}]=0
\qquad
\text{for all }(\pi_1,\ldots,\pi_b)
\in\prod_{j=1}^b S_{n_j}.
```

These unitaries may entangle different classes. The direct-product Schur decomposition nevertheless preserves the tuple of Young labels $`(\lambda^{(1)},\ldots,\lambda^{(b)})`$. In a fixed tuple block, the initial normalized state is $`\bigotimes_j q_{\lambda^{(j)}}`$ and the excitation Hamiltonian above its block floor is the sum of the class excitation Hamiltonians. Its initial mean excitation satisfies

```math
\sum_{j=1}^b
 \mathrm{Tr}\!\left(q_{\lambda^{(j)}}K_{\lambda^{(j)}}\right)
\le b\,C(p,E).
```

No unitary preserving that tuple can lower the energy below the tuple's ground floor. Averaging over tuple labels proves

```math
\boxed{W_{n,b}\le b\,C(p,E).}
```

Consequently $`b=o(n)`$ precludes a positive asymptotic work density from a fixed strictly passive source. If $`W_{n,b}\ge wn`$ for a fixed $`w>0`$, then necessarily

```math
b\ge\frac{w}{C(p,E)}\,n.
```

For a non-Gibbs source, linear growth of the number of classes is also sufficient in order: choosing $`b=n`$ removes the restriction and permits extensive activation. One can see this without an asymptotic work formula. Use the same adjacent transitions and integers $`m,\ell`$ as above. Among $`m+\ell`$ copies, compare the product configuration with $`m`$ copies in the upper level of transition $`a`$ and $`\ell`$ copies in the lower level of transition $`b`$ to the configuration with those choices reversed. The first configuration has both higher energy and higher probability. Their transposition extracts a fixed positive amount of work; repeating this operation on disjoint groups gives work proportional to $`n`$.

This establishes a necessary linear count and an achievable linear count; it does not assign the same work density to all partitions with that count. Repartitioning the ensemble during a protocol, selecting new batches, or relabeling copies changes the stipulated control resource.

## A concrete qutrit extraction operation

Take

```math
p=\left(\frac35,\frac14,\frac3{20}\right),
\qquad
(E_1,E_2,E_3)=(0,1,5).
```

The three root modes have

| Mode | Frequency | Geometric ratio | Mean occupation |
|---|---:|---:|---:|
| $`12`$ | $`1`$ | $`5/12`$ | $`5/7`$ |
| $`13`$ | $`5`$ | $`1/4`$ | $`1/3`$ |
| $`23`$ | $`4`$ | $`3/5`$ | $`3/2`$ |

Their joint vacuum probability is $`Z_\infty^{-1}=7/40`$, and their mean excitation energy is

```math
\mu_\infty
=\frac57+\frac53+6
=\frac{176}{21}.
```

Swap the entire occupation coordinates of modes $`12`$ and $`23`$, and leave mode $`13`$ unchanged. This puts the more occupied mode at the smaller frequency and extracts

```math
W_{\rm swap}
=(4-1)\left(\frac32-\frac57\right)
=\frac{33}{14}\approx2.35714.
```

It is an explicit lower bound on $`W_\infty`$, with no claim of optimality. Ordering thermal occupations against oscillator frequencies is an established mode-sorting principle; Brown, Friis, and Huber's Gaussian-passivity analysis supplies a related primary reference, as recorded in the [source locators](theorem_source_locators.md).

The infinite swap also has finite implementations adequate for the theorem. Restrict it to the finite set $`|\boldsymbol m|_1\le M`$ and act as the identity outside. This set is invariant under the coordinate swap. Its work converges to $`33/14`$: the absolute energy change is bounded by a constant times $`|\boldsymbol m|_1`$, whose geometric expectation is finite. For $`g(\lambda)\ge M`$, the entire finite set lies in $`S_\lambda`$, so the same permutation is available inside that Schur block. This provides a concrete sequence of allowed finite operations approaching the displayed witness.
