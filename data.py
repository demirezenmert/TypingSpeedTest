import json

PATH = 'scores/scores.json'

def create_scores():
# Create a dictionary to store the scores
    scores = {"e_high_score": 0, "e_current_score": 0, 
            "m_high_score": 0, "m_current_score": 0,
            "h_high_score": 0, "h_current_score": 0}

# Create a file to store the scores
    with open("scores.json", "w") as f:
        json.dump(scores, f)


def update_scores(current_score, level_sign):
     # Load the scores from the file
    try :
        with open(PATH, "r") as f:
            scores = json.load(f)
    except: 
        create_scores()
    # Update the current score
    scores[f"{level_sign}_current_score"] = current_score

    # Check if the current score is higher than the high score
    if current_score > scores[f"{level_sign}_high_score"]:
        scores[f"{level_sign}_high_score"] = current_score

    # Save the updated scores to the file
    with open(PATH, "w") as f:
        json.dump(scores, f)


def read_scores(level_sign):
    try: 
        with open(PATH, "r") as f:
            scores = json.load(f)
    except: 
        create_scores()

    return scores[f"{level_sign}_high_score"], scores[f"{level_sign}_current_score"]

# print("High score:", scores["high_score"])  # Output: High score: 20
# print("Current score:", scores["current_score"])  # Output: Current score: 15