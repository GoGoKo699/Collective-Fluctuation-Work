#!/usr/bin/env python3
"""Exact numerical certificates for collective fluctuation work (qutrit example).

The certificates and finite-size enumerations use integer arithmetic only.
NumPy is used solely for independent low-n central-projector checks; Matplotlib
is an optional plotting dependency. No Monte Carlo or arbitrary precision
floating-point ordering is used in any claimed rigorous interval.

Run from any directory:
    python certify_collective_work.py --output-dir ./results

Default source: p=(12,5,3)/20, E=(0,1,5).
The root-mode labels (u,v) have multiplicity min(u,v)+1, probability
    (7/40) (5/12)^u (3/5)^v,
and energy u+4v. Every energy-cutoff state is included, including degeneracies.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations, product
import json
import math
from pathlib import Path
import platform
import time


P_NUM = (12, 5, 3)
P_DEN = 20
ENERGIES = (0, 1, 5)
FINITE_SIZES = (1, 2, 3, 4, 6, 10, 20, 30, 40, 60)


def fixed_decimal(value: Fraction, digits: int, upward: bool = False) -> str:
    """A genuinely directed decimal conversion, using integer division."""
    scale = 10 ** digits
    q, remainder = divmod(value.numerator * scale, value.denominator)
    if upward and remainder:
        q += 1
    sign = "-" if q < 0 else ""
    q = abs(q)
    whole, tail = divmod(q, scale)
    return f"{sign}{whole}.{tail:0{digits}d}"


def fraction_record(value: Fraction, digits: int = 18) -> dict:
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
        "decimal_lower": fixed_decimal(value, digits),
        "decimal_upper": fixed_decimal(value, digits, upward=True),
    }


def dot_population_energy(groups, energy_counts):
    """Minimum energy numerator for integer populations and integer energies.

    groups contains (population_numerator, multiplicity), and every population
    shares a common denominator. energy_counts maps energy to multiplicity.
    All sorting and population-energy pairing are exact.
    """
    groups = sorted(groups, reverse=True)
    energy_groups = sorted(energy_counts.items())
    assert sum(count for _, count in groups) == sum(energy_counts.values())
    e_index = 0
    current_energy, capacity = energy_groups[0]
    total = 0
    for population, count in groups:
        while count:
            take = min(count, capacity)
            total += population * current_energy * take
            count -= take
            capacity -= take
            if capacity == 0:
                e_index += 1
                if e_index < len(energy_groups):
                    current_energy, capacity = energy_groups[e_index]
    assert e_index == len(energy_groups)
    return total


def root_energy_certificate(cutoff: int) -> dict:
    """Exact W_cut <= W_infinity <= W_cut + omitted initial energy."""
    max_v = cutoff // 4
    # Common denominator for all (7/40)(5/12)^u(3/5)^v with u+4v<=cutoff.
    denominator = 40 * 12 ** cutoff * 5 ** max_v
    powers12 = [12 ** j for j in range(cutoff + 1)]
    powers5 = [5 ** j for j in range(cutoff + max_v + 1)]
    powers3 = [3 ** j for j in range(max_v + 1)]
    populations = []
    energy_counts = Counter()
    trace_numerator = energy_numerator = 0
    labels = 0
    for v in range(max_v + 1):
        for u in range(cutoff - 4 * v + 1):
            multiplicity = min(u, v) + 1
            weight = (
                7 * powers12[cutoff - u]
                * powers5[max_v + u - v] * powers3[v]
            )
            energy = u + 4 * v
            populations.append((weight, multiplicity))
            energy_counts[energy] += multiplicity
            trace_numerator += weight * multiplicity
            energy_numerator += weight * multiplicity * energy
            labels += 1
    passive_numerator = dot_population_energy(populations, energy_counts)
    trace = Fraction(trace_numerator, denominator)
    initial_energy = Fraction(energy_numerator, denominator)
    passive_energy = Fraction(passive_numerator, denominator)
    work = initial_energy - passive_energy
    full_mean_energy = Fraction(176, 21)
    omitted_energy = full_mean_energy - initial_energy
    upper = work + omitted_energy
    assert 0 < trace <= 1
    assert omitted_energy >= 0 and work >= 0
    return {
        "energy_cutoff": cutoff,
        "basis_dimension": sum(energy_counts.values()),
        "distinct_weight_labels": labels,
        "retained_probability": fraction_record(trace),
        "omitted_probability": fraction_record(1 - trace),
        "initial_energy_inside": fraction_record(initial_energy),
        "passive_energy_inside": fraction_record(passive_energy),
        "finite_permutation_work": fraction_record(work),
        "omitted_initial_energy": fraction_record(omitted_energy),
        "work_interval": {
            "lower_exact": fraction_record(work),
            "upper_exact": fraction_record(upper),
            "lower_decimal": fixed_decimal(work, 15),
            "upper_decimal": fixed_decimal(upper, 15, upward=True),
            "width_exact": fraction_record(omitted_energy, 30),
        },
    }


def partitions3(n: int):
    for c in range(n // 3 + 1):
        for b in range(c, (n - c) // 2 + 1):
            yield (n - b - c, b, c)


def symmetric_group_multiplicity(lam) -> int:
    a, b, c = lam
    numerator = math.factorial(a + b + c) * (a - b + 1) * (a - c + 2) * (b - c + 1)
    denominator = math.factorial(a + 2) * math.factorial(b + 1) * math.factorial(c)
    value, remainder = divmod(numerator, denominator)
    assert remainder == 0
    return value


def gt_weight_multiplicities(lam):
    a, b, c = lam
    n = a + b + c
    weights = Counter()
    for u in range(b, a + 1):
        for v in range(c, b + 1):
            for z in range(v, u + 1):
                weights[(z, u + v - z, n - u - v)] += 1
    expected_dimension = (a - b + 1) * (a - c + 2) * (b - c + 1) // 2
    assert sum(weights.values()) == expected_dimension
    return weights


def schur_exact(n: int, p_num=P_NUM, p_den=P_DEN, energies=ENERGIES, save_sectors=False):
    assert sum(p_num) == p_den
    denominator = p_den ** n
    powers = [[p ** j for j in range(n + 1)] for p in p_num]
    trace_numerator = initial_numerator = work_numerator = surplus_numerator = 0
    enumerated_states = hilbert_dimension = 0
    sectors = []
    for lam in partitions3(n):
        m_lam = symmetric_group_multiplicity(lam)
        weights = gt_weight_multiplicities(lam)
        energy_counts = Counter()
        populations = []
        sector_trace = sector_initial = 0
        floor = sum(l * e for l, e in zip(lam, energies))
        for weight, count in weights.items():
            pop = math.prod(powers[i][weight[i]] for i in range(3))
            energy = sum(w * e for w, e in zip(weight, energies))
            assert energy >= floor
            populations.append((pop, count))
            energy_counts[energy] += count
            sector_trace += pop * count
            sector_initial += pop * count * energy
        sector_passive = dot_population_energy(populations, energy_counts)
        dim = sum(weights.values())
        enumerated_states += dim
        hilbert_dimension += m_lam * dim
        trace_numerator += m_lam * sector_trace
        initial_numerator += m_lam * sector_initial
        work_numerator += m_lam * (sector_initial - sector_passive)
        surplus_numerator += m_lam * (sector_initial - floor * sector_trace)
        if save_sectors:
            sectors.append({
                "young_diagram": list(lam), "irrep_dimension": dim,
                "multiplicity": m_lam,
                "probability": fraction_record(Fraction(m_lam * sector_trace, denominator)),
                "work_contribution": fraction_record(Fraction(m_lam * (sector_initial - sector_passive), denominator)),
            })
    assert trace_numerator == denominator
    assert hilbert_dimension == 3 ** n
    assert Fraction(initial_numerator, denominator) == n * sum(Fraction(p, p_den) * e for p, e in zip(p_num, energies))
    result = {
        "n": n, "trace_exact": "1", "hilbert_dimension": str(hilbert_dimension),
        "enumerated_irrep_states": enumerated_states,
        "work": fraction_record(Fraction(work_numerator, denominator)),
        "energy_above_sector_ground": fraction_record(Fraction(surplus_numerator, denominator)),
    }
    if save_sectors:
        result["sectors"] = sectors
    return result


def all_types(n: int):
    factorials = [math.factorial(j) for j in range(n + 1)]
    powers = [[p ** j for j in range(n + 1)] for p in P_NUM]
    for c in range(n + 1):
        for b in range(n - c + 1):
            a = n - b - c
            multiplicity = factorials[n] // (factorials[a] * factorials[b] * factorials[c])
            population = powers[0][a] * powers[1][b] * powers[2][c]
            energy = b + 5 * c
            yield (a, b, c), multiplicity, population, energy


def unrestricted_and_classical_exact(n: int):
    """Exact type-grouped sorting, with no enumeration of 3**n basis states.

    An equivariant bijection preserves a word's stabilizer, hence the multiset
    of its symbol counts. Conversely, any two type orbits in a count-multiset
    block are equivariantly isomorphic, and arbitrary permutations of these
    orbits are realizable. Their orbit sizes are equal, so population-energy
    sorting within each block is the exact basis-permutation optimum.
    """
    groups = []
    energies = Counter()
    classical_blocks = defaultdict(list)
    initial = 0
    for counts, multiplicity, population, energy in all_types(n):
        groups.append((population, multiplicity))
        energies[energy] += multiplicity
        initial += population * multiplicity * energy
        classical_blocks[tuple(sorted(counts, reverse=True))].append((population, multiplicity, energy))
    unrestricted_passive = dot_population_energy(groups, energies)
    classical_passive = 0
    for block in classical_blocks.values():
        assert len({multiplicity for _, multiplicity, _ in block}) == 1
        block_groups = [(p, m) for p, m, e in block]
        block_energies = Counter()
        for p, m, e in block:
            block_energies[e] += m
        classical_passive += dot_population_energy(block_groups, block_energies)
    denominator = P_DEN ** n
    assert initial == n * denominator  # the example's one-copy mean energy is one
    return {
        "unrestricted_work": fraction_record(Fraction(initial - unrestricted_passive, denominator)),
        "classical_equivariant_work": fraction_record(Fraction(initial - classical_passive, denominator)),
    }


def cycle_type(perm):
    seen = set()
    lengths = []
    for start in range(len(perm)):
        if start in seen:
            continue
        current = start
        length = 0
        while current not in seen:
            seen.add(current)
            length += 1
            current = perm[current]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


# Character tables of S_n, n<=4. Rows are partitions; columns are cycle types.
CHARACTERS = {
    1: {(1,): {(1,): 1}},
    2: {(2,): {(1, 1): 1, (2,): 1}, (1, 1): {(1, 1): 1, (2,): -1}},
    3: {
        (3,): {(1, 1, 1): 1, (2, 1): 1, (3,): 1},
        (2, 1): {(1, 1, 1): 2, (2, 1): 0, (3,): -1},
        (1, 1, 1): {(1, 1, 1): 1, (2, 1): -1, (3,): 1},
    },
    4: {
        (4,): {(1, 1, 1, 1): 1, (2, 1, 1): 1, (2, 2): 1, (3, 1): 1, (4,): 1},
        (3, 1): {(1, 1, 1, 1): 3, (2, 1, 1): 1, (2, 2): -1, (3, 1): 0, (4,): -1},
        (2, 2): {(1, 1, 1, 1): 2, (2, 1, 1): 0, (2, 2): 2, (3, 1): -1, (4,): 0},
        (2, 1, 1): {(1, 1, 1, 1): 3, (2, 1, 1): -1, (2, 2): -1, (3, 1): 0, (4,): 1},
    },
}


def direct_low_n_projectors(n: int):
    """Independent tensor-space projector verification; all arithmetic integer.

    Q_lam=n! P_lam=m_lam sum_pi chi_lam(pi) U_pi. Check exact projector
    identities and extract weight multiplicities from traces on type spaces.
    """
    import numpy as np

    words = list(product(range(3), repeat=n))
    indices = {word: i for i, word in enumerate(words)}
    dim = len(words)
    order = math.factorial(n)
    matrices = []
    for perm in permutations(range(n)):
        mat = np.zeros((dim, dim), dtype=np.int64)
        for column, word in enumerate(words):
            moved = tuple(word[perm[j]] for j in range(n))
            mat[indices[moved], column] = 1
        matrices.append((cycle_type(perm), mat))
    type_indices = defaultdict(list)
    for i, word in enumerate(words):
        type_indices[tuple(word.count(j) for j in range(3))].append(i)
    projectors = {}
    total_work = 0
    details = []
    for short_lam, table in CHARACTERS[n].items():
        lam = short_lam + (0,) * (3 - len(short_lam))
        multiplicity = table[(1,) * n]
        q = multiplicity * sum((table[ct] * mat for ct, mat in matrices), np.zeros((dim, dim), dtype=np.int64))
        assert np.array_equal(q @ q, order * q)
        assert np.array_equal(q, q.T)
        projectors[lam] = q
        gt = gt_weight_multiplicities(lam)
        populations = []
        energy_counts = Counter()
        initial = 0
        for weight, positions in type_indices.items():
            trace_q = int(sum(q[i, i] for i in positions))
            rank, remainder = divmod(trace_q, order)
            assert remainder == 0
            assert rank == multiplicity * gt.get(weight, 0)
            if rank:
                population = math.prod(P_NUM[i] ** weight[i] for i in range(3))
                energy = weight[1] + 5 * weight[2]
                populations.append((population, rank))
                energy_counts[energy] += rank
                initial += population * rank * energy
        passive = dot_population_energy(populations, energy_counts)
        total_work += initial - passive
        details.append({"young_diagram": list(lam), "tensor_space_rank": int(np.trace(q)) // order})
    assert np.array_equal(sum(projectors.values()), order * np.eye(dim, dtype=np.int64))
    labels = list(projectors)
    for i, left in enumerate(labels):
        for right in labels[i + 1:]:
            assert np.count_nonzero(projectors[left] @ projectors[right]) == 0
    expected = schur_exact(n)["work"]
    assert Fraction(total_work, P_DEN ** n) == Fraction(int(expected["numerator"]), int(expected["denominator"]))
    return {"n": n, "projector_checks": "exact integer identities passed", "all_weight_multiplicities_match": True,
            "direct_work": fraction_record(Fraction(total_work, P_DEN ** n)), "sectors": details}


def gibbs_zero_checks():
    # beta=log(2), H=(0,1,5): p=(32,16,1)/49, so p^mu is a decreasing
    # function of the exact energy, independent of the sector.
    rows = []
    for n in (2, 4, 10):
        result = schur_exact(n, p_num=(32, 16, 1), p_den=49)
        assert result["work"]["numerator"] == "0"
        rows.append({"n": n, "work_exact": "0"})
    cutoff = 40
    denominator = 2 ** cutoff
    groups = []
    energy_counts = Counter()
    initial = 0
    for v in range(cutoff // 4 + 1):
        for u in range(cutoff - 4 * v + 1):
            energy = u + 4 * v
            count = min(u, v) + 1
            population = 2 ** (cutoff - energy)
            groups.append((population, count))
            energy_counts[energy] += count
            initial += population * count * energy
    assert dot_population_energy(groups, energy_counts) == initial
    return {"p_exact": ["32/49", "16/49", "1/49"], "beta_exact": "log(2)",
            "finite_n": rows, "root_energy_cutoff": cutoff, "root_work_exact": "0"}


def finite_root_mode_swap(cut: int) -> Fraction:
    """Swap modes12 and23 inside the invariant cube 0<=a,b,c<=cut."""
    r = Fraction(5, 12)
    t = Fraction(3, 5)
    middle = sum(Fraction(1, 4) ** b for b in range(cut + 1))
    total = sum((c - a) * r ** a * t ** c for a in range(cut + 1) for c in range(cut + 1))
    return Fraction(21, 40) * middle * total


def scientific_figure(data, output_dir: Path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    def val(rec):
        return float(Fraction(int(rec["numerator"]), int(rec["denominator"])))

    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 10.5,
        "axes.labelsize": 11, "axes.titlesize": 11.5,
        "axes.spines.top": False, "axes.spines.right": False,
        "pdf.fonttype": 42, "ps.fonttype": 42,
    })
    rows = data["finite_n"]
    ns = np.array([r["n"] for r in rows])
    sym = np.array([val(r["work"]) for r in rows])
    unr = np.array([val(r["unrestricted_work"]) for r in rows])
    cls = np.array([val(r["classical_equivariant_work"]) for r in rows])
    limit = val(data["root_certificates"][-1]["work_interval"]["lower_exact"])
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.15), constrained_layout=True)
    blue, orange, gray = "#1D5C96", "#C66B28", "#66717B"
    ax = axes[0]
    ax.plot(ns, unr, "s-", color=orange, lw=1.6, ms=4, label="Unrestricted unitary work")
    ax.plot(ns, sym, "o-", color=blue, lw=1.9, ms=4.5, label="Permutation-invariant quantum work")
    ax.plot(ns, cls, "^-", color=gray, lw=1.5, ms=4, label="Equivariant basis-permutation work")
    ax.axhline(limit, color=blue, ls=(0, (4, 3)), lw=1.3,
               label=rf"Certified quantum limit $W_\infty\simeq{limit:.6f}$")
    ax.set(xlabel="Number of copies $n$", ylabel="Extracted work", title="(a) Exact finite-ensemble optimization")
    ax.set_xlim(0, 61)
    ax.set_ylim(bottom=0)
    ax.grid(axis="y", alpha=.16)
    ax.legend(frameon=False, fontsize=8.5, loc="upper left")
    ax = axes[1]
    ax.plot(ns, sym / ns, "o-", color=blue, lw=1.9, ms=4.5, label="Permutation-invariant quantum")
    ax.plot(ns, unr / ns, "s-", color=orange, lw=1.6, ms=4, label="Unrestricted quantum")
    ax.plot(ns, cls / ns, "^-", color=gray, lw=1.5, ms=4, label="Equivariant basis permutations")
    ax.set(xlabel="Number of copies $n$", ylabel="Extracted work per copy", title="(b) Work density")
    ax.set_xlim(0, 61)
    ax.set_ylim(bottom=0)
    ax.grid(axis="y", alpha=.16)
    ax.legend(frameon=False, fontsize=8.5, loc="center right", bbox_to_anchor=(.99, .66))
    fig.suptitle(r"Passive qutrit fuel: $p=(0.60,0.25,0.15)$, $E=(0,1,5)$", fontsize=12)
    fig.savefig(output_dir / "collective_work_finite_size.pdf")
    fig.savefig(output_dir / "collective_work_finite_size.svg")
    fig.savefig(output_dir / "collective_work_finite_size.png", dpi=200)
    plt.close(fig)
    return {"matplotlib": matplotlib.__version__, "numpy": np.__version__}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent / "results")
    parser.add_argument("--figure-dir", type=Path, default=None,
                        help="Figure destination; defaults to --output-dir")
    parser.add_argument("--plot-from", type=Path, default=None,
                        help="Regenerate figures from a saved results JSON, without rerunning numerical checks")
    parser.add_argument("--skip-plot", action="store_true")
    parser.add_argument("--root-cutoff", type=int, default=320)
    parser.add_argument("--sizes", type=int, nargs="+", default=list(FINITE_SIZES))
    args = parser.parse_args()
    if args.plot_from is not None:
        figure_dir = args.figure_dir or args.output_dir
        figure_dir.mkdir(parents=True, exist_ok=True)
        data = json.loads(args.plot_from.read_text())
        scientific_figure(data, figure_dir)
        print(f"Regenerated PNG, PDF and SVG in {figure_dir} from {args.plot_from}", flush=True)
        return
    args.output_dir.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    rows = []
    for n in args.sizes:
        row = schur_exact(n, save_sectors=(n <= 4))
        row.update(unrestricted_and_classical_exact(n))
        rows.append(row)
        print(f"n={n:2d}: symmetric work {row['work']['decimal_lower']}, exact trace 1", flush=True)
    certificates = [root_energy_certificate(r) for r in sorted(set((80, args.root_cutoff)))]
    for certificate in certificates:
        interval = certificate["work_interval"]
        print(f"root cutoff {certificate['energy_cutoff']}: [{interval['lower_decimal']}, {interval['upper_decimal']}]", flush=True)
    assert Fraction(int(certificates[-1]["work_interval"]["width_exact"]["numerator"]),
                    int(certificates[-1]["work_interval"]["width_exact"]["denominator"])) < Fraction(1, 10 ** 12)
    direct = [direct_low_n_projectors(n) for n in (1, 2, 3, 4)]
    data = {
        "model": {"p_exact": ["3/5", "1/4", "3/20"], "energies": list(ENERGIES),
                  "root_ratios_exact": ["5/12", "1/4", "3/5"], "root_gaps": [1, 5, 4],
                  "root_mean_energy_exact": "176/21"},
        "finite_n": rows,
        "root_certificates": certificates,
        "direct_low_n_checks": direct,
        "gibbs_zero_checks": gibbs_zero_checks(),
        "explicit_extraction": {
            "two_copy_symmetric_swap_work": fraction_record(Fraction(33, 400)),
            "single_root_basis_swap_work": fraction_record(Fraction(77, 800)),
            "entire_root_mode_swap_work": fraction_record(Fraction(33, 14)),
            "finite_cube_root_mode_swaps": [
                {"occupation_cutoff": c, "work": fraction_record(finite_root_mode_swap(c))}
                for c in (1, 3, 8, 20)
            ],
        },
        "reproducibility": {"python": platform.python_version(), "platform": platform.platform(),
                            "arithmetic": "Exact Python integers and fractions; directed decimal endpoints by integer division",
                            "dependencies_for_certificate_and_finite_size": "Python standard library",
                            "dependencies_for_direct_projector_check": "NumPy (integer matrix multiplication)",
                            "wall_seconds_before_plot": time.perf_counter() - started},
    }
    if not args.skip_plot:
        figure_dir = args.figure_dir or args.output_dir
        figure_dir.mkdir(parents=True, exist_ok=True)
        data["reproducibility"].update(scientific_figure(data, figure_dir))
    (args.output_dir / "certified_results.json").write_text(json.dumps(data, indent=2) + "\n")
    print(f"Saved {args.output_dir / 'certified_results.json'}", flush=True)


if __name__ == "__main__":
    main()
