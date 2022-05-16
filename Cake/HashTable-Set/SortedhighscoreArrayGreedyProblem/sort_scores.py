def sort_scores(unsorted_scores, highest_possible_score):
	sorted_scores = []

	score_count = [0]*(highest_possible_score+1)


	for score in unsorted_scores:
		score_count[score] += 1

	for score in range(highest_possible_score, -1, -1):

		times = score_count[score]
		for i in range(times):
			sorted_scores.append(score)

	return sorted_scores


unsorted_scores = [37, 89, 41, 65, 1, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

# Returns [91, 89, 65, 53, 41, 37, 1]
print(sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE))