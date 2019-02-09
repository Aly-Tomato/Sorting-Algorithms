## Sorting Algorithms
Algorithms project that implements, tests and compares three different sorting algorithms using python, pandas, numpy and plotly.  
The sorting algorithms are 1. Selection Sort 2. Merge Sort 3. Counting Sort.

## Usage  
```
$ git clone https://github.com/Aly-Tomato/SortingAlgorithms.git  
$ cd SortingAlgorithms
$ python3 hw2.py  
```
## Project Write Up
#### Briefly describe your development process. What sources did you use for your algorithms? What programming language did you choose and why?  
I chose to work with Python because I'm at the exciting stage in the language where I'm building useful scripts to automate certain tasks at work.I'm relatively new to Python and thought this project would be the best way to better hone in my Python skills. I also wanted to get better acquainted with the data analyzing libraries available to Python such as pandas, numpy and plotly. Below you will see links to the results of these tests graphed out using these aformentioned tools.

#### Did you run into any difficulties with the implementation? How are you timing the algorithms? What hardware are you timing on?  
The biggest difficulty faced with implementation is learning a new language and exploring the vast libraries python has to offer in data analysis. You may see some C tendencies in the code which I plan on cleaning up later and making the code more "pythonic". To time the algorithms I used clock as part of the library time to count the ticks that occur during the individual runs of the tests. Per documentation found at https://docs.python.org/2/library/time.html, time.clock() when used on Unix, which is the case here, "returns the current processor time as a floating point number expressed in seconds."

```python
  t1 = time.clock()
  #perform test
  t = time.clock()
  ticks = t -t1
```


#### Graph or tables of the run times of your algorithm implementations on various sized inputs. Do this with sorted and randomized inputs. Do your observations match the theoretical analysis from class? Why or why not?
The default test framework will execute tests for three sorting algorithms: selection sort, merge sort and counting sort.  

[View interactive Plotly line graph results for all sorts with small data sets](https://htmlpreview.github.io/?https://github.com/Aly-Tomato/SortingAlgorithms/blob/master/Graph_4500.html "Default test results link")  
[![](https://github.com/Aly-Tomato/SortingAlgorithms/blob/master/default_test.JPG)](https://htmlpreview.github.io/?https://github.com/Aly-Tomato/SortingAlgorithms/blob/master/Graph_4500.html "Default test image link")  
The default test will execute a total of 4,500 tests, 500 tests are performed with unsorted lists, sorted lists, and reverse sorted lists of various sizes starting at 30 for each sorting algorithm. 

[View interactive Plotly line graph results for merge sort & counting sort with large data sets](https://htmlpreview.github.io/?https://github.com/Aly-Tomato/SortingAlgorithms/blob/master/Merge%20%26%20Count%20Sort%20Large%20Set.html "Large test results link")    
[![](https://github.com/Aly-Tomato/SortingAlgorithms/blob/master/large_test.JPG)](https://htmlpreview.github.io/?https://github.com/Aly-Tomato/SortingAlgorithms/blob/master/Merge%20%26%20Count%20Sort%20Large%20Set.html "Large test image link") 

Selection sort performed at an alarmingly slow rate as list sizes approached 50,000. Because of this, I decided to omit selection sort from the following test. This test pushed the boundries of merge sort and counting sort to better see how their performance compares from one another. This test will execute a total of 5000 tests with the size of the lists starting at 1000 and growing until list size of close to 11,000. This was enough to start seeing where these two algorithms start to difference in performance.


#### Comparison of your results with each other. How does each fare under different testing circumstances? Given your results, in what real world situations would you favor one algorithm over the others?
Given the results it is safe to conclude that selection sort was the poorest performing algorithm of the three. When the data set is small, selection sort will perform roughy within the time frame as merge sort and counting sort. However, as you can see by the interactive graph, selection sort performance starts to grow exponentially at a list size of 200. 

## Links

The following are resources used on this project:
* [http://interactivepython.org/courselib/static/pythonds/SortSearch/TheSelectionSort.html](http://interactivepython.org/courselib/static/pythonds/SortSearch/TheSelectionSort.html)
* [http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html](http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html)
* [https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

