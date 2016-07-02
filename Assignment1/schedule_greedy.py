'''
Problem 1:

In this programming problem and the next you'll code up the greedy algorithms from lecture for minimizing the weighted sum of completion times..

Download the text file below.

jobs.txt
This file describes a set of jobs with positive and integral weights and lengths. It has the format

[number_of_jobs]

[job_1_weight] [job_1_length]

[job_2_weight] [job_2_length]

...

For example, the third line of the file is "74 59", indicating that the second job has weight 74 and length 59.

You should NOT assume that edge weights or lengths are distinct.

Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of the difference (weight - length). Recall from lecture that this algorithm is not always optimal. IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the job with higher weight first. Beware: if you break ties in a different way, you are likely to get the wrong answer. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.

ADVICE: If you get the wrong answer, try out some small test cases to debug your algorithm (and post your test cases to the discussion forum).

Problem 2:

For this problem, use the same data set as in the previous problem.

Your task now is to run the greedy algorithm that schedules jobs (optimally) in decreasing order of the ratio (weight/length). In this algorithm, it does not matter how you break ties. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.


SOLUTIONS:
Diff:  69119377652
Ratio:  67311454237

'''


import csv
import numpy as np


def read_jobs(fname):
    jobs = {}
    with open(fname) as f:
        reader = csv.reader(f, delimiter=' ')
        next(reader, None)  # skip the headers
        for row in reader:
            w = float(row[0])
            l = float(row[1])
            jobs[int(reader.line_num - 1)] = {'weight': w, 'length': l}
    return jobs


def compute_sum_completion_times(jobs, jobs_scores):
    # Computes the lengths in order
    lengths = [jobs[v[0]]['length'] for v in jobs_scores]
    weights = [jobs[v[0]]['weight'] for v in jobs_scores]
    C = np.cumsum(lengths)
    return (C * weights).sum()


def schedule_diff(jobs):
    jobs_scores = [(k, v['weight'] - v['length'], v['weight'])
                   for k, v in jobs.iteritems()]
    jobs_scores.sort(key=lambda x: (x[1], x[2]), reverse=True)
    return jobs_scores


def schedule_ratio(jobs):
    jobs_scores = [(k, v['weight'] / v['length']) for k, v in jobs.iteritems()]
    jobs_scores.sort(key=lambda x: x[1], reverse=True)
    return jobs_scores


def main():
    fname = "/home/edoardo/docker-drive/AlgorithmsDesignII/Assignment1/jobs.txt"
    jobs = read_jobs(fname)

    scores_diff = schedule_diff(jobs)
    scores_ratio = schedule_ratio(jobs)

    print "Diff: ", compute_sum_completion_times(jobs, scores_diff)
    print "Ratio: ", compute_sum_completion_times(jobs, scores_ratio)


if __name__ == "__main__":
    main()


