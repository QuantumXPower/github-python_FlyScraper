1. Why did you create a the python program called Schedule_Scraping?

The reason why I created the python program called Schedule_Scraping is because I quite my job at the The Row Kitchen and Pub and I wanted to create a webpage and python program that would store and list the names, emails, and phone numbers of my former employees.

2. Where did you procure the names, emails, and phone numbers of your former employees?

I procured the names, emails, and phone numbers from a scheduling system called Schedulefly before the general manager disabled my account access. I did this by logging into Schedulefly.com and saved a Schedulefly webpage that contains the personal information of my co-workers, so that I can keep in contact with my co-workers and friends.

3. What exactly is the scheduling system called Schedulefly?

The scheduling system called Schedulefly is a website that allows managers to construct schedules for their employees. It will often be subdivided into different departments with lists of employees working in those departments. 

4. How does the Scheduling_Scraping program work?

The Scheduling_Scraping program is a program that scrapes the webpage called SceduleFlyContact_Book.html. The focal point of this webpage are the table tags that hold the names, emails, and phone numbers of my co-workers. Furthermore, I took my co-workers contact information from the original Schedulefly.com webpage and created ScheduleFlyContact_Book.html in order to facilitate present and future scraping operations. Overall in the program's main operations, the Scheduling_Scraping program uses Beautiful Soup's findAll() method to put all of the tr tags (which is the HTML equivalent of a row) into a list. The [1:] modifier at the end instructs the loop to skip the first item. Then, after the loop is set up on the tr tags, we set up another list that will grab all of the td tags (the HTML equivalent of a column) from each row.Now pulling out the data is simply a matter of figuring out which order we can expect the data to appear in each row and pulling the corresponding values from the list. Since I expect name, email, and mobile number to appear in each row from left to right, the first element of the col variable (col[0]) can always be expected to be the name and the last element (col[3]) can always be expected to be the mobile number. Lastly, we create a new set of values to retrieve each, with some Beautiful Soup specific objects tacked on the end to grab only the bits we want. 
