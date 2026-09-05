import numpy as np

class KMMatch:
    def __init__(self, num_doctor, num_hospital, preference, capacity):
        # Basic input parameters
        self.num_doctor = num_doctor
        self.num_hospital = num_hospital
        self.preference = preference
        self.capacity = capacity

        # Calculate and prepare some important parameters
        self.total_capacity = np.sum(capacity)
        self.extl = max(num_doctor, self.total_capacity)
        self.extended_preference = np.zeros((self.extl, self.extl), dtype=int)
        self.hospital_map = np.ones(self.extl, dtype=int) * -1
        self.assignment = np.ones(self.extl, dtype=int) * -1
        self.extend_preference()

        # If a doctor or a hospital is not assigned, it is marked as -1
        self.assignment_doctor = np.ones(self.extl, dtype=int) * -1
        self.assignment_hospital = np.ones(self.extl, dtype=int) * -1
        self.top_values_doctor = np.zeros(self.extl, dtype=int)
        self.top_values_hospital = np.zeros(self.extl, dtype=int)
        self.assignment = np.zeros(self.num_doctor, dtype=int)

        # In the graph matrix, viewable edges are marked as 1, matched edges are marked as 2, and other edges are marked as 0
        self.graph = np.zeros((self.extl, self.extl), dtype=int)
        self.viewable_dist = np.zeros((self.extl, self.extl), dtype=int)
        self.init_graph()
        self.calc_viewable_dist()

        self.ext_path_finded = False
        self.visited_doctor = []
        self.visited_hospital = []

    def init_graph(self):
        # Initialize the graph
        # Initialize the top values for doctors
        # The top values for hospitals are initialized to 0
        
        for i in range(self.extl):
            self.top_values_doctor[i] = np.max(self.extended_preference[i])
            for j in range(self.extl):
                if self.extended_preference[i][j] == self.top_values_doctor[i]:
                    self.graph[i][j] = 1

    def calc_viewable_dist(self):
        # Calculate whether the edge is viewable or not

        for i in range(self.extl):
            for j in range(self.extl):
                self.viewable_dist[i][j] = self.extended_preference[i][j] - self.top_values_doctor[i] - self.top_values_hospital[j]

    def extend_preference(self):
        # Extend the preference matrix based on hospital capacities
        # If doctors are fewer than the total hospital capacity, then these fake doctors will have 0 preference for all hospitals
        
        cur_idx = 0
        for i in range(self.num_hospital):
            self.hospital_map[cur_idx:cur_idx + self.capacity[i]] = i
            self.extended_preference[:self.num_doctor, cur_idx:cur_idx + self.capacity[i]] = self.preference[:, i].reshape(-1, 1)
            cur_idx += self.capacity[i]

    def extend_graph(self, ext_path):
        # When the extended path cannot be found
        # Expand the set of edges in the graph
        # Adjust the top values for doctors and hospitals
        
        # Go over each doctor in the extended path to find the minimum adjustment value
        # Because the adjustment value is a negative number, we need to find a maximum
        # Simultaneously record the edges that need to be switched into viewable ones
        adjust = np.min(self.viewable_dist)
        adjust_edge = []
        for k in range(len(ext_path)):
            if k % 2 == 0:
                doctor = ext_path[k]
                for l in range(self.extl):
                    if self.viewable_dist[doctor][l] < 0:
                        if adjust > self.viewable_dist[doctor][l]:
                            adjust = self.viewable_dist[doctor][l]
                            adjust_edge = [doctor, l]
                        elif adjust == self.viewable_dist[doctor][l]:
                            adjust_edge.append(doctor)
                            adjust_edge.append(l)
        # print(f"Adjusting top values by {adjust}.")

        # Adjust the top values
        for k in range(len(ext_path)):
            if k % 2 == 0:
                self.top_values_doctor[ext_path[k]] += adjust
            else:
                self.top_values_hospital[ext_path[k]] -= adjust

        # Update the graph with new viewable edges
        for k in range(len(adjust_edge) // 2):
            self.graph[adjust_edge[2*k]][adjust_edge[2*k+1]] = 1

        # Update the viewable distance matrix
        self.calc_viewable_dist()  

    def extend_path(self, ext_path):
        # Extend the path to find an augmenting path in the graph
        tmp_doctor = ext_path[-1]
        flag = 0
        for k in range(self.extl):
            if k not in self.visited_hospital and self.graph[tmp_doctor][k] == 1:
                flag = 1
                if self.assignment_hospital[k] == -1:
                    # If the hospital is unassigned, we can extend the path and mark it as found
                    ext_path.append(k)
                    self.ext_path_finded = True
                    return ext_path
                else:
                    # If the hospital is assigned, we can extend the path and continue searching
                    if self.assignment_hospital[k] not in self.visited_doctor:
                        ext_path.append(k)
                        self.visited_hospital.append(k)
                        ext_path.append(self.assignment_hospital[k])
                        self.visited_doctor.append(self.assignment_hospital[k])
                        return self.extend_path(ext_path)

        if flag == 0:
            # If no further extension is possible, return the current path and mark it as not found
            return ext_path
    
    def match(self):
        # Use KM algorithm to match

        # Go over each doctor
        for i in range(self.extl):
            self.visited_doctor = []
            self.visited_hospital = []
            if self.assignment_doctor[i] != -1:
                # If the doctor is already assigned, skip to the next doctor
                continue
            # print(f"Matching for doctor {i + 1}...")

            # Go over each hospital currently available to the doctor
            for j in range(self.extl):
                if self.graph[i][j] == 1 and self.assignment_doctor[i] == -1 and self.assignment_hospital[j] == -1:
                    # If the doctor and hospital are both unassigned, assign them to each other
                    self.assignment_doctor[i] = j
                    self.assignment_hospital[j] = i
                    self.graph[i][j] = 2
                    # print(f"Doctor {i + 1} simply assigned.")
                    break
                elif self.graph[i][j] == 1 and self.assignment_doctor[i] == -1 and self.assignment_hospital[j] != -1:
                    # If the doctor is unassigned but the hospital is assigned, find an extended path
                    # Initialize the extended path
                    self.ext_path_finded = False
                    ext_path = [i, j, self.assignment_hospital[j]]
                    self.visited_doctor.append(i)
                    self.visited_hospital.append(j)
                    self.visited_doctor.append(self.assignment_hospital[j])

                    # Try to find an extended path
                    ext_path = self.extend_path(ext_path)

                    while not self.ext_path_finded:
                        # If the trial fails, extend the graph and try to find an extended path again
                        # KM algorithm guarantees that the extended path can be found in finite steps
                        # print("No extended path found, extending the graph...")
                        self.extend_graph(ext_path)
                        ext_path = self.extend_path(ext_path)
                    # print("Extended path found!")

                    # Reassign the doctors and hospitals along the extended path
                    for k in range(len(ext_path) - 1):
                        if k % 2 == 0:
                            self.assignment_doctor[ext_path[k]] = ext_path[k + 1]
                        else:
                            self.assignment_hospital[ext_path[k]] = ext_path[k - 1]
                    # print(f"Doctor {i + 1} assigned via extended path.")
                    break

    def reshape_assignment(self):
        # Fix the index of hospitals to match the initial input
        # If doctors are fewer than the total hospital capacity, remove the fake doctors

        if self.num_doctor < self.total_capacity:
            self.assignment = self.assignment_doctor[:self.num_doctor]

        for i in range(self.num_doctor):
            self.assignment[i] = self.hospital_map[self.assignment_doctor[i]] if self.assignment_doctor[i] != -1 else -1

if __name__ == "__main__":
    # Program to solve the doctor-hospital matching problem using the KM algorithm

    # Necessary inputs according to the problem description
    num_doctor = int(input("Enter the number of doctors: "))
    num_hospital = int(input("Enter the number of hospitals: "))

    preference = np.zeros((num_doctor, num_hospital), dtype=int)
    for i in range(num_doctor):
        preference[i] = np.array(list(map(int, input(f"Enter the preferences of doctor {i + 1} (space-separated): ").split())))

    capacity = np.array(list(map(int, input("Enter the capacities of hospitals (space-separated): ").split())))

    # Create an instance of the KMMatch class and perform the matching
    matcher = KMMatch(num_doctor, num_hospital, preference, capacity)
    matcher.match()
    matcher.reshape_assignment()

    print("Final Assignment:")
    for i in range(matcher.num_doctor):
        if matcher.assignment[i] != -1:
            print(f"Doctor {i + 1} is assigned to Hospital {matcher.assignment[i] + 1}")
        else:
            print(f"Doctor {i + 1} is not assigned to any hospital.")