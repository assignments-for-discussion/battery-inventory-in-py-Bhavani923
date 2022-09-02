#function for counting bateries by usage
def count_batteries_by_usage(cycles):
    low_count=0
    mid_count=0
    high_count=0
    counts=dict()
    #It take batteries one by one and put it in group
    for x in cycles:
        if x<=400:
            low_count+=1   # if the battery has charged less than 400 times then the lowercount is incremented to 1
        elif x>400 and x<=919: 
            mid_count+=1   #similarly  if the battery has charged more than 400 times and less then 919 is incremented to 1
        else:
            high_count+=1
    counts['lowCount']=low_count
    counts['mediumCount']=mid_count
    counts['highCount']=high_count
            
    return counts


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");  #Array has been defined based on how many time the batteries are charged
  #calling to function count_batteries_by_usage()
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  #printing lowcount
  print('lowCount:',counts['lowCount']) 
  #printing mediumCount
  print('mediumCount',counts['mediumCount'])
  #printing highCount
  print('highCount:',counts['highCount'])
  print("Done counting :)")


if _name_ == '_main_':
  test_bucketing_by_number_of_cycles()
