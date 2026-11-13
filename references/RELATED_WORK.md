# Related work and operational scope

For a fixed finite-dimensional nondegenerate Hamiltonian and a fixed strictly passive, full-rank iid source, the work accessible under all permutation-invariant cyclic unitaries converges to a finite fluctuation-state ergotropy. The [main theorem](../science/model_and_main_theorem.md) establishes this optimized work law using known representation-theoretic and asymptotic-normality ingredients. The [source locator table](../science/theorem_source_locators.md) identifies the exact statements used in the proof; [references.bib](references.bib) supplies their bibliographic records.

## Unrestricted work activation

Robert Alicki and Mark Fannes established the unrestricted many-copy benchmark in [*Entanglement boost for extractable work from ensembles of quantum batteries*, Physical Review E 87, 042123 (2013)](https://doi.org/10.1103/PhysRevE.87.042123). Theorem 3 of their [author manuscript](https://arxiv.org/pdf/1211.1209v2) gives

```math
\lim_{n\to\infty}\frac{W_n^{\mathrm{all}}(\rho,H)}{n}
=\operatorname{Tr}(\rho H)-\operatorname{Tr}(\gamma_{\bar\beta}H),
\qquad
\gamma_{\bar\beta}=\frac{e^{-\bar\beta H}}{\operatorname{Tr}e^{-\bar\beta H}},
\qquad
S(\gamma_{\bar\beta})=S(\rho).
```

Here $`W_n^{\mathrm{all}}`$ optimizes over all joint unitaries, and $`\bar\beta>0`$ is determined by the entropy of the strictly passive full-rank source. A non-Gibbs source has a positive rate because the Gibbs state minimizes energy at that entropy. This gives the extensive-work comparison in the README. The present result concerns the smaller control group whose every element commutes with all copy permutations.

## Closest external results

| Primary source | Established ingredient | Relation to the present result |
|---|---|---|
| **Yadin, Morris, and Brandner, Physical Review Research 5, 033018 (2023)**: [publisher](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.5.033018), [arXiv:2206.12639v2](https://arxiv.org/abs/2206.12639v2) | Schur-sector thermodynamics for permutation-invariant multilevel ensembles, the sector ground energy in Appendix C, and collective thermalization and heat-engine applications. | The present law concerns closed extraction from the unchanged, strictly passive iid source, with a bound uniform in copy number and an exact optimized residual work. The sector framework and ground-energy formula are inherited. |
| **Boeyens, Yadin, and Nimmrichter, New Journal of Physics 27, 013021 (2025)**: [DOI](https://doi.org/10.1088/1367-2630/ada796), [arXiv:2408.08797](https://arxiv.org/abs/2408.08797) | Published §4.1, Eq. (17), optimizes arbitrary permutation-invariant unitaries within each irrep, beyond product SU(3) rotations. Work is extracted from a two-bath steady state. | General within-sector ergotropy is already part of their model. The present result gives the asymptotic work of the original iid fuel without bath preparation. |
| **Kahn and Guţă, Communications in Mathematical Physics 289, 597–652 (2009)**: [publisher](https://link.springer.com/article/10.1007/s00220-009-0787-3), [arXiv:0804.3876v1](https://arxiv.org/abs/0804.3876v1) | Exact tableau spectra and quantum local asymptotic normality. Theorem 5.2 and Eq. (5.9) give the tableau basis and source eigenvalues; Lemma 6.3 and §7.6 give thermal root modes, convergence, and geometric tails. | The present proof uses a joint spectral identification for fixed state and energy operators, then controls the optimized energy through finite cutoffs. The tableau description, fluctuation state, and geometric tail mechanism are inherited. |
| **Yadin, Morris, and Adesso, Nature Communications 12, 1471 (2021)**: [publisher](https://www.nature.com/articles/s41467-021-21620-7), [arXiv:2006.12482v2](https://arxiv.org/abs/2006.12482v2) | Quantum work advantages in exchange-symmetric gas mixing. Supplementary Note 1, Eqs. (25)–(28), gives the reversible stabilizer obstruction and its quantum-superposition escape. | The present classical comparison applies this mechanism to cyclic work from a nondegenerate iid passive source and obtains its exponentially vanishing bound. |
| **Mitsuhashi, Kaneko, and Sagawa, Physical Review X 12, 021013 (2022)**: [publisher](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.12.021013), [arXiv:2103.06060v2](https://arxiv.org/abs/2103.06060v2) | Complete passivity under a fixed connected compact group with a tensor-power representation; a generalized Gibbs characterization, including explicit work storage. | Here the permutation group and its representation change with copy number. Substituting $`S_n`$ for their fixed single-copy symmetry group does not give the present theorem. |
| **Watanabe and Takagi, Nature Communications 17, 1857 (2026)**: [publisher](https://www.nature.com/articles/s41467-026-69143-3), [arXiv:2504.12373v2](https://arxiv.org/abs/2504.12373v2) | Universal work extraction from unknown sources through thermal operations, with spectrum-estimation and Schur-based ingredients. | Bath access, a battery, and discarded systems define a different operation class. Symmetry of an input or averaged channel does not impose commutation with permutations on every system unitary. |
| **Watanabe, Chen, and Venkatesh, “Scaling law of asymptotic freedom in collective charging of quantum batteries,” arXiv:2606.10054v1 (2026)**: [primary](https://arxiv.org/abs/2606.10054v1) | Ergotropy-to-energy scaling for collectively charged states supported on the fully symmetric Hilbert space. | A full-rank iid source occupies many Schur sectors. Restricted discharge of that source differs from charging into the fully symmetric sector and evaluating its ergotropy. |

### Preparation and spectrum assumptions

The 2023 framework's high-temperature limit, Eqs. (69)–(72), gives a cold-bath energy reduction of order $`\sqrt n`$ from a maximally mixed preparation. Equal populations lie outside the present strict-spectrum hypothesis, and the fluctuation occupation diverges as population gaps close. Its Section VI also identifies representation-space degeneracy as a possible source of nonclassical thermodynamic effects.

Boeyens, Yadin, and Nimmrichter study extraction after the collective two-bath evolution, published Eq. (15), with Schur-sector probabilities fixed by the initial preparation. Their passive-source example on p. 9 also has equal populations on the lasing transition. The present theorem keeps the initial iid state unchanged before cyclic extraction and assumes strictly ordered populations. Equation numbers here refer to the published 2025 article; its arXiv v1 numbers the bath evolution and full ergotropy as Eqs. (14) and (16).

### Further proof ingredients

[Keyl and Werner, *Estimating the spectrum of a density operator*, Physical Review A 64, 052311 (2001)](https://doi.org/10.1103/PhysRevA.64.052311), supply the Schur probabilities and concentration of normalized Young shapes at the ordered source spectrum. The theorem here needs only convergence in probability. The [source locator table](../science/theorem_source_locators.md#schur-probabilities-and-concentration) records the relevant equations.

The explicit oscillator-mode swap uses the established relation between thermal populations and mode frequencies. [Brown, Friis, and Huber, *Passivity and practical work extraction using Gaussian operations*, New Journal of Physics 18, 113028 (2016)](https://doi.org/10.1088/1367-2630/18/11/113028), characterize Gaussian passivity and give the associated mode sorting. The [qutrit construction](../science/qutrit_example.md) is a directly evaluated lower bound on full ergotropy. Its simple swap is not claimed to be the global optimum. The precise comparison is in the [mode-swap source locator](../science/theorem_source_locators.md#the-elementary-mode-swap-witness).

## Related projects

The following projects study different operational resources. Commit links fix the compared versions.

| Repository and model | Commit pin | Relation to the present result |
|---|---|---|
| [Quantum-Work-Activation: science/model.md](https://github.com/GoGoKo699/Quantum-Work-Activation/blob/1d17a9f23cc729719ed171454ac6978528984e86/science/model.md) | `1d17a9f23cc729719ed171454ac6978528984e86` | Known near-Gibbs qutrit fuel and arbitrary copy-block unitaries; block sizes for activation or a fraction of asymptotic work as the distance from Gibbs shrinks. Here the state is fixed, copy number grows, and the permutation commutant restricts every allowed unitary. |
| [Collective-Work-Thresholds: science/model.md](https://github.com/GoGoKo699/Collective-Work-Thresholds/blob/79689300d19dc8cda1d8ddd3f02fd755ef1d0ee8/science/model.md) | `79689300d19dc8cda1d8ddd3f02fd755ef1d0ee8` | Near-Gibbs activation and useful-work thresholds for unrestricted copy-block unitaries with a fixed commensurate local spectrum. The present asymptotic restriction is the control symmetry, rather than the available copy-block size. |
| [Universal-Quantum-Work: science/model_theorem.md](https://github.com/GoGoKo699/Universal-Quantum-Work/blob/3fb8e9dca2eaec4c1ab449323820c2f97251c15b/science/model_theorem.md) | `3fb8e9dca2eaec4c1ab449323820c2f97251c15b` | A source-independent thermal processor for unknown iid states, with Gibbs ancillas, an explicit battery, and discarding; its rate is relative-entropy free energy. This project concerns a known finite-dimensional source and closed cyclic system unitaries with exact permutation symmetry. |

## Operational scope

### Strong symmetry and channel covariance

The model requires $`[U,P_\pi]=0`$ for every particle permutation. Permutation covariance of the resulting channel is insufficient. For example, take any unrestricted work-extracting unitary $`V`$ and average its conjugates:

```math
\Phi(X)=\frac1{n!}\sum_{\pi}P_\pi V P_\pi^\dagger X P_\pi V^\dagger P_\pi^\dagger.
```

This channel is permutation covariant. On a permutation-invariant input with a permutation-invariant Hamiltonian, it has the same average output energy as $`V`$. Its individual Kraus operators generally do not commute with permutations. Allowing this weaker class would remove the work limitation. A random choice of an addressing pattern therefore remains an access resource even when the averaged channel has a symmetric description.

### Auxiliary systems

If an auxiliary system carries the trivial representation of particle permutations, a joint unitary obeying $`[V,P_\pi\otimes I_A]=0`$ preserves the system's Schur label. Its system-energy decrease is then bounded by the initial energy above the corresponding sector floor. The uniform $`O(1)`$ bound survives such auxiliaries even if they absorb entropy.

The exact ergotropy constant need not survive. A sufficiently large initially pure memory can receive the within-sector state while leaving the system in its sector ground state, changing the allowed spectrum transformation. The exact limiting constant is therefore stated for closed system unitaries. Catalysts, correlated return conditions, measurement records, and explicit work storage require their own operational assumptions.

An auxiliary carrying a nontrivial permutation representation can exchange representation charge with the system, so the system's Schur label need not remain fixed. A particle-addressing register or spatially resolved environment can supply this additional resource.

### Fixed parameters and fixed control classes

The theorem assumes fixed full rank, fixed strictly separated populations, a fixed finite local dimension, and a fixed nondegenerate energy spectrum. Equal or shrinking population gaps define a different asymptotic regime. A source prepared entirely in the fully symmetric subspace is also a different input resource.

Cyclic work means the mean decrease of system energy. Abstract access to every commuting unitary does not specify implementation time, interaction order, bandwidth, circuit complexity, or work-storage fluctuations. Arbitrarily weak inhomogeneous controls may change the accessible algebra over long times, so exact symmetry alone gives no finite-time robustness statement.

For a fixed partition into $`b`$ addressing classes, the product symmetry preserves a tuple of Schur labels and gives $`W\le bC`$. A sublinear number of permanently distinct classes cannot yield extensive work. Repartitioning during a protocol or changing which particles are addressed changes the control algebra. The [control-class result](../science/consequences.md) is a scaling statement, not a sharp work formula for every partition.

## Classical comparison and attribution

The [classical comparison](../science/classical_comparison.md) allows bijections of the product energy-basis strings that commute with all site permutations, optionally mixed independently or supplemented by compatible basis phases. Its work decays exponentially, up to a linear prefactor, for the fixed strictly passive iid source. The quantum work can converge to a positive constant.

Yadin, Morris, and Adesso's Supplementary Note 1 supplies the stabilizer obstruction and the quantum-superposition mechanism. The finite-copy sorting formula and the iid decay bound are the consequences developed here. This benchmark concerns the specified reversible classical controls; a bath, feedback with reset memory, or an averaged nonsymmetric addressing operation defines a different comparison.
