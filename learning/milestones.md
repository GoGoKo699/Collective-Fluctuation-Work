# Thirty milestones for collective fluctuation work

This is a project-defined understanding map with exactly **30 milestones**. **M01–M12** build the background from local state-and-energy objects to the complete control model. **M13–M30** connect the spectral mechanism, energetic limit and physical consequences. The allocation gives the convergence argument enough room while retaining the operational question that motivates it.

Source labels **W1–2, W3, W4 and W7** refer to the precise Watrous chapters and sections in the [source map](anchor_bridge.md#source-map). Watrous (2018) is the one educational anchor. A source entry that cites a primary theorem or a project derivation marks a step beyond the textbook foundations; the [primary locator table](../science/theorem_source_locators.md) gives versions and exact theorem/equation locations.

Dependencies name earlier milestones needed for the understanding target, rather than every concept mentioned incidentally. The map is a route through the central argument, not a claim to cover every technical lemma or neighboring topic.

## Background and preliminaries: M01-M12

### M01 — State, spectrum and mean energy

- **Central question:** What describes the source, and which number is its mean energy?
- **Understanding target:** Distinguish a density operator's eigenvalues, its energy-basis populations and the expectation of a Hermitian energy observable.
- **Dependencies and story role:** None within this map. Establish the local objects before introducing an operation.
- **Conceptual connection:** Operator language makes energy a property of both the source and its placement relative to the Hamiltonian.
- **Source pointers:** W1–2, operator and density-operator foundations; [model: closed cyclic work](../science/model_and_main_theorem.md#closed-cyclic-work-under-a-fixed-permutation-symmetry).

### M02 — Cyclic unitary work

- **Central question:** What is extracted when a closed control changes a state's mean energy?
- **Understanding target:** Explain why the work objective is the initial minus final bare energy, and why unitary evolution preserves the state spectrum.
- **Dependencies and story role:** M01. Add the operation and score to the local setting.
- **Conceptual connection:** Spectrum preservation turns work extraction into an optimization over eigenvectors rather than arbitrary output populations.
- **Source pointers:** W1–2, unitaries and unitary channels; [model and allowed operations](../science/model_and_main_theorem.md#closed-cyclic-work-under-a-fixed-permutation-symmetry).

### M03 — Opposite ordering and passive rearrangement

- **Central question:** Which placement of a fixed spectrum minimizes energy?
- **Understanding target:** Relate descending populations and ascending energies to the finite sorted-spectrum minimum and distinguish it from a general noisy-channel transformation.
- **Dependencies and story role:** M01–M02. Identify the elementary optimization used later inside each sector.
- **Conceptual connection:** Majorization and the possible diagonals of a Hermitian operator connect quantum basis changes to spectral sorting.
- **Source pointers:** W4, §4.3.1–2, especially Theorems 4.32–4.33; [bridge: passive work](anchor_bridge.md#bridge-1-from-spectral-ordering-to-passive-work); [finite sector minimum](../science/fluctuation_limit.md#convergence-within-a-deep-sector).

### M04 — Passive does not mean Gibbs

- **Central question:** Why can decreasing populations be passive without having one temperature?
- **Understanding target:** Distinguish passive ordering from a common logarithmic population-to-energy slope; recognize that every strictly passive full-rank two-level state is Gibbs, while higher dimension allows non-Gibbs passive sources.
- **Dependencies and story role:** M03. Identify the fuel for the many-copy question.
- **Conceptual connection:** A local inability to extract work does not determine the behavior of a tensor-power source.
- **Source pointers:** W4, §4.3.2 as the spectral foundation; project thermodynamic definitions in the [main theorem](../science/model_and_main_theorem.md) and [Gibbs criterion](../science/consequences.md#zero-fluctuation-work-exactly-for-gibbs-populations).

### M05 — Many copies and activation

- **Central question:** What changes when the same passive source is available many times?
- **Understanding target:** Explain iid product populations, additive energy and the distinction between independent single-copy and unrestricted joint control.
- **Dependencies and story role:** M02–M04. Move from one system to an ensemble before imposing symmetry.
- **Conceptual connection:** Product probabilities and additive energies can develop inversions absent from one copy.
- **Source pointers:** W1–2, tensor products and compound systems; [qutrit two-copy operation](../science/qutrit_example.md#two-copies-already-allow-extraction); [unrestricted activation attribution](../references/RELATED_WORK.md#unrestricted-work-activation).

### M06 — Permuting tensor factors

- **Central question:** What does exchanging copies do to a state or control?
- **Understanding target:** Read the register-permutation action and explain why identical local states and the additive Hamiltonian are invariant under it.
- **Dependencies and story role:** M05. Introduce the symmetry acting on the entire ensemble.
- **Conceptual connection:** Copy labels define an algebraic action that can constrain physical control access.
- **Source pointers:** W7, §7.1.1, Eq. (7.3); [permutation-constrained model](../science/model_and_main_theorem.md#closed-cyclic-work-under-a-fixed-permutation-symmetry).

### M07 — Invariant state or symmetric vector?

- **Central question:** Does a permutation-invariant mixed state live only in the symmetric subspace?
- **Understanding target:** Distinguish invariance of an operator under conjugation from invariance of a vector, and explain why an iid mixed source generally occupies multiple sectors.
- **Dependencies and story role:** M01 and M06. Prevent an incorrect reduction of the ensemble before optimizing work.
- **Conceptual connection:** The symmetry of a density operator does not select one irreducible representation.
- **Source pointers:** W7, §7.1.1 versus §7.1.2, including Eq. (7.59); [bridge: sector access](anchor_bridge.md#bridge-2-from-invariant-operators-to-sector-access); [Schur reduction](../science/schur_tableau_spectrum.md#schur-reduction-of-the-optimization).

### M08 — The full commutant control class

- **Central question:** How much control is allowed by commuting with every copy permutation?
- **Understanding target:** Distinguish arbitrary unitary elements of the commutant from product rotations, and distinguish exact symmetry of each unitary from covariance obtained by averaging a channel.
- **Dependencies and story role:** M02 and M06–M07. Fix the precise resource restriction.
- **Conceptual connection:** A broad entangling control class can still conserve information that an unrestricted unitary could change.
- **Source pointers:** W7, §7.1.2 and Theorem 7.11; [model and scope](../science/model_and_main_theorem.md); [linear-span qualification](anchor_bridge.md#source-map).

### M09 — Two commuting actions and sector labels

- **Central question:** What does the Schur decomposition make accessible and inaccessible?
- **Understanding target:** Explain the roles of the sector space, permutation multiplicity space and Young label, and why a commutant unitary preserves sector probabilities.
- **Dependencies and story role:** M06–M08. Turn the symmetry restriction into a usable decomposition.
- **Conceptual connection:** Operator-algebra foundations lead to a direct sum of smaller work optimizations.
- **Source pointers:** W7, §7.1.2 as the algebraic foundation; [Schur reduction](../science/schur_tableau_spectrum.md#schur-reduction-of-the-optimization); supplementary Keyl–Werner Eqs. (2)–(4) in the [source locators](../science/theorem_source_locators.md#schur-probabilities-and-concentration).

### M10 — Finite energy in geometric modes

- **Central question:** How can an infinite occupation space still have finite mean excitation?
- **Understanding target:** Interpret a geometric occupation ratio strictly below one, its finite mean, and the energy gap attached to each level pair.
- **Dependencies and story role:** M01 and M04. Introduce the candidate fluctuation objects without assuming the limiting theorem.
- **Conceptual connection:** Strict population ordering creates decaying occupation tails; these tails will control the work objective.
- **Source pointers:** W1–2 for diagonal states and expectations; project [fluctuation state](../science/model_and_main_theorem.md#fluctuation-state); supplementary Kahn–Guţă §7.6 in the [source locators](../science/theorem_source_locators.md#exact-representation-theory-ingredients).

### M11 — State convergence versus energy convergence

- **Central question:** Why is closeness of states insufficient for an unbounded energy objective?
- **Understanding target:** Explain how a small probability at a large energy can retain finite energy, and why a uniform bound on omitted first moments is stronger than a small omitted probability.
- **Dependencies and story role:** M01 and M10. Identify the limiting argument's main analytical hazard.
- **Conceptual connection:** Norm control of states must be supplemented by energetic tail control before optimizing work in the oscillator limit.
- **Source pointers:** W3, norm and state-distinguishability foundations; [bridge: optimized energy limit](anchor_bridge.md#bridge-3-from-state-convergence-to-an-optimized-energy-limit); [uniform excitation and tails](../science/schur_tableau_spectrum.md#uniform-excitation-and-energy-tails).

### M12 — The complete fixed-ensemble question

- **Central question:** What exactly must be proved to distinguish finite collective work from extensive activation?
- **Understanding target:** Assemble the fixed source, Hamiltonian, allowed control, energy score and order of limits; separate total work from work per copy.
- **Dependencies and story role:** M01–M11. Synthesize the background into one operational problem.
- **Conceptual connection:** The interesting comparison holds even when collective controls may entangle copies; it is the fixed symmetry, rather than a product-control restriction, that survives.
- **Source pointers:** W4, §4.3.2 and W7, §7.1.2; [model and main theorem](../science/model_and_main_theorem.md); [science overview](../science/README.md).

## Narrative and contribution: M13-M30

### M13 — Sectorwise work optimization

- **Central question:** How does the global optimum become an average of sector optima?
- **Understanding target:** Explain sector normalization, multiplicity and probability, and why independently available block unitaries make the weighted optimization exact.
- **Dependencies and story role:** M03 and M09–M12. Begin the proof by reducing the full control problem.
- **Conceptual connection:** Fixed sector weights are the conserved part of the source; work can only exploit spectra within sectors.
- **Source pointers:** W7, §7.1.2; [Schur reduction and definitions of sector probabilities](../science/schur_tableau_spectrum.md#schur-reduction-of-the-optimization).

### M14 — Tableau occupations and the sector floor

- **Central question:** What do the root occupations count in a finite sector?
- **Understanding target:** Translate tableau entries into occupations, population ratios and excitation energies above the lowest sector energy.
- **Dependencies and story role:** M09–M10 and M13. Resolve the finite block into concrete joint spectral coordinates.
- **Conceptual connection:** The same tableau move changes a logarithmic population weight and an additive energy by paired amounts.
- **Source pointers:** W1–2 for joint diagonal spectra; [tableau occupation coordinates](../science/schur_tableau_spectrum.md#tableau-occupation-coordinates); supplementary Kahn–Guţă Theorem 5.2 and Eq. (5.9) in the [source locators](../science/theorem_source_locators.md#exact-representation-theory-ingredients).

### M15 — Exact spectra without an orthogonal tableau basis

- **Central question:** Why does a nonorthogonal representation basis not invalidate the spectral construction?
- **Understanding target:** Explain orthogonality of distinct torus weights, scalar action within each weight space, and the resulting joint spectral isometry.
- **Dependencies and story role:** M01 and M14. Establish the exact identification needed before taking any limit.
- **Conceptual connection:** Spectral equivalence of state and energy does not require exact identification of every raising and lowering operator with an oscillator.
- **Source pointers:** W1–2, orthonormal bases and spectral decompositions; [nonorthogonal tableau qualification](../science/schur_tableau_spectrum.md#why-a-nonorthogonal-tableau-basis-is-sufficient); [restricted geometric state](../science/schur_tableau_spectrum.md#exact-restricted-geometric-state).

### M16 — Stabilization of every finite occupation set

- **Central question:** Why does every fixed finite fluctuation operation eventually fit inside deep sectors?
- **Understanding target:** Explain how sufficiently large adjacent Young-row gaps permit any bounded collection of occupations, without assuming nested sector sets.
- **Dependencies and story role:** M14–M15. Build the bridge from finite tableaux to limiting constructions.
- **Conceptual connection:** A finite operation in the fluctuation space becomes a valid finite-sector unitary once the relevant occupation vectors exist there.
- **Source pointers:** W7 as symmetry background; the project [finite-set stabilization lemma](../science/schur_tableau_spectrum.md#elementary-stabilization-of-every-finite-occupation-set); attribution in the [source locators](../science/theorem_source_locators.md#exact-representation-theory-ingredients).

### M17 — A uniform bound on sector work

- **Central question:** Why can no sector supply arbitrarily large excitation work as the ensemble grows?
- **Understanding target:** Derive the role of the geometric normalization bound in uniformly dominating the sector excitation and its energy tail; distinguish the proved constant from a sharper unsupported one.
- **Dependencies and story role:** M10–M11 and M15. Establish the finite-work ceiling before proving convergence.
- **Conceptual connection:** Subtracting the sector floor isolates an energy budget that exact symmetric control can spend.
- **Source pointers:** W1–2 for nonnegative observables; [uniform excitation and tails](../science/schur_tableau_spectrum.md#uniform-excitation-and-energy-tails); [main theorem's non-sharp constant](../science/model_and_main_theorem.md#theorem-finite-collective-activation-work).

### M18 — Passive rearrangement on the full fluctuation space

- **Central question:** Does sorting an infinite state spectrum define an attainable finite energy minimum?
- **Understanding target:** Explain the projection inequality, the energy-tail integral and the unitary basis permutation that realizes the ordered minimum.
- **Dependencies and story role:** M03, M10–M11 and M17. Define the actual limiting optimization rather than just a candidate state.
- **Conceptual connection:** Finite spectral ordering extends through a controlled infinite argument, not through an assumed continuity of ergotropy.
- **Source pointers:** W4, §4.3.2 as finite-dimensional background; project [sorted-spectrum minimum](../science/passive_rearrangement.md#the-sorted-spectrum-minimum).

### M19 — The complete energy-cutoff certificate

- **Central question:** Which finite approximation gives a rigorous error on optimal work?
- **Understanding target:** Explain why sorting all states below an energy threshold, using their original unnormalized populations, leaves an error bounded by the omitted first moment.
- **Dependencies and story role:** M11 and M18. Make the infinite optimum finitely approximable with the right error budget.
- **Conceptual connection:** A complete low-energy list controls possible population inversions across the cutoff; an arbitrary occupation box need not.
- **Source pointers:** W4, §4.3.2 for spectral ordering; project [certified finite-cutoff approximation](../science/passive_rearrangement.md#a-certified-finite-cutoff-approximation).

### M20 — Convergence after optimization

- **Central question:** Why does the finite-sector work optimum converge to the fluctuation optimum?
- **Understanding target:** Distinguish the upper argument using ordered final energies from the lower argument embedding finite cutoff permutations, and explain why both are required.
- **Dependencies and story role:** M15–M19. Resolve the central energetic limiting step.
- **Conceptual connection:** Exact spectra, finite-set stabilization and energy control allow optimization and the deep-sector limit to be compared without tracking optimal unitaries.
- **Source pointers:** W3 and W4 as norm/ordering foundations; [deep-sector work convergence and uniformity](../science/fluctuation_limit.md#convergence-within-a-deep-sector).

### M21 — Typical Young sectors become deep

- **Central question:** Why are the sectors needed by the limiting proof typical for the actual iid source?
- **Understanding target:** Connect convergence of normalized Young shapes to the ordered source spectrum with diverging adjacent row gaps, using the fixed strict population gap.
- **Dependencies and story role:** M04, M09 and M16. Return from an individual sector to the physical ensemble distribution.
- **Conceptual connection:** Statistical concentration identifies where the energetic sector limit applies with probability tending to one.
- **Source pointers:** W7 for permutation algebra; supplementary Keyl–Werner Eqs. (10) and (17) in the [source locators](../science/theorem_source_locators.md#schur-probabilities-and-concentration); project [Schur concentration](../science/fluctuation_limit.md#concentration-of-the-schur-distribution).

### M22 — The many-copy finite-work law

- **Central question:** How do typical-sector convergence and a uniform bound establish the ensemble theorem?
- **Understanding target:** Explain the split into deep and rare sectors, and why a rare sector cannot hide a macroscopic work contribution under the uniform bound.
- **Dependencies and story role:** M13, M17 and M20–M21. Combine the proof's local parts into the global limit.
- **Conceptual connection:** Convergence of optimized sector work becomes convergence of the actual allowed ensemble work; dividing by copy number gives vanishing work density.
- **Source pointers:** W1–2 for expectations; [averaging the optimized work](../science/fluctuation_limit.md#averaging-the-optimized-work); [main theorem](../science/model_and_main_theorem.md#theorem-finite-collective-activation-work).

### M23 — Positive work precisely off the Gibbs family

- **Central question:** What physical mismatch makes the limiting work positive?
- **Understanding target:** Explain why common-temperature geometric modes are passive, and how unequal adjacent-mode inverse temperatures admit a finite population-energy inversion.
- **Dependencies and story role:** M04, M10, M16 and M22. Identify when the finite residue is a usable work resource.
- **Conceptual connection:** A finite inversion witness connects non-Gibbs source populations to attainable asymptotic work.
- **Source pointers:** W4, §4.3.2 as ordering background; project [Gibbs equivalence and rational inversion witness](../science/consequences.md#zero-fluctuation-work-exactly-for-gibbs-populations).

### M24 — A complete two-copy qutrit operation

- **Central question:** How does a symmetry-respecting unitary extract work from two passive qutrits?
- **Understanding target:** Track the two chosen eigenvectors, their populations and energies, the symmetric swap, and the extracted work of 33/400.
- **Dependencies and story role:** M03–M08 and M13. Ground the general mechanism in a complete finite operation.
- **Conceptual connection:** A coherent vector inside a permutation orbit enables a transformation absent from the restricted reversible classical basis model.
- **Source pointers:** W7, §7.1.1–2; [two-copy qutrit construction](../science/qutrit_example.md#two-copies-already-allow-extraction); [classical two-copy comparison](../science/classical_comparison.md#concrete-two-copy-separation).

### M25 — An explicit mode swap below the full optimum

- **Central question:** What does a simple fluctuation operation achieve in the qutrit limit?
- **Understanding target:** Explain the three geometric root modes, the work of swapping the 12 and 23 modes, and why 33/14 is a witness rather than the full ergotropy.
- **Dependencies and story role:** M10, M16, M22–M24. Connect the finite operation language to an asymptotic constructive lower bound.
- **Conceptual connection:** Finite restrictions of a mode swap can be embedded into deep sectors without claiming efficient physical compilation.
- **Source pointers:** W1–2 for diagonal tensor states; [qutrit limiting state and swap](../science/qutrit_example.md#the-limiting-state); [finite swap construction](../science/consequences.md#a-concrete-qutrit-extraction-operation).

### M26 — A certified number, not a fitted asymptote

- **Central question:** Why is the qutrit limiting value rigorously enclosed rather than inferred from finite-size data?
- **Understanding target:** Connect exact integer population sorting, complete-energy multiplicities and omitted energy tails to the certified enclosure near 2.894208160219019.
- **Dependencies and story role:** M19 and M25. Separate a numerical certificate from a plot or convergence fit.
- **Conceptual connection:** The analytical error certificate makes a finite computation informative about an infinite optimum, while projector checks independently test small finite sectors.
- **Source pointers:** W4 for spectral ordering; [qutrit enclosure](../science/qutrit_example.md#a-rigorous-numerical-enclosure); [verification account](../verification/README.md) and [saved exact results](../verification/results/certified_results.json).

### M27 — Separate single-copy work from activation

- **Central question:** What changes if the original source is not passive?
- **Understanding target:** Explain the exact decomposition into copy number times single-copy ergotropy plus the symmetric work of the passive rearrangement; retain the strict-spectrum qualification on its asymptotic corollary.
- **Dependencies and story role:** M02–M03, M08 and M22. Extend the interpretation without silently broadening the limiting theorem.
- **Conceptual connection:** A tensor power of the same local passivating unitary stays inside the allowed group and gives a bijection of its control set.
- **Source pointers:** W1–2 for tensor-product unitaries and W4 for passive rearrangement; project [arbitrary-input identity](../science/consequences.md#exact-identity-for-an-arbitrary-input-state).

### M28 — Control classes and extensive work

- **Central question:** How much fixed addressability is needed to escape the finite-work ceiling?
- **Understanding target:** Explain the bound proportional to the number of fixed control classes, including controls entangling classes, and the necessary linear class count for extensive passive-state work.
- **Dependencies and story role:** M09, M17 and M22. Translate sector protection into a statement about control resources.
- **Conceptual connection:** Preserving a tuple of Young labels keeps the excitation budget additive even when the available block unitary is entangling.
- **Source pointers:** W7, §7.1.2 as algebraic foundation; project [fixed control-class bound and scope](../science/consequences.md#a-fixed-partition-into-control-classes).

### M29 — The precisely restricted classical comparison

- **Central question:** Why does equivariant reversible basis processing lose even the finite quantum residue?
- **Understanding target:** Explain stabilizer preservation, the occupation-count multiset constraint and the exponentially rare disordered counts; identify the admitted reversible model before interpreting the comparison.
- **Dependencies and story role:** M05–M08, M23–M24. Connect the asymptotic quantum residue to an explicit, attributed comparator.
- **Conceptual connection:** Quantum superpositions inside orbits and reversible classical relabelings have different accessible transformations, without establishing a comparison against every thermodynamic classical device.
- **Source pointers:** W7, §7.1.1–2 for permutation actions; [classical model and inherited mechanism](../science/classical_comparison.md#model-and-inherited-mechanism), [stabilizer argument](../science/classical_comparison.md#stabilizers-force-preservation-of-the-count-multiset) and [exponential bound](../science/classical_comparison.md#exponential-upper-bound).

### M30 — The complete result and its boundaries

- **Central question:** What has the project established, and which changes would define a different task?
- **Understanding target:** Connect zero independent work, a positive finite symmetric limit off Gibbs, and extensive unrestricted activation; explain the roles of fixed gaps, a fixed ensemble and partition, exact per-unitary symmetry, and abstract control access.
- **Dependencies and story role:** M12–M29. Synthesize the proof, examples, attribution and operational consequence into the whole contribution.
- **Conceptual connection:** The conserved sector structure determines which part of passive fuel can be converted into mean work. Finite-size agreement, efficient implementation and exhaustive novelty are separate claims.
- **Source pointers:** W4, §4.3.2 and W7, §7.1.2; [main theorem and scope](../science/model_and_main_theorem.md), [physical consequences](../science/consequences.md), [related work](../references/RELATED_WORK.md), and [verification limits](../verification/README.md).

[Learning overview](README.md) · [Source bridge](anchor_bridge.md) · [Science overview](../science/README.md)
