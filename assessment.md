# Assessment Abdul Hameed

## Outline

The assessment consists of two tasks, each to be completed within the given time period of 6 h. The Assessment starts at 11:00 CET, Thursday 25th of March, 2021. Results to the tasks are to be pushed into the git repsository, the last commit before 5:00 pm CET, Thursday 25th of March, 2021 will be used as the final contribution. 
The first task entails the implementation of a certain piece of code. The second task includes a written concept.

Programming tasks may be implemented in any common programming language. Criteria for the evaluation of the code submitted include:
- executability: the submitted script has to run in order to pass the assessment
- documentation and formatting: code must be committed in a well documented and formatted form, such that ideas and layouts are to be understood easily by a reader
- original code: whereever possible the assessee shall use standard library functions. However, the submitted code must be original work implemented by the assessee. 

## Task 1

Write a programm that simulates a harmonic signal indefinetly (for as long as the programm is executed). Add white noise to the signal such that the original signal is masked by the noise. Implement a suitable live filter to filter out the noise. Display all three signals (original, noisy signal and filtered signal) in a live plot. 

## Task 2

You are given sensor box that records linear acceleration (g), angular velocity (deg/sec) and magnetic field data (micro-Tesla) with a sampling frequency of 100 Hz. The type of sensors used in the sensorbox are unknown. The noise and drift of each of the parameters are unknown. The sensor box shall be used to estimate the absolute position in space and time with respect to a given reference point. 

To investigate the sensor box you have access to a robot that allows you to move the sensor box with 6 degrees of freedom with arbitrary precision and magnitude. 

You are to devise an experiment to assess noise and drift of each of the parameters dependending on the motion patterns imposed on the sensor box. Please describe in details the experimental procedures and the parameter space to be explored. What are potential pitfall in the experiment? How do you assess the error of your experimental setup? 
