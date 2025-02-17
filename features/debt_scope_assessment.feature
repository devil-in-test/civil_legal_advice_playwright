Feature: Debt Scope Assessment

        ====== income =======
        Q1 - Maintenance received amount
        Q2 - Maintenance frequency
        Q3 - Pension received amount
        Q4 - Pension frequency
        Q5 - Other income amount
        Q6 - Other income frequency
         ====== outgoings =======
        Q7 - Rent amount
        Q8 - Rent frequency
        Q9 - Maintenance paid amount
        Q10 - Maintenance paid frequency
        Q11 - Monthly income contribution

Background:
          Given I navigate to the civil legal advice start page
          And I click start now
          Then I am viewing the civil legal advice topic page
          When I click the debt topic

Scenario Outline: Yes I'm  a home owner at risk 
						- no partner 
						- no children 
						- no benefits  
						- no dependents
						- no job
						- no savings
						- no valuables
						- no other properties
						
						Variations of income and outgoings to determine that we are correctly advising 
						a citizen of their eligibility
						

          Then I am viewing the civil legal advice debt page
          When I click that I am at risk of losing my home
          Then I am viewing the civil legal aid is available for this problem page
          When I click check if I qualify financially
          And answer No to Do You have a partner?
          And answer No to Do you receive any benefits (including Child Benefit)?
          And answer No to Do you have any children aged 15 or under?
          And answer No to Do you have any dependants aged 16 or over?
          And answer No to Do you own any property?
          And answer No to Are you employed?
          And answer No to Are you self-employed?
          And answer No to Are you or your partner (if you have one) aged 60 or over?
          And answer No to Do you have any savings or investments?
          And answer No to Do you have any valuable items worth over £500 each?
          And I click continue to Your money coming in page
          And answer <Q1> to your maintenance received
          And answer <Q2> to your maintenance frequency
          And answer <Q3> to your pension received
          And answer <Q4> to your pension frequency
          And answer <Q5> to your other income
          And answer <Q6> to your other income frequency
          And I click continue to Your outgoings page
          And answer <Q7> to your rent amount
          And answer <Q8> to your rent schedule
          And answer <Q9> to your maintenance payment
          And answer <Q10> to your maintenance payment schedule
          And answer <Q11> to your monthly income contribution order
          And I click continue to review the answers page
          And I click reviewed answers
          Then I get confirmed my eligibility is <eligibility>


          Examples:

		     |Q1  |Q2        |Q3   |Q4       |Q5 |Q6        |Q7 |Q8        |Q9 |Q10       |Q11|eligibility  |
		     |0   |per week  |0   |per week  |0  |per week  |0  |per week  |0  |per week  |0  |eligible     |
		     |100 |per week  |0   |per week  |0  |per week  |0  |per week  |0  |per week  |0  |eligible     |
		     |100 |per week  |100 |per week  |0  |per week  |0  |per week  |0  |per week  |0  |not eligible |
	     

          

       

                                                                                                             
