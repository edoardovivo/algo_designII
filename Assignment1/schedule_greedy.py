
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
            jobs[int(reader.line_num-1)] = {'weight': w, 'length': l}
    return jobs


def compute_sum_completion_times(jobs, jobs_scores):
    #Computes the lengths in order
    lengths = [jobs[v[0]]['length'] for v in jobs_scores]
    weights = [jobs[v[0]]['weight'] for v in jobs_scores]
    C = np.cumsum(lengths)
    return (C*weights).sum()


def schedule_diff(jobs):
    jobs_scores = [(k, v['weight'] - v['length'], v['weight']) for k,v in jobs.iteritems()]
    jobs_scores.sort(key=lambda x: (x[1], x[2]), reverse=True)
    return jobs_scores

def schedule_ratio(jobs):
    jobs_scores = [(k, v['weight']/v['length']) for k,v in jobs.iteritems()]
    jobs_scores.sort(key=lambda x: x[1], reverse=True)
    return jobs_scores

fname = "/home/edoardo/docker-drive/AlgorithmsDesignII/Assignment1/jobs.txt"
jobs = read_jobs(fname)

scores_diff = schedule_diff(jobs)
scores_ratio = schedule_ratio(jobs)

print "Diff: ", compute_sum_completion_times(jobs, scores_diff)
print "Ratio: ", compute_sum_completion_times(jobs, scores_ratio)


