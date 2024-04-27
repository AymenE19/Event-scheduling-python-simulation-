#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Queuing System Discrete Event Simulation

This script simulates a queuing system with a single server using discrete event simulation.
Customers arrive according to an exponential inter-arrival time distribution with a mean of 3 time units,
and each customer's service time follows an exponential distribution with a mean of 4 time units.
The simulation tracks the number of arrivals and departures, as well as the total simulation time and average waiting time per customer.

Author: [Your Name]

"""

import numpy as np 

class Simulation():
    def __init__(self):
        # Initialize simulation parameters
        self.num_in_system = 0
        self.clock = 0.0 
        self.next_arrival = self.generate_interarrival()
        self.next_depart = float("inf")
        self.num_arrivals = 0
        self.num_departs = 0
        self.total_wait = 0.0
        
    def advance_time(self):
        # Advance simulation time to the next event
        t_event = min(self.next_arrival, self.next_depart)
        self.total_wait += self.num_in_system * (t_event - self.clock)
        self.clock = t_event
        if self.next_arrival <= self.next_depart:
            self.handle_arrival_event()
        else:
            self.handle_depart_event()
            
    def handle_arrival_event(self):
        # Process an arrival event
        self.num_in_system += 1
        self.num_arrivals += 1
        if self.num_in_system <= 1:
            self.next_depart = self.clock + self.generate_service()
        self.next_arrival = self.clock + self.generate_interarrival()
        
    def handle_depart_event(self):
        # Process a departure event
        self.num_in_system -= 1
        self.num_departs += 1
        if self.num_in_system > 0:
            self.next_depart = self.clock + self.generate_service()
        else:
            self.next_depart = float("inf")
    
    def generate_interarrival(self):
        # Generate inter-arrival time exponentially distributed with mean 3
        return np.random.exponential(1./3)
    
    def generate_service(self):
        # Generate service time exponentially distributed with mean 4
        return np.random.exponential(1./4)

# Set random seed for reproducibility
np.random.seed(0)    

# Create simulation instance
s = Simulation()

# Run simulation until time reaches 1000
while s.clock < 1000:
    s.advance_time()

# Calculating average waiting time per customer
avg_waiting_time = s.total_wait / s.num_arrivals

# Print simulation results
print("Simulation Results:")
print("Number of arrivals:", s.num_arrivals)
print("Number of departures:", s.num_departs)
print("Total simulation time:", s.clock)
print("Average waiting time per customer:", avg_waiting_time)
