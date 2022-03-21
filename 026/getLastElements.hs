getFirstElements n _  
               | n <= 0   = []  
getFirstElements _ []     = []  
getFirstElements n (x:xs) = x : getFirstElements (n-1) xs

reverseList [] = []
reverseList (x:xs) = reverseList xs ++ [x]

getLastElements n arr = reverseList (getFirstElements n (reverseList arr))