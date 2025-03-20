class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # overall approach
        # 1. build the graph 
        # 2. DFS finds the cycle 
        # 3. return results if found, return False, else return True
        
        # 1. build the graph
        # key is the course number
        # value is a set
        graph = dict()
        # since each pair is unique, so it is ok to initialize based on length
        for i in range(numCourses):
            graph[i] = set()
        for pair in prerequisites:
            graph[pair[0]].add(pair[1])


        # 2. Use dfs to find cycle 
        # 
        # need a visit history record to trace if each node is visited
        # 0: unvisited
        # 1: visiting
        # 2: visited
        record = [0] * numCourses
        def dfs(course):
            # in the search progress, the source node is found here again, 
            # one node points back to the source node and a cycle is found 
            if record[course] == 1:
                return False
            # this node is finished with the search (no cycle found), no need to search further 
            if record[course] == 2:
                return True
        
            # un visited scenario
            # check its prerequisites
            for prereq in graph[course]:
                record[course] = 1
                if dfs(prereq) == False: 
                    return False
            # after checking all prerequs and no cycle
            # update to 2 
            record[course] = 2
            return True

        # 3. check last return 
        for course in graph.keys():
            if record[course] == 0:
                if dfs(course) == False:
                    return False
        
        return True


















        # # overall understanding: find the loop of prerequisites of each class, if loop, return false
        # # need to check numCourses is <= prerequisites

        # # edge case: numCourses > prerequisites
        # all_courses = set()
        # for courses in prerequisites:
        #     all_courses.update(set(courses))
        # if numCourses > len(all_courses):
        #     return False

        # # normal scenarios
        # # for each list in prerequisites, convert it to a dict, key is the first element, following elements are in the value list 
        # # current key and value list pair, check the other key and value list pairs
        # # take one element from current value list, take it as a next key, take out its catering next value list 
        # # check if current key is in one of the children's value list 
        # # if yes, return False

        # # build this dict, key is the first element in list, value is a list that courses required before taking this key course
        # course_map = dict()
        # for prereq in prerequisites:
        #     # add new course into dict
        #     if prereq[0] not in course_map:
        #         course_map[prereq[0]] = set()
        #     # add prereq
        #     course_map[prereq[0]].add(prereq[1])

        # def checkLoop(wanted_course, prereqs_set):
        #     # input current course, check if its prereqs contain this course
        #     # if contain, return True, else False
        #     # cur_prereqs_set = course_map[cur_course]
        #     for course in prereqs_set:
        #         if wanted_course in course_map[course]:
        #             return False
        #         else:
        #             return checkloop(wanted_course, course_map[])
            
        #     return 