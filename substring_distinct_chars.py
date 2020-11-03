def find_min_distinct_substring(S):

	dist_chars = len(set(S))

	dist_string = {}
	count = 0
	start_window = 0
	min_dist_chars = len(S)
	end_window = len(S)
	start_window_index = start_window

	for j in range(len(S)):
		if S[j] in dist_string:
			dist_string[S[j]] +=1
		else:
			dist_string[S[j]] = 1
			count+=1

		if count == dist_chars:
			while dist_string[S[start_window]] > 1:
				if dist_string[S[start_window]] > 1:
					dist_string[S[start_window]] -= 1

				start_window += 1

			len_window = j - start_window + 1

			if min_dist_chars > len_window:
				min_dist_chars = len_window
				start_window_index = start_window
				end_window = start_window_index + min_dist_chars

	sub_string = str(S[start_window_index: end_window])

	return len(sub_string)



s=input()

print(find_min_distinct_substring(s))
