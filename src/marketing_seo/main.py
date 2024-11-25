#!/usr/bin/env python
import sys

from marketing_seo.crew import MarketingSEOCrew


# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """
    inputs = {
        "organization": "SkiBoots.com was founded after the 1948 Olympics by Hedy Schlunegger and Gretchen Fraser. We make custom-fit ski boots for competition in cross-county, ski jump, and slalom. We have staff of twelve and $14 million in sales.",
        "product": "Bluetooth-enabled cross-country ski boots connected to GPS-smartphones via Bluetooth 4.0, providing skiers with real-time GPS connectivity for feedback and turn-by-turn directions while exploring new trails.",
        "distribution": "Sales through specialized ski shops, outdoor sports stores, and ski resorts. Overnight delivery via FedEx/UPS, truck shipments via DHL.",
        "target_audience": "Professional competitive skiers in cross-county skiing, ski jump, and slalom in the United States, aged 18-35, from middle to upper-income backgrounds in northern and mountainous states.",
        "business_goals": "Increase annual sales revenue by 10% (from $14m to $15.4m) by end of Q4 2025 through expanded online marketing.",
        "unique_proposition": "Custom-made ski boots by Olympic gold winners for competitive skiers in cross-county, ski jump, and slalom, featuring Bluetooth connectivity to provide turn-by-turn GPS directions for exploring new trails."
    }

    MarketingSEOCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "Low code, no code AI Application Development"}
    try:
        MarketingSEOCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        SimilarFrameworkFinderTemplateCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {"topic": "Low code, no code AI Application Development"}
    try:
        SimilarFrameworkFinderTemplateCrew().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
