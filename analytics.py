import pandas as pd
from datetime import datetime

class AnalyticsEngine:

    def __init__(self, sessions):
        self.sessions = sessions

    def total_hours(self):
        if not self.sessions:
            return 0

        df = pd.DataFrame(self.sessions, columns=[
            "id", "user_id", "subject", "hours",
            "difficulty", "mood", "notes", "date"
        ])

        return df["hours"].sum()

    def subject_breakdown(self):
        if not self.sessions:
            return {}

        df = pd.DataFrame(self.sessions, columns=[
            "id", "user_id", "subject", "hours",
            "difficulty", "mood", "notes", "date"
        ])

        result = df.groupby("subject")["hours"].sum()
        return result.to_dict()

    def productivity_score(self):
        if not self.sessions:
            return 0

        score = 0
        for session in self.sessions:
            hours = session[3]
            difficulty = session[4]
            score += hours * difficulty

        return round(score, 2)

    def kcet_prediction(self):
        """
        Simple manual prediction logic:
        Higher productivity → better estimated rank
        """

        score = self.productivity_score()

        if score > 500:
            return "Top 5,000 Rank"
        elif score > 300:
            return "Top 15,000 Rank"
        elif score > 150:
            return "Top 30,000 Rank"
        else:
            return "Needs Improvement"
