# -----------------------------------
# CSC 315 / DSC 615
# Project 3 RANSAC Circles
#
# Alex Ramos
# -----------------------------------
import time
import numpy as np
import matplotlib.pyplot as plt
import random

pi = 3.14159265358979323846264


def GenPoints():
    n_circle = 5
    points_per_circle = 100
    noise_points = 200
    total_points = n_circle * points_per_circle + noise_points

    xy = np.random.uniform((-10.0, -10.0), (10.0, 10.0), (total_points, 2))

    for c in range(n_circle):
        xpos = random.uniform(-8.0, 8.0)
        ypos = random.uniform(-8.0, 8.0)
        radius = random.uniform(0.5, 2.0)
        spread = random.uniform(0.05, 0.2)

        thetas = np.random.uniform(0.0, 2 * pi, (points_per_circle,))
        rhos = np.random.normal(radius, spread, (points_per_circle,))

        circle_xy = np.zeros((points_per_circle, 2), dtype="float64")
        for i in range(points_per_circle):
            circle_xy[i][0] = xpos + rhos[i] * np.cos(thetas[i])
            circle_xy[i][1] = ypos + rhos[i] * np.sin(thetas[i])

        sidx = c * points_per_circle
        eidx = (c + 1) * points_per_circle
        idx = 0
        for k in range(sidx, eidx):
            xy[k] = circle_xy[idx]
            idx = idx + 1

    # Shuffle points
    for i in range(total_points):
        j = random.randint(i, total_points - 1)
        temp = np.array(xy[i])
        xy[i] = xy[j]
        xy[j] = temp

    return xy


def circle_from_3_points(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    if abs(d) < 1e-10:
        return None

    x1s = x1 * x1 + y1 * y1
    x2s = x2 * x2 + y2 * y2
    x3s = x3 * x3 + y3 * y3

    cx = (x1s * (y2 - y3) + x2s * (y3 - y1) + x3s * (y1 - y2)) / d
    cy = (x1s * (x3 - x2) + x2s * (x1 - x3) + x3s * (x2 - x1)) / d
    r = np.sqrt((x1 - cx) ** 2 + (y1 - cy) ** 2)
    return cx, cy, r


def ransac_one_circle(xy, iterations=1400, inlier_threshold=0.20):
    n = len(xy)
    if n < 3:
        return None

    best_model = None
    best_score = -1

    for _ in range(iterations):
        i1 = random.randint(0, n - 1)
        i2 = random.randint(0, n - 1)
        i3 = random.randint(0, n - 1)

        if i1 == i2 or i1 == i3 or i2 == i3:
            continue

        circle = circle_from_3_points(xy[i1], xy[i2], xy[i3])
        if circle is None:
            continue

        cx, cy, r = circle
        if r < 0.3 or r > 3.5:
            continue

        dx = []
        dy = []
        for p in xy:
            dx.append(p[0] - cx)
            dy.append(p[1] - cy)
        dx = np.array(dx)
        dy = np.array(dy)
        dist = np.sqrt(dx * dx + dy * dy)
        err = np.abs(dist - r)
        inliers = err <= inlier_threshold
        score = int(np.sum(inliers))

        if score > best_score:
            best_score = score
            best_model = {
                "cx": cx,
                "cy": cy,
                "r": r,
                "score": score,
                "inliers": inliers,
            }

    return best_model


def detect_5_circles(xy):
    found = []
    remaining = xy.copy()

    for _ in range(5):
        model = ransac_one_circle(remaining)
        if model is None:
            break

        if model["score"] < 45:
            break

        inlier_points = remaining[model["inliers"]]

        found.append(
            {
                "cx": model["cx"],
                "cy": model["cy"],
                "r": model["r"],
                "inlier_points": inlier_points,
            }
        )

        # remove near points so same circle is not found again
        new_remaining = []
        for i in range(len(remaining)):
            if model["inliers"][i] == False:
                new_remaining.append(remaining[i])
        remaining = np.array(new_remaining)

        if len(remaining) < 3:
            break

    return found


def draw_interval(ax, cx, cy, r, inlier_points, color):
    if len(inlier_points) < 2:
        return

    angles = []
    for p in inlier_points:
        a = np.arctan2(p[1] - cy, p[0] - cx)
        angles.append(a)

    angles.sort()
    t = np.linspace(angles[0], angles[-1], 100)
    x = cx + r * np.cos(t)
    y = cy + r * np.sin(t)
    ax.plot(x, y, "--", color=color, linewidth=2)


def plot_run(run_number, xy, circles):
    plt.figure(figsize=(8.0, 8.0))
    plt.scatter(xy[:, 0], xy[:, 1], c="black", s=10)

    colors = ["red", "blue", "green", "orange", "purple"]
    t = np.linspace(0, 2 * pi, 250)

    for i in range(len(circles)):
        c = circles[i]
        color = colors[i]

        x = c["cx"] + c["r"] * np.cos(t)
        y = c["cy"] + c["r"] * np.sin(t)
        plt.plot(x, y, color=color, linewidth=2)

        draw_interval(plt.gca(), c["cx"], c["cy"], c["r"], c["inlier_points"], color)

    plt.title("Run " + str(run_number))
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.gca().set_aspect("equal", adjustable="box")


def main():
    n_runs = 5
    times = []

    for run in range(n_runs):
        xy = GenPoints()

        t0 = time.time()
        circles = detect_5_circles(xy)
        elapsed = time.time() - t0
        times.append(elapsed)

        print(
            "Run",
            run + 1,
            ": found",
            len(circles),
            "circles in",
            round(elapsed, 3),
            "seconds",
        )
        plot_run(run + 1, xy, circles)

    print("Average time per run:", round(float(np.mean(times)), 3), "seconds")
    plt.show()
    print("Done!")


if __name__ == "__main__":
    main()
