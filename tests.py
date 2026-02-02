from ats_engine.ats_scoring import score_candidate

def test_score():
    profile = {"skills": ["Python", "ML"]}
    assert score_candidate(profile) == 20
