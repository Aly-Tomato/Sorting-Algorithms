import time
import myUtils
import sort

ROUND = 4 #round to ith of a second
RANGE = 1000 #run how many tests
iSIZE = 1000 #initial size of list
           #every subsequent size*=10
PRINT = False #print results after every run?

def main():
    global RANGE
    global iSIZE
    global ROUND
    global PRINT
    size = iSIZE
    """
    #Selection Sort Test
    test_name = "Selection Sort - unsorted"
    print("*******************************") 
    print(f"Test Name:\t{test_name}")
    print("*******************************") 
    sel_sorted_lists=[]
    for i in range(0,RANGE):
        list = myUtils.make_list(size)
        t1 = time.clock()
        sel_sorted_lists.append(sort.selection_sort(list))
        t = time.clock()
        ticks = t-t1
        if(PRINT):
            myUtils.print_pretty(i, size, ticks, ROUND)
        myUtils.write_to_file([(test_name,size,round(ticks,ROUND))])
        size += 10
    print("\n...Performing tests with sorted lists...\n")
    test_name = "Selection Sort - sorted"
    for i in range(0,RANGE):
        t1 = time.clock()
        sort.selection_sort(sel_sorted_lists[i])
        t = time.clock()
        ticks = t-t1
        if(PRINT):
            myUtils.print_pretty(i, len(sel_sorted_lists[i]), ticks, ROUND)
        myUtils.write_to_file([(test_name,len(sel_sorted_lists[i]),round(ticks,ROUND))])
    print("\n...Performing tests with reverse sorted lists...\n")
    test_name = "Selection Sort - reverse sorted"
    for i in range(0,RANGE):
        sel_sorted_lists[i].reverse()
        t1 = time.clock()
        sort.selection_sort(sel_sorted_lists[i])
        t = time.clock()
        ticks = t-t1
        if(PRINT):
            myUtils.print_pretty(i, len(sel_sorted_lists[i]), ticks, ROUND)
        myUtils.write_to_file([(test_name,len(sel_sorted_lists[i]),round(ticks,ROUND))])
    """
    #Merge Sort Test
    test_name = "Merge Sort - unsorted"
    print("\n*******************************") 
    print(f"Test Name:\t{test_name}")
    print("*******************************") 
    merg_sorted_lists =[]
    for i in range(0,RANGE):
        list = myUtils.make_list(size)
        t1 = time.clock()
        merg_sorted_lists.append(sort.merge_sort(list))
        t = time.clock()
        ticks = t-t1
        if(PRINT):
            myUtils.print_pretty(i, size, ticks, ROUND)
        myUtils.write_to_file([(test_name,size,round(ticks,4))])
        size += 10
    print("\n...Performing tests with sorted lists...\n")
    test_name = "Merge Sort - sorted"
    for i in range(0,RANGE):
        t1 = time.clock()
        sort.merge_sort(merg_sorted_lists[i])
        t = time.clock()
        ticks = t-t1
        if(PRINT):
            myUtils.print_pretty(i, len(merg_sorted_lists[i]), ticks, ROUND)
        myUtils.write_to_file([(test_name,len(merg_sorted_lists[i]),round(ticks,4))])
    print("\n...Performing tests with sorted reverse lists...\n")
    test_name = "Merge Sort - reverse sorted"
    for i in range(0,RANGE):
        merg_sorted_lists[i].reverse()
        t1 = time.clock()
        sort.merge_sort(merg_sorted_lists[i])
        t = time.clock()
        ticks = t-t1
        if(PRINT):
            myUtils.print_pretty(i, len(merg_sorted_lists[i]), ticks, ROUND)
        myUtils.write_to_file([(test_name,len(merg_sorted_lists[i]),round(ticks,4))])
    #Counting Sort Test
    size = iSIZE
    test_name = "Counting Sort - unsorted"
    print("\n*******************************") 
    print(f"Test Name:\t{test_name}")
    print("*******************************") 
    count_sorted_lists = []
    for i in range(0,RANGE):
        list = myUtils.make_list(size)
        t1 = time.clock()
        count_sorted_lists.append(sort.count_sort(list,size))
        t = time.clock()
        ticks = t-t1
        if(PRINT):
            myUtils.print_pretty(i, size, ticks, ROUND)
        myUtils.write_to_file([(test_name,size,round(ticks,ROUND))])
        size += 10
    print("\n...Performing tests with sorted lists...\n")
    test_name = "Counting Sort - sorted"
    for i in range(0,RANGE):
        max = len(count_sorted_lists[i])
        t1 = time.clock()
        sort.count_sort(count_sorted_lists[i],max)
        t = time.clock()
        ticks = t-t1
        if(PRINT):
            myUtils.print_pretty(i, len(count_sorted_lists[i]), ticks, ROUND)
        myUtils.write_to_file([(test_name,len(count_sorted_lists[i]),round(ticks,ROUND))])
    print("\n...Performing tests with reverse sorted lists...\n")
    test_name = "Counting Sort - reverse sorted"
    for i in range(0,RANGE):
        count_sorted_lists[i].reverse()
        max = len(count_sorted_lists[i])
        t1 = time.clock()
        sort.count_sort(count_sorted_lists[i],max)
        t = time.clock()
        ticks = t-t1
        if(PRINT):
            myUtils.print_pretty(i, max, ticks, ROUND)
        myUtils.write_to_file([(test_name,max,round(ticks,ROUND))])

if __name__ == "__main__":
    main()
