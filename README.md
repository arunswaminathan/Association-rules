Extract Association Rules
=================

Through this project, we extract association rules from an interesting data set. The algorithm for extracting the association rules is based on Agarwal and Srikant paper of 1994. A copy of the paper can be found here: http://rakesh.agrawal-family.com/papers/vldb94apriori.pdf


Dataset:
--------
We used the NYC Open Dataset which contains the details of all the 311-Requests in the year 2013. The dataset itself was of 800MB containing close to a million rows.

The raw dataset is available here https://data.cityofnewyork.us/Social-Services/311-Requests-2013-No-Timestamp/ve2c-ib6g


For our integrated dataset, we wrote a python script which sorts the rows according to the ‘Months’ field and then took the top 1000 rows for each month. We also took only six rows from the raw dataset, vis-à-vis- Month, Department, Complaint Type, Location Type, Zipcode, Borough.

The resulting dataset set therefore has 12000 rows (1000 rows for each month of the year) and 6 rows.

We chose this dataset because we wanted to analyse the trends in the domestic complaints that New Yorkers file. We wanted to check if there are relationships between the borough and the type of complaints, or between the type of complaint and the department handling the complaint, etc.

We have attached the create_dataset.py script which we used to create out integrated dataset. When this script is run on the raw dataset defined about, our integrated dataset is generated.


Description:
------------

We used the apriori algorithm described in section 2.1 of the Agrawal and Srikant paper in VLDB 1994. We calculate the frequent itemsets as freq_itemset from scratch each time the program is run. 

Specifically, the program does the following:

Specifically, you should write a program to do the following:

1. Accept as input the name of a file from which to extract association rules; we will input here the name of your INTEGRATED-DATASET file. You can assume that we will only test your program with your INTEGRATED-DATASET file, so you can implement variations of the a-priori algorithm that are a good fit for your data (see below). In this case, you must explain in the README file precisely what variation(s) you have implemented and why (see item 3 below for more details on what variations are acceptable).
2. Prompt the user for a minimum support min_sup and a minimum confidence min_conf, which are two values between 0 and 1. These values must be specified in the command line (and not, for example, using  JOptionPane.showInputDialog()). So we should be able to call your program, for example, as:
run.sh INTEGRATED-DATASET.csv 0.3 0.5
which specifies min_sup=0.3 and min_conf=0.5.
3. Compute all the "frequent (i.e., large) itemsets," using min_sup as your support threshold. The frequent itemsets have support greater than or equal to min_sup. You should use the a-priori algorithm described in Section 2.1 of the Agrawal and Srikant paper in VLDB 1994 (see class schedule) to compute these frequent itemsets. You do not need to implement the "subset function" using the hash tree as described in Section 2.1.2. However, you must implement the version of a-priori in Section 2.1.1, which we discussed in class briefly but is slightly more sophisticated than the version that we covered in detail in class.  Note: Your program has to compute all the frequent itemsets from scratch every time the program is run; you cannot "precompute" anything ahead of time, but rather all computations have to happen each time your program is run. You are welcome to implement variations of the a-priori algorithm that are a good fit for your data, as discussed above (e.g., to account for item hierarchies, as we discussed in class, or numerical items). IMPORTANT NOTE: These variations have to be at least as "sophisticated" as the description of a-priori in Section 2.1 in general, and in Section 2.1.1 in particular (i.e., your variations cannot be more primitive than the algorithm as described in these sections of the paper). A good place to start to search for relevant variations of the original algorithm is Rakesh Agrawal's publications in the 1990s, http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/a/Agrawal:Rakesh.html. Implementing such a variation is strictly optional; if you decide to implement such a variation, you must so indicate in the README file, explaining precisely what variation(s) you have implemented and why.
3. For each of the frequent itemsets, build all possible association rules and identify those that have a confidence of at least min_conf. Generate only association rules with one item on the right hand side and with at least one item on the left hand side. We will call the rules with confidence greater than or equal to min_conf as the "high-confidence rules."
4. Output the frequent itemsets to a file named "output.txt": each line should include one itemset, within square brackets, and its support, separated by a comma (e.g., [item1,item2], 7.4626%). The lines in the file should be listed in decreasing order of their support. Output also in the same output.txt file the high-confidence association rules, in decreasing order of confidence, reporting the support and confidence of each rule (e.g., [item1] => [item2] (Conf: 100%, Supp: 7.4626%)).
