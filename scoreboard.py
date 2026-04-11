from __future__ import annotations

import os
import pandas as pd


class ScoreBoard:
    def __init__(self, filename: str = "scores.csv"):
        self.filename = filename
        self.data = self._load_scores()

    def _load_scores(self) -> pd.DataFrame:
        if os.path.exists(self.filename):
            try:
                df = pd.read_csv(self.filename)
                if {"player", "score"}.issubset(df.columns):
                    return df[["player", "score"]]
            except Exception:
                pass
        return pd.DataFrame(columns=["player", "score"])

    def add_score(self, player: str, score: int) -> None:
        new_row = pd.DataFrame([{"player": player, "score": int(score)}])
        self.data = pd.concat([self.data, new_row], ignore_index=True)
        self.data = self.data.sort_values(by="score", ascending=False).reset_index(drop=True)
        self.data.to_csv(self.filename, index=False)

    def top_lines(self, limit: int = 8) -> list[str]:
        if self.data.empty:
            return ["No scores yet."]

        top = self.data.sort_values(by="score", ascending=False).head(limit).reset_index(drop=True)
        lines: list[str] = []
        for rank, row in enumerate(top.itertuples(index=False), start=1):
            lines.append(f"#{rank} - {row.player}: {row.score}")
        return lines
