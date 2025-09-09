#!/usr/bin/env python3
"""
Script to create charts for close-ended survey results
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

# Set style
plt.style.use("default")
sns.set_palette("husl")


def create_question_chart(data, question, title, chart_type="bar", save_path=None):
    """Create a chart for a specific question"""

    # Filter data for the question
    q_data = data[data["item"] == question].copy()

    if q_data.empty:
        print(f"No data found for {question}")
        return

    # Sort by percentage for better visualization
    q_data = q_data.sort_values("percent", ascending=True)

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))

    if chart_type == "bar":
        # Horizontal bar chart
        bars = ax.barh(
            q_data["option"],
            q_data["percent"],
            color=sns.color_palette("husl", len(q_data)),
        )

        # Add value labels on bars
        for i, (bar, value) in enumerate(zip(bars, q_data["percent"])):
            ax.text(
                bar.get_width() + 1,
                bar.get_y() + bar.get_height() / 2,
                f"{value}%",
                va="center",
                fontweight="bold",
            )

        ax.set_xlabel("Percentage (%)")
        ax.set_xlim(0, max(q_data["percent"]) * 1.15)

    elif chart_type == "pie":
        # Pie chart
        wedges, texts, autotexts = ax.pie(
            q_data["percent"], labels=q_data["option"], autopct="%1.0f%%", startangle=90
        )

        # Make percentage text bold
        for autotext in autotexts:
            autotext.set_fontweight("bold")
            autotext.set_fontsize(10)

    # Customize
    ax.set_title(title, fontsize=14, fontweight="bold", pad=20)

    # Add sample size info
    total_n = q_data["n"].sum()
    fig.suptitle(f"Total Responses: {total_n}", fontsize=10, y=0.95, alpha=0.7)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"Saved chart: {save_path}")

    return fig


def create_summary_dashboard(data, save_path=None):
    """Create a summary dashboard with all questions"""

    # Get unique questions
    questions = data["item"].unique()

    # Create subplots
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    axes = axes.flatten()

    question_titles = {
        "Q7": "Fair Compensation (Q7)",
        "Q8": "Basic Needs Met (Q8)",
        "Q9": "Task Rejected/Unpaid (Q9)",
        "Q10": "Disturbing Content Frequency (Q10)",
        "Q11": "Platform Transparency (Q11)",
    }

    for i, question in enumerate(questions):
        if i >= len(axes):
            break

        q_data = data[data["item"] == question].copy()
        q_data = q_data.sort_values("percent", ascending=True)

        # Create horizontal bar chart
        bars = axes[i].barh(
            q_data["option"],
            q_data["percent"],
            color=sns.color_palette("husl", len(q_data)),
        )

        # Add value labels
        for bar, value in zip(bars, q_data["percent"]):
            axes[i].text(
                bar.get_width() + 1,
                bar.get_y() + bar.get_height() / 2,
                f"{value}%",
                va="center",
                fontweight="bold",
                fontsize=9,
            )

        axes[i].set_title(
            question_titles.get(question, question), fontweight="bold", fontsize=11
        )
        axes[i].set_xlabel("Percentage (%)", fontsize=9)
        axes[i].set_xlim(0, max(q_data["percent"]) * 1.15)

        # Add sample size
        total_n = q_data["n"].sum()
        axes[i].text(
            0.02,
            0.98,
            f"n={total_n}",
            transform=axes[i].transAxes,
            fontsize=8,
            verticalalignment="top",
            alpha=0.7,
        )

    # Hide unused subplots
    for i in range(len(questions), len(axes)):
        axes[i].set_visible(False)

    plt.suptitle("Close-Ended Survey Results Summary", fontsize=16, fontweight="bold")
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"Saved dashboard: {save_path}")

    return fig


def create_comprehensive_chart(data, save_path=None):
    """Create one single chart with all close-ended data combined"""

    # Prepare data for a single chart
    # Create combined labels that include question and option
    data_combined = data.copy()
    data_combined["combined_label"] = (
        data_combined["item"] + ": " + data_combined["option"]
    )

    # Sort by question and then by percentage for better visualization
    data_combined = data_combined.sort_values(
        ["item", "percent"], ascending=[True, True]
    )

    # Create a single large figure
    fig, ax = plt.subplots(figsize=(16, 12))

    # Define colors for each question
    question_colors = {
        "Q7": "#1f77b4",  # Blue
        "Q8": "#ff7f0e",  # Orange
        "Q9": "#2ca02c",  # Green
        "Q10": "#d62728",  # Red
        "Q11": "#9467bd",  # Purple
    }

    # Question labels for legend
    question_labels = {
        "Q7": "Fair Compensation",
        "Q8": "Basic Needs Met",
        "Q9": "Task Rejected/Unpaid",
        "Q10": "Disturbing Content",
        "Q11": "Platform Transparency",
    }

    # Create color list based on question
    colors = [question_colors[row["item"]] for _, row in data_combined.iterrows()]

    # Create horizontal bar chart with all data
    bars = ax.barh(
        data_combined["combined_label"],
        data_combined["percent"],
        color=colors,
    )

    # Add value labels on bars
    for bar, value in zip(bars, data_combined["percent"]):
        ax.text(
            bar.get_width() + 1,
            bar.get_y() + bar.get_height() / 2,
            f"{value}%",
            va="center",
            fontweight="bold",
            fontsize=9,
        )

    # Customize the chart
    ax.set_xlabel("Percentage (%)", fontsize=12, fontweight="bold")
    ax.set_title(
        "All Close-Ended Survey Results", fontsize=16, fontweight="bold", pad=20
    )
    ax.set_xlim(0, max(data_combined["percent"]) * 1.15)

    # Add grid for better readability
    ax.grid(axis="x", alpha=0.3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Add sample size info
    total_responses = data_combined["n"].sum()
    ax.text(
        0.02,
        0.98,
        f"Total Responses: {total_responses}",
        transform=ax.transAxes,
        fontsize=10,
        verticalalignment="top",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.7),
    )

    # Add question separators (vertical lines)
    question_positions = []
    current_question = None
    for i, (idx, row) in enumerate(data_combined.iterrows()):
        if row["item"] != current_question:
            if current_question is not None:
                question_positions.append(i - 0.5)
            current_question = row["item"]

    # Add vertical separator lines
    for pos in question_positions:
        ax.axhline(y=pos, color="gray", linestyle="--", alpha=0.5, linewidth=1)

    # Create legend
    legend_elements = []
    for question, color in question_colors.items():
        legend_elements.append(
            plt.Rectangle(
                (0, 0), 1, 1, facecolor=color, label=question_labels[question]
            )
        )

    ax.legend(
        handles=legend_elements,
        loc="center left",
        bbox_to_anchor=(1, 0.5),
        fontsize=10,
        title="Questions",
        title_fontsize=11,
    )

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"Saved comprehensive chart: {save_path}")

    return fig


def main():
    """Main function to create all charts"""

    # Load data
    data_path = Path("/Users/qrutz/rawest/data_repository/closed_item_descriptives.csv")
    data = pd.read_csv(data_path)

    # Create output directory
    output_dir = Path("/Users/qrutz/rawest/analysis/results/charts")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create the comprehensive chart
    comprehensive_path = output_dir / "closed_ended_comprehensive.png"
    create_comprehensive_chart(data, save_path=comprehensive_path)
    plt.close()

    print("\nComprehensive chart created successfully!")
    print(f"Chart saved to: {comprehensive_path}")


if __name__ == "__main__":
    main()
