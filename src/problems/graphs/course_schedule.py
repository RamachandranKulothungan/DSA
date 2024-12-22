"""
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

The pair [0, 1], indicates that must take course 1 before taking course 0.

There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return true if it is possible to finish all courses, otherwise return false.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        pre_req_map = {}
        post_courses = {}
        for i in range(numCourses):
            pre_req_map[i] = []
            post_courses[i] = []
        for prereq in prerequisites:
            pre_req_map[prereq[0]] = pre_req_map.get(prereq[0]) + [prereq[1]]
            post_courses[prereq[1]] = post_courses.get(prereq[1]) + [prereq[0]]
        q = []
        for course, prereq  in pre_req_map.items():
            if len(prereq)==0:
                q.append(course)
        count = 0
        while q:
            count = count + 1
            c = q[0]
            q.pop(0)
            for course in post_courses[c]:
                print(course, pre_req_map[course], c)
                pre_req_map[course].remove(c)
                if len(pre_req_map[course]) == 0:
                    q.append(course)
        return count>=numCourses
