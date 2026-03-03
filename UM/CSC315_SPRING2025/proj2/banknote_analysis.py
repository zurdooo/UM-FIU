"""
CSC 315/615 Project 2 - Counterfeit Money Analysis
Name: Alex Ramos
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# dataset file (relative to repo root)
DATA_PATH = "UM/CSC315_SPRING2025/proj2/data_banknote_authentication.csv"
FEATURES = ["variance", "skewness", "kurtosis", "entropy"]
LABELS = {0: "real", 1: "counterfeit"}


def load_data():
    # load csv and clean up any bad rows
    df = pd.read_csv(DATA_PATH, names=FEATURES + ["class"])
    df = df.apply(pd.to_numeric)
    df = df.dropna().reset_index(drop=True)
    df["class"] = df["class"].astype(int)
    return df


def compute_centroids(df):
    # average of each feature per class
    return df.groupby("class")[FEATURES].mean()


def compute_stds(df):
    # standard deviations for gaussian classifier
    return df.groupby("class")[FEATURES].std(ddof=0)


def classify_distance(df, centroids):
    # classify by distance to the two centroids
    features = df[FEATURES].to_numpy()
    real_centroid = centroids.loc[0].to_numpy()
    fake_centroid = centroids.loc[1].to_numpy()

    dist_real = np.linalg.norm(features - real_centroid, axis=1)
    dist_fake = np.linalg.norm(features - fake_centroid, axis=1)

    predictions = []
    for i in range(len(dist_real)):
        if dist_real[i] <= dist_fake[i]:
            predictions.append(0)
        else:
            predictions.append(1)

    return np.array(predictions)


def classify_gaussian(df, centroids, stds):
    # classify using gaussian probability
    features = df[FEATURES].to_numpy()
    epsilon = 1e-6

    def log_prob(class_id):
        # log probability for one class
        means = centroids.loc[class_id].to_numpy()
        sigmas = np.maximum(stds.loc[class_id].to_numpy(), epsilon)
        z = (features - means) / sigmas
        return -0.5 * np.sum(np.log(2 * np.pi) + 2 * np.log(sigmas) + z**2, axis=1)

    log_real = log_prob(0)
    log_fake = log_prob(1)

    predictions = []
    for i in range(len(log_real)):
        if log_real[i] >= log_fake[i]:
            predictions.append(0)
        else:
            predictions.append(1)

    return np.array(predictions)


def build_colors(actual, predicted):
    # color map for correct/incorrect predictions
    colors = np.empty(actual.shape, dtype=object)
    real = actual == 0
    fake = actual == 1
    pred_real = predicted == 0

    colors[real & pred_real] = "#8888ff"
    colors[real & ~pred_real] = "#ccccff"
    colors[fake & pred_real] = "#ffcccc"
    colors[fake & ~pred_real] = "#ff8888"
    return colors


def add_centroid_annotation(ax, centroid, x_feature, y_feature, label):
    # mark centroid with X and label
    cx = centroid[x_feature]
    cy = centroid[y_feature]
    ax.scatter(cx, cy, marker="x", color="black", s=90, linewidths=2)

    y_min, y_max = ax.get_ylim()
    offset = (y_max - y_min) * 0.05
    ax.text(cx, cy - offset, label, ha="center", va="top", fontsize=9)


def plot_results(df, predicted, centroids, accuracy, classifier_name):
    # draw the 6 scatter plots
    pairs = [
        ("variance", "skewness"),
        ("variance", "kurtosis"),
        ("variance", "entropy"),
        ("skewness", "kurtosis"),
        ("skewness", "entropy"),
        ("kurtosis", "entropy"),
    ]

    colors = build_colors(df["class"].to_numpy(), predicted)
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    fig.suptitle(f"Banknote Authentication ({classifier_name} classifier)")

    index = 0
    for row in range(2):
        for col in range(3):
            ax = axes[row][col]
            x_feature, y_feature = pairs[index]
            index += 1

            ax.scatter(df[x_feature], df[y_feature], c=colors, s=18)
            ax.set_title(f"{x_feature} vs {y_feature} ({accuracy:.2f}%)")
            ax.set_xlabel(x_feature)
            ax.set_ylabel(y_feature)

            add_centroid_annotation(
                ax, centroids.loc[0], x_feature, y_feature, "real"
            )
            add_centroid_annotation(
                ax, centroids.loc[1], x_feature, y_feature, "counterfeit"
            )

    fig.tight_layout(rect=(0, 0.03, 1, 0.95))

    plt.show()
    plt.close(fig)


def main():
    # ask user which classifier to use
    classifier = input("Enter classifier (distance/gaussian): ").strip().lower()

    # Default is distance
    if classifier not in ("distance", "gaussian"):
        classifier = "distance"

    df = load_data()
    centroids = compute_centroids(df)

    if classifier == "gaussian":
        stds = compute_stds(df)
        predicted = classify_gaussian(df, centroids, stds)
    else:
        predicted = classify_distance(df, centroids)

    accuracy = float((predicted == df["class"].to_numpy()).mean() * 100)

    plot_results(df, predicted, centroids, accuracy, classifier)

    print(f"Accuracy ({classifier}): {accuracy:.2f}%")


if __name__ == "__main__":
    main()
