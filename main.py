#function for counting bateries by usage
def count_batteries_by_usage(cycles):
    low_count=0
    mid_count=0
    high_count=0
    counts=dict()
    
    for x in cycles:       #It take batteries one by one and put it in group
        if x<=400:
            low_count+=1   # if the battery has charged less than or equal to 400 times than the lowercount is incremented to 1
        elif x>400 and x<=919: 
            mid_count+=1   #similarly  if the battery has charged more than 400 times and less than or equal to 919 is incremented to 1
        else:
            high_count+=1  #else high count will be incremented
    counts['lowCount']=low_count
    counts['mediumCount']=mid_count
    counts['highCount']=high_count
            
    return counts          #returning  the values of counts


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n"); 

  #calling to function count_batteries_by_usage()
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])  #Array has been defined based on how many time the batteries are charged
  
  print('lowCount:',counts['lowCount'])             #prints the number of batteries come under lowercount
  
  print('mediumCount',counts['mediumCount'])        #prints the number of batteries come under mediumCount             
 
  print('highCount:',counts['highCount'])           #prints the number of batteries come under highCount
  print("Done counting :)")


if _name_ == '_main_':
  test_bucketing_by_number_of_cycles()
