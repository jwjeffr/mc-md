from ovito.io import import_file
from cowley_sro_parameters import nearest_neighbor_topology, sro_modifier
import numpy as np
import matplotlib.pyplot as plt


NUM_NEAREST_NEIGHBORS: int = 12
TYPE_MAP: dict[int, str] = {1: "Co", 2: "Ni", 3: "Cr", 4: "Fe", 5: "Mn"}


def main():

    pipeline = import_file("mc.dump")
    pipeline.modifiers.append(nearest_neighbor_topology(NUM_NEAREST_NEIGHBORS))
    pipeline.modifiers.append(sro_modifier(TYPE_MAP))

    data = pipeline.compute(pipeline.source.num_frames - 1)

    num_types = len(TYPE_MAP)
    sro_matrix = np.zeros((num_types, num_types), dtype=float)

    for i, first_element in TYPE_MAP.items():
        for j, second_element in TYPE_MAP.items():
            sro_matrix[i - 1, j - 1] = data.attributes[f"sro_{first_element}{second_element}"]

    plt.pcolormesh(TYPE_MAP.keys(), TYPE_MAP.keys(), sro_matrix, cmap="cividis", edgecolors="black")
    plt.gca().set_aspect("equal")

    for i in TYPE_MAP.keys():
        for j in TYPE_MAP.keys():
            sro_value = sro_matrix[i - 1, j - 1]
            if sro_value > 0.5:
                text_color = "black"
            else:
                text_color = "white"
            plt.text(i, j, f"{sro_value:.2f}", ha="center", va="center", color=text_color)

    plt.xticks(ticks=list(TYPE_MAP.keys()), labels=list(TYPE_MAP.values()))
    plt.yticks(ticks=list(TYPE_MAP.keys()), labels=list(TYPE_MAP.values()))
    plt.colorbar(label="Cowley SRO-parameter")
    plt.savefig("sro.pdf", bbox_inches="tight")


if __name__ == "__main__":

    main()

