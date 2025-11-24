"""
Course Schedule
---------------
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
---------------
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
---------------
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
---------------
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""
from typing import List


class Solution:
    def canFinish(self, number_of_courses: int, prerequisites: List[List[int]]) -> bool:
        # Create a list to store the in-degree of each course
        course_indegree = [0] * number_of_courses

        # Create a list to store the adjacencies of each course
        course_adjacencies = [[] for _ in range(number_of_courses)]

        for course, prerequisite in prerequisites:
            course_indegree[course] += 1
            course_adjacencies[prerequisite].append(course)

        # Queue for courses with no prerequisites.
        no_prerequisites_queue = []
        for course in range(number_of_courses):
            if course_indegree[course] == 0:
                no_prerequisites_queue.append(course)

        courses_taken_count = 0

        # Iteratively take courses.
        while no_prerequisites_queue:
            course = no_prerequisites_queue.pop(0)
            courses_taken_count += 1

            # Reduce the in-degree of dependent courses.
            for dependent_course in course_adjacencies[course]:
                course_indegree[dependent_course] -= 1

                # Enqueue courses with no remaining prerequisites.
                if course_indegree[dependent_course] == 0:
                    no_prerequisites_queue.append(dependent_course)

        # If we've taken all courses, it's possible.
        if courses_taken_count == number_of_courses:
            return True
        else:
            # Cycle exists if we can't take all courses
            return False

if __name__ == '__main__':
    preq1 = [[1, 0]]
    preq = [[1,0],[0,1]]
    result = Solution().canFinish(2, preq)
    print(result)

"""
Time Complexity:
O(V + E) – The algorithm iterates through all courses (V vertices) and their prerequisites (E edges).
Space Complexity:
O(N) - where N represents the number of courses
"""