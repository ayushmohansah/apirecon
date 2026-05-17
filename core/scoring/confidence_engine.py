class ConfidenceEngine:

    @staticmethod
    def calculate(signals=None, penalties=None):

        score = 0

        signals = signals or []
        penalties = penalties or []

        for signal in signals:
            score += signal

        for penalty in penalties:
            score -= penalty

        if score < 0:
            score = 0

        if score > 100:
            score = 100

        return score
