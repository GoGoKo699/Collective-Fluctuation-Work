# From Watrous to collective fluctuation work

The anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press (2018)**, DOI [10.1017/9781316848142](https://doi.org/10.1017/9781316848142). The [author's official distribution page](https://cs.uwaterloo.ca/~watrous/TQI/) provides the manuscript and chapter links. Its manuscript is linked here for personal study and is not redistributed.

The book provides the operator language for the project. The bridge below applies that language to closed cyclic work and then identifies the extra representation-theoretic and energy-limit arguments required by the theorem. Watrous remains the single educational anchor; the primary papers in the [source locator account](../science/theorem_source_locators.md) supply attributed research ingredients.

## Source map

The labels in the milestone map refer to this table. Section and theorem numbers refer to the 2018 book and the author's chapter manuscripts.

| Label and source | Relevant material | Role in this project |
|---|---|---|
| **W1–2:** Chapters 1–2, via the [official chapter index](https://cs.uwaterloo.ca/~watrous/TQI/) | Operators, tensor products, density operators, unitary channels and observables. | Read the finite-dimensional state, energy and many-copy control definitions. |
| **W3:** Chapter 3, via the [official chapter index](https://cs.uwaterloo.ca/~watrous/TQI/) | Norms and distinguishability of states and channels. | Interpret state convergence; the project separately proves convergence of an unbounded energy objective. |
| **W4:** [Chapter 4](https://jhwatrous.github.io/TQI.4.pdf), §4.3.1–2 | Vector and Hermitian-operator majorization; Theorem 4.32 (Uhlmann) and Theorem 4.33 (Schur–Horn). | Supply the spectrum-and-diagonal viewpoint behind finite passive rearrangement. |
| **W7:** [Chapter 7](https://jhwatrous.github.io/TQI.7.pdf), §7.1.1–2 | Permutation-invariant vectors and operators; Theorem 7.11 on the invariant operator algebra. | Distinguish a symmetric vector from an invariant operator and identify the commutant setting. |

The chapter title “Unital channels and majorization” does not make general unital channels admissible controls in this project. The physical optimization is over closed ensemble-only unitaries. Likewise, the linear-span statement in Theorem 7.11 does not restrict every allowed unitary to one tensor power of a single-site unitary, or provide a circuit for an arbitrary linear combination.

## Notation translation

| Book language | Project notation and meaning |
|---|---|
| A complex Euclidean space for one register | The one-copy space is $`\mathbb C^d`$; $`d`$ stays fixed. |
| A density operator and a Hermitian observable | $`\rho`$ is the source state and $`H`$ is the bare energy observable. |
| Adjoint written with a star | Scientific pages write the adjoint as $`\dagger`$. |
| Tensor-factor permutation $`W_\pi`$ | The project writes $`P_\pi`$ for the same register-permutation action. |
| An ordered eigenvalue vector, often denoted using $`\lambda`$ | Here $`\lambda=(\lambda_1,\ldots,\lambda_d)`$ usually labels a Young partition, not the source's eigenvalue vector $`p`$. |
| The algebra of invariant operators | Its unitary elements form the allowed group $`\mathcal G_n`$. |

The Schur decomposition introduces $`V_\lambda`$, the sector space on which collective controls act, and $`M_\lambda`$, the permutation multiplicity space on which they act as the identity. These labels require the additional representation-theory construction supplied in the scientific account.

## Bridge 1: from spectral ordering to passive work

A cyclic unitary preserves the eigenvalues of a state while changing how its eigenvectors sit relative to the energy levels. For a finite-dimensional state with descending eigenvalues $`a_1\ge\cdots\ge a_D`$ and an energy observable with ascending eigenvalues $`e_1\le\cdots\le e_D`$, passive rearrangement gives

```math
\min_U\operatorname{Tr}(U\sigma U^\dagger K)
=\sum_{j=1}^{D}a_je_j.
```

Schur–Horn describes the possible diagonal entries in a changed basis. A linear energy objective is minimized by assigning the largest populations to the lowest energies. A state already ordered this way is passive; its ergotropy is the initial energy minus this minimum. The thermodynamic interpretation is supplied by the [model](../science/model_and_main_theorem.md), not asserted as a theorem from Watrous.

For example, the source with populations $`(0.60,0.25,0.15)`$ on energies $`(0,1,5)`$ is passive. On two copies, the symmetric vector $`(|02\rangle+|20\rangle)/\sqrt2`$ has population $`0.09`$ and energy $`5`$, whereas $`|11\rangle`$ has population $`0.0625`$ and energy $`2`$. Swapping these vectors and fixing their orthogonal complement commutes with copy exchange and extracts

```math
(0.09-0.0625)(5-2)=\frac{33}{400}.
```

The [qutrit account](../science/qutrit_example.md) establishes the finite optimum and the many-copy comparison. This example connects spectral ordering with a permitted control; it does not prove the asymptotic law.

## Bridge 2: from invariant operators to sector access

W7 separates the symmetric subspace of vectors from the algebra of permutation-invariant operators. A mixed iid state is permutation invariant without being confined to the symmetric subspace. Omitting its other sectors changes the source and the work calculation.

The project's [Schur reduction](../science/schur_tableau_spectrum.md#schur-reduction-of-the-optimization) resolves the whole space into sectors. Every allowed unitary acts independently on each $`V_\lambda`$ and leaves its $`M_\lambda`$ factor untouched. Sector probabilities are therefore fixed. The work is the probability-weighted sum of sector ergotropies, even though the unitary can entangle the physical copies.

The Young-diagram and highest-weight machinery is beyond the chosen chapters. The account credits Kahn–Guţă's Theorem 5.2 and Eq. (5.9) for tableau spectra and Keyl–Werner for the Schur probabilities and concentration. See [exact source locations](../science/theorem_source_locators.md). Watrous's measure-concentration material is not substituted for that particular spectrum-estimation theorem.

## Bridge 3: from state convergence to an optimized energy limit

Within a sector, subtracting its ground floor leaves a nonnegative excitation Hamiltonian. The [tableau construction](../science/schur_tableau_spectrum.md) identifies its joint population-and-energy spectrum with a finite subset of geometric root-mode occupations. These mathematical modes are coordinates for fluctuations inside the original ensemble, not extra physical oscillators supplied to the protocol.

W3 supplies useful norm language, but trace-norm convergence alone does not control expectations of an unbounded Hamiltonian. This project proves a uniform excitation bound and tail domination. It then proves infinite passive rearrangement and approximates its work by sorting a complete energy subspace, leaving its complement fixed:

```math
0\le W_\infty-W_L\le T_L,
\qquad
T_L=\operatorname{Tr}\!\left(\tau_\infty K_\infty
 \mathbf1_{\{K_\infty>L\}}\right)\longrightarrow0.
```

The [cutoff proof](../science/passive_rearrangement.md) uses unnormalized retained populations. An arbitrary occupation box or small omitted probability does not give this certificate. The [limit proof](../science/fluctuation_limit.md) bounds both sides of the optimized work and then averages over the Schur distribution.

## What the full route explains

The result concerns a fixed strictly passive, full-rank source and a nondegenerate Hamiltonian as the number of copies grows. Total work stays uniformly bounded and converges to the fluctuation ergotropy; the limit is positive precisely off the Gibbs family. The [consequences](../science/consequences.md) distinguish this finite activation premium from single-copy work, and show why a sublinear number of fixed control classes cannot unlock extensive passive-state work.

The [30 milestones](milestones.md) connect those claims to their proofs, the certified example and the [restricted reversible classical comparison](../science/classical_comparison.md). The route retains exact unitary symmetry, a closed fixed ensemble and abstract control access. Efficient implementation, finite power, changing partitions and imperfect symmetry require separate analysis.

[Learning overview](README.md) · [Milestone map](milestones.md) · [Science overview](../science/README.md)
